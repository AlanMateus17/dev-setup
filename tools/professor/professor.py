#!/usr/bin/env python3
"""O Professor do setup: aula, prática, prova e revisão espaçada de cada tópico de que você precisa para operar o setup e
subir no eixo (software e finanças).

O método: objetivo único por bloco de 25 minutos; pergunta diagnóstica antes de explicar; explicação em camadas
(intuição → modelo → detalhe); exemplo resolvido e depois exemplo com lacunas; prática no seu próprio setup; perguntas de
recuperação; cartões Anki; prova corrigida com rubrica; revisão em 1, 3, 7, 21, 60 e 120 dias. Domínio vai de 0 a 4:
nada, viu a aula, fez a prática, passou na prova, ensinou.

As aulas ficam no Obsidian (~/dev/notas/60-Professor) e são geradas uma vez só: reler não gasta token.

    python3 tools/professor/professor.py hoje                 # o que estudar hoje (revisões + próxima aula de cada trilha)
    python3 tools/professor/professor.py trilha               # o currículo com o seu nível em cada módulo
    python3 tools/professor/professor.py aula s-backup [--motor claude|ollama|imprimir] [--refazer]
    python3 tools/professor/professor.py ferramenta restic    # mini-aula sobre qualquer bloco do ecossistema
    python3 tools/professor/professor.py praticei s-backup    # nível 2
    python3 tools/professor/professor.py prova s-backup       # gera a prova; você responde no próprio arquivo
    python3 tools/professor/professor.py corrigir s-backup    # a IA corrige com rubrica, marca o nível e agenda a revisão
    python3 tools/professor/professor.py ensinei s-backup     # nível 4: escreveu post ou deu a aula
    python3 tools/professor/professor.py cartoes              # exporta todos os cartões para importar no Anki
"""
from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
from datetime import date, timedelta
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(RAIZ / "tools" / "nucleo"))
import nucleo as nuc  # noqa: E402

CURRICULO = RAIZ / "data" / "professor" / "curriculo.json"
CONTEXTO = RAIZ / "docs" / "akita" / "contexto-setup.md"
INTERVALOS = (1, 3, 7, 21, 60, 120)
APROVA = 80
TRILHAS = {"oficio": "Ofício (2 h)", "setup": "Operar o setup (dentro das 2 h de ofício)", "financas": "Domínio: finanças (1 h)"}


def pasta() -> Path:
    return Path(os.environ.get("PROFESSOR_NOTAS") or Path.home() / "dev" / "notas" / "60-Professor")


def curriculo() -> dict:
    return json.loads(CURRICULO.read_text(encoding="utf-8"))


def modulo(mid: str) -> dict:
    for m in curriculo()["modulos"]:
        if m["id"] == mid:
            return m
    raise ValueError(f"módulo {mid} não existe (veja: just professor trilha)")


# ---------- domínio e revisão espaçada ----------

def niveis(con) -> dict[str, dict]:
    return {r["topico"]: dict(r) for r in con.execute("SELECT * FROM dominio")}


def subir(con, topico: str, nivel: int) -> None:
    """Sobe o nível (nunca desce por aqui)."""
    con.execute("INSERT INTO dominio (topico, nivel) VALUES (?, ?) ON CONFLICT(topico) DO UPDATE SET "
                "nivel = max(nivel, excluded.nivel), atualizado = strftime('%Y-%m-%dT%H:%M:%S','now','localtime')",
                (topico, nivel))
    con.commit()


def registrar_prova(con, topico: str, nota: int, hoje: date | None = None) -> tuple[int, str]:
    """Aprovado: nível 3 e o próximo intervalo da escada. Reprovado: volta para 1 dia (o nível não sobe)."""
    hoje = hoje or date.today()
    atual = niveis(con).get(topico, {"intervalo_dias": 0, "nivel": 0})
    if nota >= APROVA:
        maiores = [i for i in INTERVALOS if i > atual["intervalo_dias"]]
        intervalo = maiores[0] if maiores else INTERVALOS[-1]
        nivel = max(3, atual["nivel"])
    else:
        intervalo, nivel = 1, min(atual["nivel"], 2)
    prox = (hoje + timedelta(days=intervalo)).isoformat()
    con.execute("INSERT INTO dominio (topico, nivel, ultima_nota, intervalo_dias, proxima_revisao) VALUES (?,?,?,?,?) "
                "ON CONFLICT(topico) DO UPDATE SET nivel=excluded.nivel, ultima_nota=excluded.ultima_nota, "
                "intervalo_dias=excluded.intervalo_dias, proxima_revisao=excluded.proxima_revisao, "
                "atualizado=strftime('%Y-%m-%dT%H:%M:%S','now','localtime')", (topico, nivel, nota, intervalo, prox))
    con.commit()
    return intervalo, prox


def plano_do_dia(mods: list[dict], nv: dict[str, dict], hoje: date | None = None) -> dict:
    """Revisões vencidas e, por trilha, o primeiro módulo ainda não dominado cujos pré-requisitos já passaram na prova."""
    hoje = (hoje or date.today()).isoformat()
    revisoes = sorted(t for t, r in nv.items() if r.get("proxima_revisao") and r["proxima_revisao"] <= hoje)
    proximos = {}
    for m in sorted(mods, key=lambda m: m["trimestre"]):
        if m["trilha"] in proximos or nv.get(m["id"], {}).get("nivel", 0) >= 3:
            continue
        if all(nv.get(p, {}).get("nivel", 0) >= 3 for p in m["prereq"]):
            proximos[m["trilha"]] = m
    return {"revisoes": revisoes, "proximos": proximos}


# ---------- pedidos à IA ----------

AULA = """Você é o professor particular do Alan: muito experiente, detalhista e didático. Ele é professor de TI,
dev em formação rumo a sênior (eixo: software e finanças) e tem TDAH. Escreva UMA aula em português do Brasil, em
Markdown, sobre o módulo abaixo, seguindo exatamente esta estrutura:

# {titulo}
## Objetivo (uma frase) e por que isso importa no setup dele
## Antes de começar (3 perguntas diagnósticas, sem resposta: ele responde de cabeça antes de ler)
## Bloco 1 (25 min) · Intuição: uma analogia do dia a dia dele (escola, restaurante, a casa)
## Bloco 2 (25 min) · O modelo: como funciona por dentro, com um diagrama em texto ou Mermaid
## Bloco 3 (25 min) · Os detalhes que pegam: casos de borda, erros comuns e como diagnosticar
## Exemplo resolvido (passo a passo, explicando cada decisão)
## Agora você (o mesmo tipo de exemplo com lacunas ___ para ele completar)
## Prática no seu setup (comandos de UMA linha, dizendo ONDE rodar: Ubuntu do WSL ou PowerShell; nada destrutivo
   sem cópia antes; critério de pronto verificável)
## Perguntas de recuperação (5, de lembrar a aplicar; respostas só no fim, num bloco recolhido <details>)
## Cartões (8 linhas no formato "- pergunta :: resposta", curtas, uma ideia cada)
## Se quiser ir além (as fontes oficiais abaixo, dizendo o que ler em cada uma)

Regras: explique com as suas palavras; nada copiado de curso pago ou livro; quando não tiver certeza de um detalhe,
diga "confira na fonte oficial" em vez de inventar; aplique tudo ao setup dele (contexto abaixo); nada de dado de aluno,
senha ou documento pessoal nos exemplos.

MÓDULO: {titulo}
Objetivos: {objetivos}
Prática pedida: {pratica}
Fontes oficiais: {fontes}

O SETUP DELE:
{contexto}

O QUE O SETUP JÁ SABE SOBRE O ASSUNTO (decisões, regras do Akita aprovadas, lições):
{nucleo}
"""

PROVA = """Monte uma prova em português do Brasil sobre o módulo "{titulo}" (objetivos: {objetivos}). 8 questões: 3 de
explicar com as próprias palavras, 3 de aplicar no setup dele (comando ou decisão), 2 de diagnosticar um erro. Nada de
múltipla escolha. Depois de cada questão deixe a linha "Resposta:" vazia. Não dê as respostas. Só a prova, em Markdown."""

CORRECAO = """Corrija a prova abaixo como um professor exigente e justo. Para cada questão: certo, parcial ou errado,
e o porquê em uma ou duas frases, com a correção. No fim, uma linha só com o JSON {{"nota": 0 a 100, "revisar": ["tópico
fraco", ...]}}. Módulo: "{titulo}". Objetivos: {objetivos}.

{prova}"""


def pedido_aula(m: dict, contexto_nucleo: str = "") -> str:
    ctx = CONTEXTO.read_text(encoding="utf-8") if CONTEXTO.exists() else ""
    return (AULA.replace("{titulo}", m["titulo"]).replace("{objetivos}", "; ".join(m["objetivos"]))
            .replace("{pratica}", m["pratica"]).replace("{fontes}", ", ".join(m["fontes"]))
            .replace("{contexto}", ctx).replace("{nucleo}", contexto_nucleo or "(nada ainda)"))


def rodar(motor: str, pedido: str) -> str:
    if motor == "imprimir":
        return pedido
    cmd = {"claude": ["claude", "-p", "--output-format", "text"],
           "ollama": ["ollama", "run", os.environ.get("PROFESSOR_MODELO", "qwen2.5:7b")]}.get(motor)
    if not cmd:
        raise ValueError("motor: claude, ollama ou imprimir")
    return subprocess.run(cmd, input=pedido, capture_output=True, text=True, check=True, timeout=1800).stdout


def cartoes_de(texto: str) -> list[tuple[str, str]]:
    """Linhas '- pergunta :: resposta' da seção Cartões."""
    i = texto.find("## Cartões")
    if i < 0:
        return []
    saida = []
    for ln in texto[i:].splitlines()[1:]:
        if ln.startswith("## "):
            break
        m = re.match(r"^\s*[-*]\s*(.+?)\s*::\s*(.+)$", ln)
        if m:
            saida.append((m.group(1), m.group(2)))
    return saida


def nota_da_correcao(texto: str) -> int:
    achado = re.findall(r"\{[^{}]*\"nota\"\s*:\s*(\d{1,3})[^{}]*\}", texto)
    if not achado:
        raise ValueError("a correção não trouxe a nota em JSON")
    return max(0, min(100, int(achado[-1])))


# ---------- CLI ----------

def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    s = ap.add_subparsers(dest="cmd", required=True)
    s.add_parser("hoje")
    s.add_parser("trilha")
    a = s.add_parser("aula"); a.add_argument("id"); a.add_argument("--motor", default="claude"); a.add_argument("--refazer", action="store_true")
    f = s.add_parser("ferramenta"); f.add_argument("bloco"); f.add_argument("--motor", default="claude")
    for nome in ("praticei", "ensinei"):
        s.add_parser(nome).add_argument("id")
    p = s.add_parser("prova"); p.add_argument("id"); p.add_argument("--motor", default="claude")
    c = s.add_parser("corrigir"); c.add_argument("id"); c.add_argument("--motor", default="claude")
    s.add_parser("cartoes")
    args = ap.parse_args(argv)
    con = nuc.abrir()
    try:
        cur = curriculo()
        if args.cmd == "hoje":
            pl = plano_do_dia(cur["modulos"], niveis(con))
            if pl["revisoes"]:
                print("Revisar primeiro (prova curta de novo): " + ", ".join(pl["revisoes"]))
            for trilha, rotulo in TRILHAS.items():
                m = pl["proximos"].get(trilha)
                if m:
                    print(f"{rotulo}: {m['id']} · {m['titulo']}\n   just professor aula {m['id']}")
            if not pl["proximos"] and not pl["revisoes"]:
                print("Currículo do trimestre dominado. Hora de acrescentar módulos (data/professor/curriculo.json).")
        elif args.cmd == "trilha":
            nv, nomes = niveis(con), cur["niveis"]
            for m in sorted(cur["modulos"], key=lambda m: (m["trimestre"], m["trilha"])):
                n = nv.get(m["id"], {}).get("nivel", 0)
                print(f"T{m['trimestre']} {m['trilha']:<9} {'●' * n}{'○' * (4 - n)} {m['id']:<20} {m['titulo']}  ({nomes[n]})")
        elif args.cmd in ("aula", "ferramenta"):
            if args.cmd == "ferramenta":
                eco = json.loads((RAIZ / "data" / "ecossistema.json").read_text(encoding="utf-8"))
                b = next((x for x in eco["blocos"] if x["id"] == args.bloco), None)
                if not b:
                    raise ValueError(f"bloco {args.bloco} não existe no ecossistema")
                m = {"id": f"ferramenta-{b['id']}", "titulo": f"Conhecer: {b['rotulo'].replace('|', ' ')}",
                     "objetivos": [b["descricao"], "saber quando usar e quando não usar", "usar o básico no setup"],
                     "pratica": "o primeiro uso real dessa ferramenta no setup dele", "fontes": ["a documentação oficial da ferramenta"]}
                refazer = False
            else:
                m, refazer = modulo(args.id), args.refazer
            destino = pasta() / "aulas" / f"{m['id']}.md"
            if destino.exists() and not refazer:
                print(f"A aula já existe (reler não gasta token): {destino}")
            else:
                texto = rodar(args.motor, pedido_aula(m, nuc.contexto(con, m["titulo"])))
                if args.motor == "imprimir":
                    print(texto)
                    return 0
                destino.parent.mkdir(parents=True, exist_ok=True)
                destino.write_text(texto, encoding="utf-8")
                print(f"Aula salva: {destino}")
            subir(con, m["id"], 1)
            nuc.evento(con, "professor.aula", {"modulo": m["id"]}, fonte="professor")
        elif args.cmd == "praticei":
            modulo(args.id); subir(con, args.id, 2); print(f"{args.id}: nível 2 (fez a prática). Próximo: just professor prova {args.id}")
        elif args.cmd == "ensinei":
            modulo(args.id); subir(con, args.id, 4); print(f"{args.id}: nível 4 (ensinou). É assim que o assunto fica de vez.")
        elif args.cmd == "prova":
            m = modulo(args.id)
            texto = rodar(args.motor, PROVA.replace("{titulo}", m["titulo"]).replace("{objetivos}", "; ".join(m["objetivos"])))
            destino = pasta() / "provas" / f"{m['id']}-{date.today().isoformat()}.md"
            destino.parent.mkdir(parents=True, exist_ok=True)
            destino.write_text(texto, encoding="utf-8")
            print(f"Prova em {destino}. Responda sem consultar e depois: just professor corrigir {m['id']}")
        elif args.cmd == "corrigir":
            m = modulo(args.id)
            provas = sorted((pasta() / "provas").glob(f"{m['id']}-*.md"))
            provas = [p for p in provas if not p.stem.endswith("-correcao")]
            if not provas:
                raise ValueError(f"nenhuma prova de {m['id']} (rode: just professor prova {m['id']})")
            texto = rodar(args.motor, CORRECAO.replace("{titulo}", m["titulo"]).replace("{objetivos}", "; ".join(m["objetivos"]))
                          .replace("{prova}", provas[-1].read_text(encoding="utf-8")))
            provas[-1].with_name(provas[-1].stem + "-correcao.md").write_text(texto, encoding="utf-8")
            nota = nota_da_correcao(texto)
            intervalo, prox = registrar_prova(con, m["id"], nota)
            nuc.evento(con, "professor.prova", {"modulo": m["id"], "nota": nota}, fonte="professor")
            veredito = "aprovado" if nota >= APROVA else f"abaixo de {APROVA}: releia o Bloco 3 e refaça"
            print(f"Nota {nota} ({veredito}). Próxima revisão em {intervalo} dia(s): {prox}.")
        elif args.cmd == "cartoes":
            linhas = []
            for arq in sorted((pasta() / "aulas").glob("*.md")):
                for p, r in cartoes_de(arq.read_text(encoding="utf-8")):
                    linhas.append(f"{p}\t{r}\t{arq.stem}")
            destino = pasta() / "cartoes-anki.tsv"
            destino.parent.mkdir(parents=True, exist_ok=True)
            destino.write_text("\n".join(linhas) + "\n", encoding="utf-8")
            print(f"{len(linhas)} cartões em {destino}. No Anki: Arquivo > Importar, separado por tabulação, 3º campo como etiqueta.")
    except (ValueError, subprocess.CalledProcessError) as erro:
        print(erro, file=sys.stderr)
        return 2
    finally:
        con.close()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
