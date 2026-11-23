#!/usr/bin/env python3
"""Deixa a visibilidade dos repositórios no GitHub igual à de repos.json, sem IA e sempre com o seu ok.

    just repos-visibilidade              # só confere: mostra o que está diferente (não muda nada)
    just repos-visibilidade --aplicar    # mostra o plano, pede a sua confirmação e só então muda

A chave do GitHub vem do KeePassXC (scripts/wsl/segredos.sh, entrada GitHub/gh-admin) e existe só
no ambiente deste comando: nada fica salvo em arquivo. Crie a chave uma vez:
  GitHub → Settings → Developer settings → Fine-grained tokens → Generate new token
  Repository access: All repositories · Permissions: Administration = Read and write · validade: 90 dias
  Guarde no KeePassXC no grupo GitHub, título gh-admin, campo Senha.

Regras de segurança:
- Nunca muda nada sem você digitar a confirmação (não existe opção para pular).
- Repositório com site no GitHub Pages ou com estrelas pede confirmação própria, digitando o nome,
  porque no plano gratuito o site sai do ar e as estrelas somem ao ficar privado.
- Fork de repositório público não pode virar privado (regra do GitHub): só avisa.
- Cada mudança vai para a auditoria do núcleo (nucleo.db), com você como quem aprovou.
"""
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]
DADOS = RAIZ / "repos.json"
DONO = "AlanMateus17"


def desejada(texto: str | None) -> str | None:
    """'privado' → private; 'público', 'público (GitHub Pages)' → public; vazio → None (não mexe)."""
    t = (texto or "").strip().lower()
    if t.startswith("privad"):
        return "private"
    if t.startswith("públic") or t.startswith("public"):
        return "public"
    return None


def nome_completo(nome: str) -> str:
    return nome if "/" in nome else f"{DONO}/{nome}"


def alvos(dados: dict) -> list[tuple[str, str]]:
    """(dono/repo, visibilidade desejada) de cada repositório que já existe e tem visibilidade definida."""
    saida = []
    for r in dados["repos"]:
        quer = desejada(r.get("visibilidade"))
        if quer and r.get("status") != "planejado":
            saida.append((nome_completo(r["nome"]), quer))
    return saida


def plano(alvos_: list[tuple[str, str]], atual: dict[str, dict]) -> list[dict]:
    """Compara o desejado com o estado do GitHub. atual[repo] = resposta de GET /repos/{repo} (ou {'erro': ...})."""
    itens = []
    for repo, quer in alvos_:
        a = atual.get(repo, {})
        if "erro" in a:
            itens.append({"repo": repo, "quer": quer, "tem": "?", "acao": "erro", "motivo": a["erro"]})
            continue
        tem = a.get("visibility", "?")
        if tem == quer:
            itens.append({"repo": repo, "quer": quer, "tem": tem, "acao": "ok"})
        elif a.get("fork") and quer == "private":
            itens.append({"repo": repo, "quer": quer, "tem": tem, "acao": "impossivel",
                          "motivo": "fork de repositório público não pode ser privado; apague ou mantenha"})
        elif not a.get("permissions", {}).get("admin", False):
            itens.append({"repo": repo, "quer": quer, "tem": tem, "acao": "impossivel",
                          "motivo": "a chave não tem permissão de administrador neste repositório"})
        else:
            avisos = []
            if quer == "private" and a.get("has_pages"):
                avisos.append("tem site no GitHub Pages: no plano gratuito o site SAI DO AR")
            if quer == "private" and a.get("stargazers_count", 0):
                avisos.append(f"as {a['stargazers_count']} estrela(s) serão apagadas")
            itens.append({"repo": repo, "quer": quer, "tem": tem, "acao": "mudar", "avisos": avisos})
    return itens


def gh(args: list[str]) -> subprocess.CompletedProcess:
    return subprocess.run(["gh", *args], capture_output=True, text=True)


def ler_atual(repos: list[str], rodar=gh) -> dict[str, dict]:
    atual = {}
    for repo in repos:
        r = rodar(["api", f"repos/{repo}"])
        if r.returncode != 0:
            atual[repo] = {"erro": (r.stderr or r.stdout).strip().splitlines()[-1] if (r.stderr or r.stdout).strip() else "falhou"}
        else:
            atual[repo] = json.loads(r.stdout)
    return atual


def mostrar(itens: list[dict]) -> None:
    marca = {"ok": "ok  ", "mudar": "MUDA", "impossivel": "NÃO ", "erro": "ERRO"}
    nome = {"private": "privado", "public": "público", "?": "?"}
    for i in itens:
        linha = f"  [{marca[i['acao']]}] {i['repo']}: {nome[i['tem']]}"
        if i["acao"] != "ok":
            linha += f" → {nome[i['quer']]}"
        print(linha)
        for av in i.get("avisos", []):
            print(f"         atenção: {av}")
        if i.get("motivo"):
            print(f"         {i['motivo']}")


def confirmou_lote(n: int, ler=input) -> bool:
    return ler(f"\nPara mudar {n} repositório(s), digite {n} e Enter (qualquer outra coisa cancela): ").strip() == str(n)


def confirmou_repo(repo: str, ler=input) -> bool:
    return ler(f"  {repo}: digite o nome do repositório para confirmar ({repo.split('/')[1]}): ").strip() == repo.split("/")[1]


def auditar(acao: str, resultado: str) -> None:
    try:
        sys.path.insert(0, str(RAIZ / "tools" / "nucleo"))
        import nucleo  # type: ignore
        con = nucleo.abrir()
        if con is not None:
            nucleo.auditar(con, "repos-visibilidade", acao, "pede-ok", motivo="repos.json é a fonte da visibilidade",
                           resultado=resultado, aprovado_por="alan")
    except Exception as e:  # a auditoria nunca impede a mudança já confirmada, mas avisa
        print(f"  (aviso: não gravei na auditoria do núcleo: {e})")


def aplicar(itens: list[dict], rodar=gh, ler=input) -> int:
    mudar = [i for i in itens if i["acao"] == "mudar"]
    if not mudar:
        print("\nNada para mudar.")
        return 0
    if not confirmou_lote(len(mudar), ler):
        print("Cancelado. Nada foi mudado.")
        return 1
    falhas = 0
    for i in mudar:
        if i.get("avisos") and not confirmou_repo(i["repo"], ler):
            print(f"  pulado: {i['repo']}")
            continue
        r = rodar(["repo", "edit", i["repo"], "--visibility", i["quer"], "--accept-visibility-change-consequences"])
        ok = r.returncode == 0
        falhas += not ok
        print(f"  {'feito' if ok else 'FALHOU'}: {i['repo']} → {i['quer']}" + ("" if ok else f" ({(r.stderr or r.stdout).strip()})"))
        auditar(f"visibilidade {i['repo']} {i['tem']}→{i['quer']}", "feito" if ok else "falhou")
    return 1 if falhas else 0


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    p.add_argument("--aplicar", action="store_true", help="muda o que estiver diferente, depois da sua confirmação")
    a = p.parse_args(argv)
    dados = json.loads(DADOS.read_text(encoding="utf-8"))
    alvos_ = alvos(dados)
    itens = plano(alvos_, ler_atual([r for r, _ in alvos_]))
    print("Visibilidade no GitHub × repos.json")
    mostrar(itens)
    if a.aplicar:
        return aplicar(itens)
    diferentes = sum(i["acao"] in ("mudar", "erro") for i in itens)
    if diferentes:
        print(f"\n{diferentes} diferença(s). Para corrigir: just repos-visibilidade --aplicar")
    return 1 if diferentes else 0


if __name__ == "__main__":
    sys.exit(main())
