#!/usr/bin/env python3
"""Allowlist da Central (ADR 0023): o que pode rodar, com que argumentos e em que nível.

Fonte única: data/central.json. Este módulo só usa a biblioteca padrão, para rodar no just check e no CI.

    python3 tools/central/allowlist.py --check     # toda receita classificada e nenhuma colando argumento no bash
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]
NIVEIS = ("automatico", "avisa", "pede-ok", "so-terminal", "proibido")
EXECUTAVEIS = ("automatico", "avisa", "pede-ok")
MAX_VALOR = 1000
RECEITA_RE = re.compile(r"^([a-z][a-z0-9_-]*)([^:\n]*?):(?!=)(.*)$")


class ErroAllowlist(ValueError):
    """Pedido fora da allowlist: não roda."""


def carregar(raiz: Path = RAIZ) -> dict:
    return json.loads((raiz / "data" / "central.json").read_text(encoding="utf-8"))


def receitas_do_justfile(raiz: Path = RAIZ) -> dict[str, dict]:
    """{nome: {"params": [...], "corpo": [linhas]}} lido do justfile (sem depender do binário just)."""
    receitas: dict[str, dict] = {}
    atual = None
    for linha in (raiz / "justfile").read_text(encoding="utf-8").splitlines():
        if linha.startswith(("    ", "\t")):
            if atual:
                receitas[atual]["corpo"].append(linha.strip())
            continue
        atual = None
        if not linha.strip() or linha.startswith(("#", "set ", "[")):
            continue
        m = RECEITA_RE.match(linha)
        if m and ":=" not in linha.split(":", 1)[0] + ":" + linha.split(":", 1)[1][:1]:
            params = [p.lstrip("+*$").split("=")[0] for p in m.group(2).split()]
            atual = m.group(1)
            receitas[atual] = {"params": params, "corpo": []}
    return receitas


def _padrao(dados: dict, ref: str) -> re.Pattern[str] | None:
    if ref.startswith("texto:"):
        return None
    texto = dados["padroes"].get(ref, ref)
    return re.compile(texto)


def checar(raiz: Path = RAIZ) -> list[str]:
    erros: list[str] = []
    dados = carregar(raiz)
    justfile = receitas_do_justfile(raiz)
    receitas = dados.get("receitas", {})
    for nome in sorted(set(justfile) - set(receitas)):
        erros.append(f"receita '{nome}' do justfile não está em data/central.json: classifique o nível")
    for nome in sorted(set(receitas) - set(justfile)):
        erros.append(f"'{nome}' está em data/central.json mas não existe no justfile")
    for nome, info in justfile.items():
        for linha in info["corpo"]:
            if "{{" in linha:
                erros.append(f"receita '{nome}' cola {{{{…}}}} no texto do bash (injeção): use \"$1\" ou \"$@\" — {linha[:80]}")
    for nome, r in receitas.items():
        if r.get("nivel") not in NIVEIS:
            erros.append(f"{nome}: nível inválido {r.get('nivel')!r}")
        if r.get("area") not in dados.get("areas", {}):
            erros.append(f"{nome}: área desconhecida {r.get('area')!r}")
        refs = [a["padrao"] for a in r.get("args", []) if "padrao" in a]
        refs += [ref for subs in r.get("subcomandos", {}).values() for ref in subs]
        for ref in refs:
            try:
                _padrao(dados, ref)
            except re.error as e:
                erros.append(f"{nome}: padrão {ref!r} inválido: {e}")
        if r.get("gatilhos") and r.get("nivel") not in EXECUTAVEIS:
            erros.append(f"{nome}: tem gatilhos, mas não roda pela Central")
        for sub in r.get("gatilhos_sub", {}):
            if sub not in r.get("subcomandos", {}):
                erros.append(f"{nome}: gatilhos_sub cita '{sub}', que não está em subcomandos")
        for a in r.get("args", []):
            if a.get("flag") and not re.fullmatch(r"--[a-z][a-z0-9-]*", a["flag"]):
                erros.append(f"{nome}: flag inválida {a['flag']!r}")
        for chave in ("subcomandos_pede_ok", "subcomandos_avisa"):
            for sub in r.get(chave, []):
                if sub not in r.get("subcomandos", {}):
                    erros.append(f"{nome}: {chave} cita '{sub}', que não está em subcomandos")
    return erros


def _limpar(valor: object, nome: str, texto_max: int | None) -> str:
    if not isinstance(valor, str):
        raise ErroAllowlist(f"'{nome}' precisa ser texto")
    valor = valor.strip()
    if texto_max is not None:
        valor = " ".join(valor.replace("\r", "\n").split("\n")).strip()
        if len(valor) > texto_max:
            raise ErroAllowlist(f"'{nome}' passa de {texto_max} caracteres")
    elif len(valor) > MAX_VALOR:
        raise ErroAllowlist(f"'{nome}' grande demais")
    if "\x00" in valor:
        raise ErroAllowlist(f"'{nome}' tem caractere proibido")
    if valor.startswith("-"):
        raise ErroAllowlist(f"'{nome}' não pode começar com '-'")
    return valor


def _validar(dados: dict, ref: str, valor: object, nome: str) -> str:
    if ref.startswith("texto:"):
        limpo = _limpar(valor, nome, int(ref.split(":", 1)[1]))
        if not limpo:
            raise ErroAllowlist(f"'{nome}' está vazio")
        return limpo
    limpo = _limpar(valor, nome, None)
    if not _padrao(dados, ref).fullmatch(limpo):
        raise ErroAllowlist(f"'{nome}' = {limpo!r} fora do formato permitido")
    return limpo


def nivel_maior(a: str, b: str) -> str:
    return a if EXECUTAVEIS.index(a) >= EXECUTAVEIS.index(b) else b


def montar(dados: dict, receita: str, campos: dict | None = None, opcoes: list[str] | None = None,
           subcomando: str | None = None) -> tuple[list[str], str]:
    """Valida o pedido e devolve (argumentos depois do nome da receita, nível efetivo). Erro se não puder rodar."""
    campos, opcoes = dict(campos or {}), list(opcoes or [])
    r = dados["receitas"].get(receita)
    if not r:
        raise ErroAllowlist(f"receita '{receita}' não existe na allowlist")
    nivel = r["nivel"]
    if nivel not in EXECUTAVEIS:
        raise ErroAllowlist(f"'{receita}' só roda no terminal: {r.get('motivo', nivel)}")
    args: list[str] = []
    if r.get("subcomandos"):
        if subcomando not in r["subcomandos"]:
            raise ErroAllowlist(f"subcomando {subcomando!r} não permitido em '{receita}'")
        args.append(subcomando)
        for i, ref in enumerate(r["subcomandos"][subcomando], 1):
            args.append(_validar(dados, ref, campos.get(f"sub_{i}", ""), f"{subcomando} #{i}"))
        if subcomando in r.get("subcomandos_pede_ok", []):
            nivel = nivel_maior(nivel, "pede-ok")
        elif subcomando in r.get("subcomandos_avisa", []):
            nivel = nivel_maior(nivel, "avisa")
    elif subcomando:
        raise ErroAllowlist(f"'{receita}' não tem subcomandos")
    for a in r.get("args", []):
        valor = campos.get(a["nome"], "")
        if (valor is None or (isinstance(valor, str) and not valor.strip())):
            if a.get("obrigatorio", True):
                raise ErroAllowlist(f"falta '{a['nome']}'")
            continue
        ref = f"texto:{a['max']}" if a.get("tipo") == "texto" else a["padrao"]
        if a.get("repetir"):
            partes = [_validar(dados, ref, parte, a["nome"]) for parte in _limpar(valor, a["nome"], None).split()]
        else:
            partes = [_validar(dados, ref, valor, a["nome"])]
        for parte in partes:
            args.extend([a["flag"], parte] if a.get("flag") else [parte])
    extras = set(campos) - {a["nome"] for a in r.get("args", [])} - {f"sub_{i}" for i in range(1, 4)}
    if extras:
        raise ErroAllowlist(f"campos desconhecidos: {sorted(extras)}")
    permitidas = set(r.get("opcoes", [])) | set(r.get("opcoes_pede_ok", []))
    for o in opcoes:
        if o not in permitidas:
            raise ErroAllowlist(f"opção {o!r} não permitida em '{receita}'")
        if o in r.get("opcoes_pede_ok", []):
            nivel = nivel_maior(nivel, "pede-ok")
        if o not in args:
            args.append(o)
    return args, nivel


def visiveis(dados: dict) -> dict[str, list[tuple[str, dict]]]:
    """Receitas que aparecem na tela, por área (proibidas não aparecem)."""
    por_area: dict[str, list[tuple[str, dict]]] = {}
    for nome, r in dados["receitas"].items():
        if r["nivel"] != "proibido":
            por_area.setdefault(r["area"], []).append((nome, r))
    return por_area


def main(argv: list[str] | None = None) -> int:
    argv = sys.argv[1:] if argv is None else argv
    if argv[:1] != ["--check"]:
        print(__doc__)
        return 2
    erros = checar()
    for e in erros:
        print(f"ERRO: {e}", file=sys.stderr)
    if not erros:
        d = carregar()
        n = len(d["receitas"])
        por_nivel = {k: sum(1 for r in d["receitas"].values() if r["nivel"] == k) for k in NIVEIS}
        print(f"central.json: {n} receitas classificadas {por_nivel}; nenhuma cola argumento no bash.")
    return 1 if erros else 0


if __name__ == "__main__":
    sys.exit(main())
