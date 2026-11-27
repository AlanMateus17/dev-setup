import json
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import allowlist  # noqa: E402
import prompt  # noqa: E402

SEM_IA = lambda: False  # noqa: E731
COM_IA = lambda: True  # noqa: E731


def ia(passos, resposta="ok"):
    return lambda _msgs: json.dumps({"passos": passos, "resposta": resposta})


class TestRegra(unittest.TestCase):
    def setUp(self):
        self.d = allowlist.carregar()

    def plano(self, texto, **kw):
        return prompt.planejar(self.d, texto, ia_no_ar=kw.pop("ia_no_ar", SEM_IA), **kw)

    def test_perguntas_comuns_por_regra_sem_tokens(self):
        casos = {
            "Como está o backup?": ["validar"],
            "o que estudo hoje?": ["professor hoje"],
            "o que faço agora?": ["agora"],
            "o que está ligado?": ["ligado"],
            "progresso da empresa software": ["progresso software"],
            "busque no núcleo deploy arm": ["buscar deploy arm"],
        }
        for texto, esperado in casos.items():
            with self.subTest(texto=texto):
                p = self.plano(texto)
                self.assertEqual(p.origem, "regra")
                self.assertEqual(p.tokens, 0)
                self.assertEqual([x.rotulo() for x in p.passos], esperado)
                self.assertTrue(p.roda_sozinho)

    def test_site_pelo_prompt_so_confere(self):
        """Achado da revisão: 'pendências do site' rodava 'just site amtech', que sobrescreve o site."""
        for texto in ("quais as pendencias do site da amtech?", "Gerar o site da Editora AMS Silva"):
            with self.subTest(texto=texto):
                p = self.plano(texto)
                self.assertIn("--checar", p.passos[0].args)
                self.assertEqual(p.passos[0].nivel, "automatico")

    def test_acao_por_regra_nao_roda_sozinha(self):
        for texto in ("aprove o PR 41", "colher a etapa 0.2", "ligar o perfil trabalho", "lembre que o HD está na gaveta"):
            with self.subTest(texto=texto):
                p = self.plano(texto)
                self.assertEqual(p.origem, "regra")
                self.assertFalse(p.roda_sozinho)

    def test_pedir_recebe_o_pedido_inteiro(self):
        p = self.plano("crie uma página de vendas para o curso de lógica")
        self.assertEqual(p.passos[0].args, ["crie uma página de vendas para o curso de lógica"])

    def test_decisao_humana_nao_vira_receita(self):
        p = self.plano("quero comprar uma GPU nova")
        self.assertEqual((p.origem, p.passos), ("voce", []))

    def test_sem_ia_pergunta_geral_nao_vai_para_a_fila(self):
        self.assertEqual(self.plano("qual a capital da França").origem, "nada")

    def test_sem_ia_trabalho_de_codigo_vai_para_a_fila(self):
        p = self.plano("calcular o rateio da conta de luz")
        self.assertEqual((p.origem, p.passos[0].receita), ("fila", "pedir"))

    def test_injecao_pelo_texto_nao_escapa(self):
        p = self.plano('colher a etapa 0.2"; rm -rf ~; "')
        self.assertTrue(all(";" not in a for x in p.passos for a in x.args))


class TestIALocal(unittest.TestCase):
    def setUp(self):
        self.d = allowlist.carregar()

    def test_plano_da_ia_passa_pela_allowlist(self):
        falsa = ia([{"receita": "rm-rf", "campos": {}},
                    {"receita": "professor", "subcomando": "aula", "campos": {"sub_1": "b-aprender"}},
                    {"receita": "colher", "campos": {"etapa": "0.1; reboot"}},
                    {"receita": "senha", "campos": {}}])
        p = prompt.planejar(self.d, "me mostra a aula de aprender a aprender", ia=falsa, ia_no_ar=COM_IA)
        self.assertEqual(p.origem, "ia-local")
        self.assertGreater(p.tokens, 0)
        validos = [x.rotulo() for x in p.validos]
        self.assertEqual(validos, ["professor aula b-aprender"])
        self.assertFalse(p.roda_sozinho, "plano de IA sempre pede um clique")

    def test_ia_fora_do_formato(self):
        p = prompt.planejar(self.d, "faça qualquer coisa estranha", ia=lambda _m: "não sei", ia_no_ar=COM_IA)
        self.assertEqual(p.passos, [])
        self.assertIn("fora do formato", p.resposta)

    def test_ia_recebe_poucas_receitas(self):
        recebido = {}

        def espia(msgs):
            recebido["texto"] = msgs[1]["content"]
            return json.dumps({"passos": [], "resposta": "pergunta geral"})
        prompt.planejar(self.d, "explique o que é idempotência", ia=espia, ia_no_ar=COM_IA)
        linhas = recebido["texto"].split("Pedido:")[0].strip().splitlines()[1:]
        self.assertLessEqual(len(linhas), prompt.CANDIDATOS_IA + 1)
        self.assertNotIn("senhas-rodar", recebido["texto"])
        self.assertNotIn("medir", recebido["texto"].split())


if __name__ == "__main__":
    unittest.main()
