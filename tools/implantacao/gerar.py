#!/usr/bin/env python3
"""Gera o roteiro de implantação a partir de data/implantacao.json.

Saídas: docs/implantacao/roteiro.md e docs/implantacao/acompanhamento.html.

    python tools/implantacao/gerar.py          # valida e regenera
    python tools/implantacao/gerar.py --check  # falha se algo estiver desatualizado (CI)
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]
DADOS = RAIZ / "data" / "implantacao.json"
MD = RAIZ / "docs" / "implantacao" / "roteiro.md"
HTML = RAIZ / "docs" / "implantacao" / "acompanhamento.html"
TEMPLATE = RAIZ / "tools" / "implantacao" / "acompanhamento.template.html"
AVISO = "<!-- Arquivo GERADO por tools/implantacao/gerar.py a partir de data/implantacao.json. Não edite à mão. -->\n"
QUEM = {"voce": "Você", "script": "Script", "claude": "Claude com você"}
ID_RE = re.compile(r"^[a-z0-9-]+$")


def carregar() -> dict:
    return json.loads(DADOS.read_text(encoding="utf-8"))


def validar(d: dict) -> list[str]:
    erros, vistos = [], set()
    for f in d["fases"]:
        if not ID_RE.match(f["id"]):
            erros.append(f"fase com id inválido: {f['id']}")
        if not f["passos"]:
            erros.append(f"fase {f['id']} sem passos")
        for p in f["passos"]:
            if p["id"] in vistos:
                erros.append(f"passo repetido: {p['id']}")
            vistos.add(p["id"])
            if not ID_RE.match(p["id"]):
                erros.append(f"passo com id inválido: {p['id']}")
            if p["quem"] not in QUEM:
                erros.append(f"{p['id']}: quem inválido {p['quem']}")
            if not isinstance(p["tempo_min"], int) or p["tempo_min"] <= 0:
                erros.append(f"{p['id']}: tempo_min deve ser inteiro positivo")
            if not p["pronto"].strip():
                erros.append(f"{p['id']}: sem critério de pronto")
            for arq in re.findall(r"(scripts/[\w./-]+\.(?:ps1|sh)|tools/[\w./-]+\.py|infra/[\w./-]+)", p.get("comando", "").replace("\\", "/")):
                if not (RAIZ / arq).exists():
                    erros.append(f"{p['id']}: o comando cita {arq}, que não existe")
    return erros


def horas(minutos: int) -> str:
    h, m = divmod(minutos, 60)
    return f"{h} h {m:02d} min" if h else f"{m} min"


def gerar_md(d: dict) -> str:
    total = sum(p["tempo_min"] for f in d["fases"] for p in f["passos"])
    n = sum(len(f["passos"]) for f in d["fases"])
    o = [AVISO, "# Roteiro de implantação\n", "[← Implantação](README.md)\n",
         f"{len(d['fases'])} fases, {n} passos, cerca de **{horas(total)}** de trabalho no total. "
         "Cada passo tem um critério de pronto que dá para conferir. A versão para marcar o progresso é o "
         "[`acompanhamento.html`](acompanhamento.html) (e o artefato Implantação AMtech).\n",
         "Legenda de quem faz: **Você** (só você pode: contas, senhas, decisões), **Script** (você roda o comando), "
         "**Claude com você** (o Claude faz pelo conector ou pelo Claude Code, com a sua aprovação).\n",
         "| Fase | Objetivo | Passos | Tempo |", "|---|---|---:|---:|"]
    for i, f in enumerate(d["fases"]):
        t = sum(p["tempo_min"] for p in f["passos"])
        o.append(f"| [{i} · {f['titulo']}](#{f['id']}) | {f['objetivo']} | {len(f['passos'])} | {horas(t)} |")
    o.append("")
    for i, f in enumerate(d["fases"]):
        o.append(f'<a id="{f["id"]}"></a>\n')
        o.append(f"## {i} · {f['titulo']}\n")
        o.append(f"{f['objetivo']}\n")
        for j, p in enumerate(f["passos"], 1):
            o.append(f"### {i}.{j} {p['titulo']}\n")
            o.append(f"**{QUEM[p['quem']]}** · {horas(p['tempo_min'])}\n")
            if p.get("comando"):
                lang = "powershell" if "powershell" in p["comando"] or p["comando"].startswith("wsl ") else ("text" if p["comando"].startswith("http") else "bash")
                o.append(f"```{lang}\n{p['comando']}\n```\n")
            o.append(f"- [ ] **Pronto quando:** {p['pronto']}")
            if p.get("nota"):
                o.append(f"- {p['nota']}")
            o.append("")
    return "\n".join(o)


def gerar_html(d: dict) -> str:
    corpo = TEMPLATE.read_text(encoding="utf-8").replace("__DATA__", json.dumps(d, ensure_ascii=False).replace("</", "<\\/"))
    return ('<!doctype html>\n<html lang="pt-BR">\n<head>\n<meta charset="utf-8">\n'
            '<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">\n'
            "<!-- Arquivo GERADO por tools/implantacao/gerar.py. Edite o template ou data/implantacao.json. -->\n"
            "</head>\n<body>\n" + corpo + "\n</body>\n</html>\n")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true")
    a = ap.parse_args()
    d = carregar()
    erros = validar(d)
    if erros:
        for e in erros:
            print("ERRO:", e, file=sys.stderr)
        return 1
    saidas = {MD: gerar_md(d), HTML: gerar_html(d)}
    if a.check:
        ruins = [c for c, t in saidas.items() if (c.read_text(encoding="utf-8") if c.exists() else "") != t]
        for c in ruins:
            print(f"{c.relative_to(RAIZ)} está desatualizado. Rode: python tools/implantacao/gerar.py", file=sys.stderr)
        if ruins:
            return 1
        print("Roteiro de implantação em dia.")
        return 0
    for c, t in saidas.items():
        c.write_text(t, encoding="utf-8")
        print(f"Gerado {c.relative_to(RAIZ)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
