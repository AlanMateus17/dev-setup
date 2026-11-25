import copy
import shutil
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import ferramentas  # noqa: E402

RAIZ = ferramentas.RAIZ
FONTES = ["scripts/windows/pacotes.json", "scripts/windows/vscode-extensoes.txt", "scripts/wsl/bootstrap.sh",
          "scripts/wsl/extras.sh", "scripts/wsl/ferramentas-re.sh", "scripts/wsl/nuvem.sh", "scripts/wsl/ligar-tudo.sh",
          "scripts/wsl/segredos.sh", "scripts/wsl/lab-ia.sh", "scripts/wsl/ativar-pipeline.sh",
          "infra/dotfiles/dot_config/mise/config.toml", "infra/ai-memory-hooks/README.md"]


class CopiaDoRepositorio:
    """Cópia só das fontes que o --check lê, para estragar uma de cada vez sem tocar no repositório."""

    def __enter__(self) -> Path:
        self.dir = tempfile.TemporaryDirectory()
        raiz = Path(self.dir.name)
        for f in FONTES + [str(p.relative_to(RAIZ)) for p in RAIZ.glob("infra/*/compose.yaml")]:
            (raiz / f).parent.mkdir(parents=True, exist_ok=True)
            shutil.copy(RAIZ / f, raiz / f)
        return raiz

    def __exit__(self, *_):
        self.dir.cleanup()


class TestRegistro(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.dados = ferramentas.carregar()

    def test_registro_valido(self):
        self.assertEqual(ferramentas.validar(self.dados), [])

    def test_fontes_batem(self):
        self.assertEqual(ferramentas.conferir_fontes(self.dados), [])

    def test_doc_gerada_em_dia(self):
        self.assertEqual(ferramentas.MD.read_text(encoding="utf-8"), ferramentas.gerar_md(self.dados))

    def test_decisoes_de_25_11(self):
        por_id = {f["id"]: f for f in self.dados["ferramentas"]}
        self.assertEqual(por_id["cli-keepassxc-cli"]["decisao"], "adiada")
        self.assertEqual(por_id["win-keepassxcteam-keepassxc"]["decisao"], "adiada")
        self.assertEqual(por_id["cli-mise-sops"]["decisao"], "parada")
        self.assertEqual(por_id["docker-ia-litellm"]["decisao"], "parada")
        self.assertEqual(por_id["svc-pipeline"]["decisao"], "parada")

    def test_acesso_de_fora_marcado(self):
        com = {f["id"] for f in self.dados["ferramentas"] if f.get("acesso_externo")}
        for fid in ("svc-remoto", "svc-bot", "docker-soberania-headscale", "cli-mise-bore", "win-ollama-ollama", "win-cloudflared"):
            self.assertIn(fid, com)


class TestValidacao(unittest.TestCase):
    def base(self) -> dict:
        return copy.deepcopy(ferramentas.carregar())

    def test_id_repetido(self):
        d = self.base()
        d["ferramentas"].append(copy.deepcopy(d["ferramentas"][0]))
        self.assertTrue(any("repetido" in e for e in ferramentas.validar(d)))

    def test_parada_sem_motivo(self):
        d = self.base()
        f = next(f for f in d["ferramentas"] if f["decisao"] == "normal")
        f["decisao"] = "parada"
        self.assertTrue(any("sem motivo" in e for e in ferramentas.validar(d)))

    def test_conferir_errado_para_o_tipo(self):
        d = self.base()
        f = next(f for f in d["ferramentas"] if f["tipo"] == "docker")
        f["conferir"] = {"dpkg": "x"}
        self.assertTrue(any("'conferir'" in e for e in ferramentas.validar(d)))

    def test_parada_sem_rever_em(self):
        d = self.base()
        f = next(f for f in d["ferramentas"] if f["decisao"] != "normal")
        del f["rever_em"]
        self.assertTrue(any("rever_em" in e for e in ferramentas.validar(d)))

    def test_rever_em_invalido(self):
        d = self.base()
        next(f for f in d["ferramentas"] if f["decisao"] != "normal")["rever_em"] = "20/01/2027"
        self.assertTrue(any("rever_em" in e for e in ferramentas.validar(d)))

    def test_docker_sem_ram(self):
        d = self.base()
        del next(f for f in d["ferramentas"] if f["tipo"] == "docker")["ram_mb"]
        self.assertTrue(any("ram_mb" in e for e in ferramentas.validar(d)))


class TestDivergencia(unittest.TestCase):
    """Cada fonte de instalação ganhando ou perdendo uma ferramenta tem de quebrar o --check."""

    def erros_com(self, arquivo: str, antes: str, depois: str, todas: bool = False) -> list[str]:
        with CopiaDoRepositorio() as raiz:
            p = raiz / arquivo
            t = p.read_text(encoding="utf-8")
            self.assertIn(antes, t)
            p.write_text(t.replace(antes, depois) if todas else t.replace(antes, depois, 1), encoding="utf-8")
            return ferramentas.conferir_fontes(ferramentas.carregar(), raiz)

    def test_copia_intacta_passa(self):
        with CopiaDoRepositorio() as raiz:
            self.assertEqual(ferramentas.conferir_fontes(ferramentas.carregar(), raiz), [])

    def test_programa_novo_no_winget(self):
        e = self.erros_com("scripts/windows/pacotes.json", '"id": "7zip.7zip"', '"id": "Exemplo.Novo"')
        self.assertTrue(any("Exemplo.Novo" in x for x in e))

    def test_extensao_nova(self):
        e = self.erros_com("scripts/windows/vscode-extensoes.txt", "ms-python.python", "ms-python.python\nexemplo.nova")
        self.assertTrue(any("exemplo.nova" in x for x in e))

    def test_pacote_apt_novo(self):
        e = self.erros_com("scripts/wsl/extras.sh", "PACOTES=(podman", "PACOTES=(htop podman")
        self.assertTrue(any("'htop'" in x for x in e))

    def test_cli_do_mise_nova(self):
        e = self.erros_com("infra/dotfiles/dot_config/mise/config.toml", '"github:charmbracelet/gum" = "latest"',
                           '"github:charmbracelet/gum" = "latest"\n"github:exemplo/novacli" = "latest"')
        self.assertTrue(any("novacli" in x for x in e))

    def test_ferramenta_python_nova(self):
        e = self.erros_com("scripts/wsl/extras.sh", '"fava"; do', '"fava" "ruff"; do')
        self.assertTrue(any("'ruff'" in x for x in e))

    def test_servico_docker_novo(self):
        e = self.erros_com("infra/rede/compose.yaml", "services:\n", "services:\n  novo:\n    image: exemplo/novo:1\n")
        self.assertTrue(any("'novo'" in x for x in e))

    def test_cli_some_do_script(self):
        e = self.erros_com("scripts/wsl/nuvem.sh", "terraform", "tf-removido", todas=True)
        self.assertTrue(any("cli-terraform" in x for x in e))


class TestDecisoes(unittest.TestCase):
    def test_adr_0022_registrada(self):
        por_id = {f["id"]: f for f in ferramentas.carregar()["ferramentas"]}
        for fid in ("docker-soberania-headscale", "cli-mise-bore", "win-cloudflared"):
            self.assertEqual(por_id[fid]["decisao"], "parada")
            self.assertIn("ADR 0022", por_id[fid]["motivo"])
        self.assertTrue(all(f.get("rever_em") for f in por_id.values() if f["decisao"] != "normal"))

    def test_revisao_vencida(self):
        import datetime as dt
        d = ferramentas.carregar()
        self.assertEqual(ferramentas.revisoes_vencidas(d, dt.date(2026, 11, 25)), [])
        vencidas = ferramentas.revisoes_vencidas(d, dt.date(2027, 1, 21))
        self.assertEqual(len(vencidas), sum(f["decisao"] != "normal" for f in d["ferramentas"]))

    def test_parada_presente(self):
        d = ferramentas.carregar()
        est = [{"id": "win-cloudflared", "tipo": "windows", "decisao": "parada", "instalada": True, "rodando": None},
               {"id": "docker-soberania-headscale", "tipo": "docker", "decisao": "parada", "instalada": True, "rodando": False},
               {"id": "cli-mise-bore", "tipo": "wsl-cli", "decisao": "parada", "instalada": False, "rodando": None}]
        self.assertEqual([e["id"] for e in ferramentas.paradas_presentes(d, est)], ["win-cloudflared"])
        est[1]["rodando"] = True
        self.assertIn("docker-soberania-headscale", [e["id"] for e in ferramentas.paradas_presentes(d, est)])

    def test_portas_expostas(self):
        saida = "11434 ::\r\n11434 127.0.0.1\n5432 0.0.0.0\n6379 ::1\n"
        self.assertEqual(ferramentas.portas_expostas_windows(linhas=saida), [(5432, "0.0.0.0"), (11434, "::")])
        self.assertEqual(ferramentas.portas_expostas_windows(linhas="11434 127.0.0.1\n"), [])


class TestEstado(unittest.TestCase):
    def sondas_falsas(self, **k) -> dict:
        s = {"winget": "Git.Git  2.47", "extensao": {"ms-python.python"}, "dpkg": {"jq"}, "container": {"soberania/forgejo": "running"},
             "path": ""}
        s.update(k)
        return s

    def test_estados(self):
        s = self.sondas_falsas()
        def est(conf, tipo="wsl-apt"):
            return ferramentas.estado_de({"id": "x", "nome": "x", "tipo": tipo, "obrigatoria": True, "decisao": "normal",
                                          "conferir": conf, "instalar": ""}, s)
        self.assertTrue(est({"winget": "Git.Git"}, "windows")["instalada"])
        self.assertFalse(est({"winget": "7zip.7zip"}, "windows")["instalada"])
        self.assertTrue(est({"dpkg": "jq"})["instalada"])
        self.assertTrue(est({"extensao": "ms-python.python"}, "vscode")["instalada"])
        r = est({"container": "soberania/forgejo"}, "docker")
        self.assertTrue(r["instalada"] and r["rodando"])
        self.assertFalse(est({"container": "rede/adguard"}, "docker")["instalada"])

    def test_sem_como_saber_fica_desconhecido(self):
        s = self.sondas_falsas(winget=None)
        r = ferramentas.estado_de({"id": "x", "nome": "x", "tipo": "windows", "obrigatoria": True, "decisao": "normal",
                                   "conferir": {"winget": "Git.Git"}, "instalar": ""}, s)
        self.assertIsNone(r["instalada"])

    def test_faltando_ignora_decisao_e_desconhecido(self):
        est = [{"obrigatoria": True, "decisao": "normal", "instalada": False},
               {"obrigatoria": True, "decisao": "adiada", "instalada": False},
               {"obrigatoria": True, "decisao": "normal", "instalada": None},
               {"obrigatoria": False, "decisao": "normal", "instalada": False}]
        self.assertEqual(len(ferramentas.faltando(est)), 1)


if __name__ == "__main__":
    unittest.main()
