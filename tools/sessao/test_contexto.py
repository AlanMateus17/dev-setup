import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from contexto import pacote_passo, pacote_resumo  # noqa: E402


class TestContexto(unittest.TestCase):
    def test_passo_curto_e_com_regras(self):
        t = pacote_passo("fa-plano")
        self.assertIn("Pronto quando", t)
        self.assertIn("Dados de alunos", t)
        self.assertLess(len(t) // 4, 1500)  # cabe em poucos milhares de tokens

    def test_resumo(self):
        self.assertIn("fases", pacote_resumo())

    def test_passo_inexistente(self):
        with self.assertRaises(SystemExit):
            pacote_passo("nao-existe")


if __name__ == "__main__":
    unittest.main()
