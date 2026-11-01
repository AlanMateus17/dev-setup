#!/usr/bin/env python3
"""Investimentos: aplica as SUAS metodologias (Barsi, Bazin, Graham, Buffett, Sena e as que você adicionar).

Não é recomendação de investimento: o script só calcula com as regras e os dados que você fornece.
Seus dados ficam em ~/financas (fora do repositório).

    python tools/investimentos/investimentos.py docs [--check]              # docs/investimentos.md (CI)
    python tools/investimentos/investimentos.py iniciar                     # copia os modelos para ~/financas
    python tools/investimentos/investimentos.py avaliar indicadores.csv     # quem passa em cada metodologia
    python tools/investimentos/investimentos.py aporte carteira.csv 800     # para onde vai o aporte (ARCA dentro de ações)
    python tools/investimentos/investimentos.py comparar carteiras.csv      # rentabilidade de cada carteira contra o índice
"""
from __future__ import annotations

import argparse
import csv
import json
import math
import shutil
import sys
import tomllib
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]
DADOS = RAIZ / "data" / "investimentos.json"
MD = RAIZ / "docs" / "investimentos.md"
MODELOS = Path(__file__).resolve().parent / "modelos"
PASTA = Path.home() / "financas"
AVISO = "<!-- Arquivo GERADO por tools/investimentos/investimentos.py a partir de data/investimentos.json. Não edite à mão. -->\n"
STATUS = ["já usa", "adicionar", "avaliar"]
REGRAS = {">=", "<=", ">", "<", "em", "<=teto_bazin", "<=graham", "rank_desc", "rank_asc"}


def carregar() -> dict:
    return json.loads(DADOS.read_text(encoding="utf-8"))


def carregar_config(caminho: Path | None = None) -> dict:
    c = caminho or PASTA / "investimentos.toml"
    if not c.exists():
        c = MODELOS / "investimentos.example.toml"
    return tomllib.loads(c.read_text(encoding="utf-8"))


def validar(d: dict) -> list[str]:
    e = []
    ids = set()
    for m in d["metodologias"]:
        if m["id"] in ids:
            e.append(f"metodologia repetida: {m['id']}")
        ids.add(m["id"])
        if m["status"] not in STATUS:
            e.append(f"{m['id']}: status inválido {m['status']}")
        if not m["fonte"].strip():
            e.append(f"{m['id']}: sem fonte")
        for c in m["criterios"]:
            if c["regra"] not in REGRAS:
                e.append(f"{m['id']}: regra inválida {c['regra']}")
    if sum(d["alocacao_acoes_padrao"].values()) != 100:
        e.append("alocacao_acoes_padrao precisa somar 100")
    return e


# ---------- cálculo ----------

def num(v) -> float | None:
    if v is None:
        return None
    s = str(v).strip().replace("%", "")
    if not s or s in {"-", "—"}:
        return None
    if "," in s:
        s = s.replace(".", "").replace(",", ".")
    try:
        return float(s)
    except ValueError:
        return None


def teto_bazin(linha: dict, taxa_pct: float) -> float | None:
    dm = num(linha.get("dividendo_medio"))
    return round(dm / (taxa_pct / 100), 2) if dm is not None and taxa_pct > 0 else None


def valor_graham(linha: dict) -> float | None:
    lpa, vpa = num(linha.get("lpa")), num(linha.get("vpa"))
    if lpa is None or vpa is None or lpa <= 0 or vpa <= 0:
        return None
    return round(math.sqrt(22.5 * lpa * vpa), 2)


def criterio_ok(c: dict, linha: dict) -> bool | None:
    """True passa, False reprova, None sem dado (não conta como aprovação)."""
    r = c["regra"]
    if r in ("rank_desc", "rank_asc"):
        return None
    if r == "em":
        v = (linha.get(c["chave"]) or "").strip().lower()
        return None if not v else v in c["valor"]
    preco = num(linha.get("preco"))
    if r == "<=teto_bazin":
        t = teto_bazin(linha, c["valor"])
        return None if t is None or preco is None else preco <= t
    if r == "<=graham":
        g = valor_graham(linha)
        return None if g is None or preco is None else preco <= g * (1 - c["valor"] / 100)
    v = num(linha.get(c["chave"]))
    if v is None:
        return None
    return {">=": v >= c["valor"], "<=": v <= c["valor"], ">": v > c["valor"], "<": v < c["valor"]}[r]


def avaliar(linhas: list[dict], d: dict) -> list[dict]:
    met = [m for m in d["metodologias"] if m["criterios"]]
    res = []
    for l in linhas:
        r = {"ticker": l["ticker"], "teto_bazin": teto_bazin(l, 6), "valor_graham": valor_graham(l)}
        for m in met:
            if any(c["regra"].startswith("rank") for c in m["criterios"]):
                continue
            oks = [criterio_ok(c, l) for c in m["criterios"]]
            r[m["id"]] = "sem dado" if None in oks and False not in oks else ("passa" if all(oks) else "não")
        res.append(r)
    # Fórmula Mágica: soma das posições nos dois rankings (menor é melhor); bancos e seguros ficam de fora
    validas = [l for l in linhas if num(l.get("roic")) is not None and num(l.get("ev_ebit")) not in (None, 0)
               and (l.get("setor") or "").lower() not in ("bancos", "seguros")]
    roic = sorted(validas, key=lambda l: -num(l["roic"]))
    ev = sorted(validas, key=lambda l: num(l["ev_ebit"]))
    pontos = {l["ticker"]: roic.index(l) + ev.index(l) + 2 for l in validas}
    ordem = sorted(pontos, key=pontos.get)
    for r in res:
        r["formula_magica"] = f"{ordem.index(r['ticker']) + 1}º" if r["ticker"] in pontos else "fora"
    return res


def ler_csv(caminho: Path) -> list[dict]:
    with caminho.open(encoding="utf-8-sig", newline="") as f:
        amostra = f.read(2048)
        f.seek(0)
        sep = ";" if amostra.count(";") > amostra.count(",") else ","
        return [{k.strip().lower(): (v or "").strip() for k, v in row.items()} for row in csv.DictReader(f, delimiter=sep)]


def aporte(carteira: list[dict], valor: float, cfg: dict, d: dict) -> tuple[list[str], dict]:
    """Divide o aporte entre as metodologias mais abaixo do alvo e aponta candidatos dentro dos limites."""
    avisos = []
    p = cfg.get("portao", {})
    if not (p.get("cartao_zerado") and p.get("reserva_completa")):
        return ["Portão fechado: zere o cartão e complete a reserva antes de aportar em ações (atualize [portao] em investimentos.toml)."], {}
    alvo = cfg.get("alocacao_acoes") or d["alocacao_acoes_padrao"]
    lim = {**d["concentracao_padrao"], **cfg.get("concentracao", {})}
    total = sum(num(l["valor_atual"]) or 0 for l in carteira) + valor
    atual = {k: 0.0 for k in alvo}
    por_ticker, por_setor = {}, {}
    for l in carteira:
        v = num(l["valor_atual"]) or 0
        atual[l["metodo"]] = atual.get(l["metodo"], 0) + v
        por_ticker[l["ticker"]] = por_ticker.get(l["ticker"], 0) + v
        por_setor[l["setor"]] = por_setor.get(l["setor"], 0) + v
    falta = {k: max(0.0, alvo[k] / 100 * total - atual.get(k, 0)) for k in alvo}
    soma = sum(falta.values())
    divisao = {k: round(valor * f / soma, 2) for k, f in falta.items() if f > 0} if soma else {k: round(valor * alvo[k] / 100, 2) for k in alvo}
    teto_emp, teto_set = lim["max_empresa_pct"] / 100 * total, lim["max_setor_pct"] / 100 * total
    for k in divisao:
        cands = sorted({l["ticker"] for l in carteira if l["metodo"] == k}, key=lambda t: por_ticker[t])
        setor = {l["ticker"]: l["setor"] for l in carteira}
        livres = [t for t in cands if por_ticker[t] < teto_emp and por_setor[setor[t]] < teto_set]
        if not livres:
            avisos.append(f"{k}: nenhuma empresa da carteira abaixo dos limites; avalie uma nova pela metodologia.")
        else:
            avisos.append(f"{k}: candidatas dentro dos limites (menor peso primeiro): {', '.join(livres[:3])}")
    n = len(por_ticker)
    if n < lim["min_empresas"]:
        avisos.append(f"A carteira tem {n} empresas; o seu mínimo é {lim['min_empresas']}.")
    for t, v in por_ticker.items():
        if v > teto_emp:
            avisos.append(f"{t} passou de {lim['max_empresa_pct']}% da carteira: não aporte nela.")
    return avisos, divisao


def comparar(linhas: list[dict]) -> list[str]:
    res = []
    ref = None
    for l in linhas:
        inv, atual = num(l["investido"]), num(l["valor_atual"])
        if not inv:
            continue
        r = (atual - inv) / inv * 100
        if l["carteira"].lower() == "indice":
            ref = r
        res.append((l["carteira"], r))
    o = []
    for nome, r in sorted(res, key=lambda x: -x[1]):
        dif = "" if ref is None or nome.lower() == "indice" else f" ({r - ref:+.1f} p.p. contra o índice)"
        o.append(f"{nome}: {r:+.1f}%{dif}")
    return o


# ---------- documentação ----------

def gerar(d: dict) -> str:
    o = [AVISO, "# Investimentos: as suas metodologias, aplicadas por script\n", "[← Índice da documentação](README.md)\n",
         f"> {d['aviso']}\n", "## Regras\n"]
    o += [f"- {x}" for x in d["regras"]]
    o += ["", "## Metodologias\n", "| Metodologia | Tipo | Situação | Ideia |", "|---|---|---|---|"]
    o += [f"| [{m['nome']}](#{m['id']}) | {m['tipo']} | **{m['status']}** | {m['ideia']} |" for m in d["metodologias"]]
    o.append("")
    for m in d["metodologias"]:
        o += [f'<a id="{m["id"]}"></a>', f"### {m['nome']}\n", m["ideia"], ""]
        if m["criterios"]:
            o += ["Critérios que o script confere:"] + [f"- {c['texto']}" for c in m["criterios"]] + [""]
        if m["perguntas"]:
            o += ["Perguntas que só você responde:"] + [f"- {p}" for p in m["perguntas"]] + [""]
        o += [f"**Quando vender:** {m['venda']}", "", f"Fonte: {m['fonte']}", ""]
    c, a = d["concentracao_padrao"], d["alocacao_acoes_padrao"]
    o += ["## ARCA dentro de ações (ponto de partida; você ajusta em investimentos.toml)\n", "| Grupo de metodologia | % alvo |", "|---|---:|"]
    o += [f"| {k} | {v}% |" for k, v in a.items()]
    o += ["", f"Limites: no máximo {c['max_empresa_pct']}% da carteira numa empresa e {c['max_setor_pct']}% num setor; pelo menos {c['min_empresas']} empresas.", "",
          "## Como usar\n", "```bash", "python tools/investimentos/investimentos.py iniciar", "python tools/investimentos/investimentos.py avaliar ~/financas/indicadores.csv",
          "python tools/investimentos/investimentos.py aporte ~/financas/carteira.csv 800", "python tools/investimentos/investimentos.py comparar ~/financas/carteiras.csv", "```", "",
          "Os modelos de CSV estão em tools/investimentos/modelos (tickers inventados). A política completa fica em ~/financas/politica-investimentos.md."]
    return "\n".join(o) + "\n"


def main() -> int:
    ap = argparse.ArgumentParser()
    sp = ap.add_subparsers(dest="cmd", required=True)
    g = sp.add_parser("docs")
    g.add_argument("--check", action="store_true")
    sp.add_parser("iniciar")
    a = sp.add_parser("avaliar")
    a.add_argument("csv", type=Path)
    b = sp.add_parser("aporte")
    b.add_argument("csv", type=Path)
    b.add_argument("valor", type=float)
    b.add_argument("--config", type=Path)
    c = sp.add_parser("comparar")
    c.add_argument("csv", type=Path)
    x = ap.parse_args()
    d = carregar()
    e = validar(d)
    if e:
        print("\n".join("ERRO: " + i for i in e), file=sys.stderr)
        return 1
    if x.cmd == "docs":
        t = gerar(d)
        if x.check:
            if (MD.read_text(encoding="utf-8") if MD.exists() else "") != t:
                print("docs/investimentos.md está desatualizado. Rode: python tools/investimentos/investimentos.py docs", file=sys.stderr)
                return 1
            print(f"Investimentos em dia: {len(d['metodologias'])} metodologias.")
            return 0
        MD.write_text(t, encoding="utf-8")
        print(f"Gerado {MD.relative_to(RAIZ)}")
    elif x.cmd == "iniciar":
        PASTA.mkdir(exist_ok=True)
        for m in MODELOS.iterdir():
            destino = PASTA / m.name.replace(".example", "")
            if not destino.exists():
                shutil.copy(m, destino)
                print(f"criado: {destino}")
    elif x.cmd == "avaliar":
        res = avaliar(ler_csv(x.csv), d)
        cols = [k for k in res[0] if k not in ("ticker",)] if res else []
        print("ticker | " + " | ".join(cols))
        for r in res:
            print(r["ticker"] + " | " + " | ".join(str(r[k]) if r[k] is not None else "—" for k in cols))
        print("\n" + d["aviso"])
    elif x.cmd == "aporte":
        avisos, div = aporte(ler_csv(x.csv), x.valor, carregar_config(x.config), d)
        for k, v in div.items():
            print(f"{k}: R$ {v:.2f}")
        print("\n".join(avisos))
    elif x.cmd == "comparar":
        print("\n".join(comparar(ler_csv(x.csv))))
    return 0


if __name__ == "__main__":
    sys.exit(main())
