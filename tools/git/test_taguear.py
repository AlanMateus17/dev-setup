import unittest
import taguear

CHANGELOG = """# Changelog

## [2.8.0] - 2026-11-02
### Adicionado
- c

## [2.7.1] - 2026-11-02
### Alterado
- b

## [1.24.0] - 2026-10-01
### Adicionado
- a
"""


class TesteTaguear(unittest.TestCase):
    def test_versoes_da_mais_antiga_para_a_mais_nova(self):
        self.assertEqual(taguear.versoes(CHANGELOG), ["1.24.0", "2.7.1", "2.8.0"])

    def test_pega_todas_as_versoes_do_changelog_real(self):
        from pathlib import Path
        real = (Path(taguear.__file__).resolve().parents[2] / "CHANGELOG.md").read_text(encoding="utf-8")
        vs = taguear.versoes(real)
        self.assertIn("2.8.0", vs)
        self.assertGreater(len(vs), 10)  # histórico longo

    def test_planejar_pula_as_ja_tagueadas(self):
        # sem acesso a git aqui: passo commit_da_versao por um substituto
        orig = taguear.commit_da_versao
        taguear.commit_da_versao = lambda v: "abc123"
        try:
            plano = taguear.planejar(CHANGELOG, {"v2.8.0"})
            versoes = [v for v, _ in plano]
        finally:
            taguear.commit_da_versao = orig
        self.assertEqual(versoes, ["1.24.0", "2.7.1"])  # 2.8.0 já existe, fica de fora


if __name__ == "__main__":
    unittest.main()
