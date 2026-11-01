import copy
import unittest
from pathlib import Path

import investimentos as inv

M = Path(inv.__file__).parent / "modelos"


class TesteInvestimentos(unittest.TestCase):
    def setUp(self):
        self.d = inv.carregar()

    def test_dados_validos(self):
        self.assertEqual(inv.validar(self.d), [])

    def test_alocacao_soma_100(self):
        d = copy.deepcopy(self.d)
        d["alocacao_acoes_padrao"]["graham"] = 99
        self.assertTrue(inv.validar(d))

    def test_bazin_e_graham(self):
        l = {"dividendo_medio": "1,6", "lpa": "2.5", "vpa": "15"}
        self.assertEqual(inv.teto_bazin(l, 6), 26.67)
        self.assertEqual(inv.valor_graham(l), 29.05)
        self.assertIsNone(inv.valor_graham({"lpa": "-1", "vpa": "10"}))

    def test_avaliar_exemplo(self):
        r = {x["ticker"]: x for x in inv.avaliar(inv.ler_csv(M / "indicadores.example.csv"), self.d)}
        self.assertEqual(r["EXEM3"]["bazin"], "passa")
        self.assertEqual(r["TEST4"]["buffett"], "não")
        self.assertEqual(r["FICT3"]["graham"], "sem dado")
        self.assertEqual(r["FICT3"]["formula_magica"], "fora")  # bancos ficam fora
        self.assertEqual(r["EXEM3"]["formula_magica"], "1º")

    def test_portao_fechado(self):
        cfg = inv.carregar_config(M / "investimentos.example.toml")
        avisos, div = inv.aporte(inv.ler_csv(M / "carteira.example.csv"), 800, cfg, self.d)
        self.assertEqual(div, {})
        self.assertIn("Portão fechado", avisos[0])

    def test_aporte_vai_para_o_mais_abaixo(self):
        cfg = inv.carregar_config(M / "investimentos.example.toml")
        cfg["portao"] = {"cartao_zerado": True, "reserva_completa": True}
        avisos, div = inv.aporte(inv.ler_csv(M / "carteira.example.csv"), 800, cfg, self.d)
        self.assertAlmostEqual(sum(div.values()), 800, delta=0.05)
        self.assertNotIn("barsi_bazin", div)  # já está acima do alvo
        self.assertTrue(any("mínimo" in a for a in avisos))

    def test_comparar(self):
        o = inv.comparar(inv.ler_csv(M / "carteiras.example.csv"))
        self.assertTrue(o[0].startswith("barsi_bazin: +12.0%"))
        self.assertIn("+4.0 p.p.", o[0])

    def test_docs(self):
        t = inv.gerar(self.d)
        self.assertIn("Não é recomendação", t)
        self.assertIn("Fórmula Mágica", t)


if __name__ == "__main__":
    unittest.main()
