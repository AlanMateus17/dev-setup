import hashlib
import json
import os
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import allowlist  # noqa: E402
import banco  # noqa: E402
from allowlist import ErroAllowlist, montar  # noqa: E402

MALICIOSOS = ['0.1"; touch /tmp/x; "', "$(id)", "`id`", "-rf", "--exec=x", "0.1\x00", "a; b", "../../etc/passwd"]


class TestAllowlistReal(unittest.TestCase):
    def test_repositorio_sem_erros(self):
        self.assertEqual(allowlist.checar(), [])

    def test_check_pega_receita_que_cola_argumento(self):
        with tempfile.TemporaryDirectory() as d:
            raiz = Path(d)
            (raiz / "data").mkdir()
            (raiz / "justfile").write_text('set positional-arguments\n\nx texto:\n    echo "{{texto}}"\n', encoding="utf-8")
            (raiz / "data" / "central.json").write_text(
                '{"padroes": {}, "areas": {"a": "A"}, "receitas": {"x": {"area": "a", "nivel": "automatico", "args": []}}}',
                encoding="utf-8")
            erros = allowlist.checar(raiz)
            self.assertTrue(any("injeção" in e for e in erros), erros)

    def test_check_pega_lista_em_receita_de_parametro_fixo(self):
        """Achado da revisão: um argumento a mais vira outra receita para o just."""
        with tempfile.TemporaryDirectory() as d:
            raiz = Path(d)
            (raiz / "data").mkdir()
            (raiz / "justfile").write_text('set positional-arguments\n\nbuscar texto:\n    echo "$1"\n', encoding="utf-8")
            (raiz / "data" / "central.json").write_text(json.dumps({"padroes": {}, "areas": {"a": "A"}, "receitas": {
                "buscar": {"area": "a", "nivel": "automatico", "args": [{"nome": "texto", "padrao": "^[a-z]+$", "repetir": True}]}}}),
                encoding="utf-8")
            self.assertTrue(any("não é variádica" in e for e in allowlist.checar(raiz)))

    def test_check_pega_receita_sem_classificacao(self):
        with tempfile.TemporaryDirectory() as d:
            raiz = Path(d)
            (raiz / "data").mkdir()
            (raiz / "justfile").write_text("nova:\n    echo oi\n", encoding="utf-8")
            (raiz / "data" / "central.json").write_text('{"padroes": {}, "areas": {}, "receitas": {}}', encoding="utf-8")
            self.assertTrue(any("não está em data/central.json" in e for e in allowlist.checar(raiz)))


class TestMontar(unittest.TestCase):
    def setUp(self):
        self.d = allowlist.carregar()

    def test_argumento_valido(self):
        self.assertEqual(montar(self.d, "colher", {"etapa": "0.2"}, ["--seco"]), (["0.2", "--seco"], "pede-ok"))
        self.assertEqual(montar(self.d, "agora", {}), ([], "automatico"))
        self.assertEqual(montar(self.d, "agora", {"empresa": "software"}), (["software"], "automatico"))

    def test_maliciosos_recusados_em_padrao(self):
        for v in MALICIOSOS:
            with self.subTest(v=v), self.assertRaises(ErroAllowlist):
                montar(self.d, "colher", {"etapa": v})

    def test_texto_livre_vai_como_um_argumento_so(self):
        args, nivel = montar(self.d, "pedir", {"texto": 'criar "página" $(id)\nsegunda linha'})
        self.assertEqual(args, ['criar "página" $(id) segunda linha'])
        self.assertEqual(nivel, "avisa")
        with self.assertRaises(ErroAllowlist):
            montar(self.d, "pedir", {"texto": "--opcao-escondida"})
        with self.assertRaises(ErroAllowlist):
            montar(self.d, "pedir", {"texto": "x" * 1001})

    def test_subcomandos(self):
        self.assertEqual(montar(self.d, "professor", {}, subcomando="hoje"), (["hoje"], "automatico"))
        self.assertEqual(montar(self.d, "professor", {"sub_1": "b-aprender", "sub_2": "8"}, subcomando="nota"),
                         (["nota", "b-aprender", "8"], "avisa"))
        self.assertEqual(montar(self.d, "akita", {"sub_1": "ak-1"}, subcomando="aprovar")[1], "pede-ok")
        with self.assertRaises(ErroAllowlist):
            montar(self.d, "akita", {}, subcomando="sincronizar")
        with self.assertRaises(ErroAllowlist):
            montar(self.d, "professor", {"sub_1": "x", "sub_2": "11"}, subcomando="nota")

    def test_opcao_eleva_nivel(self):
        self.assertEqual(montar(self.d, "validar", {}, ["--rapido"])[1], "automatico")
        self.assertEqual(montar(self.d, "validar", {}, ["--restaurar"])[1], "pede-ok")
        with self.assertRaises(ErroAllowlist):
            montar(self.d, "validar", {}, ["--qualquer"])

    def test_proibidas_e_so_terminal_nao_montam(self):
        for receita in ("senha", "senhas-rodar", "medir", "cofre-abrir", "central", "diag", "vitrine"):
            with self.subTest(receita=receita), self.assertRaises(ErroAllowlist):
                montar(self.d, receita, {})

    def test_campo_desconhecido(self):
        with self.assertRaises(ErroAllowlist):
            montar(self.d, "agora", {"empresa": "software", "extra": "x"})

    def test_site_so_le_sem_aprovacao_com_checar(self):
        self.assertEqual(montar(self.d, "site", {"marca": "amtech"}), (["amtech"], "pede-ok"))
        self.assertEqual(montar(self.d, "site", {"marca": "amtech"}, ["--checar"]), (["amtech", "--checar"], "automatico"))

    def test_aprovar_so_numero(self):
        self.assertEqual(montar(self.d, "aprovar", {"n": "41"}), (["41"], "pede-ok"))
        with self.assertRaises(ErroAllowlist):
            montar(self.d, "aprovar", {"n": "41; rm"})


class TestBanco(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self._seg = os.environ.get("AMTECH_CENTRAL_SEGREDOS")
        os.environ["AMTECH_CENTRAL_SEGREDOS"] = str(Path(self.tmp.name) / "segredos")
        self.caminho = Path(self.tmp.name) / "nucleo.db"
        banco.migrar(self.caminho)
        self.con = banco.abrir(self.caminho)

    def tearDown(self):
        self.con.close()
        if self._seg is None:
            os.environ.pop("AMTECH_CENTRAL_SEGREDOS", None)
        else:
            os.environ["AMTECH_CENTRAL_SEGREDOS"] = self._seg
        self.tmp.cleanup()

    def test_migracao_idempotente(self):
        banco.migrar(self.caminho)
        self.assertEqual(self.con.execute("SELECT COUNT(*) FROM central_organizacoes").fetchone()[0], 1)

    def test_senha_curta_e_login(self):
        with self.assertRaises(ValueError):
            banco.salvar_usuario(self.con, "alan", "curta")
        banco.salvar_usuario(self.con, "alan", "senha-longa-123")
        self.assertIsNotNone(banco.autenticar(self.con, "alan", "senha-longa-123"))
        self.assertIsNone(banco.autenticar(self.con, "alan", "errada-errada"))
        self.assertIsNone(banco.autenticar(self.con, "ninguem", "senha-longa-123"))

    def test_bloqueio_depois_de_5_falhas(self):
        banco.salvar_usuario(self.con, "alan", "senha-longa-123")
        for _ in range(5):
            banco.autenticar(self.con, "alan", "errada-errada")
        self.assertIsNone(banco.autenticar(self.con, "alan", "senha-longa-123"), "deveria estar bloqueado")
        depois = banco.agora() + banco.BLOQUEIO + banco.timedelta(seconds=1)
        self.assertIsNotNone(banco.autenticar(self.con, "alan", "senha-longa-123", depois))

    def test_sessao_expira_ociosa(self):
        uid = banco.salvar_usuario(self.con, "alan", "senha-longa-123")
        u = self.con.execute("SELECT * FROM central_usuarios WHERE id = ?", (uid,)).fetchone()
        token, _ = banco.criar_sessao(self.con, u)
        self.assertIsNotNone(banco.sessao(self.con, token))
        self.assertIsNone(banco.sessao(self.con, token, banco.agora() + banco.SESSAO_OCIOSA + banco.timedelta(minutes=1)))

    def test_troca_de_senha_derruba_sessoes(self):
        uid = banco.salvar_usuario(self.con, "alan", "senha-longa-123")
        u = self.con.execute("SELECT * FROM central_usuarios WHERE id = ?", (uid,)).fetchone()
        token, _ = banco.criar_sessao(self.con, u)
        banco.salvar_usuario(self.con, "alan", "outra-senha-456")
        self.assertIsNone(banco.sessao(self.con, token))

    def test_auditoria_detecta_alteracao(self):
        for i in range(3):
            banco.auditar(self.con, f"acao{i}")
        self.assertEqual(banco.verificar_auditoria(self.con), (True, None))
        self.con.execute("UPDATE central_auditoria SET resultado = 'mexido' WHERE id = 2")
        self.assertEqual(banco.verificar_auditoria(self.con), (False, 2))

    def test_auditoria_detecta_linha_apagada(self):
        for i in range(3):
            banco.auditar(self.con, f"acao{i}")
        self.con.execute("DELETE FROM central_auditoria WHERE id = 2")
        self.assertEqual(banco.verificar_auditoria(self.con), (False, 3))

    def test_auditoria_recalculada_sem_a_chave_e_detectada(self):
        """Achado da revisão: com SHA-256 puro, quem mexe no banco recalcula a corrente. Com HMAC, não."""
        for i in range(3):
            banco.auditar(self.con, f"acao{i}")
        linhas = self.con.execute("SELECT * FROM central_auditoria ORDER BY id").fetchall()
        anterior = banco.INICIO_CORRENTE
        for linha in linhas:  # o atacante reescreve tudo com SHA-256 (não tem a chave)
            campos = {c: linha[c] for c in banco._CAMPOS_AUDITORIA}
            if linha["id"] == 2:
                campos["resultado"] = "mexido"
            h = hashlib.sha256((anterior + json.dumps(campos, ensure_ascii=False, sort_keys=True,
                                                       separators=(",", ":"))).encode()).hexdigest()
            self.con.execute("UPDATE central_auditoria SET resultado = ?, hash_anterior = ?, hash = ? WHERE id = ?",
                             (campos["resultado"], anterior, h, linha["id"]))
            anterior = h
        self.assertFalse(banco.verificar_auditoria(self.con)[0])

    def test_auditoria_linhas_apagadas_no_fim(self):
        for i in range(4):
            banco.auditar(self.con, f"acao{i}")
        self.con.execute("DELETE FROM central_auditoria WHERE id >= 3")
        self.assertFalse(banco.verificar_auditoria(self.con)[0], "a âncora deveria acusar as linhas apagadas")
        self.assertFalse(banco.auditoria_resumo(self.con))

    def test_auditoria_v1_antes_da_chave_continua_valida(self):
        # linhas antigas (SHA-256, assinatura 1) seguidas de linhas novas (HMAC)
        anterior = banco.INICIO_CORRENTE
        for i in range(2):
            campos = {c: None for c in banco._CAMPOS_AUDITORIA}
            campos.update({"quando": f"2026-11-27T0{i}:00:00", "origem": "web", "acao": f"v1-{i}", "alvo": "", "nivel": "", "resultado": ""})
            h = banco._hash_auditoria(anterior, campos, 1)
            self.con.execute("INSERT INTO central_auditoria (quando, organizacao_id, usuario_id, origem, acao, alvo, nivel, resultado, "
                             "hash_anterior, hash, assinatura) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, 1)",
                             (*[campos[c] for c in banco._CAMPOS_AUDITORIA], anterior, h))
            anterior = h
        banco.auditar(self.con, "v2")
        self.assertEqual(banco.verificar_auditoria(self.con), (True, None))
        self.con.execute("UPDATE central_auditoria SET assinatura = 1 WHERE acao = 'v2'")
        self.assertFalse(banco.verificar_auditoria(self.con)[0], "linha sem chave depois da primeira linha com chave")

    def test_ancora_apagada_e_acusada(self):
        for i in range(3):
            banco.auditar(self.con, f"acao{i}")
        banco._ancora().unlink()
        self.con.execute("DELETE FROM central_auditoria WHERE id = 3")
        self.assertFalse(banco.verificar_auditoria(self.con)[0])
        self.assertFalse(banco.auditoria_resumo(self.con))

    def test_rebaixar_tudo_para_v1_e_acusado(self):
        for i in range(3):
            banco.auditar(self.con, f"acao{i}")
        anterior = banco.INICIO_CORRENTE
        for linha in self.con.execute("SELECT * FROM central_auditoria ORDER BY id").fetchall():
            campos = {c: linha[c] for c in banco._CAMPOS_AUDITORIA}
            h = banco._hash_auditoria(anterior, campos, 1)
            self.con.execute("UPDATE central_auditoria SET assinatura = 1, hash_anterior = ?, hash = ? WHERE id = ?",
                             (anterior, h, linha["id"]))
            anterior = h
        banco._ancora().write_text(f"3 {anterior} 999 {'0' * 64}\n")  # sem a chave, a âncora não confere
        self.assertFalse(banco.verificar_auditoria(self.con)[0])

    def test_apagar_chave_e_ancora_e_acusado(self):
        for i in range(3):
            banco.auditar(self.con, f"acao{i}")
        pasta = Path(os.environ["AMTECH_CENTRAL_SEGREDOS"])
        (pasta / "central-auditoria.key").unlink()
        banco._ancora().unlink()
        self.assertFalse(banco.verificar_auditoria(self.con)[0])
        self.assertFalse(banco.auditoria_resumo(self.con))

    def test_primeiro_uso_concorrente_cria_uma_chave_so(self):
        import threading
        erros = []

        def gravar():
            con = banco.abrir(self.caminho)
            try:
                for i in range(10):
                    banco.auditar(con, f"t{i}")
            except Exception as err:  # noqa: BLE001
                erros.append(err)
            finally:
                con.close()
        ts = [threading.Thread(target=gravar) for _ in range(10)]
        for t in ts:
            t.start()
        for t in ts:
            t.join()
        self.assertEqual(erros, [])
        self.assertEqual(banco.verificar_auditoria(self.con), (True, None))

    def test_auditoria_concorrente_sem_erro_e_integra(self):
        import threading
        erros = []

        def gravar():
            con = banco.abrir(self.caminho)
            try:
                for i in range(25):
                    banco.auditar(con, f"t{i}")
            except Exception as err:  # noqa: BLE001
                erros.append(err)
            finally:
                con.close()
        ts = [threading.Thread(target=gravar) for _ in range(8)]
        for t in ts:
            t.start()
        for t in ts:
            t.join()
        self.assertEqual(erros, [])
        self.assertEqual(banco.verificar_auditoria(self.con), (True, None))
        self.assertEqual(self.con.execute("SELECT COUNT(*) FROM central_auditoria").fetchone()[0], 200)

    def test_chave_fora_do_banco_com_permissao_600(self):
        banco.auditar(self.con, "x")
        chave = Path(os.environ["AMTECH_CENTRAL_SEGREDOS"]) / "central-auditoria.key"
        self.assertEqual(oct(chave.stat().st_mode & 0o777), "0o600")

    def test_aprovacao_volta_para_pendente(self):
        org = banco.org_padrao(self.con)
        a = banco.criar_aprovacao(self.con, org, "backup", [], None, "web", 30, {"campos": {}})
        banco.decidir_aprovacao(self.con, a, org, 1, True)
        banco.devolver_aprovacao(self.con, a)
        self.assertEqual(self.con.execute("SELECT estado FROM central_aprovacoes WHERE id = ?", (a,)).fetchone()[0], "pendente")

    def test_aprovacao_uso_unico_e_validade(self):
        org = banco.org_padrao(self.con)
        a = banco.criar_aprovacao(self.con, org, "backup", [], None, "web", 30)
        self.assertIsNotNone(banco.decidir_aprovacao(self.con, a, org, 1, True))
        self.assertIsNone(banco.decidir_aprovacao(self.con, a, org, 1, True))
        b = banco.criar_aprovacao(self.con, org, "backup", [], None, "web", 0)
        self.con.execute("UPDATE central_aprovacoes SET expira = '2000-01-01T00:00:00' WHERE id = ?", (b,))
        self.assertIsNone(banco.decidir_aprovacao(self.con, b, org, 1, True))
        self.assertEqual(banco.expirar_aprovacoes(self.con), 1)


class TestExecutorFilhoSilencioso(unittest.TestCase):
    def test_filho_que_escapou_nao_prende_a_receita(self):
        """Achado da revisão: um filho fora do grupo segurando a saída deixava a receita 'rodando' para sempre."""
        import executor
        with tempfile.TemporaryDirectory() as d:
            t = Path(d)
            os.environ["AMTECH_CENTRAL_SEGREDOS"] = str(t / "segredos")
            falso = t / "just-falso"
            falso.write_text("#!/bin/sh\necho comecei\nsetsid sleep 20 &\nsleep 20\n", encoding="utf-8")
            falso.chmod(0o755)
            caminho = t / "n.db"
            banco.migrar(caminho)
            ex = executor.Executor(t, caminho, comando_just=[str(falso)])
            eid = ex.iniciar("x", [], nivel="automatico", organizacao_id=1, usuario_id=None, origem="teste", timeout=1)
            for _ in range(80):
                if ex.ler(eid, 0)[1]:
                    break
                import time
                time.sleep(0.1)
            linhas, fim, codigo, _ = ex.ler(eid, 0)
            os.environ.pop("AMTECH_CENTRAL_SEGREDOS", None)
            self.assertTrue(fim, "a receita deveria terminar logo depois do tempo esgotado")
            self.assertIn("comecei", linhas)


class TestExecutorFilhoQueContinuaEscrevendo(unittest.TestCase):
    def test_receita_que_terminou_fecha_mesmo_com_filho_escrevendo(self):
        import time
        import executor
        with tempfile.TemporaryDirectory() as d:
            t = Path(d)
            os.environ["AMTECH_CENTRAL_SEGREDOS"] = str(t / "segredos")
            falso = t / "just-falso"
            falso.write_text("#!/bin/sh\necho pronto\n(setsid sh -c 'for i in 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 "
                             "21 22 23 24 25 26 27 28 29 30; do echo log; sleep 0.2; done' &)\nexit 0\n", encoding="utf-8")
            falso.chmod(0o755)
            caminho = t / "n.db"
            banco.migrar(caminho)
            ex = executor.Executor(t, caminho, comando_just=[str(falso)])
            eid = ex.iniciar("x", [], nivel="automatico", organizacao_id=1, usuario_id=None, origem="teste", timeout=60)
            for _ in range(60):
                if ex.ler(eid, 0)[1]:
                    break
                time.sleep(0.1)
            _, fim, codigo, _ = ex.ler(eid, 0)
            os.environ.pop("AMTECH_CENTRAL_SEGREDOS", None)
            self.assertTrue(fim, "a receita terminou; o filho que continua escrevendo não pode mantê-la aberta")
            self.assertEqual(codigo, 0)


class TestExecucaoMemoria(unittest.TestCase):
    def test_saida_limitada_e_leitura_continua(self):
        import executor
        x = executor.Execucao("id", "r")
        for i in range(executor.LINHAS_MAX + 10):
            x.anotar(str(i))
        self.assertEqual(len(x.linhas), executor.LINHAS_MAX)
        self.assertEqual(x.descartadas, 10)
        ex = executor.Executor(Path("."), Path("x.db"))
        ex._vivas["id"] = x
        linhas, _, _, posicao = ex.ler("id", executor.LINHAS_MAX + 5)
        self.assertEqual(linhas, [str(executor.LINHAS_MAX + 5 + i) for i in range(5)])
        self.assertEqual(posicao, executor.LINHAS_MAX + 10)
        linhas, _, _, posicao2 = ex.ler("id", 0)  # tela atrasada: recebe o que restou, sem repetir depois
        self.assertEqual(len(linhas), executor.LINHAS_MAX)
        self.assertEqual(ex.ler("id", posicao2)[0], [])


if __name__ == "__main__":
    unittest.main()
