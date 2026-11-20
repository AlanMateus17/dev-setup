#!/usr/bin/env python3
"""Gera docs/empresas.md a partir de data/empresas.json, data/portfolio.json e data/softwares.json:
as empresas do Grupo AMtech Digital, o estado de cada uma e todos os produtos de cada uma.

    python3 tools/empresas/empresas.py          # regenera
    python3 tools/empresas/empresas.py --check  # falha se estiver desatualizado ou se algum produto ficar sem empresa
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]
EMPRESAS = RAIZ / "data" / "empresas.json"
PORTFOLIO = RAIZ / "data" / "portfolio.json"
SOFTWARES = RAIZ / "data" / "softwares.json"
SAIDA = RAIZ / "docs" / "empresas.md"
AVISO = "<!-- Arquivo GERADO por tools/empresas/empresas.py a partir de data/empresas.json. Não edite à mão. -->\n"
ESTADOS = {"ativa": "Ativa", "pausada": "Pausada", "software-primeiro": "Software primeiro, empresa depois"}
VEREDITO = {"agora": "agora", "proxima": "próxima", "manter": "manter", "fila": "fila", "em2027": "2027",
            "decidir": "decidir", "descartar": "descartada"}


def carregar() -> tuple[dict, dict, dict]:
    ler = lambda p: json.loads(p.read_text(encoding="utf-8"))  # noqa: E731
    return ler(EMPRESAS), ler(PORTFOLIO), ler(SOFTWARES)


def dono_das_ofertas(e: dict, p: dict) -> dict[str, str]:
    por_frente = {f: x["id"] for x in e["empresas"] for f in x["frentes"]}
    extra = {o: x["id"] for x in e["empresas"] for o in x.get("ofertas_extra", [])}
    return {o["id"]: extra.get(o["id"], por_frente.get(o["frente"], "")) for o in p["ofertas"]}


def validar(e: dict, p: dict, s: dict) -> list[str]:
    erros, vistas = [], {}
    ofs = {o["id"] for o in p["ofertas"]}
    suites = {x["id"] for x in s.get("suites", [])}
    for x in e["empresas"]:
        if x["estado"] not in ESTADOS:
            erros.append(f"{x['id']}: estado inválido {x['estado']}")
        if x["estado"] == "software-primeiro" and not all(x.get(k) for k in ("fase1", "fase2", "gatilho")):
            erros.append(f"{x['id']}: software primeiro precisa de fase1, fase2 e gatilho")
        for f in x["frentes"]:
            if f not in p["frentes"]:
                erros.append(f"{x['id']}: frente inexistente {f}")
            if f in vistas:
                erros.append(f"frente {f} em duas empresas ({vistas[f]} e {x['id']})")
            vistas[f] = x["id"]
        for o in x.get("ofertas_extra", []):
            if o not in ofs:
                erros.append(f"{x['id']}: oferta inexistente {o}")
        for su in x.get("suites", []):
            if su not in suites:
                erros.append(f"{x['id']}: suíte inexistente {su}")
    for f in p["frentes"]:
        if f not in vistas and f not in e.get("fora", {}):
            erros.append(f"frente {f} sem empresa (ponha numa empresa ou em 'fora' com o motivo)")
    for o, d in dono_das_ofertas(e, p).items():
        frente = next(x["frente"] for x in p["ofertas"] if x["id"] == o)
        if not d and frente not in e.get("fora", {}):
            erros.append(f"oferta {o} sem empresa")
    return erros


def gerar(e: dict, p: dict, s: dict) -> str:
    dono = dono_das_ofertas(e, p)
    nome_sw = {x["id"]: x["nome"].split(" (")[0] for x in s["softwares"]}
    o = [AVISO, f"# Empresas do {e['grupo']}\n", "[← Índice da documentação](../README.md)\n",
         f"**Regra:** {e['regra']}\n", "| Empresa | Estado | O que faz | Produtos | Agora |\n|---|---|---|---:|---|"]
    for x in e["empresas"]:
        g = [of for of in p["ofertas"] if dono[of["id"]] == x["id"] and of["veredito"] != "descartar"]
        ag = ", ".join(of["nome"].split(" (")[0] for of in g if of["veredito"] == "agora") or "—"
        o.append(f"| [{x['nome']}](#{x['id']}) | {ESTADOS[x['estado']]} | {x['faz']} | {len(g)} | {ag} |")
    o.append("")
    for x in e["empresas"]:
        o.append(f'<a id="{x["id"]}"></a>\n')
        o.append(f"## {x['nome']}\n")
        o.append(f"**{ESTADOS[x['estado']]}.** {x['faz']}.\n")
        if x["estado"] == "software-primeiro":
            o.append(f"1. **Primeiro, software:** {x['fase1']}.")
            o.append(f"2. **Depois, empresa:** {x['fase2']}.")
            o.append(f"3. **Quando vira empresa:** {x['gatilho']} (a decisão é sua).\n")
        for su in x.get("suites", []):
            sx = next(y for y in s["suites"] if y["id"] == su)
            o.append(f"- **Suíte {sx['ordem']}, {sx['nome']}:** {', '.join(nome_sw[i] for i in sx['sistemas'])} ({sx['estado']})")
        if x.get("suites"):
            o.append("")
        g = sorted((of for of in p["ofertas"] if dono[of["id"]] == x["id"]),
                   key=lambda of: (of["veredito"] == "descartar", of.get("onda") is None, of.get("onda") or 0, of["nome"]))
        o.append("| Produto | Tipo | Onda | Veredito |\n|---|---|---|---|")
        for of in g:
            onda = "—" if of.get("onda") is None else str(of["onda"])
            o.append(f"| {of['nome'].replace('|', '/')} | {of.get('tipo', '')} | {onda} | {VEREDITO[of['veredito']]} |")
        o.append("")
    for f, motivo in e.get("fora", {}).items():
        o.append(f"**Fora das empresas — {p['frentes'][f]}:** {motivo}.\n")
    return "\n".join(o)


def main() -> int:
    e, p, s = carregar()
    erros = validar(e, p, s)
    for x in erros:
        print("ERRO:", x, file=sys.stderr)
    if erros:
        return 1
    txt = gerar(e, p, s)
    if "--check" in sys.argv:
        if not SAIDA.exists() or SAIDA.read_text(encoding="utf-8") != txt:
            print("docs/empresas.md está desatualizado. Rode: python3 tools/empresas/empresas.py", file=sys.stderr)
            return 1
        print(f"Empresas em dia: {len(e['empresas'])}.")
        return 0
    SAIDA.write_text(txt, encoding="utf-8")
    print(f"Gerado {SAIDA.relative_to(RAIZ)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
