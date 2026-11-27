"""Telas e rotas da Central (FastAPI, HTML gerado aqui, JavaScript só de arquivo estático: a CSP proíbe script inline).

Segurança desde a primeira linha (ADR 0022 e 0023): login, cookie HttpOnly + SameSite=Strict, CSRF em todo POST,
conferência de Host e de Origin, allowlist, aprovação com validade e uso único, auditoria encadeada.
"""
from __future__ import annotations

import asyncio
import hmac
import html
import json
import re
import secrets
from collections import Counter
from pathlib import Path
from urllib.parse import urlsplit

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse, RedirectResponse, Response, StreamingResponse
from fastapi.staticfiles import StaticFiles
from starlette.concurrency import run_in_threadpool

import allowlist
import banco
import prompt
import telas
from executor import Executor

COOKIE = "central_sessao"
COOKIE_PRE = "central_pre"
NIVEL_ORDEM = ("automatico", "avisa", "pede-ok")
ROTULO_NIVEL = {"automatico": "roda direto", "avisa": "roda e avisa", "pede-ok": "pede aprovação",
                "so-terminal": "só no terminal", "proibido": "proibido"}
RAPIDOS = [("agora", None, []), ("professor", "hoje", []), ("fila", None, []), ("tarefas", None, []),
           ("ligado", None, []), ("validar", None, ["--rapido"])]
CSP = ("default-src 'self'; script-src 'self'; style-src 'self'; img-src 'self' data:; connect-src 'self'; "
       "frame-ancestors 'none'; form-action 'self'; base-uri 'none'; object-src 'none'")
e = html.escape


def criar_app(raiz: Path, caminho_banco: Path, hosts: set[str] | None = None, executor: Executor | None = None) -> FastAPI:
    banco.migrar(caminho_banco)
    dados = allowlist.carregar(raiz)
    hosts = {"127.0.0.1", "localhost", *(hosts or set())}
    ex = executor or Executor(raiz, caminho_banco)
    app = FastAPI(docs_url=None, redoc_url=None, openapi_url=None)
    app.mount("/static", StaticFiles(directory=Path(__file__).parent / "static"), name="static")

    def con():
        return banco.abrir(caminho_banco)

    # ------------------------------------------------------------------ proteção geral
    @app.middleware("http")
    async def protecao(request: Request, chamar):
        host = (request.headers.get("host") or "").rsplit(":", 1)[0].strip("[]").lower()
        if host not in hosts:
            return Response("Host não permitido.", status_code=400, media_type="text/plain; charset=utf-8")
        if request.method == "POST":
            origem = request.headers.get("origin")
            # host E porta: outro app local (ex.: 127.0.0.1:3000) não conta como a Central; "null" é recusado
            if origem is not None and (origem == "null" or urlsplit(origem).netloc.lower() != (request.headers.get("host") or "").lower()):
                return Response("Origem não permitida.", status_code=403, media_type="text/plain; charset=utf-8")
        resp = await chamar(request)
        resp.headers["Content-Security-Policy"] = CSP
        resp.headers["X-Frame-Options"] = "DENY"
        resp.headers["X-Content-Type-Options"] = "nosniff"
        resp.headers["Referrer-Policy"] = "same-origin"  # no-referrer faz o navegador mandar Origin: null
        if not request.url.path.startswith("/static"):
            resp.headers["Cache-Control"] = "no-store"
        return resp

    def sessao_de(request: Request) -> dict | None:
        c = con()
        try:
            return banco.sessao(c, request.cookies.get(COOKIE))
        finally:
            c.close()

    async def form_com_csrf(request: Request, s: dict):
        form = await request.form()
        if not hmac.compare_digest(str(form.get("csrf", "")), s["csrf"]):
            raise PermissionError("Formulário expirado ou de outra página. Recarregue e tente de novo.")
        return form

    def ir(url: str) -> RedirectResponse:
        return RedirectResponse(url, status_code=303)

    def erro(s: dict | None, msg: str, status: int = 400) -> HTMLResponse:
        return HTMLResponse(pagina("Não deu certo", f'<p class="erro">{e(msg)}</p><p><a href="/">Voltar ao Hoje</a></p>', s),
                            status_code=status)

    # ------------------------------------------------------------------ login
    @app.get("/login")
    async def login_tela(request: Request):
        pre = secrets.token_urlsafe(16)
        resp = HTMLResponse(pagina("Entrar", tela_login(pre), None))
        resp.set_cookie(COOKIE_PRE, pre, httponly=True, samesite="strict", secure=request.url.scheme == "https", max_age=900)
        return resp

    @app.post("/login")
    async def login(request: Request):
        form = await request.form()
        pre = request.cookies.get(COOKIE_PRE, "")
        if not pre or not hmac.compare_digest(str(form.get("pre", "")), pre):
            return ir("/login")
        nome, senha = str(form.get("usuario", ""))[:60], str(form.get("senha", ""))[:200]
        ip = request.client.host if request.client else ""
        c = con()
        try:
            u = banco.autenticar(c, nome, senha)
            if not u:
                banco.auditar(c, "login.falha", alvo=nome, resultado=ip)
                novo = secrets.token_urlsafe(16)
                resp = HTMLResponse(pagina("Entrar", tela_login(novo, "Usuário ou senha incorretos (ou bloqueado por 15 min)."), None),
                                    status_code=401)
                resp.set_cookie(COOKIE_PRE, novo, httponly=True, samesite="strict", secure=request.url.scheme == "https", max_age=900)
                return resp
            token, _ = banco.criar_sessao(c, u, ip)
            banco.auditar(c, "login.ok", organizacao_id=u["organizacao_id"], usuario_id=u["id"], resultado=ip)
        finally:
            c.close()
        resp = ir("/")
        resp.set_cookie(COOKIE, token, httponly=True, samesite="strict", secure=request.url.scheme == "https",
                        max_age=int(banco.SESSAO_MAXIMA.total_seconds()))
        resp.delete_cookie(COOKIE_PRE)
        return resp

    @app.post("/sair")
    async def sair(request: Request):
        s = sessao_de(request)
        if s:
            try:
                await form_com_csrf(request, s)
            except PermissionError as err:
                return erro(s, str(err), 403)
            c = con()
            try:
                banco.encerrar_sessao(c, request.cookies.get(COOKIE, ""))
                banco.auditar(c, "logout", organizacao_id=s["organizacao_id"], usuario_id=s["usuario_id"])
            finally:
                c.close()
        resp = ir("/login")
        resp.delete_cookie(COOKIE)
        return resp

    # ------------------------------------------------------------------ telas
    def pendentes(c, org: int):
        banco.expirar_aprovacoes(c)
        return c.execute("SELECT * FROM central_aprovacoes WHERE organizacao_id = ? AND estado = 'pendente' ORDER BY criado",
                         (org,)).fetchall()

    def pode(s: dict, nivel: str) -> bool:
        c = con()
        try:
            p = banco.papel(c, s["papel"])
        finally:
            c.close()
        return NIVEL_ORDEM.index(nivel) <= NIVEL_ORDEM.index(p["nivel_max"])

    @app.get("/")
    async def hoje(request: Request):
        s = sessao_de(request)
        if not s:
            return ir("/login")
        c = con()
        try:
            pend = pendentes(c, s["organizacao_id"])
            ultimas = c.execute("SELECT * FROM central_execucoes WHERE organizacao_id = ? ORDER BY inicio DESC LIMIT 8",
                                (s["organizacao_id"],)).fetchall()
            pedidos = c.execute("SELECT id, texto, origem, tokens, criado FROM central_prompts WHERE organizacao_id = ? "
                                "ORDER BY criado DESC LIMIT 5", (s["organizacao_id"],)).fetchall()
            sugestoes = sugestoes_regra(c, s["organizacao_id"])
        finally:
            c.close()
        corpo = [caixa_pedido(s["csrf"], pedidos), '<section><h2>Esperando você</h2>']
        if pend:
            corpo.append(f'<p><a class="botao" href="/aprovar">{len(pend)} aprovação(ões) pendente(s)</a></p>')
        else:
            corpo.append('<p class="calmo">Nada esperando aprovação.</p>')
        corpo.append('</section><section><h2>Agora</h2><div class="rapidos">')
        for receita, sub, opcoes in RAPIDOS:
            r = dados["receitas"].get(receita)
            if r and r["nivel"] in NIVEL_ORDEM:
                rotulo = " ".join(p for p in (receita, sub, *opcoes) if p)
                corpo.append(form_rapido(s["csrf"], receita, sub, opcoes, rotulo))
        corpo.append('</div></section>')
        if sugestoes:
            corpo.append('<section><h2>Virar regra (economiza tokens)</h2>' + "".join(
                f'<p>A IA local resolveu <code>{e(chave)}</code> {n} vezes, por exemplo “{e(ex[:80])}”. '
                f'Acrescente uma frase assim em <code>gatilhos</code> dessa receita em <code>data/central.json</code>: '
                'da próxima vez vai por regra, com 0 tokens.</p>' for chave, n, ex in sugestoes) + '</section>')
        for receita, titulo in (("lembrar", "Guardar no núcleo"),):
            r = dados["receitas"].get(receita)
            if r and r["nivel"] in NIVEL_ORDEM:
                corpo.append(f'<section><h2>{e(titulo)}</h2>{form_receita(s["csrf"], dados, receita, r)}</section>')
        corpo.append('<section><h2>Últimas execuções</h2>' + tabela_execucoes(ultimas) + '</section>')
        return HTMLResponse(pagina("Hoje", "".join(corpo), s, len(pend)))

    @app.get("/comandos")
    async def comandos(request: Request):
        s = sessao_de(request)
        if not s:
            return ir("/login")
        c = con()
        try:
            n_pend = len(pendentes(c, s["organizacao_id"]))
        finally:
            c.close()
        corpo = ['<p class="calmo">Só aparece o que está em <code>data/central.json</code>. '
                 'Os valores são conferidos de novo no servidor antes de rodar.</p>']
        for area, itens in allowlist.visiveis(dados).items():
            corpo.append(f'<section><h2>{e(dados["areas"].get(area, area))}</h2>')
            for nome, r in sorted(itens):
                corpo.append(cartao_receita(s["csrf"], dados, nome, r))
            corpo.append('</section>')
        return HTMLResponse(pagina("Comandos", "".join(corpo), s, n_pend))

    @app.post("/rodar")
    async def rodar(request: Request):
        s = sessao_de(request)
        if not s:
            return ir("/login")
        try:
            form = await form_com_csrf(request, s)
        except PermissionError as err:
            return erro(s, str(err), 403)
        receita = str(form.get("receita", ""))
        sub = str(form.get("subcomando", "")) or None
        campos = {k[2:]: str(v) for k, v in form.multi_items() if k.startswith("a_")}
        campos.update({k: str(v) for k, v in form.multi_items() if k.startswith("sub_")})
        opcoes = [str(v) for k, v in form.multi_items() if k == "opcao"]
        c = con()
        try:
            try:
                args, nivel = allowlist.montar(dados, receita, campos, opcoes, sub)
            except allowlist.ErroAllowlist as err:
                banco.auditar(c, "receita.recusada", organizacao_id=s["organizacao_id"], usuario_id=s["usuario_id"],
                              alvo=receita, resultado=str(err))
                return erro(s, f"Recusado: {err}")
            if not pode(s, nivel):
                banco.auditar(c, "receita.sem-permissao", organizacao_id=s["organizacao_id"], usuario_id=s["usuario_id"],
                              alvo=receita, nivel=nivel)
                return erro(s, "O seu papel não permite isso.", 403)
            if nivel == "pede-ok":
                id_ = banco.criar_aprovacao(c, s["organizacao_id"], receita, args, s["usuario_id"], "web",
                                            dados.get("aprovacao", {}).get("validade_min", 30),
                                            {"campos": campos, "opcoes": opcoes, "subcomando": sub})
                banco.auditar(c, "aprovacao.pedida", organizacao_id=s["organizacao_id"], usuario_id=s["usuario_id"],
                              alvo=f"{id_} {receita} {json.dumps(args, ensure_ascii=False)}", nivel=nivel)
                return ir("/aprovar")
        finally:
            c.close()
        return iniciar(s, receita, args, nivel, "web")

    def iniciar(s: dict, receita: str, args: list[str], nivel: str, origem: str):
        r = dados["receitas"][receita]
        try:
            id_ = ex.iniciar(receita, args, nivel=nivel, organizacao_id=s["organizacao_id"], usuario_id=s["usuario_id"],
                             origem=origem, timeout=int(r.get("timeout", 900)), python=r.get("python"))
        except RuntimeError as err:
            return erro(s, str(err), 409)
        return ir(f"/execucao/{id_}")

    # ------------------------------------------------------------------ pedido em português (prompt)
    @app.post("/prompt")
    async def pedido(request: Request):
        s = sessao_de(request)
        if not s:
            return ir("/login")
        try:
            form = await form_com_csrf(request, s)
        except PermissionError as err:
            return erro(s, str(err), 403)
        texto = " ".join(str(form.get("texto", "")).split())[:1000]
        if not texto:
            return ir("/")
        plano = await run_in_threadpool(prompt.planejar, dados, texto)
        id_ = secrets.token_urlsafe(9)
        c = con()
        try:
            c.execute("INSERT INTO central_prompts (id, organizacao_id, usuario_id, texto, origem, plano, tokens, criado) "
                      "VALUES (?, ?, ?, ?, ?, ?, ?, ?)", (id_, s["organizacao_id"], s["usuario_id"], texto, plano.origem,
                                                         plano.para_json(), plano.tokens, banco._iso(banco.agora())))
            banco.auditar(c, "prompt", organizacao_id=s["organizacao_id"], usuario_id=s["usuario_id"], alvo=texto[:200],
                          resultado=f"{plano.origem}; {len(plano.validos)} passo(s); ~{plano.tokens} tokens")
        finally:
            c.close()
        if plano.roda_sozinho:
            executar_plano(s, id_)
        return ir(f"/prompt/{id_}")

    def executar_plano(s: dict, id_: str) -> str | None:
        """Roda o plano guardado uma vez só: confere a allowlist de novo, roda o que pode e manda o resto para aprovação."""
        c = con()
        try:
            linha = c.execute("SELECT plano, executado FROM central_prompts WHERE id = ? AND organizacao_id = ?",
                              (id_, s["organizacao_id"])).fetchone()
        finally:
            c.close()
        if not linha:
            return "Pedido não encontrado."
        if linha["executado"]:
            return "Esse plano já foi executado."
        passos = prompt.validar(dados, [prompt.Passo(p["receita"], p.get("subcomando"), p.get("campos", {}), p.get("opcoes", []))
                                        for p in json.loads(linha["plano"])["passos"] if not p.get("erro")])
        problema = ex.sem_vaga([p.receita for p in passos if not p.erro and p.nivel in ("automatico", "avisa")])
        if problema:
            return problema
        c = con()
        try:
            marcado = c.execute("UPDATE central_prompts SET executado = ? WHERE id = ? AND organizacao_id = ? AND executado IS NULL",
                                (banco._iso(banco.agora()), id_, s["organizacao_id"])).rowcount
        finally:
            c.close()
        if marcado != 1:
            return "Esse plano já foi executado."
        feitos = []
        for p in passos:
            if p.erro:
                feitos.append({"rotulo": p.receita, "erro": p.erro})
                continue
            if not pode(s, p.nivel):
                feitos.append({"rotulo": p.rotulo(), "erro": "o seu papel não permite"})
                continue
            if p.nivel == "pede-ok":
                c = con()
                try:
                    aid = banco.criar_aprovacao(c, s["organizacao_id"], p.receita, p.args, s["usuario_id"], "prompt",
                                                dados.get("aprovacao", {}).get("validade_min", 30),
                                                {"campos": p.campos, "opcoes": p.opcoes, "subcomando": p.subcomando})
                    banco.auditar(c, "aprovacao.pedida", origem="prompt", organizacao_id=s["organizacao_id"],
                                  usuario_id=s["usuario_id"], alvo=f"{aid} {p.rotulo()}", nivel="pede-ok")
                finally:
                    c.close()
                feitos.append({"rotulo": p.rotulo(), "aprovacao": aid})
                continue
            r = dados["receitas"][p.receita]
            try:
                eid = ex.iniciar(p.receita, p.args, nivel=p.nivel, organizacao_id=s["organizacao_id"], usuario_id=s["usuario_id"],
                                 origem="prompt", timeout=int(r.get("timeout", 900)), python=r.get("python"))
                feitos.append({"rotulo": p.rotulo(), "execucao": eid})
            except RuntimeError as err:
                feitos.append({"rotulo": p.rotulo(), "erro": str(err)})
        c = con()
        try:
            c.execute("UPDATE central_prompts SET execucoes = ? WHERE id = ?", (json.dumps(feitos, ensure_ascii=False), id_))
        finally:
            c.close()
        return None

    @app.post("/prompt/{id_}/executar")
    async def executar(request: Request, id_: str):
        s = sessao_de(request)
        if not s:
            return ir("/login")
        try:
            await form_com_csrf(request, s)
        except PermissionError as err:
            return erro(s, str(err), 403)
        problema = executar_plano(s, id_)
        return erro(s, problema, 409) if problema else ir(f"/prompt/{id_}")

    @app.get("/prompt/{id_}")
    async def ver_pedido(request: Request, id_: str):
        s = sessao_de(request)
        if not s:
            return ir("/login")
        c = con()
        try:
            x = c.execute("SELECT * FROM central_prompts WHERE id = ? AND organizacao_id = ?", (id_, s["organizacao_id"])).fetchone()
            n_pend = len(pendentes(c, s["organizacao_id"]))
            estados = {}
            if x:
                for f in json.loads(x["execucoes"]):
                    if f.get("execucao"):
                        y = c.execute("SELECT fim, codigo, saida FROM central_execucoes WHERE id = ?", (f["execucao"],)).fetchone()
                        estados[f["execucao"]] = y
        finally:
            c.close()
        if not x:
            return erro(s, "Pedido não encontrado.", 404)
        return HTMLResponse(pagina("Pedido", tela_pedido(s["csrf"], x, estados), s, n_pend))

    # ------------------------------------------------------------------ telas de dados (roteiro, estudo, empresas, serviços, núcleo)
    def tela_simples(request: Request, titulo: str, gerar):
        s = sessao_de(request)
        if not s:
            return ir("/login")
        c = con()
        try:
            n_pend = len(pendentes(c, s["organizacao_id"]))
        finally:
            c.close()
        try:
            corpo = gerar(s)
        except Exception as err:  # noqa: BLE001  a tela mostra o problema em vez de cair
            corpo = f'<p class="erro">Não consegui montar esta tela: {e(type(err).__name__)}: {e(str(err))[:200]}</p>'
        return HTMLResponse(pagina(titulo, corpo, s, n_pend))

    @app.get("/roteiro")
    async def tela_roteiro(request: Request, empresa: str = ""):
        emp = empresa if re.fullmatch(r"[a-z]{2,20}", empresa or "") else None
        return await run_in_threadpool(tela_simples, request, "Roteiro", lambda s: telas.roteiro(s["csrf"], emp))

    @app.get("/estudo")
    async def tela_estudo(request: Request):
        return await run_in_threadpool(tela_simples, request, "Estudo", lambda s: telas.estudo(s["csrf"], dados, cartao_receita))

    @app.get("/empresas")
    async def tela_empresas(request: Request):
        return await run_in_threadpool(tela_simples, request, "Empresas e rendas", lambda s: telas.empresas(s["csrf"]))

    @app.get("/servicos")
    async def tela_servicos(request: Request):
        return await run_in_threadpool(tela_simples, request, "Serviços", lambda s: telas.servicos(s["csrf"], dados, cartao_receita))

    @app.get("/nucleo")
    async def tela_nucleo(request: Request, q: str = ""):
        return await run_in_threadpool(tela_simples, request, "Núcleo", lambda s: telas.nucleo(s["csrf"], q[:120]))

    @app.get("/ajuda")
    async def tela_ajuda(request: Request):
        return tela_simples(request, "Ajuda", lambda s: telas.AJUDA)

    async def acao_nucleo(request: Request, acao: str, fazer, voltar: str):
        s = sessao_de(request)
        if not s:
            return ir("/login")
        try:
            form = await form_com_csrf(request, s)
        except PermissionError as err:
            return erro(s, str(err), 403)
        if not pode(s, "avisa"):
            return erro(s, "O seu papel não permite isso.", 403)
        try:
            alvo = await run_in_threadpool(fazer, form)
        except (ValueError, KeyError) as err:
            return erro(s, f"Recusado: {err}")
        c = con()
        try:
            banco.auditar(c, acao, organizacao_id=s["organizacao_id"], usuario_id=s["usuario_id"], alvo=str(alvo)[:200], nivel="avisa")
        finally:
            c.close()
        return ir(voltar)

    @app.post("/roteiro/feito")
    async def roteiro_feito(request: Request):
        return await acao_nucleo(request, "roteiro.feito", lambda f: telas.marcar_feito(str(f.get("passo", ""))[:60]), "/roteiro")

    @app.post("/nucleo/lembrar")
    async def nucleo_lembrar(request: Request):
        return await acao_nucleo(request, "nucleo.lembrar",
                                 lambda f: telas.lembrar(str(f.get("texto", "")), str(f.get("tipo", "nota"))), "/nucleo")

    @app.post("/nucleo/tarefa-nova")
    async def nucleo_tarefa_nova(request: Request):
        return await acao_nucleo(request, "nucleo.tarefa", lambda f: telas.tarefa_nova(str(f.get("titulo", ""))), "/nucleo")

    @app.post("/nucleo/tarefa")
    async def nucleo_tarefa(request: Request):
        def feita(f):
            tid = str(f.get("id", ""))
            if not tid.isdigit():
                raise ValueError("id inválido")
            telas.tarefa_feita(int(tid))
            return f"tarefa {tid} feita"
        return await acao_nucleo(request, "nucleo.tarefa-feita", feita, "/nucleo")

    @app.get("/execucao/{id_}")
    async def execucao(request: Request, id_: str):
        s = sessao_de(request)
        if not s:
            return ir("/login")
        c = con()
        try:
            x = c.execute("SELECT * FROM central_execucoes WHERE id = ? AND organizacao_id = ?",
                          (id_, s["organizacao_id"])).fetchone()
        finally:
            c.close()
        if not x:
            return erro(s, "Execução não encontrada.", 404)
        args = " ".join(json.loads(x["args"]))
        estado = "rodando…" if x["fim"] is None else f"terminou com código {x['codigo']}"
        saida = "" if x["fim"] is None else e(x["saida"])
        corpo = (f'<p><strong>{e(x["receita"])}</strong> <code>{e(args)}</code> · {e(ROTULO_NIVEL.get(x["nivel"], x["nivel"]))} · '
                 f'<span data-estado-de="{e(id_)}">{e(estado)}</span></p>'
                 f'<pre class="saida" data-id="{e(id_)}" data-vivo="{1 if x["fim"] is None else 0}">{saida}</pre>'
                 '<p><a href="/">Voltar ao Hoje</a> · <a href="/comandos">Comandos</a></p>')
        return HTMLResponse(pagina(f"Execução: {x['receita']}", corpo, s))

    @app.get("/execucao/{id_}/eventos")
    async def eventos(request: Request, id_: str):
        s = sessao_de(request)
        if not s:
            return Response(status_code=401)
        c = con()
        try:
            x = c.execute("SELECT id FROM central_execucoes WHERE id = ? AND organizacao_id = ?",
                          (id_, s["organizacao_id"])).fetchone()
        finally:
            c.close()
        if not x:
            return Response(status_code=404)

        async def fluxo():
            desde = 0
            while True:
                lido = ex.ler(id_, desde)
                if lido is None:
                    c2 = con()
                    try:
                        y = c2.execute("SELECT saida, codigo FROM central_execucoes WHERE id = ?", (id_,)).fetchone()
                    finally:
                        c2.close()
                    for linha in (y["saida"] or "").splitlines():
                        yield f"data: {json.dumps(linha, ensure_ascii=False)}\n\n"
                    yield f"event: fim\ndata: {y['codigo']}\n\n"
                    return
                linhas, fim, codigo, desde = lido
                for linha in linhas:
                    yield f"data: {json.dumps(linha, ensure_ascii=False)}\n\n"
                if fim:
                    yield f"event: fim\ndata: {codigo}\n\n"
                    return
                if await request.is_disconnected():
                    return
                await asyncio.sleep(0.3)

        return StreamingResponse(fluxo(), media_type="text/event-stream", headers={"X-Accel-Buffering": "no"})

    @app.get("/aprovar")
    async def aprovar_tela(request: Request):
        s = sessao_de(request)
        if not s:
            return ir("/login")
        c = con()
        try:
            pend = pendentes(c, s["organizacao_id"])
            feitas = c.execute("SELECT * FROM central_aprovacoes WHERE organizacao_id = ? AND estado != 'pendente' "
                               "ORDER BY criado DESC LIMIT 15", (s["organizacao_id"],)).fetchall()
        finally:
            c.close()
        corpo = ['<section><h2>Pendentes</h2>']
        if not pend:
            corpo.append('<p class="calmo">Nada esperando você.</p>')
        for a in pend:
            r = dados["receitas"].get(a["receita"], {})
            args = json.loads(a["args"])
            dupla = ""
            if r.get("confirmacao_dupla"):
                dupla = (f'<label>Para confirmar, digite <strong>{e(args[0] if args else "")}</strong>'
                         '<input name="confirmacao" autocomplete="off" inputmode="numeric" required></label>')
            corpo.append(
                f'<div class="cartao"><p><strong>{e(a["receita"])}</strong> <code>{e(" ".join(args))}</code></p>'
                f'<p class="calmo">{e(r.get("descricao", ""))}{(" · " + e(r["motivo"])) if r.get("motivo") else ""}</p>'
                f'<p class="calmo">Pedido em {e(data(a["criado"]))} · vale até {e(a["expira"][11:16])}</p>'
                f'<form method="post" action="/aprovar/{e(a["id"])}" data-confirmar="Rodar {e(a["receita"])} agora?">'
                f'<input type="hidden" name="csrf" value="{e(s["csrf"])}">{dupla}'
                '<div class="linha"><button name="acao" value="aprovar">✅ Aprovar e rodar</button>'
                '<button name="acao" value="recusar" class="secundario" formnovalidate>❌ Recusar</button></div></form></div>')
        corpo.append('</section><section><h2>Decididas</h2>')
        corpo.append('<table><tr><th>Receita</th><th>Estado</th><th>Quando</th></tr>' + "".join(
            f'<tr><td>{e(a["receita"])} <code>{e(" ".join(json.loads(a["args"])))}</code></td><td>{e(a["estado"])}</td>'
            f'<td>{e(data(a["decidido_em"] or a["expira"]))}</td></tr>' for a in feitas) + '</table></section>')
        return HTMLResponse(pagina("Aprovar", "".join(corpo), s, len(pend)))

    @app.post("/aprovar/{id_}")
    async def aprovar(request: Request, id_: str):
        s = sessao_de(request)
        if not s:
            return ir("/login")
        try:
            form = await form_com_csrf(request, s)
        except PermissionError as err:
            return erro(s, str(err), 403)
        aprovar_ = form.get("acao") == "aprovar"
        c = con()
        try:
            if not banco.papel(c, s["papel"])["pode_aprovar"]:
                return erro(s, "O seu papel não pode aprovar.", 403)
            atual = c.execute("SELECT * FROM central_aprovacoes WHERE id = ? AND organizacao_id = ?",
                              (id_, s["organizacao_id"])).fetchone()
            if not atual:
                return erro(s, "Aprovação não encontrada.", 404)
            r = dados["receitas"].get(atual["receita"])
            args = json.loads(atual["args"])
            if aprovar_:
                if not r or r["nivel"] not in NIVEL_ORDEM:
                    return erro(s, "Essa receita não pode mais rodar pela Central (allowlist mudou).", 409)
                if r.get("confirmacao_dupla") and str(form.get("confirmacao", "")).strip() != (args[0] if args else ""):
                    return erro(s, "A confirmação não bate. Nada foi feito.")
                pedido_orig = json.loads(atual["pedido"] or "{}")
                if pedido_orig:
                    try:
                        args2, nivel2 = allowlist.montar(dados, atual["receita"], pedido_orig.get("campos"),
                                                         pedido_orig.get("opcoes"), pedido_orig.get("subcomando"))
                    except allowlist.ErroAllowlist as err:
                        return erro(s, f"A allowlist mudou e este pedido não passa mais: {err}. Nada foi feito.", 409)
                    if args2 != args:
                        return erro(s, "A allowlist mudou os argumentos deste pedido. Peça de novo. Nada foi feito.", 409)
                problema = ex.sem_vaga([atual["receita"]])
                if problema:
                    return erro(s, problema, 409)
            decidida = banco.decidir_aprovacao(c, id_, s["organizacao_id"], s["usuario_id"], aprovar_)
            if not decidida:
                return erro(s, "Essa aprovação já foi decidida ou expirou. Peça de novo.", 409)
            banco.auditar(c, "aprovacao." + ("aprovada" if aprovar_ else "recusada"), organizacao_id=s["organizacao_id"],
                          usuario_id=s["usuario_id"], alvo=f"{id_} {atual['receita']}", nivel="pede-ok")
        finally:
            c.close()
        if not aprovar_:
            return ir("/aprovar")
        resp = iniciar(s, atual["receita"], args, "pede-ok", "aprovacao")
        if not isinstance(resp, RedirectResponse):
            c = con()
            try:
                banco.devolver_aprovacao(c, id_)  # não começou: a aprovação volta para a lista
            finally:
                c.close()
        if isinstance(resp, RedirectResponse):
            exec_id = resp.headers["location"].rsplit("/", 1)[-1]
            c = con()
            try:
                c.execute("UPDATE central_aprovacoes SET execucao_id = ? WHERE id = ?", (exec_id, id_))
            finally:
                c.close()
        return resp

    @app.get("/auditoria")
    async def auditoria(request: Request):
        s = sessao_de(request)
        if not s:
            return ir("/login")
        c = con()
        try:
            ok, linha = banco.verificar_auditoria(c)
            regs = c.execute("SELECT a.*, u.nome FROM central_auditoria a LEFT JOIN central_usuarios u ON u.id = a.usuario_id "
                             "WHERE a.organizacao_id = ? OR a.organizacao_id IS NULL ORDER BY a.id DESC LIMIT 100",
                             (s["organizacao_id"],)).fetchall()
        finally:
            c.close()
        estado = ('<p class="ok">✅ Corrente íntegra: nenhuma linha foi apagada ou mudada.</p>' if ok else
                  f'<p class="erro">🚨 Auditoria alterada a partir da linha {linha}.</p>')
        tabela = '<table><tr><th>Quando</th><th>Quem</th><th>Ação</th><th>Alvo</th><th>Resultado</th></tr>' + "".join(
            f'<tr><td>{e(data(r["quando"]))}</td><td>{e(r["nome"] or r["origem"])}</td><td>{e(r["acao"])}</td>'
            f'<td>{e(r["alvo"][:90])}</td><td>{e(r["resultado"][:60])}</td></tr>' for r in regs) + '</table>'
        return HTMLResponse(pagina("Auditoria", estado + tabela, s))

    @app.get("/api/status")
    async def status(request: Request):
        s = sessao_de(request)
        if not s:
            return JSONResponse({"erro": "login"}, status_code=401)
        c = con()
        try:
            ok = banco.auditoria_resumo(c)
            n = len(pendentes(c, s["organizacao_id"]))
        finally:
            c.close()
        return {"usuario": s["nome"], "papel": s["papel"], "pendentes": n, "rodando": ex.em_andamento(), "auditoria_ok": ok}

    @app.get("/manifest.webmanifest")
    async def manifesto():
        return Response((Path(__file__).parent / "static" / "manifest.webmanifest").read_text(encoding="utf-8"),
                        media_type="application/manifest+json")

    return app


ORIGEM = {"regra": ("regra fixa", "0 tokens"), "voce": ("decisão sua", "0 tokens"), "ia-local": ("IA local", "R$ 0"),
          "fila": ("fila", "a fila escolhe o modelo"), "nada": ("não reconhecido", "0 tokens")}


def sugestoes_regra(c, org: int) -> list[tuple[str, int, str]]:
    """Regra de três (ADR 0014): o que a IA local resolveu 3 vezes do mesmo jeito deve virar regra fixa."""
    cont, exemplo = Counter(), {}
    for linha in c.execute("SELECT texto, plano FROM central_prompts WHERE organizacao_id = ? AND origem = 'ia-local' "
                           "ORDER BY criado DESC LIMIT 300", (org,)):
        passos = [p for p in json.loads(linha["plano"])["passos"] if not p.get("erro")]
        chave = " + ".join(" ".join(x for x in (p["receita"], p.get("subcomando")) if x) for p in passos)
        if chave:
            cont[chave] += 1
            exemplo.setdefault(chave, linha["texto"])
    return [(k, n, exemplo[k]) for k, n in cont.most_common() if n >= 3]


def caixa_pedido(csrf: str, recentes) -> str:
    lista = "".join(f'<li><a href="/prompt/{e(p["id"])}">{e(p["texto"][:70])}</a> '
                    f'<span class="calmo">· {e(ORIGEM.get(p["origem"], (p["origem"], ""))[0])}</span></li>' for p in recentes)
    return ('<section class="pedido"><h2>O que você quer fazer?</h2>'
            '<form method="post" action="/prompt" data-pensando="Pensando… (a IA local pode levar até 1 minuto)">'
            f'<input type="hidden" name="csrf" value="{e(csrf)}">'
            '<textarea name="texto" rows="3" maxlength="1000" required placeholder="Ex.: o que estudo hoje? · como está o backup? · '
            'crie a página de vendas do curso de lógica · lembre que o HD externo está na gaveta"></textarea>'
            '<button>Enviar</button></form>'
            '<p class="calmo">Primeiro tento por regra (0 tokens); depois a IA local (R$ 0). Ações que mudam algo pedem o seu ✅.</p>'
            + (f'<details><summary>Pedidos recentes</summary><ul>{lista}</ul></details>' if recentes else "") + '</section>')


def tela_pedido(csrf: str, x, estados: dict) -> str:
    plano = json.loads(x["plano"])
    nome, custo = ORIGEM.get(x["origem"], (x["origem"], ""))
    tok = f" · ~{x['tokens']} tokens" if x["tokens"] else ""
    partes = [f'<section><p class="pedido-texto">“{e(x["texto"])}”</p>'
              f'<p><span class="nivel">{e(nome)}</span> <span class="calmo">{e(custo)}{tok}</span></p>']
    if plano.get("resposta"):
        partes.append(f'<p>{e(plano["resposta"])}</p>')
    if plano.get("sensivel"):
        partes.append(f'<p class="erro">Dado sensível no pedido ({e(", ".join(plano["sensivel"]))}): só IA local.</p>')
    partes.append('</section>')
    if plano["passos"]:
        partes.append('<section><h2>Plano</h2><ol>')
        for p in plano["passos"]:
            rot = " ".join(v for v in (p["receita"], *(p.get("args") or [])) if v)
            if p.get("erro"):
                partes.append(f'<li><code>{e(p["receita"])}</code> <span class="erro">recusado: {e(p["erro"])}</span></li>')
            else:
                partes.append(f'<li><code>just {e(rot)}</code> <span class="nivel n-{e(p["nivel"])}">{e(ROTULO_NIVEL[p["nivel"]])}</span></li>')
        partes.append('</ol>')
        validos = [p for p in plano["passos"] if not p.get("erro")]
        if x["executado"] is None and validos:
            partes.append(f'<form method="post" action="/prompt/{e(x["id"])}/executar">'
                          f'<input type="hidden" name="csrf" value="{e(csrf)}"><button>Executar plano</button></form>'
                          '<p class="calmo">O que pede aprovação vai para a tela Aprovar; o resto roda agora.</p>')
        partes.append('</section>')
    feitos = json.loads(x["execucoes"])
    if feitos:
        partes.append('<section><h2>Resultado</h2>')
        for f in feitos:
            if f.get("erro"):
                partes.append(f'<p><code>{e(f["rotulo"])}</code> <span class="erro">{e(f["erro"])}</span></p>')
            elif f.get("aprovacao"):
                partes.append(f'<p><code>{e(f["rotulo"])}</code> → <a href="/aprovar">esperando o seu ✅</a></p>')
            else:
                y = estados.get(f["execucao"])
                vivo = y is None or y["fim"] is None
                estado = "rodando…" if vivo else ("terminou: ok" if y["codigo"] == 0 else f"terminou com código {y['codigo']}")
                saida = "" if vivo else e(y["saida"])
                partes.append(f'<h3><a href="/execucao/{e(f["execucao"])}">{e(f["rotulo"])}</a> · '
                              f'<span data-estado-de="{e(f["execucao"])}">{e(estado)}</span></h3>'
                              f'<pre class="saida" data-id="{e(f["execucao"])}" data-vivo="{1 if vivo else 0}">{saida}</pre>')
        partes.append('</section>')
    partes.append('<p><a href="/">Voltar ao Hoje</a></p>')
    return "".join(partes)



# ---------------------------------------------------------------------- HTML
def pagina(titulo: str, corpo: str, s: dict | None, pendentes: int | None = None) -> str:
    nav = ""
    if s:
        badge = f' <span class="badge">{pendentes}</span>' if pendentes else ""
        nav = ('<nav><a href="/">Hoje</a><a href="/roteiro">Roteiro</a><a href="/estudo">Estudo</a>'
               '<a href="/empresas">Empresas</a><a href="/servicos">Serviços</a><a href="/nucleo">Núcleo</a>'
               f'<a href="/comandos">Comandos</a><a href="/aprovar">Aprovar{badge}</a><a href="/auditoria">Auditoria</a>'
               '<a href="/ajuda">Ajuda</a>'
               f'<form method="post" action="/sair"><input type="hidden" name="csrf" value="{e(s["csrf"])}">'
               f'<button class="link">Sair ({e(s["nome"])})</button></form></nav>')
    return ('<!doctype html><html lang="pt-BR"><head><meta charset="utf-8">'
            '<meta name="viewport" content="width=device-width, initial-scale=1">'
            f'<title>{e(titulo)} · Central AMtech</title><link rel="stylesheet" href="/static/central.css">'
            '<link rel="manifest" href="/manifest.webmanifest"><link rel="icon" href="/static/icone.svg">'
            '<meta name="theme-color" content="#1f4e79"><script src="/static/central.js" defer></script></head>'
            f'<body><header><strong>Central AMtech</strong>{nav}</header><main><h1>{e(titulo)}</h1>{corpo}</main></body></html>')


def tela_login(pre: str, msg: str = "") -> str:
    aviso = f'<p class="erro">{e(msg)}</p>' if msg else ""
    return (f'{aviso}<form method="post" action="/login" class="cartao">'
            f'<input type="hidden" name="pre" value="{e(pre)}">'
            '<label>Usuário<input name="usuario" autocomplete="username" required autofocus></label>'
            '<label>Senha<input name="senha" type="password" autocomplete="current-password" required></label>'
            '<button>Entrar</button></form>'
            '<p class="calmo">Sem usuário? No Ubuntu: <code>just central-usuario alan</code></p>')


def data(iso: str | None) -> str:
    """2026-11-27T03:44:14 → 27/11 03:44"""
    return f"{iso[8:10]}/{iso[5:7]} {iso[11:16]}" if iso and len(iso) >= 16 else ""


def tabela_execucoes(linhas) -> str:
    if not linhas:
        return '<p class="calmo">Nada rodou ainda.</p>'
    return ('<table><tr><th>Receita</th><th>Quando</th><th>Resultado</th></tr>' + "".join(
        f'<tr><td><a href="/execucao/{e(x["id"])}">{e(x["receita"])}</a> <code>{e(" ".join(json.loads(x["args"])))[:60]}</code></td>'
        f'<td>{e(data(x["inicio"]))}</td><td>{"rodando" if x["fim"] is None else ("ok" if x["codigo"] == 0 else "falhou")}</td></tr>'
        for x in linhas) + '</table>')


def _opcoes_fixas(padrao: str) -> list[str] | None:
    m = re.fullmatch(r"\^\(([a-z0-9|_.-]+)\)\$", padrao)
    return m.group(1).split("|") if m else None


def _campo(dados: dict, nome_html: str, rotulo: str, ref: str, obrigatorio: bool) -> str:
    req = " required" if obrigatorio else ""
    if ref.startswith("texto:"):
        n = int(ref.split(":", 1)[1])
        if n > 200:
            return f'<label>{e(rotulo)}<textarea name="{e(nome_html)}" maxlength="{n}" rows="3"{req}></textarea></label>'
        return f'<label>{e(rotulo)}<input name="{e(nome_html)}" maxlength="{n}"{req}></label>'
    padrao = dados["padroes"].get(ref, ref)
    fixas = _opcoes_fixas(padrao)
    if fixas:
        vazio = "" if obrigatorio else '<option value="">(nenhum)</option>'
        ops = "".join(f'<option>{e(o)}</option>' for o in fixas)
        return f'<label>{e(rotulo)}<select name="{e(nome_html)}"{req}>{vazio}{ops}</select></label>'
    return (f'<label>{e(rotulo)}<input name="{e(nome_html)}" pattern="{e(padrao.strip("^$"))}" autocomplete="off"'
            f' placeholder="{e(ref)}"{req}></label>')


BOTAO = {"pedir": "Enviar para a fila", "lembrar": "Guardar", "buscar": "Buscar"}


def form_receita(csrf: str, dados: dict, nome: str, r: dict, sub: str | None = None) -> str:
    nivel = r["nivel"]
    if sub and sub in r.get("subcomandos_pede_ok", []):
        nivel = "pede-ok"
    partes = [f'<form method="post" action="/rodar"><input type="hidden" name="csrf" value="{e(csrf)}">'
              f'<input type="hidden" name="receita" value="{e(nome)}">']
    if sub is not None:
        partes.append(f'<input type="hidden" name="subcomando" value="{e(sub)}">')
        for i, ref in enumerate(r["subcomandos"][sub], 1):
            partes.append(_campo(dados, f"sub_{i}", ref.split(":")[0], ref, True))
    for a in r.get("args", []):
        ref = f"texto:{a['max']}" if a.get("tipo") == "texto" else a["padrao"]
        partes.append(_campo(dados, "a_" + a["nome"], a["nome"], ref, a.get("obrigatorio", True)))
    for o in r.get("opcoes", []):
        partes.append(f'<label class="check"><input type="checkbox" name="opcao" value="{e(o)}"> {e(o)}</label>')
    for o in r.get("opcoes_pede_ok", []):
        partes.append(f'<label class="check"><input type="checkbox" name="opcao" value="{e(o)}"> {e(o)} (pede aprovação)</label>')
    botao = "Pedir aprovação" if nivel == "pede-ok" else BOTAO.get(nome, "Rodar")
    partes.append(f'<button>{botao}</button></form>')
    return "".join(partes)


def form_rapido(csrf: str, receita: str, sub: str | None, opcoes: list[str], rotulo: str) -> str:
    extra = f'<input type="hidden" name="subcomando" value="{e(sub)}">' if sub else ""
    extra += "".join(f'<input type="hidden" name="opcao" value="{e(o)}">' for o in opcoes)
    return (f'<form method="post" action="/rodar"><input type="hidden" name="csrf" value="{e(csrf)}">'
            f'<input type="hidden" name="receita" value="{e(receita)}">{extra}<button class="secundario">{e(rotulo)}</button></form>')


def cartao_receita(csrf: str, dados: dict, nome: str, r: dict) -> str:
    cab = (f'<summary><strong>{e(nome)}</strong> <span class="nivel n-{e(r["nivel"])}">{e(ROTULO_NIVEL[r["nivel"]])}</span>'
           f'{" 📱" if r.get("celular") else ""}</summary><p class="calmo">{e(r.get("descricao", ""))}</p>')
    if r["nivel"] == "so-terminal":
        return f'<details class="cartao">{cab}<p class="calmo">Rode no terminal: <code>just {e(nome)}</code> · {e(r.get("motivo", ""))}</p></details>'
    if r.get("subcomandos"):
        corpo = "".join(f'<div class="sub"><h3>{e(nome)} {e(sub)}</h3>{form_receita(csrf, dados, nome, r, sub)}</div>'
                        for sub in r["subcomandos"])
    else:
        corpo = form_receita(csrf, dados, nome, r)
    return f'<details class="cartao" id="{e(nome)}">{cab}{corpo}</details>'
