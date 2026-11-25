#!/usr/bin/env python3
"""Fonte única das ferramentas do setup: Windows, extensões do VS Code, pacotes e CLIs do WSL, serviços do Ubuntu e Docker.

Fonte: data/ferramentas.json. Saída: docs/operacao/ferramentas.md (gerado).
Enquanto os scripts de instalação não leem este arquivo, o --check garante que as listas deles e o registro batem:
  - pacotes.json, vscode-extensoes.txt, arrays PACOTES/TERMINAL dos scripts, config do mise, laço do uv e compose.yaml
    têm exatamente as mesmas ferramentas que o registro;
  - toda ferramenta do registro aponta para um arquivo que existe e que a menciona.

    python3 tools/ferramentas/ferramentas.py              # valida e regenera a documentação
    python3 tools/ferramentas/ferramentas.py --check      # o que o just check e o CI rodam
    python3 tools/ferramentas/ferramentas.py --estado     # o que está instalado e rodando neste PC (lento: winget, docker)
    python3 tools/ferramentas/ferramentas.py --estado --faltando   # só o que falta e conta como falta
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]
DADOS = RAIZ / "data" / "ferramentas.json"
PORTAS = RAIZ / "data" / "portas.json"
MD = RAIZ / "docs" / "operacao" / "ferramentas.md"
AVISO = "<!-- Arquivo GERADO por tools/ferramentas/ferramentas.py a partir de data/ferramentas.json. Não edite à mão. -->\n"

TIPOS = {"windows": "Programas do Windows", "vscode": "Extensões do VS Code", "wsl-apt": "Pacotes do Ubuntu (apt)",
         "wsl-cli": "CLIs do Ubuntu", "systemd": "Serviços do Ubuntu", "docker": "Serviços Docker"}
CONFERIR = {"windows": {"winget", "arquivo"}, "vscode": {"extensao"}, "wsl-apt": {"dpkg"},
            "wsl-cli": {"comando", "arquivo"}, "systemd": {"systemd"}, "docker": {"container"}}
OBRIGATORIOS = ("id", "nome", "tipo", "grupo", "fonte", "codigo_aberto", "obrigatoria", "decisao", "conferir", "instalar", "doc")
ID_RE = re.compile(r"^[a-z0-9][a-z0-9-]*$")


def carregar(caminho: Path = DADOS) -> dict:
    return json.loads(caminho.read_text(encoding="utf-8"))


# ------------------------------------------------------------------ validação do arquivo
def validar(dados: dict) -> list[str]:
    erros: list[str] = []
    decisoes, perfis = set(dados.get("decisoes", {})), set(dados.get("perfis", {}))
    vistos: set[str] = set()
    for f in dados.get("ferramentas", []):
        fid = f.get("id", "?")
        for campo in OBRIGATORIOS:
            if campo not in f:
                erros.append(f"{fid}: falta o campo '{campo}'")
        if not ID_RE.match(str(fid)):
            erros.append(f"{fid}: id fora do padrão (minúsculas, números e hífen)")
        if fid in vistos:
            erros.append(f"{fid}: id repetido")
        vistos.add(fid)
        tipo = f.get("tipo")
        if tipo not in TIPOS:
            erros.append(f"{fid}: tipo '{tipo}' desconhecido")
            continue
        if f.get("decisao") not in decisoes:
            erros.append(f"{fid}: decisão '{f.get('decisao')}' desconhecida")
        if f.get("decisao") in ("parada", "adiada"):
            if not f.get("motivo"):
                erros.append(f"{fid}: decisão '{f['decisao']}' sem motivo")
            try:
                dt.date.fromisoformat(str(f.get("rever_em")))
            except ValueError:
                erros.append(f"{fid}: decisão '{f['decisao']}' sem rever_em válido (AAAA-MM-DD)")
        conf = f.get("conferir") or {}
        if len(conf) != 1 or next(iter(conf)) not in CONFERIR[tipo]:
            erros.append(f"{fid}: 'conferir' deve ter uma chave entre {sorted(CONFERIR[tipo])}")
        if not str(f.get("doc", "")).strip():
            erros.append(f"{fid}: falta a linha de documentação ('doc')")
        if tipo in ("docker", "systemd") and f.get("perfil") not in perfis:
            erros.append(f"{fid}: serviço sem perfil válido {sorted(perfis)}")
        if tipo == "docker":
            for campo in ("ligar", "ram_mb", "disco_gb"):
                if campo not in f:
                    erros.append(f"{fid}: serviço Docker sem '{campo}'")
    return erros


# ------------------------------------------------------------------ o que os scripts de instalação declaram
def _array_bash(script: Path, nome: str) -> list[str]:
    m = re.search(rf"^{nome}=\(([^)]*)\)", script.read_text(encoding="utf-8"), re.M | re.S)
    return m.group(1).split() if m else []


def _servicos_compose(caminho: Path) -> list[str]:
    nomes, em_servicos = [], False
    for linha in caminho.read_text(encoding="utf-8").splitlines():
        if re.match(r"^[A-Za-z]", linha):
            em_servicos = linha.startswith("services:")
            continue
        m = re.match(r"^  ([A-Za-z0-9_.-]+):\s*$", linha)
        if em_servicos and m:
            nomes.append(m.group(1))
    return nomes


def declarados(raiz: Path = RAIZ) -> dict[str, set[str]]:
    """Por fonte legível por máquina, as chaves de conferência que ela declara."""
    d: dict[str, set[str]] = {}
    pac = json.loads((raiz / "scripts/windows/pacotes.json").read_text(encoding="utf-8"))
    d["scripts/windows/pacotes.json"] = {k["id"] for g in pac["grupos"] for k in g["pacotes"]}
    ext = (raiz / "scripts/windows/vscode-extensoes.txt").read_text(encoding="utf-8").splitlines()
    d["scripts/windows/vscode-extensoes.txt"] = {l.split("#")[0].strip().lower() for l in ext if l.split("#")[0].strip()}
    for script, nome in (("scripts/wsl/bootstrap.sh", "PACOTES"), ("scripts/wsl/bootstrap.sh", "TERMINAL"),
                         ("scripts/wsl/extras.sh", "PACOTES"), ("scripts/wsl/ferramentas-re.sh", "PACOTES")):
        d[f"{script}#{nome}"] = set(_array_bash(raiz / script, nome))
    mise = raiz / "infra/dotfiles/dot_config/mise/config.toml"
    d[str(mise.relative_to(raiz))] = {m.group(1) for l in mise.read_text(encoding="utf-8").splitlines()
                                      if (m := re.match(r'^"?(?:github:[^/]+/)?([a-z0-9-]+)"?\s*=', l))} - {"experimental", "node"}
    m = re.search(r'for item in ((?:"[^"]+"\s*)+); do', (raiz / "scripts/wsl/extras.sh").read_text(encoding="utf-8"))
    d["scripts/wsl/extras.sh#uv"] = {re.sub(r"\[.*", "", x) for x in re.findall(r'"([^"]+)"', m.group(1))} if m else set()
    for c in sorted(raiz.glob("infra/*/compose.yaml")):
        d[str(c.relative_to(raiz))] = set(_servicos_compose(c))
    return d


def _chave_no_registro(f: dict) -> tuple[str, str] | None:
    """Liga uma ferramenta do registro à fonte legível que a declara (ou None se a fonte é um script com 'if tem')."""
    fonte, conf = f["fonte"], f["conferir"]
    if fonte == "scripts/windows/pacotes.json":
        return fonte, conf.get("winget", "")
    if fonte == "scripts/windows/vscode-extensoes.txt":
        return fonte, conf.get("extensao", "")
    if "#" in fonte and f["tipo"] == "wsl-apt":
        return fonte, conf.get("dpkg", "")
    if fonte.endswith("mise/config.toml"):
        return fonte, f["nome"]
    if f["id"].startswith("cli-uv-"):
        return "scripts/wsl/extras.sh#uv", f["nome"]
    if f["tipo"] == "docker":
        return fonte, conf.get("container", "/").split("/", 1)[1]
    return None


def conferir_fontes(dados: dict, raiz: Path = RAIZ) -> list[str]:
    erros: list[str] = []
    decl = declarados(raiz)
    no_registro: dict[str, set[str]] = {k: set() for k in decl}
    for f in dados["ferramentas"]:
        if f["fonte"] == "fora-do-plano":
            continue
        chave = _chave_no_registro(f)
        if chave:
            fonte, nome = chave
            if fonte not in decl:
                erros.append(f"{f['id']}: fonte '{fonte}' não existe ou não é lida")
                continue
            no_registro[fonte].add(nome)
            if f["tipo"] == "wsl-apt" and nome not in decl[fonte]:
                # o mesmo pacote pode estar em dois scripts (ex.: unzip): basta estar em algum array
                if not any(nome in v for k, v in decl.items() if "#" in k and not k.endswith("#uv")):
                    erros.append(f"{f['id']}: '{nome}' não está em {fonte}")
            continue
        arq = raiz / f["fonte"].split("#")[0]
        if not arq.exists():
            erros.append(f"{f['id']}: fonte '{f['fonte']}' não existe")
            continue
        alvo = next(iter(f["conferir"].values()))
        termo = Path(alvo).name if "/" in alvo else alvo
        texto = arq.read_text(encoding="utf-8")
        if termo not in texto and f["nome"] not in texto:
            erros.append(f"{f['id']}: {f['fonte']} não menciona '{termo}'")
    apt_registro = {f["conferir"]["dpkg"] for f in dados["ferramentas"] if f["tipo"] == "wsl-apt"}
    for fonte, nomes in decl.items():
        if "#" in fonte and not fonte.endswith("#uv"):
            faltam = nomes - apt_registro
        else:
            faltam = nomes - no_registro[fonte]
        for n in sorted(faltam):
            erros.append(f"{fonte} declara '{n}', que não está em data/ferramentas.json")
        for n in sorted(no_registro[fonte] - nomes) if "#" not in fonte or fonte.endswith("#uv") else []:
            erros.append(f"data/ferramentas.json tem '{n}' em {fonte}, mas a fonte não declara")
    return erros


# ------------------------------------------------------------------ documentação gerada
def _portas() -> dict[str, list[str]]:
    if not PORTAS.exists():
        return {}
    p: dict[str, list[str]] = {}
    for s in json.loads(PORTAS.read_text(encoding="utf-8")).get("servicos", []):
        p.setdefault(f"{s['grupo']}/{s['servico']}", []).append(str(s["porta"]))
    return p


def _decisao(f: dict) -> str:
    return {"normal": "", "parada": "parada", "adiada": "adiada"}[f["decisao"]]


def gerar_md(dados: dict) -> str:
    fs = dados["ferramentas"]
    L = [AVISO, "# Ferramentas do setup", "",
         "[← Índice da documentação](../README.md) · Fonte: [`data/ferramentas.json`](../../data/ferramentas.json) · "
         "Conferir no PC: `python3 tools/ferramentas/ferramentas.py --estado`", "",
         f"**{len(fs)} ferramentas.** Obrigatória = o setup conta com ela. Decisão *parada* ou *adiada* = escolha do Alan; "
         "não conta como falta no `just validar`.", ""]
    resumo = ["| Tipo | Total | Obrigatórias | Paradas ou adiadas |", "|---|---|---|---|"]
    for t, titulo in TIPOS.items():
        g = [f for f in fs if f["tipo"] == t]
        resumo.append(f"| {titulo} | {len(g)} | {sum(f['obrigatoria'] for f in g)} | {sum(f['decisao'] != 'normal' for f in g)} |")
    L += resumo + [""]
    portas = _portas()
    for t, titulo in TIPOS.items():
        g = [f for f in fs if f["tipo"] == t]
        if not g:
            continue
        L += [f"## {titulo}", ""]
        if t == "docker":
            L += ["| Perfil | Serviços | RAM (estimada) | Imagens (estimadas) |", "|---|---|---|---|"]
            for p, nome in dados["perfis"].items():
                sp = [f for f in g if f.get("perfil") == p]
                if sp:
                    L.append(f"| {nome} | {len(sp)} | {sum(f['ram_mb'] for f in sp) / 1024:.1f} GB | {sum(f['disco_gb'] for f in sp):.1f} GB |")
            L.append(f"| **Todos juntos** | {len(g)} | {sum(f['ram_mb'] for f in g) / 1024:.1f} GB | {sum(f['disco_gb'] for f in g):.1f} GB |")
            L += ["", "| Serviço | Grupo | Perfil | Porta | Para quê | Decisão | Ligar |", "|---|---|---|---|---|---|---|"]
            for f in g:
                porta = ", ".join(portas.get(f["conferir"]["container"], [])) or "—"
                L.append(f"| {f['nome']} | {f['grupo']} | {f['perfil']} | {porta} | {f['doc']} | {_decisao(f)} | `{f['ligar']}` |")
        else:
            L += ["| Ferramenta | Grupo | Código aberto | Obrigatória | Para quê | Decisão | Instalar |", "|---|---|---|---|---|---|---|"]
            for f in g:
                L.append(f"| {f['nome']} | {f['grupo']} | {'sim' if f['codigo_aberto'] else 'não'} | {'sim' if f['obrigatoria'] else '—'} "
                         f"| {f['doc']} | {_decisao(f)} | `{f['instalar']}` |")
        L.append("")
    ext = [f for f in fs if f.get("acesso_externo")]
    L += ["## Acesso de fora (revisão de segurança)", "", "| Ferramenta | Tipo | O que abre |", "|---|---|---|"]
    L += [f"| {f['nome']} | {TIPOS[f['tipo']]} | {f['acesso_externo']} |" for f in ext]
    L += ["", "## Paradas ou adiadas por decisão", "", "Registro das decisões: [ADR 0022](../adr/0022-decisoes-de-25-11-2026.md). "
          "O `just validar` avisa quando a data de revisão passa.", "",
          "| Ferramenta | Decisão | Motivo | Rever em |", "|---|---|---|---|"]
    L += [f"| {f['nome']} | {f['decisao']} | {f['motivo']} | {f['rever_em']} |" for f in fs if f["decisao"] != "normal"]
    return "\n".join(L) + "\n"


# ------------------------------------------------------------------ estado no PC
def _rodar(cmd: list[str], timeout: int = 60) -> str | None:
    try:
        return subprocess.run(cmd, capture_output=True, text=True, timeout=timeout, errors="replace").stdout
    except (OSError, subprocess.TimeoutExpired):
        return None


def _caminho_comandos() -> str:
    extras = [Path.home() / ".local/bin", Path.home() / ".local/share/mise/shims", Path.home() / ".cargo/bin", Path.home() / ".dotnet/tools"]
    return os.pathsep.join([str(p) for p in extras] + [os.environ.get("PATH", "")])


def sondas() -> dict:
    """Lê o PC uma vez por tipo (winget, extensões, dpkg, docker). None = não dá para saber daqui."""
    s: dict = {}
    s["winget"] = _rodar(["winget.exe", "list", "--accept-source-agreements", "--disable-interactivity"], 120) if shutil.which("winget.exe") else None
    out = _rodar(["cmd.exe", "/c", "code --list-extensions"], 60) if shutil.which("cmd.exe") else None
    s["extensao"] = {l.strip().lower() for l in out.splitlines() if l.strip()} if out is not None else None
    out = _rodar(["dpkg-query", "-W", "-f=${Package} ${Status}\n"]) if shutil.which("dpkg-query") else None
    s["dpkg"] = {l.split()[0] for l in out.splitlines() if l.endswith("install ok installed")} if out else None
    out = _rodar(["docker", "ps", "-a", "--format", '{{.Label "com.docker.compose.project"}}/{{.Label "com.docker.compose.service"}} {{.State}}']) \
        if shutil.which("docker") else None
    s["container"] = dict(l.split(" ", 1) for l in out.splitlines() if " " in l) if out is not None else None
    s["path"] = _caminho_comandos()
    return s


def estado_de(f: dict, s: dict) -> dict:
    tipo_c, alvo = next(iter(f["conferir"].items()))
    inst = rod = None
    if tipo_c == "winget":
        inst = None if s["winget"] is None else alvo in s["winget"]
    elif tipo_c == "extensao":
        inst = None if s["extensao"] is None else alvo in s["extensao"]
    elif tipo_c == "dpkg":
        inst = None if s["dpkg"] is None else alvo in s["dpkg"]
    elif tipo_c == "comando":
        inst = shutil.which(alvo, path=s["path"]) is not None
    elif tipo_c == "arquivo":
        inst = Path(os.path.expanduser(alvo)).exists()
    elif tipo_c == "systemd":
        ativo = _rodar(["systemctl", "--user", "is-active", alvo], 10)
        if (ativo or "").strip() != "active":
            ativo = _rodar(["systemctl", "is-active", alvo], 10)
        enab = _rodar(["systemctl", "--user", "is-enabled", alvo], 10)
        inst = (enab or "").strip() not in ("", "not-found") or (ativo or "").strip() == "active"
        rod = (ativo or "").strip() == "active"
    elif tipo_c == "container":
        if s["container"] is not None:
            st = s["container"].get(alvo)
            inst, rod = st is not None, st == "running"
    return {"id": f["id"], "nome": f["nome"], "tipo": f["tipo"], "obrigatoria": f["obrigatoria"], "decisao": f["decisao"],
            "instalada": inst, "rodando": rod, "instalar": f["instalar"]}


def estado(dados: dict, s: dict | None = None) -> list[dict]:
    s = s or sondas()
    return [estado_de(f, s) for f in dados["ferramentas"]]


def faltando(estados: list[dict]) -> list[dict]:
    """O que conta como falta: obrigatória, decisão normal e não instalada (desconhecido não conta)."""
    return [e for e in estados if e["obrigatoria"] and e["decisao"] == "normal" and e["instalada"] is False]


def revisoes_vencidas(dados: dict, hoje: dt.date | None = None) -> list[dict]:
    """Paradas ou adiadas cuja data de revisão já passou."""
    hoje = hoje or dt.date.today()
    return [f for f in dados["ferramentas"] if f["decisao"] != "normal" and dt.date.fromisoformat(f["rever_em"]) < hoje]


def paradas_presentes(dados: dict, estados: list[dict]) -> list[dict]:
    """Parada ou adiada que abre acesso de fora, mas continua presente: a decisão não foi cumprida no PC.
    Serviço (Docker, systemd) conta só se estiver rodando; programa e CLI contam se estiverem instalados."""
    por_id = {f["id"]: f for f in dados["ferramentas"]}
    def presente(e: dict) -> bool:
        return bool(e["rodando"]) if e["tipo"] in ("docker", "systemd") else bool(e["instalada"])
    return [e for e in estados if e["decisao"] != "normal" and presente(e) and por_id[e["id"]].get("acesso_externo")]


PORTAS_SO_LOCAIS = (11434, 5432, 6379)  # Ollama do Windows e AMKaixara (ADR 0022)


def portas_expostas_windows(portas: tuple[int, ...] = PORTAS_SO_LOCAIS, linhas: str | None = None) -> list[tuple[int, str]] | None:
    """Portas que escutam fora do loopback no Windows. None = não dá para saber daqui (sem PowerShell)."""
    if linhas is None:
        if not shutil.which("powershell.exe"):
            return None
        lista = ",".join(str(p) for p in portas)
        linhas = _rodar(["powershell.exe", "-NoProfile", "-Command",
                         f"Get-NetTCPConnection -State Listen -LocalPort {lista} -ErrorAction SilentlyContinue | "
                         "ForEach-Object { \"$($_.LocalPort) $($_.LocalAddress)\" }"], 30)
        if linhas is None:
            return None
    abertas = []
    for l in linhas.replace("\r", "").splitlines():
        partes = l.split()
        if len(partes) == 2 and partes[0].isdigit() and partes[1] not in ("127.0.0.1", "::1"):
            abertas.append((int(partes[0]), partes[1]))
    return sorted(set(abertas))


# ------------------------------------------------------------------ linha de comando
def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--check", action="store_true", help="falha se o registro, as fontes ou a doc divergirem")
    ap.add_argument("--estado", action="store_true", help="mostra o que está instalado e rodando neste PC")
    ap.add_argument("--faltando", action="store_true", help="com --estado: só o que conta como falta")
    ap.add_argument("--json", action="store_true", help="com --estado: saída em JSON")
    a = ap.parse_args(argv)
    dados = carregar()
    erros = validar(dados)
    if not erros:
        erros += conferir_fontes(dados)
    if erros:
        print("\n".join(f"ERRO: {e}" for e in erros), file=sys.stderr)
        return 1
    if a.estado:
        est = estado(dados)
        lista = faltando(est) if a.faltando else est
        if a.json:
            print(json.dumps(lista, ensure_ascii=False, indent=1))
        else:
            sim = {True: "sim", False: "NÃO", None: "?"}
            for e in lista:
                print(f"{e['tipo']:8} {e['nome'][:34]:34} instalada={sim[e['instalada']]:3} rodando={sim[e['rodando']] if e['tipo'] in ('docker', 'systemd') else '-':3} "
                      f"{'obrig' if e['obrigatoria'] else 'opc  '} {e['decisao']}")
            print(f"\nFaltando (obrigatória, decisão normal): {len(faltando(est))}")
        return 0
    md = gerar_md(dados)
    if a.check:
        if not MD.exists() or MD.read_text(encoding="utf-8") != md:
            print(f"ERRO: {MD.relative_to(RAIZ)} desatualizado: rode python3 tools/ferramentas/ferramentas.py", file=sys.stderr)
            return 1
        print(f"Ferramentas: {len(dados['ferramentas'])} registradas, fontes e documentação conferidas.")
        return 0
    MD.write_text(md, encoding="utf-8")
    print(f"Gerado {MD.relative_to(RAIZ)} ({len(dados['ferramentas'])} ferramentas).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
