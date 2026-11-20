import copy
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import empresas  # noqa: E402


class TestEmpresas(unittest.TestCase):
    def setUp(self):
        self.e, self.p, self.s = empresas.carregar()

    def test_dados_reais_validos(self):
        self.assertEqual(empresas.validar(self.e, self.p, self.s), [])

    def test_toda_oferta_tem_empresa(self):
        dono = empresas.dono_das_ofertas(self.e, self.p)
        sem = [o for o, d in dono.items() if not d and next(x for x in self.p["ofertas"] if x["id"] == o)["frente"] not in self.e["fora"]]
        self.assertEqual(sem, [])

    def test_frente_sem_empresa(self):
        e = copy.deepcopy(self.e)
        e["empresas"][0]["frentes"].remove("servicos")
        self.assertTrue(any("sem empresa" in x for x in empresas.validar(e, self.p, self.s)))

    def test_software_primeiro_precisa_de_gatilho(self):
        e = copy.deepcopy(self.e)
        next(x for x in e["empresas"] if x["id"] == "logistica").pop("gatilho")
        self.assertTrue(any("gatilho" in x for x in empresas.validar(e, self.p, self.s)))

    def test_logistica_campo_maker_sao_software_primeiro(self):
        est = {x["id"]: x["estado"] for x in self.e["empresas"]}
        self.assertEqual({k for k, v in est.items() if v == "software-primeiro"}, {"logistica", "campo", "maker"})
        self.assertEqual(empresas.dono_das_ofertas(self.e, self.p)["ponto"], "campo")


if __name__ == "__main__":
    unittest.main()
