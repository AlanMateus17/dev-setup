import io
import re
import shutil
import subprocess
import sys
import unittest
from contextlib import redirect_stdout
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import validar as v  # noqa: E402


class TestMatriz(unittest.TestCase):
    def test_pior_estado_vence(self):
        self.assertEqual(v.pior([v.OK, v.MIM, v.NAO]), v.MIM)
        self.assertEqual(v.pior([v.OK, v.FALHA, v.MIM]), v.FALHA)
        self.assertEqual(v.pior([]), v.NAO)

    def test_matriz_junta_por_item_e_coluna(self):
        rs = [v.Resultado("5. Núcleo", "pc", v.OK), v.Resultado("5. Núcleo", "pc", v.MIM, "inicie o núcleo")]
        testes = {p: (v.OK, "") for ps in v.CRITICO.values() for p in ps}
        testes["radar"] = (v.FALHA, "1 erro")
        m = v.matriz(rs, testes)
        self.assertEqual(list(m)[:len(v.CRITICO)], list(v.CRITICO), "caminho crítico primeiro, na ordem")
        self.assertEqual(m["5. Núcleo"]["pc"].status, v.MIM)
        self.assertEqual(m["5. Núcleo"]["pc"].motivo, "inicie o núcleo")
        self.assertEqual(m["5. Núcleo"]["testes"].status, v.OK)
        self.assertEqual(m["3. Backup"]["testes"].status, v.OK)
        self.assertEqual(m["módulo radar"]["testes"].status, v.FALHA)
        self.assertEqual(m["módulo radar"]["pc"].status, "—", "o resto dos módulos só tem a coluna de testes")

    def test_imprimir_sai_1_com_falha(self):
        base = {c: v.Resultado("x", c, v.OK) for c in v.COLUNAS}
        with redirect_stdout(io.StringIO()) as saida:
            self.assertEqual(v.imprimir({"x": base}), 0)
            self.assertEqual(v.imprimir({"x": {**base, "pc": v.Resultado("x", "pc", v.FALHA, "quebrou")}}), 1)
        self.assertIn("FALHA (quebrou)", saida.getvalue())

    def test_ci(self):
        ok = [{"workflowName": "vigia", "conclusion": "success", "event": "schedule"},
              {"workflowName": "docs", "conclusion": "success", "event": "pull_request"}]
        self.assertEqual(v.avaliar_ci("6", ok).status, v.OK)
        ruim = [{"workflowName": "docs", "conclusion": "failure", "event": "push"}] + ok
        self.assertEqual(v.avaliar_ci("6", ruim).status, v.FALHA)
        self.assertEqual(v.avaliar_ci("6", ok[1:]).status, v.FALHA, "sem o agendado não roda sozinho")
        self.assertEqual(v.avaliar_ci("6", []).status, v.FALHA)

    def test_runs_proprios_ignora_dependabot(self):
        brutos = [{"name": "Graph Update", "path": "dynamic/dependabot/update-graph", "conclusion": "cancelled"},
                  {"name": "docs", "path": ".github/workflows/docs.yml", "conclusion": "success", "event": "push"}]
        self.assertEqual([r["workflowName"] for r in v.runs_proprios(brutos)], ["docs"])

    def test_linha_agendada(self):
        cron = "30 22 * * * bash /x/scripts/wsl/backup.sh > log 2>&1 # amtech-setup\n0 1 * * * outro"
        self.assertTrue(v.linha_agendada("backup.sh", cron))
        self.assertFalse(v.linha_agendada("resumo-manha", cron))
        self.assertFalse(v.linha_agendada("backup.sh", None))


class TestRodar(unittest.TestCase):
    def test_comando_que_pergunta_nao_trava(self):
        # No PC (terminal de verdade) a triagem perguntava s/n escondida pela saída capturada e passava de 300 s.
        rc, _ = v.rodar([sys.executable, "-c", "input('s/n? ')"], timeout=10)
        self.assertNotEqual(rc, 124)


class TestCofre(unittest.TestCase):
    def test_procura_onde_o_roteiro_manda_criar(self):
        import os
        antigo = os.environ.pop("COFRE", None)
        try:
            nomes = [str(c) for c in v.caminhos_cofre()]
            self.assertTrue(nomes[0].endswith("Documents/Cofre/Cofre.kdbx"))
            self.assertTrue(nomes[-1].endswith("cofre senhas.kdbx"), "o nome antigo fica por último")
            os.environ["COFRE"] = "/tmp/x.kdbx"
            self.assertEqual(str(v.caminhos_cofre()[0]), "/tmp/x.kdbx")
        finally:
            os.environ.pop("COFRE", None)
            if antigo is not None:
                os.environ["COFRE"] = antigo

    def test_segredos_sh_procura_o_mesmo_lugar(self):
        txt = (v.RAIZ / "scripts/wsl/segredos.sh").read_text(encoding="utf-8")
        self.assertIn("Documents/Cofre/Cofre.kdbx", txt)


class TestEstadoBackup(unittest.TestCase):
    """O backup.env sozinho não basta: a senha precisa existir (não vazia, chmod 600) e o repositório também."""

    def montar(self, t, conteudo_senha="segredo", modo=0o600, repo_existe=True):
        h = Path(t)
        senha = h / "restic.senha"
        senha.write_text(conteudo_senha)
        senha.chmod(modo)
        repo = h / "repo"
        if repo_existe:
            repo.mkdir()
            (repo / "config").write_text("x")
        conf = h / "backup.env"
        conf.write_text(f"RESTIC_REPOSITORY={repo}\nRESTIC_PASSWORD_FILE={senha}\n")
        return conf

    def test_sem_config(self):
        import tempfile
        with tempfile.TemporaryDirectory() as t:
            pc, integ = v.estado_backup(Path(t) / "nao-existe.env")
        self.assertEqual((pc[0], integ[0]), (v.MIM, v.MIM))

    def test_tudo_certo(self):
        import tempfile
        with tempfile.TemporaryDirectory() as t:
            pc, integ = v.estado_backup(self.montar(t))
        self.assertEqual((pc[0], integ[0]), (v.OK, v.OK))

    def test_senha_vazia_e_repo_inexistente(self):
        # O caso do PC em 25/11: backup.env copiado, senha vazia, repositório nunca criado
        import tempfile
        with tempfile.TemporaryDirectory() as t:
            pc, integ = v.estado_backup(self.montar(t, conteudo_senha="", repo_existe=False))
        self.assertEqual(pc[0], v.MIM)
        self.assertIn("vazio", pc[1])
        self.assertEqual(integ[0], v.MIM)
        self.assertIn("restic init", integ[1])

    def test_disco_do_windows_desmontado(self):
        # O caso do PC em 25/11: /mnt/d existia só como pasta, sem disco D:
        self.assertFalse(v.disco_montado(Path("/mnt/d/backup-restic"), ismount=lambda p: False))
        self.assertTrue(v.disco_montado(Path("/mnt/e/backup-restic"), ismount=lambda p: p == "/mnt/e"))
        self.assertTrue(v.disco_montado(Path("/home/x/repo"), ismount=lambda p: False), "fora de /mnt/<letra> não se aplica")

    def test_permissao_aberta(self):
        import tempfile
        with tempfile.TemporaryDirectory() as t:
            pc, _ = v.estado_backup(self.montar(t, modo=0o644))
        self.assertEqual(pc[0], v.FALHA)


class TestJustfileCompativel(unittest.TestCase):
    """O bootstrap instala o just pelo apt; no Ubuntu 24.04 é o 1.21, que não conhece [positional-arguments]."""

    def test_sem_atributos_novos(self):
        txt = (v.RAIZ / "justfile").read_text(encoding="utf-8")
        self.assertIsNone(re.search(r"^\[positional-arguments\]", txt, re.M))
        self.assertRegex(txt, r"(?m)^set positional-arguments$")
        self.assertRegex(txt, r"(?m)^validar ")

    @unittest.skipUnless(shutil.which("just"), "just ausente")
    def test_just_le_o_justfile(self):
        p = subprocess.run(["just", "--summary"], cwd=v.RAIZ, capture_output=True, text=True)
        self.assertEqual(p.returncode, 0, p.stderr)
        self.assertIn("validar", p.stdout.split())


class TestEnsaioBackup(unittest.TestCase):
    @unittest.skipUnless(shutil.which("restic"), "restic ausente")
    def test_backup_restaura_e_grava_evento(self):
        # Pega o bug antigo do backup.sh: o evento backup.concluido se perdia (separador "-----" virava opção).
        st, motivo = v.ensaio_backup()
        self.assertEqual(st, v.OK, motivo)



class TestDecisoes(unittest.TestCase):
    def test_parada_por_decisao_nao_e_falta(self):
        dec = {"x": ("parada", "decisão do Alan"), "y": ("normal", "")}
        self.assertEqual(v.exigir("i", "pc", "x", False, "instale", dec).status, v.NAO)
        self.assertEqual(v.exigir("i", "pc", "y", False, "instale", dec).status, v.MIM)
        self.assertEqual(v.exigir("i", "pc", "y", True, "instale", dec).status, v.OK)
        self.assertEqual(v.exigir("i", "pc", "sem-registro", False, "instale", dec).status, v.MIM)

    def test_decisoes_do_registro(self):
        dec = v.decisoes()
        self.assertEqual(dec["cli-keepassxc-cli"][0], "normal")   # emenda da ADR 0022
        self.assertEqual(dec["cli-mise-bore"][0], "parada")


if __name__ == "__main__":
    unittest.main()
