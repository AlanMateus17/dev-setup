"""Fontes de estudo: porta de entrada, citação literal e a barreira que mantém as fontes fora do repositório."""
import json
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

sys.path.insert(0, str(Path(__file__).parent))
import fontes  # noqa: E402


class TestFontes(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.env = mock.patch.dict(os.environ, {"AMTECH_ESTUDO": self.tmp.name})
        self.env.start()

    def tearDown(self):
        self.env.stop()
        self.tmp.cleanup()

    def test_citar_aceita_so_trecho_literal(self):
        arq = Path(self.tmp.name) / "fonte.md"
        arq.write_text("# Cap. 2\nO complemento de dois representa\nnúmeros negativos usando o bit mais\n"
                       "significativo.\n", encoding="utf-8")
        r = fontes.citar(arq, "representa números negativos usando o bit")
        self.assertEqual(r["linha"], 2, "quebra de linha e espaço não importam")
        self.assertIsNone(fontes.citar(arq, "representa números positivos"), "uma palavra trocada é recusada")
        self.assertIsNone(fontes.citar(arq, ""))

    def test_citar_transcricao_devolve_o_minuto(self):
        arq = Path(self.tmp.name) / "aula.md"
        arq.write_text(fontes.srt_para_md("1\n00:00:01,000 --> 00:00:03,000\nbom dia\n\n2\n00:14:32,500 --> 00:14:35,000\n"
                                          "a implicação só é falsa quando\n"), encoding="utf-8")
        self.assertEqual(fontes.citar(arq, "só é falsa quando")["t"], "14:32")

    def test_entrada_guarda_registra_e_nao_duplica(self):
        p = fontes.pastas()
        p["entrada"].mkdir(parents=True)
        (p["entrada"] / "Notas da Aula 1.md").write_text("conteúdo", encoding="utf-8")
        (p["entrada"] / "copia.md").write_text("conteúdo", encoding="utf-8")
        (p["entrada"] / "planilha.xlsx").write_bytes(b"x")
        feitos = fontes.processar_entrada("faculdade-uso-pessoal")
        self.assertEqual(len(feitos), 1, "o mesmo conteúdo com outro nome não entra duas vezes")
        reg = feitos[0]
        self.assertEqual((reg["tipo"], reg["conversao"], reg["licenca"]), ("texto", "copiado", "faculdade-uso-pessoal"))
        self.assertTrue(reg["id"].startswith("notas-da-aula-1-"))
        self.assertTrue((p["corpus"] / f"{reg['id']}.md").exists())
        self.assertTrue(Path(reg["original"]).exists())
        self.assertEqual(len(fontes.manifesto()), 1)
        self.assertTrue((p["entrada"] / "planilha.xlsx").exists(), "tipo desconhecido fica onde está")

    def test_pdf_sem_ferramenta_fica_pendente(self):
        p = fontes.pastas()
        p["entrada"].mkdir(parents=True)
        (p["entrada"] / "livro.pdf").write_bytes(b"%PDF-1.4 teste")
        with mock.patch.object(fontes, "tem", return_value=False):
            reg = fontes.processar_entrada()[0]
        self.assertEqual((reg["conversao"], reg["sanitizado"]), ("pendente", False))
        self.assertTrue(Path(reg["original"]).exists(), "nada se perde: o original fica guardado")

    def test_barreira_do_repositorio(self):
        repo = Path(self.tmp.name) / "repo"
        repo.mkdir()
        subprocess.run(["git", "init", "-q", str(repo)], check=True)
        for f in ("docs/gerado.pdf", "tools/x.py", "corpus/livro.md", "notas/livro.epub", "anexo.pdf"):
            (repo / f).parent.mkdir(parents=True, exist_ok=True)
            (repo / f).write_text("x")
        subprocess.run(["git", "-C", str(repo), "add", "."], check=True)
        erros = fontes.conferir_repo(repo)
        self.assertEqual(sorted(e.split(":")[0] for e in erros), ["anexo.pdf", "corpus/livro.md", "notas/livro.epub"])
        self.assertEqual(fontes.conferir_repo(), [], "o dev-setup em si está limpo")

    def test_catalogo_coerente_com_o_mapa(self):
        docs = fontes.catalogo()
        ids = [d["id"] for d in docs]
        self.assertEqual(len(ids), len(set(ids)))
        retrato = json.loads((fontes.RAIZ / "data" / "professor" / "mapa-assuntos.json").read_text(encoding="utf-8"))
        for d in docs:
            self.assertTrue(d["repo"].startswith("https://github.com/"), d["id"])
            self.assertTrue(d["ref"] and d["caminhos"] and d["licenca"], d["id"])
            for a in d["assuntos"]:
                self.assertIn(a, retrato["assuntos"], f"{d['id']}: assunto {a} não existe no mapa")


if __name__ == "__main__":
    unittest.main()
