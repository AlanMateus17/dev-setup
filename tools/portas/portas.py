#!/usr/bin/env python3
"""Portas do host de todos os serviços (fase 0 da Central AMtech).

A fonte única é data/portas.json. Este script lê os infra/*/compose.yaml e confere que:
  1. nenhuma porta do host se repete (por protocolo), nem com as reservadas (Portal, OliveTin, Central);
  2. o portas.json lista exatamente as portas que os compose.yaml publicam.

    python3 tools/portas/portas.py            # tabela das portas
    python3 tools/portas/portas.py --check    # o que o just check e o CI rodam
    python3 tools/portas/portas.py --gerar    # reescreve data/portas.json a partir dos compose.yaml (mantém nomes e reservas)

Só biblioteca padrão: os compose.yaml do repositório seguem o mesmo formato (serviço com 2 espaços, "ports:" com 4).
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]
DADOS = RAIZ / "data" / "portas.json"

_SERVICO = re.compile(r"^  ([A-Za-z0-9_.-]+):\s*$")
_PERFIL = re.compile(r"^    profiles:\s*\[([^\]]*)\]")
_PORTA = re.compile(r'^\s+-\s*"?(?:(?:\$\{[A-Z_]+:-)?[0-9.]+\}?:)?(\d+):(\d+)(?:/(tcp|udp))?"?\s*$')


def ler_compose(caminho: Path) -> list[dict]:
    """Devolve as portas publicadas no host por um compose.yaml."""
    portas: list[dict] = []
    grupo = caminho.parent.name
    secao = servico = perfil = None
    em_ports = False
    for linha in caminho.read_text(encoding="utf-8").splitlines():
        if re.match(r"^[A-Za-z]", linha):
            secao = linha.split(":")[0]
            servico, em_ports = None, False
            continue
        if secao != "services":
            continue
        m = _SERVICO.match(linha)
        if m:
            servico, perfil, em_ports = m.group(1), None, False
            continue
        m = _PERFIL.match(linha)
        if m and servico:
            perfil = m.group(1).strip().strip("'\"") or None
            continue
        if re.match(r"^    ports:\s*$", linha):
            em_ports = True
            continue
        if em_ports:
            m = _PORTA.match(linha)
            if m:
                portas.append({
                    "id": f"{grupo}-{servico}-{m.group(1)}" if _conta(portas, servico) else f"{grupo}-{servico}",
                    "grupo": grupo,
                    "servico": servico,
                    "porta": int(m.group(1)),
                    "interna": int(m.group(2)),
                    "protocolo": m.group(3) or "tcp",
                    "perfil": perfil,
                    "compose": str(caminho.relative_to(RAIZ)),
                })
                continue
            if re.match(r"^    \S", linha) or re.match(r"^  \S", linha):
                em_ports = False
    return portas


def _conta(portas: list[dict], servico: str) -> int:
    return sum(1 for p in portas if p["servico"] == servico)


def ler_todos(raiz: Path = RAIZ) -> list[dict]:
    todas: list[dict] = []
    for c in sorted((raiz / "infra").glob("*/compose.yaml")):
        todas.extend(ler_compose(c))
    return todas


def repetidas(entradas: list[dict]) -> list[str]:
    """Portas do host usadas por mais de um serviço (mesmo protocolo)."""
    vistas: dict[tuple[int, str], list[str]] = {}
    for e in entradas:
        vistas.setdefault((e["porta"], e.get("protocolo", "tcp")), []).append(e["id"])
    return [f"{p}/{proto}: {', '.join(ids)}" for (p, proto), ids in sorted(vistas.items()) if len(ids) > 1]


def conferir(dados: dict, compose: list[dict]) -> list[str]:
    erros: list[str] = []
    servicos = dados.get("servicos", [])
    reservadas = [{**r, "protocolo": r.get("protocolo", "tcp")} for r in dados.get("reservadas", [])]
    for r in repetidas(servicos + reservadas):
        erros.append(f"porta repetida no host: {r}")
    chave = lambda e: (e["compose"], e["servico"], e["porta"], e.get("protocolo", "tcp"))  # noqa: E731
    no_json = {chave(e) for e in servicos}
    nos_compose = {chave(e) for e in compose}
    for c in sorted(nos_compose - no_json):
        erros.append(f"{c[0]}: {c[1]} publica {c[2]}/{c[3]}, mas não está em data/portas.json (rode --gerar)")
    for c in sorted(no_json - nos_compose):
        erros.append(f"data/portas.json: {c[1]} {c[2]}/{c[3]} não existe mais em {c[0]} (rode --gerar)")
    return erros


def gerar(dados: dict, compose: list[dict]) -> dict:
    antigos = {e["id"]: e for e in dados.get("servicos", [])}
    novos = []
    for e in compose:
        nome = antigos.get(e["id"], {}).get("nome", e["servico"])
        tela = antigos.get(e["id"], {}).get("tela", e["protocolo"] == "tcp")
        novos.append({"id": e["id"], "nome": nome, **{k: e[k] for k in ("grupo", "servico", "porta", "interna", "protocolo", "perfil", "compose")}, "tela": tela})
    return {
        "_leia": dados.get("_leia", "Fonte única das portas do host. Confira com: python3 tools/portas/portas.py --check"),
        "reservadas": dados.get("reservadas", []),
        "servicos": novos,
    }


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--check", action="store_true", help="falha se houver porta repetida ou divergência com os compose.yaml")
    ap.add_argument("--gerar", action="store_true", help="reescreve data/portas.json a partir dos compose.yaml")
    a = ap.parse_args(argv)
    dados = json.loads(DADOS.read_text(encoding="utf-8")) if DADOS.exists() else {}
    compose = ler_todos()
    if a.gerar:
        DADOS.write_text(json.dumps(gerar(dados, compose), ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
        print(f"data/portas.json: {len(compose)} portas")
        return 0
    if a.check:
        erros = conferir(dados, compose)
        for e in erros:
            print(f"ERRO {e}", file=sys.stderr)
        return 1 if erros else 0
    for e in sorted(dados.get("servicos", []) + dados.get("reservadas", []), key=lambda x: x["porta"]):
        print(f"{e['porta']:>6}/{e.get('protocolo', 'tcp'):<3}  {e.get('grupo', 'reservada'):<14} {e.get('nome', e['id'])}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
