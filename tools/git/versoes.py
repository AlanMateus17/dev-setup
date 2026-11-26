#!/usr/bin/env python3
"""Toda versão citada no ESTADO.md (vX.Y.Z) tem cabeçalho "## [X.Y.Z] - AAAA-MM-DD" no CHANGELOG.md.

    python3 tools/git/versoes.py --check    # o just check roda; sai com 1 e lista as que faltam

Pega o erro do #44 (26/11/2026): ao resolver o CHANGELOG, o cabeçalho da 2.57.0 virou " - 2026-11-25".
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]
CABECALHO = re.compile(r"^## \[(\d+\.\d+\.\d+)\] - \d{4}-\d{2}-\d{2}$", re.M)
CITADA = re.compile(r"\bv(\d+\.\d+\.\d+)\b")


def chave(v: str) -> tuple[int, ...]:
    return tuple(int(x) for x in v.split("."))


def faltando(estado: str, changelog: str) -> list[str]:
    """Versões citadas no ESTADO sem cabeçalho válido no CHANGELOG, em ordem."""
    return sorted(set(CITADA.findall(estado)) - set(CABECALHO.findall(changelog)), key=chave)


def main() -> int:
    falta = faltando((RAIZ / "ESTADO.md").read_text(encoding="utf-8"), (RAIZ / "CHANGELOG.md").read_text(encoding="utf-8"))
    if falta:
        print("Versões do ESTADO.md sem cabeçalho '## [X.Y.Z] - AAAA-MM-DD' no CHANGELOG.md: " + ", ".join(falta))
        return 1
    if "--check" not in sys.argv:
        print("Versões: ESTADO e CHANGELOG batem.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
