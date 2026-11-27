"""Telas de dados da Central: Roteiro, Estudo, Empresas e rendas, Serviços, Núcleo e Ajuda.

Regra de ouro (docs/central/README.md): a Central não guarda nada sozinha. Estas telas leem data/*.json e chamam as funções
que já existem (tools/nucleo/agenda.py e nucleo.py). Ações continuam passando pela allowlist ou por funções do núcleo,
sempre com auditoria.
"""
from __future__ import annotations

import html
import json
import socket
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor
from datetime import date
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(RAIZ / "tools" / "nucleo"))
import agenda  # noqa: E402
import nucleo as nuc  # noqa: E402

e = html.escape
NAO_WEB = {("metricas-db", 5433), ("mosquitto", 1883), ("adguard", 53), ("soft-serve", 23231), ("forgejo", 2222),
           ("frigate", 8554), ("whisper", 10300), ("piper", 10200), ("openwakeword", 10400), ("webgoat", 9090)}
SERVICOS_USUARIO = ("amtech-central", "amtech-fila", "amtech-bot", "amtech-remoto", "ollama")


def _csrf(csrf: str) -> str:
    return f'<input type="hidden" name="csrf" value="{e(csrf)}">'


def botao_pedido(csrf: str, texto: str, rotulo: str = "Pedir à Central") -> str:
    """Manda um texto pronto pelo mesmo caminho da caixa de pedido (regra → motor → IA local → fila)."""
    return (f'<form method="post" action="/prompt" class="inline">{_csrf(csrf)}'
            f'<input type="hidden" name="texto" value="{e(texto)}"><button class="secundario">{e(rotulo)}</button></form>')


# ------------------------------------------------------------------ Roteiro
def roteiro(csrf: str, empresa: str | None, limite: int = 12) -> str:
    fases = agenda.roteiro(RAIZ)
    con = nuc.abrir()
    try:
        feitos = agenda.feitos(con)
    finally:
        con.close()
    pend = agenda.pendentes(fases, feitos, empresa)
    empresas = json.loads((RAIZ / "data" / "empresas.json").read_text(encoding="utf-8"))["empresas"]
    filtro = "".join(f'<option value="{e(x["id"])}"{" selected" if x["id"] == empresa else ""}>{e(x["nome"])}</option>'
                     for x in empresas)
    partes = ['<form method="get" action="/roteiro" class="linha"><select name="empresa"><option value="">Todas as empresas</option>'
              f'{filtro}</select><button class="secundario">Filtrar</button></form>',
              f'<section><h2>O que é seu agora</h2><p class="calmo">{len(pend)} passo(s) dependem de você. Os primeiros:</p>']
    for f, p in pend[:limite]:
        tipo = "DECIDIR" if p.get("decisao") else "FAZER"
        cmd = f'<p><code>{e(p["comando"])}</code></p>' if p.get("comando") else ""
        fora = f'<p class="calmo">Fora do terminal: {e(p["fora"])}</p>' if p.get("fora") else ""
        partes.append(
            f'<div class="cartao"><p><span class="nivel">{tipo}</span> <strong>{e(p["titulo"])}</strong></p>'
            f'<p class="calmo">{e(f["titulo"])} · {p.get("tempo_min", 0)} min · pronto quando: {e(p.get("pronto", ""))}</p>{cmd}{fora}'
            f'<div class="linha"><form method="post" action="/roteiro/feito" data-confirmar="Marcar “{e(p["titulo"][:60])}” como feito?">'
            f'{_csrf(csrf)}<input type="hidden" name="passo" value="{e(p["id"])}"><button>✅ Feito</button></form>'
            f'{botao_pedido(csrf, "Me ajude com o passo " + p["id"] + ": " + p["titulo"], "Pedir ajuda")}</div></div>')
    partes.append('</section><section><h2>Progresso por fase</h2><p class="calmo">Já fez uma fase inteira antes de usar a Central? '
                  'Marque a fase de uma vez.</p><table><tr><th>Fase</th><th>Feito</th><th></th></tr>')
    for f in fases:
        ps = [p for p in f["passos"] if agenda._da_empresa(p, empresa)]
        if not ps:
            continue
        feito, total = sum(1 for p in ps if p["id"] in feitos), len(ps)
        pct = round(100 * feito / total)
        botao = "" if feito == total else (
            f'<form method="post" action="/roteiro/feito" class="inline" data-confirmar="Marcar os {total - feito} passo(s) '
            f'restantes de “{e(f["titulo"][:50])}” como feitos?">{_csrf(csrf)}<input type="hidden" name="passo" value="{e(f["id"])}">'
            '<button class="secundario">Fase feita</button></form>')
        partes.append(f'<tr><td>{e(f["titulo"])}</td><td><progress max="100" value="{pct}"></progress> {feito}/{total}</td>'
                      f'<td>{botao}</td></tr>')
    partes.append('</table></section>')
    return "".join(partes)


def marcar_feito(passo: str) -> str:
    fases = agenda.roteiro(RAIZ)
    validos = {p["id"] for f in fases for p in f["passos"]} | {f["id"] for f in fases}
    if passo not in validos:
        raise ValueError("passo ou fase desconhecido")
    con = nuc.abrir()
    try:
        agenda.marcar(con, [passo], fases)
    finally:
        con.close()
    return passo


# ------------------------------------------------------------------ Estudo
def estudo(csrf: str, dados: dict, cartao) -> str:
    con = nuc.abrir()
    try:
        hoje = date.today().isoformat()
        vencidas = con.execute("SELECT topico, nivel, proxima_revisao FROM dominio WHERE proxima_revisao IS NOT NULL "
                               "AND proxima_revisao <= ? ORDER BY proxima_revisao LIMIT 20", (hoje,)).fetchall()
        niveis = con.execute("SELECT nivel, COUNT(*) n FROM dominio GROUP BY nivel ORDER BY nivel").fetchall()
    finally:
        con.close()
    nomes = {0: "nada", 1: "reconhece", 2: "faz com consulta", 3: "faz sozinho", 4: "ensinou"}
    partes = ['<section><h2>Revisões vencidas</h2>']
    if vencidas:
        partes.append('<ul>' + "".join(f'<li><code>{e(v["topico"])}</code> · nível {v["nivel"]} · desde {e(v["proxima_revisao"])}</li>'
                                       for v in vencidas) + '</ul>')
    else:
        partes.append('<p class="calmo">Nada para revisar hoje.</p>')
    if niveis:
        partes.append('<p class="calmo">Domínio: ' + " · ".join(f'{n["n"]} em “{nomes.get(n["nivel"], n["nivel"])}”' for n in niveis) + '</p>')
    partes.append(f'<div class="linha">{botao_pedido(csrf, "o que estudo hoje?", "O que estudo hoje?")}'
                  f'{botao_pedido(csrf, "minha trilha de estudo", "Minha trilha")}{botao_pedido(csrf, "cartoes do anki", "Cartões")}</div></section>')
    ordem = ["professor", "diag", "erro", "atrito", "colher", "livros", "recrutador", "akita", "fontes", "erros", "atritos", "professor-mapa"]
    partes.append('<section><h2>Ferramentas de estudo</h2>')
    for nome in ordem:
        r = dados["receitas"].get(nome)
        if r and r["nivel"] != "proibido":
            partes.append(cartao(csrf, dados, nome, r))
    partes.append('</section>')
    return "".join(partes)


# ------------------------------------------------------------------ Empresas e rendas
def empresas(csrf: str) -> str:
    emp = json.loads((RAIZ / "data" / "empresas.json").read_text(encoding="utf-8"))["empresas"]
    port = json.loads((RAIZ / "data" / "portfolio.json").read_text(encoding="utf-8"))
    partes = ['<section><h2>Rendas agora e a próxima onda</h2>']
    for titulo, filtro in (("Onda 0 · agora", lambda o: o.get("onda") == 0),
                           ("Onda 1 · próxima", lambda o: o.get("onda") == 1)):
        ofertas = [o for o in port["ofertas"] if filtro(o)]
        partes.append(f'<h3>{e(titulo)} ({len(ofertas)})</h3>')
        for o in ofertas:
            partes.append(
                f'<div class="cartao"><p><strong>{e(o["nome"])}</strong> <span class="nivel">{e(o.get("estagio", ""))}</span> '
                f'<span class="calmo">{e(o.get("tipo", ""))}</span></p>'
                f'<p>Próximo passo: {e(o.get("proximo_passo", ""))}</p>'
                f'<p class="calmo">Medir: {e(o.get("metrica", ""))}</p>'
                f'{botao_pedido(csrf, "Próximo passo da oferta " + o["nome"] + ": " + o.get("proximo_passo", ""), "Pedir à Central")}</div>')
    resto = [o for o in port["ofertas"] if o.get("onda") not in (0, 1)]
    partes.append(f'<details><summary>As outras {len(resto)} ofertas (ondas 2 e 3, fila, decidir, 2027)</summary><table>'
                  '<tr><th>Oferta</th><th>Onda</th><th>Veredito</th></tr>' + "".join(
                      f'<tr><td>{e(o["nome"])}</td><td>{e(str(o.get("onda") if o.get("onda") is not None else "—"))}</td>'
                      f'<td>{e(o.get("veredito", ""))}</td></tr>' for o in resto) + '</table></details></section>')
    partes.append('<section><h2>As 6 empresas</h2>')
    for x in emp:
        prods = "".join(f'<li><strong>{e(p["nome"])}</strong>: {e(p.get("estado", ""))}</li>' for p in x.get("produtos", []))
        partes.append(f'<details class="cartao"><summary><strong>{e(x["nome"])}</strong> <span class="nivel">{e(x["estado"])}</span> '
                      f'<span class="calmo">etapa {e(str(x.get("etapa", "")))}</span></summary>'
                      f'<p>{e(x.get("faz", ""))}</p><p class="calmo">Para quem: {e(x.get("para_quem", ""))}</p><ul>{prods}</ul>'
                      f'<p><a href="/roteiro?empresa={e(x["id"])}">Passos do roteiro desta empresa</a> · '
                      f'<a href="/comandos#site">Site</a></p></details>')
    partes.append('</section>')
    return "".join(partes)


# ------------------------------------------------------------------ Serviços
def _porta_aberta(porta: int) -> bool:
    try:
        with socket.create_connection(("127.0.0.1", porta), timeout=0.4):
            return True
    except OSError:
        return False


def _ativo(unidade: str) -> str:
    try:
        r = subprocess.run(["systemctl", "--user", "is-active", unidade], capture_output=True, text=True, timeout=3)
        return r.stdout.strip() or "desconhecido"
    except (OSError, subprocess.TimeoutExpired):
        return "sem systemd"


def servicos(csrf: str, dados: dict, cartao) -> str:
    portas = json.loads((RAIZ / "data" / "portas.json").read_text(encoding="utf-8"))["servicos"]
    ferr = json.loads((RAIZ / "data" / "ferramentas.json").read_text(encoding="utf-8"))["ferramentas"]
    perfil = {f["id"]: f["perfil"] for f in ferr}
    web = [s for s in portas if s.get("tela") and (s["nome"], s["porta"]) not in NAO_WEB]
    with ThreadPoolExecutor(max_workers=16) as pool:
        abertas = dict(zip([s["porta"] for s in web], pool.map(_porta_aberta, [s["porta"] for s in web])))
        estados = dict(zip(SERVICOS_USUARIO, pool.map(_ativo, SERVICOS_USUARIO)))
    partes = ['<section><h2>Serviços do setup</h2><table><tr><th>Serviço</th><th>Estado</th></tr>']
    for u, est in estados.items():
        partes.append(f'<tr><td>{e(u)}</td><td class="{"ok" if est == "active" else "calmo"}">{e(est)}</td></tr>')
    partes.append('</table></section><section><h2>Ferramentas com tela</h2><p class="calmo">Links só desta máquina (127.0.0.1). '
                  'O que está parado sobe com o perfil indicado.</p>')
    grupos: dict[str, list] = {}
    for s in web:
        grupos.setdefault(s["grupo"], []).append(s)
    for g, itens in sorted(grupos.items()):
        partes.append(f'<h3>{e(g)}</h3><table><tr><th>Ferramenta</th><th>Estado</th><th>Perfil</th></tr>')
        for s in sorted(itens, key=lambda x: x["nome"]):
            no_ar = abertas.get(s["porta"])
            nome = (f'<a href="http://127.0.0.1:{s["porta"]}" target="_blank" rel="noopener noreferrer">{e(s["nome"])}</a>'
                    if no_ar else e(s["nome"]))
            p = perfil.get(f'docker-{g}-{s["servico"]}', "—")
            partes.append(f'<tr><td>{nome} <span class="calmo">:{s["porta"]}</span></td>'
                          f'<td class="{"ok" if no_ar else "calmo"}">{"no ar" if no_ar else "parado"}</td><td>{e(p)}</td></tr>')
        partes.append('</table>')
    partes.append('</section><section><h2>Ligar e desligar</h2>')
    for nome in ("ligar", "desligar", "servico", "ligado", "validar", "backup"):
        r = dados["receitas"].get(nome)
        if r and r["nivel"] != "proibido":
            partes.append(cartao(csrf, dados, nome, r))
    partes.append('</section>')
    return "".join(partes)


# ------------------------------------------------------------------ Núcleo
def nucleo(csrf: str, busca: str) -> str:
    con = nuc.abrir()
    try:
        achados = nuc.buscar(con, busca, limite=10) if busca else []
        tarefas = con.execute("SELECT id, titulo, estado, criada FROM tarefas WHERE estado IN ('aberta','fazendo','esperando-ok') "
                              "ORDER BY criada DESC LIMIT 30").fetchall()
        recentes = con.execute("SELECT tipo, titulo, quando FROM conhecimento ORDER BY id DESC LIMIT 8").fetchall()
    finally:
        con.close()
    partes = [f'<section><h2>Buscar no que já se sabe</h2><form method="get" action="/nucleo" class="linha">'
              f'<input name="q" value="{e(busca)}" maxlength="120" placeholder="ex.: deploy, backup, Kamal"><button>Buscar</button></form>']
    if busca:
        partes.append('<ul>' + ("".join(f'<li><strong>{e(a["titulo"])}</strong> <span class="calmo">{e(a["tipo"])}</span>'
                                        f'<br><span class="calmo">{e(str(a["texto"])[:220])}</span></li>' for a in achados)
                                or '<li class="calmo">Nada encontrado.</li>') + '</ul>')
    partes.append('</section><section><h2>Guardar</h2>'
                  f'<form method="post" action="/nucleo/lembrar">{_csrf(csrf)}'
                  '<label>O que guardar<textarea name="texto" rows="2" maxlength="500" required></textarea></label>'
                  '<label>Tipo<select name="tipo"><option>nota</option><option>licao</option><option>padrao</option>'
                  '<option>referencia</option><option>recusa</option></select></label><button>Guardar</button></form></section>')
    partes.append('<section><h2>Tarefas abertas</h2>')
    if tarefas:
        for t in tarefas:
            partes.append(f'<div class="linha"><span>#{t["id"]} {e(t["titulo"])} <span class="calmo">({e(t["estado"])})</span></span>'
                          f'<form method="post" action="/nucleo/tarefa" class="inline">{_csrf(csrf)}'
                          f'<input type="hidden" name="id" value="{t["id"]}"><button class="secundario">Feita</button></form></div>')
    else:
        partes.append('<p class="calmo">Nenhuma tarefa aberta.</p>')
    partes.append(f'<form method="post" action="/nucleo/tarefa-nova" class="linha">{_csrf(csrf)}'
                  '<input name="titulo" maxlength="200" required placeholder="Nova tarefa"><button>Criar</button></form></section>')
    if recentes:
        partes.append('<section><h2>Guardado recentemente</h2><ul>' + "".join(
            f'<li>{e(r["titulo"])} <span class="calmo">· {e(r["tipo"])} · {e(str(r["quando"])[:10])}</span></li>' for r in recentes)
            + '</ul></section>')
    return "".join(partes)


def lembrar(texto: str, tipo: str) -> int:
    if tipo not in ("nota", "licao", "padrao", "referencia", "recusa"):
        raise ValueError("tipo inválido")
    texto = " ".join(texto.split())[:500]
    if not texto:
        raise ValueError("texto vazio")
    con = nuc.abrir()
    try:
        return nuc.lembrar(con, texto, tipo, origem="central")
    finally:
        con.close()


def tarefa_nova(titulo: str) -> int:
    titulo = " ".join(titulo.split())[:200]
    if not titulo:
        raise ValueError("título vazio")
    con = nuc.abrir()
    try:
        return nuc.tarefa_nova(con, titulo)
    finally:
        con.close()


def tarefa_feita(tid: int) -> None:
    con = nuc.abrir()
    try:
        nuc.tarefa_estado(con, tid, "feita")
    finally:
        con.close()


# ------------------------------------------------------------------ Ajuda
AJUDA = """
<section><h2>Em uma frase</h2><p>Escreva o que você quer na caixa do <a href="/">Hoje</a>. A Central reconhece pedidos comuns
sem gastar IA, usa a IA local (de graça) quando precisa, e tudo o que muda alguma coisa espera o seu ✅.</p></section>
<section><h2>As telas</h2><table>
<tr><td><a href="/">Hoje</a></td><td>Caixa de pedido, o que espera você, botões rápidos, últimas execuções</td></tr>
<tr><td><a href="/roteiro">Roteiro</a></td><td>Os próximos passos que dependem de você, com botão Feito, e o progresso por fase</td></tr>
<tr><td><a href="/estudo">Estudo</a></td><td>Revisões vencidas, Professor, diagnóstico, erros, atritos, colheita, livros</td></tr>
<tr><td><a href="/empresas">Empresas</a></td><td>Rendas da onda 0 e 1 com o próximo passo, e as 6 empresas</td></tr>
<tr><td><a href="/servicos">Serviços</a></td><td>O que está no ar, links das ferramentas e ligar/desligar perfis</td></tr>
<tr><td><a href="/nucleo">Núcleo</a></td><td>Buscar e guardar conhecimento, tarefas</td></tr>
<tr><td><a href="/comandos">Comandos</a></td><td>Todas as receitas do just que a Central pode rodar</td></tr>
<tr><td><a href="/aprovar">Aprovar</a></td><td>O que espera o seu ✅ (vale 30 min, uma vez só)</td></tr>
<tr><td><a href="/auditoria">Auditoria</a></td><td>Quem fez o quê; avisa se alguém mexeu no registro</td></tr>
</table></section>
<section><h2>Quanto custa</h2><ul><li><strong>Regra fixa</strong>: 0 tokens. Ex.: “o que estudo hoje?”, “como está o backup?”.</li>
<li><strong>IA local</strong> (Ollama): R$ 0, alguns segundos. Precisa do <code>just ligar</code>.</li>
<li><strong>Fila</strong>: só para trabalho de código; ela escolhe o modelo pela escada do motor e devolve PR em rascunho.</li>
<li>Se a IA local resolver o mesmo pedido 3 vezes, o Hoje sugere transformar em regra fixa.</li></ul></section>
<section><h2>Quando algo não funciona</h2><ul>
<li>Não abre: no Ubuntu, <code>just ligado</code>; se a Central estiver parada, <code>just ligar</code> ou <code>just central</code>.</li>
<li>Esqueceu a senha ou bloqueou: <code>just central-usuario alan</code> (troca a senha e desbloqueia).</li>
<li>“IA local desligada”: <code>just ligar</code> sobe o Ollama.</li>
<li>Algo travou: registre com <code>just atrito "o que travou"</code> ou pela tela Estudo.</li></ul></section>
<section><h2>O que a Central nunca faz</h2><p>Não lê nem mostra senhas, não roda comando livre, não publica, paga nem envia nada em seu
nome sem aprovação, e não manda dado de aluno para IA online. Só escuta em 127.0.0.1.</p></section>
"""
