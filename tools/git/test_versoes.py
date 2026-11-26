import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import versoes as vs  # noqa: E402


class TestVersoes(unittest.TestCase):
    ESTADO = "- 2026-11-25: v2.56.1: perfil trabalho\n- 2026-11-25: v2.57.0: análise de lacunas\n"

    def test_cabecalho_quebrado_e_achado(self):
        # O caso do #44: a linha do cabeçalho perdeu o "## [2.57.0]"
        changelog = "## [2.58.0] - 2026-11-26\n\n - 2026-11-25\n\n## [2.56.1] - 2026-11-25\n"
        self.assertEqual(vs.faltando(self.ESTADO, changelog), ["2.57.0"])

    def test_cabecalho_sem_data_ou_com_formato_errado(self):
        self.assertEqual(vs.faltando("v1.2.3", "## [1.2.3]\n"), ["1.2.3"])
        self.assertEqual(vs.faltando("v1.2.3", "## 1.2.3 - 2026-01-01\n"), ["1.2.3"])
        self.assertEqual(vs.faltando("v1.2.3", "## [1.2.3] - 2026-01-01\n"), [])

    def test_ordem_por_numero(self):
        self.assertEqual(vs.faltando("v2.10.0 v2.9.0", ""), ["2.9.0", "2.10.0"])

    def test_o_repositorio_bate(self):
        raiz = Path(__file__).resolve().parents[2]
        falta = vs.faltando((raiz / "ESTADO.md").read_text(encoding="utf-8"), (raiz / "CHANGELOG.md").read_text(encoding="utf-8"))
        self.assertEqual(falta, [])


if __name__ == "__main__":
    unittest.main()
