import json
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import portas  # noqa: E402

COMPOSE = """name: teste
services:
  web:
    image: exemplo/web:1.0
    ports:
      - "127.0.0.1:3000:3000"
      - "${IP:-127.0.0.1}:9090:90"
    volumes:
      - dados:/dados
  dns:
    profiles: [rede]
    ports:
      - "53:53/tcp"
      - "53:53/udp"
volumes:
  dados:
"""


class TestPortas(unittest.TestCase):
    def ler(self, texto: str) -> list[dict]:
        with tempfile.TemporaryDirectory() as d:
            raiz = Path(d)
            c = raiz / "infra" / "teste" / "compose.yaml"
            c.parent.mkdir(parents=True)
            c.write_text(texto, encoding="utf-8")
            antigo = portas.RAIZ
            portas.RAIZ = raiz
            try:
                return portas.ler_todos(raiz)
            finally:
                portas.RAIZ = antigo

    def test_le_portas_ip_variavel_protocolo_e_perfil(self):
        p = self.ler(COMPOSE)
        self.assertEqual([(e["servico"], e["porta"], e["protocolo"]) for e in p],
                         [("web", 3000, "tcp"), ("web", 9090, "tcp"), ("dns", 53, "tcp"), ("dns", 53, "udp")])
        self.assertEqual(p[2]["perfil"], "rede")
        self.assertEqual(p[1]["interna"], 90)
        self.assertNotIn("dados", [e["servico"] for e in p])

    def test_tcp_e_udp_na_mesma_porta_nao_conflitam(self):
        self.assertEqual(portas.repetidas(self.ler(COMPOSE)), [])

    def test_porta_repetida_e_reservada_falham(self):
        servicos = [{"id": "a", "porta": 3000, "protocolo": "tcp"}, {"id": "b", "porta": 3000, "protocolo": "tcp"}]
        self.assertEqual(len(portas.repetidas(servicos)), 1)
        dados = {"servicos": [], "reservadas": [{"id": "central", "porta": 3000}]}
        compose = self.ler(COMPOSE)
        dados["servicos"] = portas.gerar(dados, compose)["servicos"]
        self.assertTrue(any("repetida" in e for e in portas.conferir(dados, compose)))

    def test_divergencia_com_o_compose_falha(self):
        compose = self.ler(COMPOSE)
        self.assertTrue(portas.conferir({"servicos": [], "reservadas": []}, compose))

    def test_repositorio_sem_porta_repetida_e_portas_json_em_dia(self):
        dados = json.loads(portas.DADOS.read_text(encoding="utf-8"))
        self.assertEqual(portas.conferir(dados, portas.ler_todos()), [])


if __name__ == "__main__":
    unittest.main()
