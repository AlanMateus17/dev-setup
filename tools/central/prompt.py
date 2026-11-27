"""Do pedido em português ao plano de receitas, gastando o mínimo de tokens (ADR 0023, seção Prompt).

Escada, para no primeiro degrau que resolve:
  1. Regra (0 tokens): frases-gatilho de data/central.json levam direto à receita.
  2. Motor de decisão (0 tokens): "aprovar, pagar, publicar…" é decisão sua; nenhuma IA decide por você.
  3. IA local (Ollama, R$ 0): recebe só as receitas mais parecidas com o pedido e devolve um plano em JSON.
  4. Sem IA local no ar: trabalho novo vira 'pedir' (a fila, que já tem a escada de modelos do motor).
Todo plano passa por allowlist.montar antes de rodar. Nada aqui chama IA paga. Só biblioteca padrão.
"""
from __future__ import annotations

import json
import os
import re
import sys
import unicodedata
import urllib.error
import urllib.request
from dataclasses import dataclass, field
from pathlib import Path

import allowlist

RAIZ = Path(__file__).resolve().parents[2]
MAX_PASSOS = 3
TEXTO_INTEIRO = {"pedir", "triagem", "motor", "arquiteto", "arquiteto-claude"}  # recebem o pedido todo
CANDIDATOS_IA = 12
OLLAMA = os.environ.get("AMTECH_CENTRAL_OLLAMA", "http://127.0.0.1:11434")
MODELO = os.environ.get("AMTECH_CENTRAL_MODELO", "qwen2.5:7b")
VAZIAS = set("a o as os um uma de do da dos das no na nos nas em e ou que para pra por com se me meu minha meus minhas "
             "eu voce isso esse essa este esta ja so mais muito como qual quais quando onde ao aos pelo pela".split())


def norm(texto: str) -> str:
    t = unicodedata.normalize("NFKD", texto.lower())
    t = "".join(c for c in t if not unicodedata.combining(c))
    return " ".join(re.sub(r"[^a-z0-9.#\- ]", " ", t).split())


def palavras(texto: str) -> set[str]:
    return {p for p in norm(texto).split() if len(p) > 2 and p not in VAZIAS}


@dataclass
class Passo:
    receita: str
    subcomando: str | None = None
    campos: dict = field(default_factory=dict)
    opcoes: list = field(default_factory=list)
    args: list = field(default_factory=list)
    nivel: str = ""
    erro: str = ""

    def rotulo(self) -> str:
        return " ".join(p for p in (self.receita, *(self.args or ([self.subcomando] if self.subcomando else []))) if p)


@dataclass
class Plano:
    texto: str
    origem: str  # regra | voce | ia-local | fila | nada
    passos: list[Passo] = field(default_factory=list)
    resposta: str = ""
    sensivel: list[str] = field(default_factory=list)
    tokens: int = 0

    @property
    def validos(self) -> list[Passo]:
        return [p for p in self.passos if not p.erro]

    @property
    def roda_sozinho(self) -> bool:
        """Só roda sem clique o que veio de regra fixa e só lê (automatico)."""
        return self.origem == "regra" and bool(self.validos) and all(p.nivel == "automatico" for p in self.validos)

    def para_json(self) -> str:
        return json.dumps({"origem": self.origem, "resposta": self.resposta, "sensivel": self.sensivel, "tokens": self.tokens,
                           "passos": [p.__dict__ for p in self.passos]}, ensure_ascii=False)


# ------------------------------------------------------------------ degrau 1: regra
def _extrair_campos(dados: dict, nome_receita: str, r: dict, texto: str, frase: str, sub: str | None) -> dict:
    """Tira do pedido os valores que a receita precisa, sem IA. Texto livre = o pedido sem a frase-gatilho."""
    t = norm(texto)
    campos: dict = {}
    resto = texto
    if frase and nome_receita not in TEXTO_INTEIRO:
        m = re.search(re.escape(frase), t)
        if m:
            resto = " ".join(texto.split()[len(t[:m.end()].split()):]) or texto
    refs = [(a["nome"], a) for a in r.get("args", [])]
    if sub:
        refs += [(f"sub_{i}", {"padrao": ref, "obrigatorio": True}) for i, ref in enumerate(r["subcomandos"][sub], 1)]
    for nome, a in refs:
        if a.get("tipo") == "texto" or str(a.get("padrao", "")).startswith("texto:"):
            campos[nome] = resto.strip(" :,.?!") if resto.strip(" :,.?!") else texto
            continue
        rx = re.compile(dados["padroes"].get(a["padrao"], a["padrao"]))
        achados = [p.strip("#.,?!") for p in t.split() if rx.fullmatch(p.strip("#.,?!"))]
        if achados:
            campos[nome] = " ".join(achados) if a.get("repetir") else achados[0]
    return campos


def por_regra(dados: dict, texto: str) -> list[Passo]:
    t = f" {norm(texto)} "
    achados: list[tuple[int, Passo]] = []
    for nome, r in dados["receitas"].items():
        if r["nivel"] not in allowlist.EXECUTAVEIS:
            continue
        opcoes_sub = [(None, r.get("gatilhos", []))] + list(r.get("gatilhos_sub", {}).items())
        for sub, frases in opcoes_sub:
            melhor = max((f for f in frases if f" {f} " in t or t.strip().startswith(f + " ") or t.strip() == f),
                         key=len, default=None)
            if melhor:
                sub_real = sub if sub else (None if not r.get("subcomandos") else None)
                if r.get("subcomandos") and not sub_real:
                    continue
                campos = _extrair_campos(dados, nome, r, texto, melhor, sub_real)
                achados.append((len(melhor), Passo(nome, sub_real, campos)))
                break
    achados.sort(key=lambda x: -x[0])
    vistos, passos = set(), []
    for _, p in achados:
        if p.receita not in vistos:
            vistos.add(p.receita)
            passos.append(p)
    # 'pedir' casa com verbos muito comuns: só fica se for o único
    if len(passos) > 1:
        passos = [p for p in passos if p.receita != "pedir"]
    return passos[:MAX_PASSOS]


# ------------------------------------------------------------------ degrau 2: decisão sua
def decisao_humana(texto: str) -> tuple[str | None, list[str], int]:
    """Usa o motor de decisão (sem IA). Devolve (motivo se for decisão sua, motivos de dado sensível, degrau)."""
    try:
        sys.path.insert(0, str(RAIZ / "tools" / "motor"))
        import motor  # noqa: PLC0415
        regras = json.loads(motor.REGRAS.read_text(encoding="utf-8"))
        d = motor.decidir(texto, regras)
        return (d["motivo"] if d["degrau"] == 5 else None), d["sensivel"], d["degrau"]
    except Exception:  # noqa: BLE001  sem motor, segue sem este degrau
        return None, [], 4


# ------------------------------------------------------------------ degrau 3: IA local
def candidatos(dados: dict, texto: str, n: int = CANDIDATOS_IA) -> list[tuple[str, dict]]:
    ps = palavras(texto)
    notas = []
    for nome, r in dados["receitas"].items():
        if r["nivel"] not in allowlist.EXECUTAVEIS:
            continue
        alvo = palavras(" ".join([nome.replace("-", " "), r.get("descricao", ""), " ".join(r.get("gatilhos", [])),
                                  " ".join(f for fs in r.get("gatilhos_sub", {}).values() for f in fs),
                                  " ".join(r.get("subcomandos", {}))]))
        notas.append((len(ps & alvo), nome, r))
    notas.sort(key=lambda x: (-x[0], x[1]))
    escolhidos = [(nome, r) for _, nome, r in notas[:n]]
    if "pedir" not in [n_ for n_, _ in escolhidos]:
        escolhidos.append(("pedir", dados["receitas"]["pedir"]))
    return escolhidos


def _linha_receita(dados: dict, nome: str, r: dict) -> str:
    args = ", ".join(f"{a['nome']}" + ("" if a.get("obrigatorio", True) else "?") for a in r.get("args", []))
    subs = "; ".join(f"{s}({', '.join(refs)})" if refs else s for s, refs in r.get("subcomandos", {}).items())
    partes = [nome, r.get("descricao", "")[:80]]
    if args:
        partes.append(f"campos: {args}")
    if subs:
        partes.append(f"subcomandos: {subs}")
    if r.get("opcoes") or r.get("opcoes_pede_ok"):
        partes.append("opcoes: " + " ".join(r.get("opcoes", []) + r.get("opcoes_pede_ok", [])))
    return " | ".join(partes)


SISTEMA = ("Você traduz o pedido do dono do setup em receitas do 'just'. Use SÓ as receitas listadas. "
           "Responda SÓ com JSON: {\"passos\": [{\"receita\": \"nome\", \"subcomando\": \"opcional\", "
           "\"campos\": {\"nome_do_campo\": \"valor\"}, \"opcoes\": []}], \"resposta\": \"uma frase\"}. "
           "Campos de subcomando se chamam sub_1, sub_2. No máximo 3 passos. "
           "Se o pedido é criar ou mudar código, documento ou arquivo, use a receita 'pedir' com o pedido inteiro em 'texto'. "
           "Se for só uma pergunta, responda curto em 'resposta' com passos vazio. Nunca invente receita, campo ou opção.")


def por_ia_local(dados: dict, texto: str, chamar=None) -> tuple[list[Passo], str, int]:
    lista = "\n".join(_linha_receita(dados, n, r) for n, r in candidatos(dados, texto))
    msgs = [{"role": "system", "content": SISTEMA}, {"role": "user", "content": f"Receitas:\n{lista}\n\nPedido: {texto}"}]
    tokens = sum(len(m["content"]) for m in msgs) // 4
    resposta = (chamar or chamar_ollama)(msgs)
    tokens += len(resposta) // 4
    try:
        d = json.loads(resposta)
    except json.JSONDecodeError:
        return [], "A IA local respondeu fora do formato. Reformule ou use os Comandos.", tokens
    passos = []
    for p in (d.get("passos") or [])[:MAX_PASSOS]:
        if not isinstance(p, dict):
            continue
        campos = {str(k): str(v) for k, v in (p.get("campos") or {}).items() if v not in (None, "")}
        opcoes = [str(o) for o in (p.get("opcoes") or [])]
        passos.append(Passo(str(p.get("receita", "")), (str(p["subcomando"]) if p.get("subcomando") else None), campos, opcoes))
    return passos, str(d.get("resposta", ""))[:500], tokens


def chamar_ollama(mensagens: list[dict]) -> str:
    corpo = {"model": MODELO, "messages": mensagens, "stream": False, "format": "json",
             "options": {"temperature": 0, "num_ctx": 4096}}
    req = urllib.request.Request(f"{OLLAMA}/api/chat", data=json.dumps(corpo).encode(), headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=180) as r:
        return json.loads(r.read())["message"]["content"]


def ia_local_no_ar() -> bool:
    try:
        with urllib.request.urlopen(f"{OLLAMA}/api/tags", timeout=2) as r:
            nomes = [m.get("name", "") for m in json.loads(r.read()).get("models", [])]
        return any(n.split(":")[0] == MODELO.split(":")[0] for n in nomes)
    except (urllib.error.URLError, OSError, ValueError):
        return False


# ------------------------------------------------------------------ o plano
def validar(dados: dict, passos: list[Passo]) -> list[Passo]:
    for p in passos:
        try:
            p.args, p.nivel = allowlist.montar(dados, p.receita, p.campos, p.opcoes, p.subcomando)
        except allowlist.ErroAllowlist as e:
            p.erro = str(e)
    return passos


def planejar(dados: dict, texto: str, *, ia=None, ia_no_ar=None) -> Plano:
    texto = " ".join(texto.split())[:1000]
    motivo_voce, sens, degrau = decisao_humana(texto)
    passos = por_regra(dados, texto)
    if passos:
        return Plano(texto, "regra", validar(dados, passos), "Reconhecido por regra fixa (0 tokens).", sens)
    if motivo_voce:
        return Plano(texto, "voce", [], f"Isso é decisão sua ({motivo_voce}). Eu preparo, você decide: "
                     "use 'Guardar no núcleo' para não esquecer, ou peça o material de apoio.", sens)
    if (ia_no_ar or ia_local_no_ar)():
        try:
            passos, resposta, tokens = por_ia_local(dados, texto, ia)
        except (urllib.error.URLError, OSError, TimeoutError, KeyError, ValueError) as e:
            return Plano(texto, "nada", [], f"A IA local não respondeu ({type(e).__name__}). Use os Comandos ou tente de novo.", sens)
        return Plano(texto, "ia-local", validar(dados, passos), resposta or "Interpretado pela IA local (R$ 0).", sens, tokens)
    if degrau not in (2, 3):
        return Plano(texto, "nada", [], "Não reconheci uma receita e a IA local está desligada. Ligue com 'ligar' "
                     "(ou just ligar) para eu interpretar pedidos livres, ou use a tela Comandos.", sens)
    passos = validar(dados, [Passo("pedir", None, {"texto": texto})])
    return Plano(texto, "fila", passos, "A IA local está desligada (just ligar). Como não é uma receita conhecida, "
                 "o pedido pode ir para a fila, que faz o trabalho num ramo e abre PR em rascunho.", sens)
