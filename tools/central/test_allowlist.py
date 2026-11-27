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

    def test_aprovar_so_numero(self):
        self.assertEqual(montar(self.d, "aprovar", {"n": "41"}), (["41"], "pede-ok"))
        with self.assertRaises(ErroAllowlist):
            montar(self.d, "aprovar", {"n": "41; rm"})


class TestBanco(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.caminho = Path(self.tmp.name) / "nucleo.db"
        banco.migrar(self.caminho)
        self.con = banco.abrir(self.caminho)

    def tearDown(self):
        self.con.close()
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

    def test_aprovacao_uso_unico_e_validade(self):
        org = banco.org_padrao(self.con)
        a = banco.criar_aprovacao(self.con, org, "backup", [], None, "web", 30)
        self.assertIsNotNone(banco.decidir_aprovacao(self.con, a, org, 1, True))
        self.assertIsNone(banco.decidir_aprovacao(self.con, a, org, 1, True))
        b = banco.criar_aprovacao(self.con, org, "backup", [], None, "web", 0)
        self.con.execute("UPDATE central_aprovacoes SET expira = '2000-01-01T00:00:00' WHERE id = ?", (b,))
        self.assertIsNone(banco.decidir_aprovacao(self.con, b, org, 1, True))
        self.assertEqual(banco.expirar_aprovacoes(self.con), 1)


if __name__ == "__main__":
    unittest.main()
