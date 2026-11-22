#!/usr/bin/env python3
"""Senhas sem procurar e sem digitar: inventário do setup + cofre KeePassXC pelo terminal, sempre com o seu ok.

    just senhas                  # inventário × cofre: o que já está guardado e o que falta (pede a senha mestra)
    just senhas-lista            # regenera docs/senhas.md (o inventário, sem nenhuma senha)
    just senha github            # escolhe a entrada e copia a senha; a área de transferência limpa sozinha em 20 s
    just senhas-criar            # gera no cofre as senhas dos serviços locais que ainda faltam (você confirma)
    just senhas-rodar soberania -- docker compose up -d   # sobe o serviço com os segredos vindos do cofre
    just cofre-abrir 30          # desbloqueio por 30 min: nesse tempo os comandos não pedem a senha mestra
    just cofre-fechar            # tranca na hora

A senha mestra nunca vai para arquivo, linha de comando ou tela: vai pela entrada padrão do keepassxc-cli.
O desbloqueio temporário guarda a senha mestra no chaveiro do kernel (keyctl) com prazo de validade;
sem o keyctl, cada comando pede a senha mestra.
No navegador quem preenche é a extensão KeePassXC-Browser; nos programas do Windows, o Auto-Type (Ctrl+Alt+A).
"""
from __future__ import annotations

import argparse
import getpass
import json
import os
import re
import shutil
import subprocess
import sys
import unicodedata
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(RAIZ / "tools" / "organizar"))
import senhas_csv as kp  # noqa: E402  (grupos do cofre e o jeito seguro de chamar o keepassxc-cli)

DOC = RAIZ / "docs" / "senhas.md"
CHAVE_SESSAO = "amtech-cofre"
SETUP = kp.SETUP
SEGREDO = re.compile(r"(SENHA|PASSWORD|SECRET|SEGREDO|CHAVE|KEY|TOKEN|ACCESS_KEY_ID)")
EXTERNA = re.compile(r"(ANTHROPIC|GEMINI|CLOUDFLARE|DEEPSEEK|OPENROUTER|LITESTREAM|OPENAI|HUGGING)")
AVISO = "<!-- Arquivo GERADO por tools/senhas/senhas.py (ecossistema.json + infra/**/*.env.example + data/senhas.json). Não edite à mão. -->\n"

GRUPO_DAS_CONTAS = {"Editora": "05 Instituto e Editora", "Marketing e automação": "04 Grupo AMtech Digital",
                    "Desenvolvimento": "06 Código e nuvem", "Inteligência artificial": "07 IA", "Sites e domínio": "04 Grupo AMtech Digital",
                    "Canais e conteúdo": "08 Redes", "Venda": "05 Instituto e Editora", "Pessoa física e impostos": "02 Governo"}
GRUPO_DA_CAMADA = {"nuvem": "06 Código e nuvem", "obs": "06 Código e nuvem", "cnt": "06 Código e nuvem", "ia": "07 IA", "chat": "07 IA",
                   "dados": "07 IA", "mkt": "04 Grupo AMtech Digital", "web": "04 Grupo AMtech Digital", "oper": "04 Grupo AMtech Digital",
                   "neg": "04 Grupo AMtech Digital", "venda": "05 Instituto e Editora", "editora": "05 Instituto e Editora",
                   "pub": "08 Redes", "cont": "08 Redes", "est": "09 Estudo", "emp": "01 Bancos e dinheiro", "win": "00 Essenciais (e-mail e contas-mãe)"}
COMO = {"conta": "extensão KeePassXC-Browser: preenche no login e oferece salvar a senha nova",
        "gerar": "o setup gera (just senhas-criar) e entrega ao serviço (just senhas-rodar)",
        "externa": "pegue no site do provedor e guarde no cofre; o terminal usa com just senhas-rodar",
        "chave": "guarde no cofre; o comando que usa lê do cofre sozinho",
        "ssh": "KeePassXC como agente SSH (passo kp-ssh)", "anotacao": "entrada no cofre com o texto em Notas",
        "memoria": "fora do cofre, de propósito"}


def sem_acento(s: str) -> str:
    return "".join(c for c in unicodedata.normalize("NFKD", s) if not unicodedata.combining(c)).lower()


def limpar(nome: str) -> str:
    return re.sub(r"\s+", " ", nome.replace("|", " ")).strip()


GENERICAS = set("""google conta the web api app agenda online dominio mail e-mail email ads midia nativa armazenamento arquivos tags
conversao comunidade agentes codigo perfil empresa ponto retirada voz clonada gpu hora vm sempre ligada bancaria separada certificado
digital acervos imagens afiliados gerenciador negocios registro marca mercado cloud drive search console wi-fi casa ou de da do dos das
plataforma pago reserva painel""".split())


def palavra_chave(nome: str, trocas: dict | None = None) -> str:
    """Palavra que acha a conta no cofre (os títulos importados do Chrome são o domínio, como github.com)."""
    if trocas and limpar(nome) in trocas:
        return trocas[limpar(nome)]
    base = sem_acento(limpar(nome))
    dentro = re.findall(r"\(([^)]*)\)", base)
    for trecho in dentro:
        for p in re.findall(r"[a-z0-9-]+\.[a-z.]+", trecho):
            return p
    palavras = re.findall(r"[a-z0-9.]+", base.split("(")[0])
    if "google" in palavras:
        return "google"
    for p in palavras + [w for t in dentro for w in re.findall(r"[a-z0-9.]+", t)]:
        p = p.strip(".")
        if len(p) > 2 and p not in GENERICAS:
            return p
    return ""


def grupo_web(nome: str, padrao: str | None) -> str:
    """Grupo do cofre pelas mesmas palavras do senhas_csv, mas por palavra inteira: 'Pinterest' não cai em Banco Inter."""
    texto = sem_acento(limpar(nome))
    palavras = re.findall(r"[a-z0-9.]+", texto)
    junto = "".join(palavras)
    for g, chaves in kp.GRUPOS.items():
        for k in chaves:
            k = k.lstrip("=")
            if any(p == k or p.startswith(k + ".") or (len(k) >= 6 and k in p) for p in palavras) or (len(k) >= 8 and k in junto):
                return g
    return padrao or kp.OUTROS


def ler_env_examples(raiz: Path = RAIZ) -> list[dict]:
    itens = []
    for arq in sorted((raiz / "infra").rglob("*.env.example")) + sorted((raiz / "infra").rglob(".env.example")):
        pasta = arq.parent.name
        for linha in arq.read_text(encoding="utf-8").splitlines():
            m = re.match(r"^([A-Z0-9_]+)=", linha)
            if m and SEGREDO.search(m[1]) and not m[1].endswith("_FILE"):
                var = m[1]
                itens.append({"nome": f"{pasta} · {var}", "grupo": SETUP, "entrada": f"{SETUP}/{pasta}/{var}",
                              "tipo": "externa" if EXTERNA.search(var) else "gerar", "fonte": str(arq.relative_to(raiz)),
                              "pasta": pasta, "var": var, "chave": var.lower()})
    vistos, unicos = set(), []
    for i in itens:
        if i["entrada"] not in vistos:
            vistos.add(i["entrada"])
            unicos.append(i)
    return unicos


def inventario(raiz: Path = RAIZ) -> list[dict]:
    eco = json.loads((raiz / "data" / "ecossistema.json").read_text(encoding="utf-8"))
    cfg = json.loads((raiz / "data" / "senhas.json").read_text(encoding="utf-8"))
    ignorar = {sem_acento(limpar(x)) for x in cfg["ignorar"]}
    trocas = cfg.get("chaves", {})
    itens, vistos = [], set()

    def add(item: dict) -> None:
        k = sem_acento(limpar(item["nome"]))
        if k in ignorar or (item["tipo"] == "conta" and item["chave"] and item["chave"] in vistos):
            return
        vistos.add(item["chave"])
        itens.append(item)

    for g in eco["contas"]:
        for c in g["itens"]:
            add({"nome": limpar(c["nome"]), "grupo": grupo_web(c["nome"], GRUPO_DAS_CONTAS.get(g["grupo"])), "tipo": "conta",
                 "fonte": f"ecossistema.json · contas · {g['grupo']}", "chave": palavra_chave(c["nome"], trocas), "obs": c.get("obs", "")})
    for b in eco["blocos"]:
        if b["conta"] and b["camada"] not in cfg["camadas_sem_login"]:
            add({"nome": limpar(b["rotulo"]), "grupo": grupo_web(b["rotulo"], GRUPO_DA_CAMADA.get(b["camada"])), "tipo": "conta",
                 "fonte": f"ecossistema.json · bloco {b['id']}", "chave": palavra_chave(b["rotulo"], trocas), "obs": ""})
    for e in cfg["extras"]:
        chave = e.get("chave") or (sem_acento(e["entrada"]).split("/")[-1] if e.get("entrada") else palavra_chave(e["nome"]))
        add({**e, "grupo": e.get("grupo") or e["entrada"].split("/")[0], "fonte": "data/senhas.json", "chave": chave})
    for grupo, nome, chave in cfg.get("do_email", []):
        add({"nome": nome, "grupo": grupo, "tipo": "conta", "fonte": "Gmail (e-mails de cadastro, login e cobrança)",
             "chave": chave, "obs": "achada no seu e-mail"})
    for s in ler_env_examples(raiz):
        add(s)
    return sorted(itens, key=lambda i: (i["grupo"], i["tipo"] != "conta", sem_acento(i["nome"])))


def gerar_doc(itens: list[dict]) -> str:
    n = {t: sum(i["tipo"] == t for i in itens) for t in COMO}
    o = [AVISO, "# Senhas do setup: o que guardar e como cada uma é preenchida\n",
         f"{len(itens)} itens: {n['conta']} contas em sites, {n['gerar']} segredos que o setup gera, {n['externa']} chaves de provedores, "
         f"{n['chave'] + n['ssh']} chaves e tokens, {n['anotacao']} anotações e {n['memoria']} que fica só na memória. Nenhuma senha aparece aqui.\n",
         "Para ver o que já está no cofre e o que falta: `just senhas`. Para pegar uma senha: `just senha NOME`.\n",
         "| Como preencher | Quando usar |\n|---|---|"]
    o += [f"| {t} | {COMO[t]} |" for t in COMO if n[t]]
    grupo = None
    for i in itens:
        if i["grupo"] != grupo:
            grupo = i["grupo"]
            o.append(f"\n## {grupo}\n\n| Item | Tipo | Observação |\n|---|---|---|")
        obs = (i.get("obs") or (f"`{i['entrada']}`" if i.get("entrada") else "")).replace("|", "/")
        o.append(f"| {i['nome']} | {i['tipo']} | {obs} |")
    cfg = json.loads((RAIZ / "data" / "senhas.json").read_text(encoding="utf-8"))
    if cfg.get("conferir_do_email"):
        o.append("\n## Achados no e-mail para você conferir\n\nRemetentes de cadastro ou cobrança que podem ser só loja, newsletter ou golpe. "
                 "O que for conta sua vai para `do_email` em `data/senhas.json`; o resto, apague a conta ou ignore.\n")
        o += [f"- {x}" for x in cfg["conferir_do_email"]]
    return "\n".join(o) + "\n"


# ---------- cofre ----------
def caminho_cofre() -> str:
    """Cofre do roteiro (passo keepass): Documentos\\Cofre\\Cofre.kdbx do Windows. COFRE=... troca o caminho."""
    if os.environ.get("COFRE"):
        return os.environ["COFRE"]
    achados = sorted(Path("/mnt/c/Users").glob("*/Documents/Cofre/Cofre.kdbx")) if Path("/mnt/c/Users").exists() else []
    if achados:
        return str(achados[0])
    return str(Path.home() / "Documents" / "Cofre" / "Cofre.kdbx")


def _keyctl(args: list[str], entrada: str | None = None, run=subprocess.run):
    return run(["keyctl", *args], input=entrada, capture_output=True, text=True)


def mestre(run=subprocess.run, pedir=getpass.getpass) -> str:
    """Senha mestra: do desbloqueio temporário, se houver; senão, pergunta."""
    if shutil.which("keyctl"):
        r = _keyctl(["request", "user", CHAVE_SESSAO], run=run)
        if r.returncode == 0:
            p = _keyctl(["pipe", r.stdout.strip()], run=run)
            if p.returncode == 0 and p.stdout:
                return p.stdout
    return pedir("Senha mestra do cofre (não aparece na tela): ")


def cli() -> str:
    c = kp.achar_cli()
    if not c:
        sys.exit("Não achei o keepassxc-cli. Instale o KeePassXC (Ubuntu: sudo apt install keepassxc).")
    if not Path(caminho_cofre()).exists():
        sys.exit(f"Cofre não encontrado: {caminho_cofre()} (defina COFRE=... no ~/.bashrc)")
    return c


def entradas(c: str, m: str, run=subprocess.run) -> list[str]:
    r = kp._cli(c, ["ls", "-q", "-R", "-f", caminho_cofre()], f"{m}\n", run, utf8=True)
    if r.returncode != 0:
        sys.exit("O cofre não abriu: senha mestra errada ou cofre em uso por outro programa.")
    return [ln.strip() for ln in r.stdout.splitlines() if ln.strip() and not ln.strip().endswith("/") and "[empty]" not in ln]


def no_cofre(item: dict, todas: list[str]) -> str | None:
    if item.get("entrada"):
        return item["entrada"] if item["entrada"] in todas else None
    if item["tipo"] == "memoria":
        return "(fora do cofre)"
    chave = item["chave"]
    if not chave:
        return None
    for e in todas:
        if chave and chave in sem_acento(e):
            return e
    return None


def area_de_transferencia() -> list[str] | None:
    for cmd in (["clip.exe"], ["wl-copy"], ["xclip", "-selection", "clipboard"], ["clip"]):
        if shutil.which(cmd[0]):
            return cmd
    return None


def copiar(texto: str, segundos: int, run=subprocess.run, popen=subprocess.Popen) -> bool:
    cmd = area_de_transferencia()
    if not cmd:
        return False
    run(cmd, input=texto, text=True, check=False)
    limpar_depois = f"sleep {segundos}; printf '' | {' '.join(cmd)}"
    popen(["bash", "-c", limpar_depois], start_new_session=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    return True


def escolher(opcoes: list[str], busca: str, ler=input) -> str | None:
    achadas = [o for o in opcoes if sem_acento(busca) in sem_acento(o)] if busca else opcoes
    if len(achadas) == 1:
        return achadas[0]
    if not achadas:
        print(f"Nada no cofre com '{busca}'.")
        return None
    if shutil.which("gum") and sys.stdin.isatty():
        r = subprocess.run(["gum", "filter", "--placeholder", "Qual senha?", *achadas], capture_output=True, text=True)
        return r.stdout.strip() or None
    for n, o in enumerate(achadas[:30], 1):
        print(f"  {n:2}. {o}")
    r = ler("Número (Enter cancela): ").strip()
    return achadas[int(r) - 1] if r.isdigit() and 0 < int(r) <= len(achadas[:30]) else None


# ---------- comandos ----------
def cmd_lista(check: bool) -> int:
    texto = gerar_doc(inventario())
    if check:
        if not DOC.exists() or DOC.read_text(encoding="utf-8") != texto:
            print("docs/senhas.md desatualizado: rode just senhas-lista", file=sys.stderr)
            return 1
        return 0
    DOC.write_text(texto, encoding="utf-8")
    print(f"docs/senhas.md: {len(inventario())} itens")
    return 0


def cmd_conferir() -> int:
    c = cli()
    todas = entradas(c, mestre())
    itens = inventario()
    faltam = [i for i in itens if not no_cofre(i, todas)]
    print(f"No cofre: {len(itens) - len(faltam)} de {len(itens)} itens do inventário ({len(todas)} entradas no total).")
    grupo = None
    for i in faltam:
        if i["grupo"] != grupo:
            grupo = i["grupo"]
            print(f"\n{grupo}")
        print(f"  falta  {i['nome']}  [{i['tipo']}]")
    if faltam:
        print("\nContas: entre no site com a extensão ligada e salve. Segredos dos serviços: just senhas-criar.")
    achadas = {no_cofre(i, todas) for i in itens}
    fora = [e for e in todas if e not in achadas]
    if fora:
        print(f"\nNo cofre e fora do inventário ({len(fora)}): são contas suas que a lista ainda não conhece.")
        grupos: dict[str, list[str]] = {}
        for e in fora:
            g, _, titulo = e.rpartition("/")
            grupos.setdefault(g or "(sem grupo)", []).append(titulo)
        for g, titulos in sorted(grupos.items()):
            print(f"  {g} ({len(titulos)}): {', '.join(sorted(titulos)[:15])}{' …' if len(titulos) > 15 else ''}")
        print("Para entrar no inventário, acrescente em data/senhas.json → extras (o que for login) ou ignorar.")
    return 0


def cmd_criar(ler=input) -> int:
    c = cli()
    m = mestre()
    todas = entradas(c, m)
    novos = [i for i in inventario() if i["tipo"] == "gerar" and i.get("entrada") and i["entrada"] not in todas]
    if not novos:
        print("Todos os segredos dos serviços já estão no cofre.")
        return 0
    for i in novos:
        print(f"  gerar  {i['entrada']}")
    if ler(f"\nGerar {len(novos)} senha(s) aleatória(s) de 32 caracteres no cofre? Digite {len(novos)} para confirmar: ").strip() != str(len(novos)):
        print("Cancelado. Nada foi criado.")
        return 1
    for pasta in sorted({str(Path(i["entrada"]).parent) for i in novos}):
        partes = pasta.split("/")
        for k in range(1, len(partes) + 1):
            kp._cli(c, ["mkdir", "-q", caminho_cofre(), "/".join(partes[:k])], f"{m}\n")
    ok = 0
    for i in novos:
        r = kp._cli(c, ["add", "-q", "-g", "-L", "32", "-l", "-U", "-n", "--notes", f"Gerada pelo setup para {i['fonte']}", caminho_cofre(), i["entrada"]], f"{m}\n")
        ok += r.returncode == 0
        print(f"  {'criada' if r.returncode == 0 else 'FALHOU'}: {i['entrada']}")
    print(f"{ok} de {len(novos)} criadas. Agora suba o serviço com: just senhas-rodar PASTA -- docker compose up -d")
    return 0 if ok == len(novos) else 1


def cmd_senha(busca: str, segundos: int, mostrar: bool, ler=input) -> int:
    c = cli()
    m = mestre()
    alvo = escolher(entradas(c, m), busca, ler)
    if not alvo:
        return 1
    usuario = kp._cli(c, ["show", "-q", "-a", "UserName", "-a", "URL", caminho_cofre(), alvo], f"{m}\n", utf8=True).stdout.strip().splitlines()
    senha = kp._cli(c, ["show", "-q", "-s", "-a", "Password", caminho_cofre(), alvo], f"{m}\n", utf8=True).stdout.rstrip("\n")
    print(f"{alvo}\n  usuário: {usuario[0] if usuario else '—'}\n  site:    {usuario[1] if len(usuario) > 1 else '—'}")
    if mostrar:
        if ler("Mostrar a senha na tela? Digite mostrar: ").strip() == "mostrar":
            print(f"  senha:   {senha}")
    elif copiar(senha, segundos):
        print(f"  senha copiada: cole com Ctrl+V. A área de transferência limpa em {segundos} s.")
    else:
        print("  Não achei como copiar (clip.exe, wl-copy ou xclip). Use --mostrar.")
    del senha
    return 0


def cmd_rodar(pasta: str, comando: list[str]) -> int:
    if not comando:
        sys.exit("Uso: just senhas-rodar PASTA -- comando")
    c = cli()
    m = mestre()
    ambiente, faltam = dict(os.environ), []
    for i in (s for s in ler_env_examples() if s["pasta"] == pasta):
        r = kp._cli(c, ["show", "-q", "-s", "-a", "Password", caminho_cofre(), i["entrada"]], f"{m}\n", utf8=True)
        if r.returncode == 0 and r.stdout.strip():
            ambiente[i["var"]] = r.stdout.rstrip("\n")
        else:
            faltam.append(i["var"])
    if faltam:
        print(f"Faltam no cofre ({SETUP}/{pasta}/...): {', '.join(faltam)}. Rode just senhas-criar ou guarde as chaves dos provedores.")
    del m
    os.execvpe(comando[0], comando, ambiente)


def cmd_abrir(minutos: int) -> int:
    if not shutil.which("keyctl"):
        sys.exit("Instale o keyctl para o desbloqueio temporário: sudo apt install keyutils")
    c = cli()
    m = getpass.getpass("Senha mestra do cofre (não aparece na tela): ")
    entradas(c, m)  # confere a senha antes de guardar
    r = _keyctl(["padd", "user", CHAVE_SESSAO, "@u"], entrada=m)
    if r.returncode != 0:
        sys.exit("O chaveiro do kernel recusou guardar a senha.")
    _keyctl(["timeout", r.stdout.strip(), str(minutos * 60)])
    print(f"Cofre aberto para o terminal por {minutos} min. Para trancar antes: just cofre-fechar")
    return 0


def cmd_fechar() -> int:
    if shutil.which("keyctl"):
        r = _keyctl(["request", "user", CHAVE_SESSAO])
        if r.returncode == 0:
            _keyctl(["unlink", r.stdout.strip(), "@u"])
    print("Cofre trancado para o terminal.")
    return 0


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    sub = p.add_subparsers(dest="cmd", required=True)
    s = sub.add_parser("lista"); s.add_argument("--check", action="store_true")
    sub.add_parser("conferir")
    sub.add_parser("criar")
    s = sub.add_parser("senha"); s.add_argument("busca", nargs="?", default=""); s.add_argument("--segundos", type=int, default=20)
    s.add_argument("--mostrar", action="store_true")
    s = sub.add_parser("rodar"); s.add_argument("pasta"); s.add_argument("comando", nargs=argparse.REMAINDER)
    s = sub.add_parser("abrir"); s.add_argument("minutos", nargs="?", type=int, default=30)
    sub.add_parser("fechar")
    a = p.parse_args(argv)
    if a.cmd == "lista":
        return cmd_lista(a.check)
    if a.cmd == "conferir":
        return cmd_conferir()
    if a.cmd == "criar":
        return cmd_criar()
    if a.cmd == "senha":
        return cmd_senha(a.busca, a.segundos, a.mostrar)
    if a.cmd == "rodar":
        return cmd_rodar(a.pasta, [x for x in a.comando if x != "--"])
    if a.cmd == "abrir":
        return cmd_abrir(a.minutos)
    return cmd_fechar()


if __name__ == "__main__":
    sys.exit(main())
