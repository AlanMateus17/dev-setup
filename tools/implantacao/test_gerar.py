import copy
import unittest

from gerar import carregar, carregar_eco, cobertura, gerar_html, gerar_md, validar


class TestImplantacao(unittest.TestCase):
    def setUp(self):
        self.d = carregar()
        self.eco = carregar_eco()

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

    def test_todo_bloco_do_setup_tem_lugar(self):
        c = cobertura(self.d, self.eco)
        self.assertEqual([b["id"] for b in c["faltando"]], [])
        soma = len(c["nos_passos"]) + len(c["construir"]) + len(c["nao_instala"]) + len(c["depois"])
        self.assertEqual(soma, len(self.eco["blocos"]))

    def test_detecta_bloco_fora_do_roteiro(self):
        d = copy.deepcopy(self.d)
        for f in d["fases"]:
            for p in f["passos"]:
                p["blocos"] = [b for b in p["blocos"] if b != "kee"]
        self.assertTrue(any("kee" in e and "fora do roteiro" in e for e in validar(d, self.eco)))

    def test_detecta_bloco_novo_no_setup(self):
        eco = copy.deepcopy(self.eco)
        eco["blocos"].append({"id": "novo", "camada": "win", "rotulo": "Programa novo", "tipo": "local",
                              "conta": False, "futuro": False, "descricao": "x"})
        self.assertTrue(any("novo" in e for e in validar(self.d, eco)))

    def test_detecta_bloco_inexistente_e_duplicado(self):
        d = copy.deepcopy(self.d)
        d["fases"][0]["passos"][0]["blocos"].append("naoexiste")
        d["cobertura"]["construir"]["kee"] = "x"
        erros = validar(d, self.eco)
        self.assertTrue(any("naoexiste" in e for e in erros))
        self.assertTrue(any("kee" in e and "também" in e for e in erros))

    def test_precisa_invalido_e_resumo_de_hoje(self):
        d = copy.deepcopy(self.d)
        d["fases"][0]["passos"][0]["precisa"] = ["sorte"]
        self.assertTrue(any("precisa inválido" in e for e in validar(d, self.eco)))
        self.assertIn("Dá para fazer hoje", gerar_md(self.d, self.eco))

    def test_roteiro_e_pagina_mostram_cobertura(self):
        md, html = gerar_md(self.d, self.eco), gerar_html(self.d, self.eco)
        self.assertIn("## Cobertura do setup", md)
        self.assertIn("Implanta: KeePassXC", md)
        self.assertIn('"implanta"', html)
        self.assertNotIn("__DATA__", html)


if __name__ == "__main__":
    unittest.main()
