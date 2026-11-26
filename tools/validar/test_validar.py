import time
import io
import os
import re
import shutil
import sqlite3
import subprocess
import sys
import tempfile
import unittest
import unittest.mock
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

    def test_ci_agendado_buscado_a_parte(self):
        """Num dia com muitos PRs o vigia sai dos 30 runs recentes; o agendado buscado à parte decide."""
        so_prs = [{"workflowName": "docs", "conclusion": "success", "event": "pull_request"}]
        agora = time.mktime(time.strptime("2026-11-25T12:00:00Z", "%Y-%m-%dT%H:%M:%SZ")) - time.timezone
        recente = {"created_at": "2026-11-23T20:51:35Z", "conclusion": "success"}
        velho = {"created_at": "2026-11-10T09:00:00Z", "conclusion": "success"}
        self.assertEqual(v.avaliar_ci("6", so_prs, recente, agora).status, v.OK)
        self.assertEqual(v.avaliar_ci("6", so_prs, velho, agora).status, v.FALHA)
        self.assertEqual(v.avaliar_ci("6", so_prs, {}, agora).status, v.FALHA)
        self.assertEqual(v.avaliar_ci("6", so_prs, {**recente, "conclusion": "failure"}, agora).status, v.FALHA)

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



class TestBackupExterno(unittest.TestCase):
    AGORA = v.datetime(2026, 11, 26, 12, 0)

    def test_estado(self):
        e = lambda ext, c, t: v.estado_backup_externo(ext, c, t, self.AGORA)
        self.assertEqual(e("", None, None)[0], v.MIM)                          # caso do PC em 26/11: só o SSD
        self.assertIn("nunca feita", e("/mnt/e/r", "", None)[1])
        self.assertIn("há 10 dias", e("/mnt/e/r", "2026-11-16T12:00:00", None)[1])
        self.assertIn("nunca testada", e("/mnt/e/r", "2026-11-25T22:00:00", None)[1])
        self.assertIn("--restaurar", e("/mnt/e/r", "2026-11-25T22:00:00", "2026-10-01T10:00:00")[1])
        self.assertEqual(e("/mnt/e/r", "2026-11-25T22:00:00", "2026-11-20T10:00:00"), (v.OK, ""))

    @unittest.skipUnless(shutil.which("restic"), "restic ausente")
    def test_copia_restaura_e_recusa_o_proprio_ssd(self):
        raiz = Path(__file__).resolve().parents[2]
        with tempfile.TemporaryDirectory() as t:
            h = Path(t)
            (h / "dados/sub").mkdir(parents=True)
            (h / "dados/a.txt").write_text("a\n")
            (h / "dados/sub/b.txt").write_text("b\n")
            senha = h / "senha"
            senha.write_text(os.urandom(18).hex())
            senha.chmod(0o600)
            conf = h / "backup.env"
            conf.write_text(f"RESTIC_REPOSITORY={h}/ssd\nRESTIC_PASSWORD_FILE={senha}\nRESTIC_REPOSITORY_EXTERNO={h}/hd\n")
            env = {**os.environ, "BACKUP_CONF": str(conf), "NUCLEO_DB": str(h / "nucleo.db"),
                   "RESTIC_PASSWORD_FILE": str(senha)}
            corre = lambda *c: subprocess.run(list(c), cwd=raiz, env=env, capture_output=True, text=True,
                                             stdin=subprocess.DEVNULL)
            self.assertEqual(corre("restic", "-q", "-r", f"{h}/ssd", "init").returncode, 0)
            self.assertEqual(corre("restic", "-q", "-r", f"{h}/ssd", "backup", f"{h}/dados", "--tag", "diario").returncode, 0)
            script = "scripts/wsl/backup-externo.sh"
            r = corre("bash", script)
            self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
            r = corre("bash", script, "--restaurar")
            self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
            self.assertIn("2 arquivos", r.stdout)
            con = sqlite3.connect(h / "nucleo.db")
            tipos = {x for (x,) in con.execute("select tipo from eventos")}
            con.close()
            self.assertEqual(tipos, {"backup.externo.concluido", "backup.externo.restaurado"})
            # O HD não pode ser o próprio SSD (C:) nem uma pasta em /mnt/<letra> sem disco montado
            for destino, msg in (("/mnt/c/backup-restic", "no C:"), ("/mnt/q/backup-restic", "não está ligado")):
                conf.write_text(f"RESTIC_REPOSITORY={h}/ssd\nRESTIC_PASSWORD_FILE={senha}\nRESTIC_REPOSITORY_EXTERNO={destino}\n")
                r = corre("bash", script)
                self.assertEqual(r.returncode, 1)
                self.assertIn(msg, r.stdout)


class TestCriticosNoBackup(unittest.TestCase):
    """P0 G1/G2: o cofre .kdbx e a chave do age precisam estar no último snapshot."""
    C = {"cofre": [Path("/c/Cofre.kdbx")], "chave_age": [Path("/h/keys.txt")]}

    def test_estado(self):
        self.assertEqual(v.estado_criticos(self.C, {"/c/Cofre.kdbx", "/h/keys.txt", "/outro"}), (v.OK, ""))
        st, msg = v.estado_criticos(self.C, {"/c/Cofre.kdbx"})
        self.assertEqual(st, v.MIM)
        self.assertIn("keys.txt", msg)
        self.assertIn("cofre", v.estado_criticos({"cofre": [], "chave_age": []}, set())[1])
        # O caso do PC em 26/11: cofre existe, chave do age ainda não
        self.assertIn("age-keygen", v.estado_criticos({"cofre": [Path("/c/Cofre.kdbx")], "chave_age": []}, set())[1])
        self.assertIn("listar", v.estado_criticos(self.C, None)[1])

    def test_criticos_respeita_cofre_e_chave_do_ambiente(self):
        with tempfile.TemporaryDirectory() as t:
            cofre, chave = Path(t) / "Cofre.kdbx", Path(t) / "keys.txt"
            cofre.write_text("x")
            amb = {"COFRE": str(cofre), "SOPS_AGE_KEY_FILE": str(chave)}
            with unittest.mock.patch.dict(os.environ, amb):
                self.assertEqual(v.criticos(), {"cofre": [cofre], "chave_age": []})
                chave.write_text("x")
                self.assertEqual(v.criticos(), {"cofre": [cofre], "chave_age": [chave]})


class TestHook(unittest.TestCase):
    def test_hook_ligado_le_o_core_hookspath(self):
        with tempfile.TemporaryDirectory() as d:
            subprocess.run(["git", "init", "-q", d], check=True)
            self.assertFalse(v.hook_ligado(Path(d)))
            subprocess.run(["git", "-C", d, "config", "core.hooksPath", "scripts/git-hooks"], check=True)
            self.assertTrue(v.hook_ligado(Path(d)))


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
