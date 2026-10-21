import copy
import unittest

from gerar import carregar, gerar_md, validar


class TestImplantacao(unittest.TestCase):
    def setUp(self):
        self.d = carregar()

    def test_dados_reais_validos(self):
        self.assertEqual(validar(self.d), [])

    def test_detecta_id_repetido(self):
        d = copy.deepcopy(self.d)
        d["fases"][1]["passos"].append(copy.deepcopy(d["fases"][0]["passos"][0]))
        self.assertTrue(any("repetido" in e for e in validar(d)))

    def test_detecta_script_inexistente(self):
        d = copy.deepcopy(self.d)
        d["fases"][0]["passos"][0]["comando"] = "bash scripts/wsl/nao-existe.sh"
        self.assertTrue(any("não existe" in e for e in validar(d)))

    def test_todo_passo_aparece_no_roteiro_com_criterio(self):
        md = gerar_md(self.d)
        for f in self.d["fases"]:
            for p in f["passos"]:
                self.assertIn(p["titulo"], md)
                self.assertIn(p["pronto"], md)


if __name__ == "__main__":
    unittest.main()
