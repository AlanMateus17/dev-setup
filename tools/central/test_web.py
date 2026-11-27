"""Testes de ponta a ponta da Central, com um 'just' falso. Precisam de fastapi e httpx; sem eles, são pulados.
No CI: pip install -r tools/central/requirements.txt httpx."""
import re
import sys
import tempfile
import time
import unittest
from pathlib import Path

AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI))

try:
    from fastapi.testclient import TestClient
    TEM_WEB = True
except ImportError:  # pragma: no cover
    TEM_WEB = False

import banco  # noqa: E402

SENHA = "senha-de-teste-123"


@unittest.skipUnless(TEM_WEB, "fastapi/httpx não instalados (pip install -r tools/central/requirements.txt httpx)")
class TestCentral(unittest.TestCase):
    def setUp(self):
        from executor import Executor
        from web import criar_app
        self.tmp = tempfile.TemporaryDirectory()
        t = Path(self.tmp.name)
        self.registro = t / "chamadas.txt"
        falso = t / "just-falso"
        falso.write_text(f'#!/bin/sh\nprintf "%s\\n" "$@" >> "{self.registro}"\necho "linha 1"\necho "linha 2"\n',
                         encoding="utf-8")
        falso.chmod(0o755)
        self.caminho = t / "nucleo.db"
        banco.migrar(self.caminho)
        con = banco.abrir(self.caminho)
        banco.salvar_usuario(con, "alan", SENHA)
        banco.salvar_usuario(con, "visita", SENHA, "leitor")
        con.close()
        raiz = AQUI.parents[1]
        self.ex = Executor(raiz, self.caminho, comando_just=[str(falso)])
        self.c = TestClient(criar_app(raiz, self.caminho, executor=self.ex), base_url="http://127.0.0.1:8700")

    def tearDown(self):
        self.tmp.cleanup()

    def entrar(self, usuario="alan", senha=SENHA):
        pre = re.search(r'name="pre" value="([^"]+)"', self.c.get("/login").text).group(1)
        r = self.c.post("/login", data={"usuario": usuario, "senha": senha, "pre": pre}, follow_redirects=False)
        if r.status_code == 303:
            self.csrf = re.search(r'name="csrf" value="([^"]+)"', self.c.get("/").text).group(1)
        return r

    def esperar(self, receita, n=1):
        for _ in range(50):
            if self.ex.em_andamento() == 0 and self.registro.exists():
                return
            time.sleep(0.05)

    def test_sem_login_nao_entra(self):
        for url in ("/", "/comandos", "/aprovar", "/auditoria"):
            self.assertEqual(self.c.get(url, follow_redirects=False).status_code, 303, url)
        self.assertEqual(self.c.get("/api/status").status_code, 401)

    def test_host_e_origem(self):
        self.assertEqual(self.c.get("/login", headers={"host": "evil.com"}).status_code, 400)
        self.entrar()
        r = self.c.post("/rodar", data={"csrf": self.csrf, "receita": "agora"}, headers={"origin": "http://evil.com"})
        self.assertEqual(r.status_code, 403)

    def test_login_errado(self):
        self.assertEqual(self.entrar(senha="errada-errada").status_code, 401)

    def test_csrf_obrigatorio(self):
        self.entrar()
        r = self.c.post("/rodar", data={"csrf": "x", "receita": "agora"}, follow_redirects=False)
        self.assertEqual(r.status_code, 403)
        self.assertFalse(self.registro.exists())

    def test_rodar_automatico_sem_shell(self):
        self.entrar()
        r = self.c.post("/rodar", data={"csrf": self.csrf, "receita": "buscar", "a_texto": 'deploy "$(id)"'},
                        follow_redirects=False)
        self.assertEqual(r.status_code, 303)
        self.esperar("buscar")
        chamadas = self.registro.read_text(encoding="utf-8").splitlines()
        self.assertEqual(chamadas[-2:], ["buscar", 'deploy "$(id)"'])
        eid = r.headers["location"].rsplit("/", 1)[1]
        with self.c.stream("GET", f"/execucao/{eid}/eventos") as s:
            texto = "".join(s.iter_text())
        self.assertIn("linha 2", texto)
        self.assertIn("event: fim", texto)

    def test_pede_ok_so_roda_depois_de_aprovar(self):
        self.entrar()
        self.c.post("/rodar", data={"csrf": self.csrf, "receita": "backup"})
        time.sleep(0.2)
        self.assertFalse(self.registro.exists(), "backup rodou sem aprovação")
        aid = re.search(r'action="/aprovar/([0-9a-f]+)"', self.c.get("/aprovar").text).group(1)
        r = self.c.post(f"/aprovar/{aid}", data={"csrf": self.csrf, "acao": "aprovar"}, follow_redirects=False)
        self.assertEqual(r.status_code, 303)
        self.esperar("backup")
        self.assertIn("backup", self.registro.read_text(encoding="utf-8"))
        r = self.c.post(f"/aprovar/{aid}", data={"csrf": self.csrf, "acao": "aprovar"})
        self.assertEqual(r.status_code, 409, "aprovação reaproveitada")

    def test_merge_exige_confirmacao(self):
        self.entrar()
        self.c.post("/rodar", data={"csrf": self.csrf, "receita": "aprovar", "a_n": "41"})
        aid = re.search(r'action="/aprovar/([0-9a-f]+)"', self.c.get("/aprovar").text).group(1)
        r = self.c.post(f"/aprovar/{aid}", data={"csrf": self.csrf, "acao": "aprovar", "confirmacao": "42"})
        self.assertEqual(r.status_code, 400)
        self.assertFalse(self.registro.exists())

    def test_leitor_nao_aprova_nem_pede(self):
        self.entrar("visita")
        r = self.c.post("/rodar", data={"csrf": self.csrf, "receita": "backup"})
        self.assertEqual(r.status_code, 403)

    def test_recusa_injecao_e_proibidas(self):
        self.entrar()
        for dados in ({"receita": "colher", "a_etapa": '0.1"; touch /tmp/x; "'}, {"receita": "senha"},
                      {"receita": "medir", "a_comando": "id"}, {"receita": "ligar", "opcao": "--qualquer"}):
            r = self.c.post("/rodar", data={"csrf": self.csrf, **dados})
            self.assertEqual(r.status_code, 400, dados)
        self.assertFalse(self.registro.exists())

    def test_proibidas_nao_aparecem(self):
        self.entrar()
        tela = self.c.get("/comandos").text
        for nome in ("senhas-rodar", "cofre-abrir", "medir", "central-usuario"):
            self.assertNotIn(f"<strong>{nome}</strong>", tela)

    def test_cabecalhos_de_seguranca(self):
        r = self.c.get("/login")
        self.assertIn("script-src 'self'", r.headers["content-security-policy"])
        self.assertEqual(r.headers["x-frame-options"], "DENY")
        self.entrar()
        cookie = [h for h in self.c.cookies.jar if h.name == "central_sessao"][0]
        self.assertTrue(cookie.has_nonstandard_attr("HttpOnly"))

    def test_auditoria_integra_depois_do_uso(self):
        self.entrar()
        self.c.post("/rodar", data={"csrf": self.csrf, "receita": "agora"})
        self.esperar("agora")
        self.assertIn("Corrente íntegra", self.c.get("/auditoria").text)


if __name__ == "__main__":
    unittest.main()
