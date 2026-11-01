import copy
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from custos import carregar, gerar, validar  # noqa: E402


class TestCustos(unittest.TestCase):
    def test_validos(self):
        d, eco = carregar()
        self.assertEqual(validar(d, eco), [])

    def test_bloco_inexistente(self):
        d, eco = carregar()
        d = copy.deepcopy(d)
        d["itens"][0]["bloco"] = "nao-existe"
        self.assertTrue(validar(d, eco))

    def test_so_uma_ia_paga_mantida(self):
        d, _ = carregar()
        pagas = [i for i in d["itens"] if i["hoje"] == "mensal" and i["decisao"] == "manter" and i["bloco"] in ("anth", "gpt", "gem", "grok", "codex", "copi")]
        self.assertEqual(len(pagas), 1)

    def test_gera(self):
        d, _ = carregar()
        self.assertIn("Modelos abertos", gerar(d))


if __name__ == "__main__":
    unittest.main()
