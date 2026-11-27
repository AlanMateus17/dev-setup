import os
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import senhas as s  # noqa: E402


class TestInventario(unittest.TestCase):
    def test_palavra_chave(self):
        self.assertEqual(s.palavra_chave("GitHub"), "github")
        self.assertEqual(s.palavra_chave("Domínio (Registro.br)"), "registro.br")
        self.assertEqual(s.palavra_chave("Google Search Console"), "google")
        self.assertEqual(s.palavra_chave("Mercado Pago", {"Mercado Pago": "mercadopago"}), "mercadopago")
        self.assertEqual(s.palavra_chave("Agenda online"), "")

    def test_grupo_por_palavra_inteira(self):
        self.assertEqual(s.grupo_web("GitHub", None), "06 Código e nuvem")
        self.assertNotEqual(s.grupo_web("Pinterest Ads", "04 Grupo AMtech Digital"), "01 Bancos e dinheiro")
        self.assertEqual(s.grupo_web("Coisa nova", "09 Estudo"), "09 Estudo")

    def test_inventario_real(self):
        itens = s.inventario()
        nomes = {i["nome"] for i in itens}
        self.assertIn("GitHub", nomes)
        self.assertTrue(any(i.get("entrada") == "20 Setup técnico/soberania/FIREFLY_DB_SENHA" for i in itens))
        self.assertFalse(any(i["nome"] == "Já conectados" for i in itens))
        chaves = [i["chave"] for i in itens if i["tipo"] == "conta" and i["chave"]]
        self.assertEqual(len(chaves), len(set(chaves)), "conta repetida no inventário")

    def test_env_externa_x_gerar(self):
        por_var = {i["var"]: i["tipo"] for i in s.ler_env_examples()}
        self.assertEqual(por_var["ANTHROPIC_API_KEY"], "externa")
        self.assertEqual(por_var["GRAFANA_DB_SENHA"], "gerar")
        self.assertNotIn("RESTIC_PASSWORD_FILE", por_var)

    def test_doc_sem_senha_e_atualizado(self):
        self.assertEqual(s.cmd_lista(check=True), 0)

    def test_no_cofre(self):
        todas = ["06 Código e nuvem/github.com", "20 Setup técnico/ia/LITELLM_MASTER_KEY"]
        self.assertEqual(s.no_cofre({"tipo": "conta", "chave": "github"}, todas), "06 Código e nuvem/github.com")
        self.assertIsNone(s.no_cofre({"tipo": "conta", "chave": ""}, todas))
        self.assertIsNone(s.no_cofre({"tipo": "gerar", "chave": "x", "entrada": "20 Setup técnico/ia/OUTRA"}, todas))

    def test_escolher(self):
        self.assertEqual(s.escolher(["a/github.com", "b/gitlab.com"], "github"), "a/github.com")
        self.assertIsNone(s.escolher(["a/github.com"], "nada"))
        self.assertEqual(s.escolher(["a/x", "b/x"], "x", ler=lambda _: "2"), "b/x")
        self.assertIsNone(s.escolher(["a/x", "b/x"], "x", ler=lambda _: ""))


@unittest.skipUnless(shutil.which("keepassxc-cli") and os.environ.get("AMTECH_TESTE_COFRE") == "1",
                     "teste lento com o keepassxc-cli real: rode com AMTECH_TESTE_COFRE=1")
class TestCofreDeVerdade(unittest.TestCase):
    """Cofre de teste descartável: confere ls, criar com confirmação e leitura, com o keepassxc-cli real.

    Fica fora do `just check`: cada chamada abre o cofre e paga a derivação da chave. No notebook do Alan
    isso levou 49 min e estourou o check. Rode à mão: AMTECH_TESTE_COFRE=1 python3 -m unittest discover -s tools/senhas -v"""

    def setUp(self):
        self.dir = tempfile.mkdtemp()
        self.cofre = os.path.join(self.dir, "t.kdbx")
        subprocess.run(["keepassxc-cli", "db-create", "-q", "-p", "-t", "100", self.cofre], input="m\nm\n", text=True, capture_output=True, check=True)
        os.environ["COFRE"] = self.cofre
        s.mestre = lambda *a, **k: "m"

    def tearDown(self):
        shutil.rmtree(self.dir)
        os.environ.pop("COFRE", None)

    def test_criar_pede_confirmacao_e_grava(self):
        self.assertEqual(s.cmd_criar(ler=lambda _: "não"), 1)
        self.assertEqual(s.entradas(s.cli(), "m"), [])
        self.assertEqual(s.cmd_criar(ler=lambda _: str(sum(i["tipo"] == "gerar" for i in s.inventario() if i.get("entrada")))), 0)
        todas = s.entradas(s.cli(), "m")
        self.assertIn("20 Setup técnico/soberania/FIREFLY_DB_SENHA", todas)
        r = s.kp._cli(s.cli(), ["show", "-q", "-s", "-a", "Password", self.cofre, "20 Setup técnico/soberania/FIREFLY_DB_SENHA"], "m\n", utf8=True)
        self.assertEqual(len(r.stdout.strip()), 32)


if __name__ == "__main__":
    unittest.main()
