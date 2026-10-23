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
ECO = RAIZ / "data" / "ecossistema.json"
MD = RAIZ / "docs" / "implantacao" / "roteiro.md"
HTML = RAIZ / "docs" / "implantacao" / "acompanhamento.html"
TEMPLATE = RAIZ / "tools" / "implantacao" / "acompanhamento.template.html"
AVISO = "<!-- Arquivo GERADO por tools/implantacao/gerar.py a partir de data/implantacao.json. Não edite à mão. -->\n"
QUEM = {"voce": "Você", "script": "Script", "claude": "Claude com você"}
PRECISA = {"compra": "comprar algo", "pagamento": "pagar um serviço", "conteudo": "conteúdo seu pronto (livro, capítulo)"}
ID_RE = re.compile(r"^[a-z0-9-]+$")


def carregar() -> dict:
    return json.loads(DADOS.read_text(encoding="utf-8"))


def carregar_eco() -> dict:
    return json.loads(ECO.read_text(encoding="utf-8"))


def rotulo(b: dict) -> str:
    return b["rotulo"].replace("|", " ").replace("  ", " ")


def cobertura(d: dict, eco: dict) -> dict:
    """Onde cada bloco do setup entra: num passo, a construir, fora de propósito ou para depois (futuro)."""
    blocos = {b["id"]: b for b in eco["blocos"]}
    nos_passos = {x for f in d["fases"] for p in f["passos"] for x in p.get("blocos", [])}
    cob = d.get("cobertura", {})
    construir, nao = cob.get("construir", {}), cob.get("nao_instala", {})
    classificados = nos_passos | set(construir) | set(nao)
    return {
        "blocos": blocos,
        "nos_passos": nos_passos,
        "construir": construir,
        "nao_instala": nao,
        "depois": [b for b in eco["blocos"] if b["futuro"] and b["id"] not in classificados],
        "faltando": [b for b in eco["blocos"] if not b["futuro"] and b["id"] not in classificados],
        "inexistentes": sorted(classificados - set(blocos)),
        "duplicados": sorted((nos_passos & (set(construir) | set(nao))) | (set(construir) & set(nao))),
    }


def validar(d: dict, eco: dict | None = None) -> list[str]:
    eco = eco if eco is not None else carregar_eco()
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
            for x in p.get("precisa", []):
                if x not in PRECISA:
                    erros.append(f"{p['id']}: precisa inválido {x} (use {', '.join(PRECISA)})")
            if not isinstance(p.get("blocos"), list):
                erros.append(f"{p['id']}: falta a lista 'blocos' (o que este passo implanta)")
    c = cobertura(d, eco)
    for b in c["inexistentes"]:
        erros.append(f"bloco {b} citado no roteiro não existe em data/ecossistema.json")
    for b in c["duplicados"]:
        erros.append(f"bloco {b} está num passo e também em 'construir' ou 'nao_instala'")
    for b in c["faltando"]:
        erros.append(f"bloco {b} ({rotulo(b)}) está no setup e fora do roteiro: ponha num passo, em 'construir' ou em 'nao_instala'")
    return erros


def horas(minutos: int) -> str:
    h, m = divmod(minutos, 60)
    return f"{h} h {m:02d} min" if h else f"{m} min"


def gerar_md(d: dict, eco: dict | None = None) -> str:
    eco = eco if eco is not None else carregar_eco()
    c = cobertura(d, eco)
    B = c["blocos"]
    camadas = {k["id"]: k["titulo"] for k in eco["camadas"]}
    total = sum(p["tempo_min"] for f in d["fases"] for p in f["passos"])
    hoje = sum(1 for f in d["fases"] for p in f["passos"] if not p.get("precisa"))
    t_hoje = sum(p["tempo_min"] for f in d["fases"] for p in f["passos"] if not p.get("precisa"))
    n = sum(len(f["passos"]) for f in d["fases"])
    o = [AVISO, "# Roteiro de implantação\n", "[← Implantação](README.md)\n",
         f"{len(d['fases'])} fases, {n} passos, cerca de **{horas(total)}** de trabalho no total. "
         "Cada passo tem um critério de pronto que dá para conferir. A versão para marcar o progresso é o "
         "[`acompanhamento.html`](acompanhamento.html) (e o artefato Implantação AMtech).\n",
         "Legenda de quem faz: **Você** (só você pode: contas, senhas, decisões), **Script** (você roda o comando), "
         "**Claude com você** (o Claude faz pelo conector ou pelo Claude Code, com a sua aprovação).\n",
         f"**Cobertura:** os {len(B)} blocos do [mapa do setup](../mapa.html) estão todos aqui: "
         f"{len(c['nos_passos'] & set(B))} entram nos passos, {len(c['construir'])} são peças a construir, "
         f"{len(c['nao_instala'])} não se instalam e {len(c['depois'])} ficam para depois. "
         "O CI falha se um bloco novo do setup ficar fora do roteiro ([lista completa](#cobertura)).\n",
         f"**Dá para fazer hoje:** {hoje} dos {n} passos ({horas(t_hoje)}) só precisam do notebook e de contas grátis. "
         "Os outros dizem o que falta: comprar algo, pagar um serviço ou ter um conteúdo seu pronto.\n",
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
            if p.get("precisa"):
                o.append("- **Precisa:** " + ", ".join(PRECISA[x] for x in p["precisa"]))
            if p.get("blocos"):
                o.append("- Implanta: " + " · ".join(rotulo(B[b]) for b in p["blocos"]))
            o.append("")
    o += ['<a id="cobertura"></a>\n', "## Cobertura do setup\n",
          "Todo bloco do mapa do setup tem lugar: num passo acima, como peça a construir, como algo que não se instala ou para depois.\n",
          "### Peças a construir\n", "| Bloco | Onde e quando |", "|---|---|"]
    o += [f"| {rotulo(B[b])} | {t} |" for b, t in c["construir"].items()]
    o += ["", "### Não se instala\n", "| Bloco | Por quê |", "|---|---|"]
    o += [f"| {rotulo(B[b])} | {t} |" for b, t in c["nao_instala"].items()]
    o += ["", "### Para depois\n",
          "Marcados como futuro no mapa: entram quando a renda, a decisão ou o negócio justificar. Cada um vira passo neste roteiro quando chegar a hora.\n",
          "| Camada | Blocos |", "|---|---|"]
    por = {}
    for b in c["depois"]:
        por.setdefault(b["camada"], []).append(rotulo(b))
    o += [f"| {camadas.get(k, k)} | {' · '.join(v)} |" for k, v in por.items()]
    o.append("")
    return "\n".join(o)


def dados_html(d: dict, eco: dict) -> dict:
    c = cobertura(d, eco)
    B = c["blocos"]
    camadas = {k["id"]: k["titulo"] for k in eco["camadas"]}
    fases = [{**f, "passos": [{**{k: v for k, v in p.items() if k != "blocos"},
                                "implanta": [rotulo(B[b]) for b in p.get("blocos", [])]} for p in f["passos"]]}
             for f in d["fases"]]
    por = {}
    for b in c["depois"]:
        por.setdefault(camadas.get(b["camada"], b["camada"]), []).append(rotulo(b))
    return {"precisa": PRECISA, "fases": fases, "cob": {
        "total": len(B), "nos_passos": len(c["nos_passos"] & set(B)),
        "construir": [[rotulo(B[b]), t] for b, t in c["construir"].items()],
        "nao_instala": [[rotulo(B[b]), t] for b, t in c["nao_instala"].items()],
        "depois": [[k, v] for k, v in por.items()], "n_depois": len(c["depois"])}}


def gerar_html(d: dict, eco: dict | None = None) -> str:
    eco = eco if eco is not None else carregar_eco()
    dados = json.dumps(dados_html(d, eco), ensure_ascii=False).replace("</", "<\\/")
    corpo = TEMPLATE.read_text(encoding="utf-8").replace("__DATA__", dados)
    return ('<!doctype html>\n<html lang="pt-BR">\n<head>\n<meta charset="utf-8">\n'
            '<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">\n'
            "<!-- Arquivo GERADO por tools/implantacao/gerar.py. Edite o template ou data/implantacao.json. -->\n"
            "</head>\n<body>\n" + corpo + "\n</body>\n</html>\n")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true")
    a = ap.parse_args()
    d, eco = carregar(), carregar_eco()
    erros = validar(d, eco)
    if erros:
        for e in erros:
            print("ERRO:", e, file=sys.stderr)
        return 1
    saidas = {MD: gerar_md(d, eco), HTML: gerar_html(d, eco)}
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
