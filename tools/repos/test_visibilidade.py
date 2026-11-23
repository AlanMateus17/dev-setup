import subprocess
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import visibilidade as v  # noqa: E402


def resposta(codigo=0, saida="", erro=""):
    return subprocess.CompletedProcess(args=[], returncode=codigo, stdout=saida, stderr=erro)


class TestVisibilidade(unittest.TestCase):
    def test_desejada(self):
        self.assertEqual(v.desejada("privado"), "private")
        self.assertEqual(v.desejada("público (GitHub Pages)"), "public")
        self.assertIsNone(v.desejada(None))
        self.assertIsNone(v.desejada("—"))

    def test_alvos_ignora_planejado_e_sem_visibilidade(self):
        dados = {"repos": [{"nome": "a", "status": "ativo", "visibilidade": "privado"},
                           {"nome": "b", "status": "planejado", "visibilidade": "privado"},
                           {"nome": "Org/c", "status": "estudo", "visibilidade": "público"},
                           {"nome": "d", "status": "ativo"}]}
        self.assertEqual(v.alvos(dados), [("AlanMateus17/a", "private"), ("Org/c", "public")])

    def test_dados_reais_tem_alvos(self):
        import json
        dados = json.loads(v.DADOS.read_text(encoding="utf-8"))
        self.assertTrue(v.alvos(dados))

    def test_plano(self):
        adm = {"admin": True}
        atual = {"X/ok": {"visibility": "private", "permissions": adm},
                 "X/muda": {"visibility": "public", "permissions": adm},
                 "X/site": {"visibility": "public", "has_pages": True, "stargazers_count": 2, "permissions": adm},
                 "X/fork": {"visibility": "public", "fork": True, "permissions": adm},
                 "X/semadm": {"visibility": "public", "permissions": {"admin": False}},
                 "X/erro": {"erro": "HTTP 404"}}
        itens = {i["repo"]: i for i in v.plano([(r, "private") for r in atual], atual)}
        self.assertEqual(itens["X/ok"]["acao"], "ok")
        self.assertEqual(itens["X/muda"]["acao"], "mudar")
        self.assertEqual(len(itens["X/site"]["avisos"]), 2)
        self.assertEqual(itens["X/fork"]["acao"], "impossivel")
        self.assertEqual(itens["X/semadm"]["acao"], "impossivel")
        self.assertEqual(itens["X/erro"]["acao"], "erro")

    def test_cancelar_nao_muda_nada(self):
        chamadas = []
        itens = [{"repo": "X/a", "quer": "private", "tem": "public", "acao": "mudar", "avisos": []}]
        cod = v.aplicar(itens, rodar=lambda a: chamadas.append(a) or resposta(), ler=lambda _: "não")
        self.assertEqual(cod, 1)
        self.assertEqual(chamadas, [])

    def test_confirmar_muda_e_aviso_pede_nome(self):
        chamadas = []
        respostas = iter(["2", "errado"])  # lote confirmado; o repositório com aviso recebe nome errado
        itens = [{"repo": "X/a", "quer": "private", "tem": "public", "acao": "mudar", "avisos": []},
                 {"repo": "X/site", "quer": "private", "tem": "public", "acao": "mudar", "avisos": ["site"]}]
        v.auditar = lambda *a, **k: None
        cod = v.aplicar(itens, rodar=lambda a: chamadas.append(a) or resposta(), ler=lambda _: next(respostas))
        self.assertEqual(cod, 0)
        self.assertEqual(len(chamadas), 1)
        self.assertEqual(chamadas[0][:3], ["repo", "edit", "X/a"])
        self.assertIn("--accept-visibility-change-consequences", chamadas[0])

    def test_ler_atual_erro(self):
        atual = v.ler_atual(["X/a"], rodar=lambda a: resposta(1, erro="HTTP 404: Not Found"))
        self.assertEqual(atual["X/a"]["erro"], "HTTP 404: Not Found")


if __name__ == "__main__":
    unittest.main()
