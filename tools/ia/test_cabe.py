import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from cabe import qlora_gb, rodar  # noqa: E402


class TestCabe(unittest.TestCase):
    def test_3b_cabe_na_gpu_em_q4(self):
        self.assertEqual(rodar(3, 4096, 32, 4, None)[0]["onde"], "inteiro na GPU")

    def test_14b_q4_offload(self):
        self.assertIn("offload", rodar(14, 8192, 32, 4, None)[0]["onde"])

    def test_70b_q4_nao_cabe_em_32gb(self):
        self.assertIn("não cabe", rodar(70, 8192, 32, 4, None)[0]["onde"])

    def test_moe_ativos_melhoram_velocidade(self):
        self.assertEqual(rodar(30, 8192, 32, 4, 3)[0]["velocidade"], "usável")

    def test_qlora_8b_cabe_no_kaggle(self):
        self.assertLessEqual(qlora_gb(8), 15)


if __name__ == "__main__":
    unittest.main()
