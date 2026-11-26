#!/usr/bin/env python3
"""Validação de ponta a ponta do setup: refaz as checagens automáticas da matriz de docs/operacao/validacao.md.

    just validar                 # caminho crítico + testes de todos os módulos, imprime a matriz
    just validar --rapido        # pula o just check (o mais lento)
    just validar --restaurar     # também restaura o último snapshot REAL numa pasta temporária (demora)

Nunca lê nem imprime segredo: do KeePassXC só confere que o cofre existe; o restic usa o arquivo de senha
sem mostrá-lo; o ensaio de backup roda num repositório descartável, com senha aleatória, numa pasta temporária.
Sai com 1 se alguma célula der FALHA.
"""
from __future__ import annotations

import argparse
import json
import os
import shutil
import sqlite3
import subprocess
import sys
import tempfile
import time
import urllib.request
from datetime import datetime
from dataclasses import dataclass
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]
OK, FALHA, NAO, MIM = "OK", "FALHA", "NÃO EXISTE", "PRECISA DE MIM"
PESO = {OK: 0, NAO: 1, MIM: 2, FALHA: 3}
COLUNAS = ("testes", "pc", "sozinho", "integracao")
VERBOSO = False  # main() liga: mostra cada passo no stderr para ninguém achar que travou

TITULOS = {"testes": "Testes", "pc": "Roda no PC", "sozinho": "Roda sozinho", "integracao": "Integração"}

# Caminho crítico, na ordem da validação: item -> pastas de tools/ cujos testes contam para ele
CRITICO = {
    "1. Instalação": ["implantacao", "vault", "sessao"],
    "2. Segredos": ["seguranca"],
    "3. Backup": ["validar"],
    "4. Motor e triagem": ["motor", "triagem", "ia", "remoto"],
    "5. Núcleo": ["nucleo"],
    "6. Coerência e docs": ["coerencia", "repos"],
    "7. Professor e mapa": ["professor", "registro", "colher"],
    "8. Ferramentas": ["ferramentas"],
}


@dataclass
class Resultado:
    item: str
    coluna: str
    status: str
    motivo: str = ""


def rodar(cmd: list[str] | str, timeout: int = 300, env: dict | None = None) -> tuple[int, str]:
    """Roda um comando e devolve (código, últimas linhas). Nunca levanta."""
    if VERBOSO:
        print(f"  … {cmd if isinstance(cmd, str) else ' '.join(cmd)}"[:110], file=sys.stderr, flush=True)
    try:
        # stdin vazio: com a saída capturada, uma pergunta (ex.: a triagem sem --nucleo) ficaria invisível e travaria
        p = subprocess.run(cmd, cwd=RAIZ, shell=isinstance(cmd, str), capture_output=True, text=True,
                           timeout=timeout, env=env, stdin=subprocess.DEVNULL)
        saida = [l for l in (p.stdout + p.stderr).strip().splitlines() if not l.startswith("error: Recipe")]
        return p.returncode, " | ".join(saida[-2:])[:160]
    except FileNotFoundError as e:
        return 127, str(e)
    except subprocess.TimeoutExpired:
        return 124, f"passou de {timeout}s"


def tem(prog: str) -> bool:
    return shutil.which(prog) is not None


def http_ok(url: str) -> bool:
    try:
        with urllib.request.urlopen(url, timeout=3) as r:
            return 200 <= r.status < 300
    except Exception:
        return False


def pior(estados: list[str]) -> str:
    return max(estados, key=lambda s: PESO[s]) if estados else NAO


def por_comando(item: str, coluna: str, cmd, falta: str = "", timeout: int = 300) -> Resultado:
    rc, ult = rodar(cmd, timeout)
    if rc == 0:
        return Resultado(item, coluna, OK)
    if rc == 127:
        return Resultado(item, coluna, MIM, falta or f"comando ausente: {ult}")
    return Resultado(item, coluna, FALHA, f"rc={rc}: {ult}")


# ------------------------------------------------------------------ testes
def pastas_com_testes() -> list[str]:
    return sorted(d.name for d in (RAIZ / "tools").iterdir() if d.is_dir() and any(d.glob("test_*.py")))


def testes(pasta: str) -> tuple[str, str]:
    rc, ult = rodar([sys.executable, "-m", "unittest", "discover", "-s", f"tools/{pasta}", "-q"], 600)
    return (OK, "") if rc == 0 else (FALHA, ult)


# ------------------------------------------------------------------ cron, núcleo, backup
def crontab() -> str | None:
    if not tem("crontab"):
        return None
    p = subprocess.run(["crontab", "-l"], capture_output=True, text=True)
    return p.stdout if p.returncode == 0 else ""


def linha_agendada(trecho: str, cron: str | None) -> bool:
    return bool(cron) and any(trecho in l and "# amtech-setup" in l for l in cron.splitlines())


def caminhos_cofre() -> list[Path]:
    """Os mesmos lugares que o segredos.sh procura: COFRE, o do roteiro (Documents\\Cofre) e o nome antigo."""
    u = os.environ.get("USER", "")
    lista = [Path(os.environ["COFRE"])] if os.environ.get("COFRE") else []
    return lista + sorted(Path("/mnt/c/Users").glob("*/Documents/Cofre/Cofre.kdbx")) + [
        Path.home() / "Documents/Cofre/Cofre.kdbx", Path(f"/mnt/c/Users/{u}/Documents/Cofre/Cofre.kdbx"),
        Path(f"/mnt/c/Users/{u}/cofre senhas.kdbx")]


def banco_nucleo() -> Path:
    return Path(os.environ.get("NUCLEO_DB") or Path.home() / ".local" / "share" / "nucleo" / "nucleo.db")


def ultimo_evento(tipo: str) -> str | None:
    db = banco_nucleo()
    if not db.exists():
        return None
    try:
        con = sqlite3.connect(f"file:{db}?mode=ro", uri=True)
        lin = con.execute("select quando from eventos where tipo=? order by id desc limit 1", (tipo,)).fetchone()
        con.close()
        return lin[0] if lin else ""
    except sqlite3.Error:
        return None


def recente(arquivo: Path, horas: float) -> bool:
    return arquivo.exists() and (time.time() - arquivo.stat().st_mtime) < horas * 3600


def ler_backup_env(conf: Path) -> dict[str, str]:
    """Lê RESTIC_REPOSITORY e RESTIC_PASSWORD_FILE do backup.env pelo próprio bash (expande $HOME). Não lê a senha."""
    p = subprocess.run(["bash", "-c", 'set -a; . "$1" >/dev/null 2>&1; printf "%s\\n%s\\n%s\\n" "${RESTIC_REPOSITORY:-}" "${RESTIC_PASSWORD_FILE:-}" "${RESTIC_REPOSITORY_EXTERNO:-}"', "_", str(conf)],
                       capture_output=True, text=True, stdin=subprocess.DEVNULL)
    linhas = (p.stdout.splitlines() + ["", "", ""])[:3]
    return {"repo": linhas[0].strip(), "senha": linhas[1].strip(), "externo": linhas[2].strip()}


def estado_backup_externo(externo: str, ult_copia: str | None, ult_teste: str | None,
                          agora: datetime | None = None) -> tuple[str, str]:
    """Cópia no HD externo (3-2-1): configurada, feita há no máximo 8 dias e restauração testada há no máximo 35."""
    if not externo:
        return MIM, "sem cópia fora do SSD: conecte um HD, ponha RESTIC_REPOSITORY_EXTERNO no backup.env e rode just backup-externo"
    agora = agora or datetime.now()

    def dias(quando: str | None) -> float | None:
        try:
            return (agora - datetime.fromisoformat(quando)).total_seconds() / 86400 if quando else None
        except ValueError:
            return None
    d_copia, d_teste = dias(ult_copia), dias(ult_teste)
    if d_copia is None or d_copia > 8:
        quando = "nunca feita" if d_copia is None else f"feita há {d_copia:.0f} dias"
        return MIM, f"cópia no HD {quando}: conecte o HD e rode just backup-externo"
    if d_teste is None or d_teste > 35:
        quando = "nunca testada" if d_teste is None else f"testada há {d_teste:.0f} dias"
        return MIM, f"restauração do HD {quando}: just backup-externo --restaurar"
    return OK, ""


def disco_montado(caminho: Path, ismount=os.path.ismount) -> bool:
    """Um caminho em /mnt/<letra>/ só vale se a letra for um disco do Windows montado de verdade (no WSL, /mnt/d pode ser só uma pasta)."""
    partes = caminho.parts
    if len(partes) >= 3 and partes[1] == "mnt" and len(partes[2]) == 1:
        return ismount(str(Path(*partes[:3])))
    return True


def estado_backup(conf: Path) -> tuple[tuple[str, str], tuple[str, str]]:
    """(Roda no PC, Integração) do backup real: config, arquivo de senha (só tamanho e permissão) e repositório."""
    if not conf.exists():
        return (MIM, f"crie {conf} (infra/templates/backup.env.example)"), (MIM, "repositório restic e senha no KeePassXC")
    v = ler_backup_env(conf)
    senha = Path(v["senha"]) if v["senha"] else None
    if not senha or not senha.is_file() or senha.stat().st_size == 0:
        pc = (MIM, f"arquivo de senha do restic vazio ou ausente ({v['senha'] or 'RESTIC_PASSWORD_FILE'}): cole a senha do KeePassXC")
    elif oct(senha.stat().st_mode & 0o777) != "0o600":
        pc = (FALHA, f"chmod 600 {senha}")
    else:
        pc = (OK, "")
    repo = v["repo"]
    if not repo:
        integ = (MIM, "defina RESTIC_REPOSITORY no backup.env")
    elif ":" in repo.split("/")[0]:
        integ = (OK, "") if pc[0] == OK and rodar(["restic", "-r", repo, "--password-file", str(senha), "cat", "config"], 60)[0] == 0 \
            else (MIM, f"repositório remoto {repo} não respondeu")
    elif (Path(repo) / "config").is_file():
        integ = (OK, "")
    elif not disco_montado(Path(repo)):
        letra = Path(repo).parts[2].upper()
        integ = (MIM, f"o disco {letra}: não está ligado ao Ubuntu ({Path(*Path(repo).parts[:3])} é só uma pasta): conecte o disco ou troque RESTIC_REPOSITORY no backup.env")
    elif not Path(repo).parent.exists():
        integ = (MIM, f"disco do repositório não existe ({Path(repo).parent})")
    else:
        integ = (MIM, f"repositório {repo} ainda não criado: restic init (com o backup.env carregado)")
    return pc, integ


def ensaio_backup() -> tuple[str, str]:
    """backup.sh + teste-restauracao.sh num HOME e repositório descartáveis; confere o evento no núcleo."""
    if not tem("restic"):
        return MIM, "instale o restic (o bootstrap já prevê: sudo apt install restic)"
    with tempfile.TemporaryDirectory() as t:
        h = Path(t)
        (h / ".config/amtech").mkdir(parents=True)
        (h / "dados").mkdir()
        (h / "dados/a.txt").write_text("ensaio\n")
        senha = h / ".config/amtech/restic.senha"
        senha.write_text(os.urandom(18).hex())
        senha.chmod(0o600)
        (h / ".config/amtech/backup.env").write_text(
            f'RESTIC_REPOSITORY={h}/repo\nRESTIC_PASSWORD_FILE={senha}\nBACKUP_PASTAS="{h}/dados"\n')
        env = {**os.environ, "HOME": str(h), "RESTIC_REPOSITORY": f"{h}/repo", "RESTIC_PASSWORD_FILE": str(senha),
               "NUCLEO_DB": str(h / "nucleo.db")}
        for passo in (["restic", "init", "-q"], ["bash", "scripts/wsl/backup.sh"],
                      ["bash", "scripts/wsl/teste-restauracao.sh"]):
            rc, ult = rodar(passo, 300, env)
            if rc:
                return FALHA, f"{' '.join(passo[-1:])}: {ult}"
        try:
            con = sqlite3.connect(h / "nucleo.db")
            n = con.execute("select count(*) from eventos where tipo='backup.concluido'").fetchone()[0]
            con.close()
        except sqlite3.Error:
            n = 0
        return (OK, "") if n else (FALHA, "backup rodou, mas o evento backup.concluido não chegou ao núcleo")


# ------------------------------------------------------------------ decisões do Alan (data/ferramentas.json)
def decisoes() -> dict[str, tuple[str, str]]:
    """id -> (decisão, nome). Parada ou adiada por decisão não conta como falta."""
    try:
        dados = json.loads((RAIZ / "data/ferramentas.json").read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return {}
    return {f["id"]: (f["decisao"], f["nome"]) for f in dados["ferramentas"]}


def exigir(item: str, coluna: str, ferramenta: str, ok: bool, falta: str, dec: dict[str, tuple[str, str]]) -> Resultado:
    """OK se ok; NÃO EXISTE se a ferramenta está parada ou adiada por decisão; senão PRECISA DE MIM."""
    d, nome = dec.get(ferramenta, ("normal", ferramenta))
    if d != "normal":
        return Resultado(item, coluna, NAO, f"{nome}: {d} por decisão do Alan")
    return Resultado(item, coluna, OK if ok else MIM, "" if ok else falta)


def checar_ferramentas() -> list[Resultado]:
    """8. Ferramentas: obrigatórias instaladas e serviços sempre ligados no ar (fonte: data/ferramentas.json)."""
    i = "8. Ferramentas"
    sys.path.insert(0, str(RAIZ / "tools" / "ferramentas"))
    import ferramentas  # noqa: E402
    dados = ferramentas.carregar()
    erros = ferramentas.validar(dados) or ferramentas.conferir_fontes(dados)
    R = [Resultado(i, "pc", FALHA, f"registro divergente: {erros[0]}")] if erros else []
    est = ferramentas.estado(dados)
    faltam = ferramentas.faltando(est)
    R.append(Resultado(i, "pc", OK if not faltam else MIM,
                       "" if not faltam else "faltam: " + ", ".join(f"{e['nome']} ({e['instalar']})" for e in faltam[:6])))
    sem_wsl = ferramentas.faltando_wsl(est)
    R.append(Resultado(i, "pc", OK if not sem_wsl else MIM,
                       "" if not sem_wsl else f"{len(sem_wsl)} extensão(ões) do VS Code faltando no Ubuntu: just extensoes-wsl"))
    vencidas = ferramentas.revisoes_vencidas(dados)
    R.append(Resultado(i, "pc", OK if not vencidas else MIM,
                       "" if not vencidas else "rever decisão (ADR 0022): " + ", ".join(f"{f['nome']} ({f['rever_em']})" for f in vencidas)))
    presentes = ferramentas.paradas_presentes(dados, est)
    R.append(Resultado(i, "pc", OK if not presentes else MIM,
                       "" if not presentes else "parada por decisão, mas ainda instalada: " + ", ".join(e["nome"] for e in presentes)))
    expostas = ferramentas.portas_expostas_windows()
    if expostas is None:
        R.append(Resultado(i, "integracao", NAO, "sem PowerShell: não dá para conferir as portas do Windows daqui"))
    else:
        R.append(Resultado(i, "integracao", OK if not expostas else FALHA,
                           "" if not expostas else "aberta fora do 127.0.0.1 (ADR 0022): " + ", ".join(f"{p} em {e}" for p, e in expostas)))
    sempre = [e for e, f in zip(est, dados["ferramentas"]) if f.get("perfil") == "sempre" and f["obrigatoria"] and f["decisao"] == "normal"]
    parados = [e["nome"] for e in sempre if e["rodando"] is False]
    R.append(Resultado(i, "sozinho", OK if not parados else MIM, "" if not parados else "fora do ar: " + ", ".join(parados) + " (just ligar)"))
    desconhecidos = sum(e["instalada"] is None for e in est)
    R.append(Resultado(i, "integracao", NAO if desconhecidos else OK,
                       f"{desconhecidos} sem como conferir daqui (winget/VS Code só no WSL com Windows)" if desconhecidos else ""))
    return R


# ------------------------------------------------------------------ checagens por item
def checar(rapido: bool, restaurar: bool) -> list[Resultado]:
    R: list[Resultado] = []
    cron = crontab()
    cron_msg = "sem cron neste ambiente" if cron is None else "rode: bash scripts/wsl/agendar.sh --aplicar"
    dec = decisoes()

    # 1. Instalação
    i = "1. Instalação"
    R.append(por_comando(i, "pc", ["just", "--summary"], "instale o just (bootstrap)"))
    R.append(por_comando(i, "pc", ["just", "bootstrap-simular"]))
    R.append(por_comando(i, "pc", ["just", "os-simular"]))
    rc, ult = rodar(["just", "verificar"], 300)
    R.append(Resultado(i, "pc", OK if rc == 0 else MIM, "" if rc == 0 else f"just verificar: {ult}"))
    R.append(Resultado(i, "sozinho", NAO, "instalação é manual por natureza"))
    R.append(Resultado(i, "integracao", OK if github_ok() else MIM, "" if github_ok() else "gh auth login (GitHub)"))

    # 2. Segredos (nunca abre o cofre)
    i = "2. Segredos"
    cofre = next((c for c in caminhos_cofre() if c.exists()), caminhos_cofre()[0])
    R.append(exigir(i, "pc", "cli-keepassxc-cli", tem("keepassxc-cli"), "sudo apt install keepassxc", dec))
    R.append(exigir(i, "pc", "win-keepassxcteam-keepassxc", cofre.exists(), "cofre .kdbx não achado (defina COFRE)", dec))
    if tem("age") and tem("age-keygen"):
        with tempfile.TemporaryDirectory() as t:
            rc, _ = rodar(f'cd "{t}" && age-keygen -o k 2>/dev/null && printf x | age -e -r "$(age-keygen -y k)" -o c '
                          f'&& [ "$(age -d -i k c)" = x ]')
        R.append(Resultado(i, "pc", OK if rc == 0 else FALHA, "" if rc == 0 else "age não cifra/decifra"))
    else:
        R.append(Resultado(i, "pc", MIM, "age ausente: bash scripts/wsl/extras.sh"))
    R.append(exigir(i, "pc", "cli-mise-sops", tem("sops"), "sops ausente: bash scripts/wsl/extras.sh", dec))
    R.append(Resultado(i, "sozinho", NAO, "segredo não tem agendamento"))
    R.append(Resultado(i, "integracao", NAO, "sops/age na VM ainda não existe (ADR 0009, fase futura)"))

    # 3. Backup
    i = "3. Backup"
    R.append(Resultado(i, "pc", *ensaio_backup()))
    conf = Path.home() / ".config/amtech/backup.env"
    pc_backup, integ_backup = estado_backup(conf)
    R.append(Resultado(i, "pc", *pc_backup))
    if restaurar and conf.exists():
        rc, ult = rodar(f'set -a; . "{conf}"; set +a; bash scripts/wsl/teste-restauracao.sh', 3600)
        R.append(Resultado(i, "pc", OK if rc == 0 else FALHA, "" if rc == 0 else f"restauração real: {ult}"))
    agendado = linha_agendada("backup.sh", cron)
    log_ok = recente(Path.home() / "backup-ultimo.log", 36)
    ev = ultimo_evento("backup.concluido")
    if agendado and log_ok and ev:
        R.append(Resultado(i, "sozinho", OK))
    else:
        R.append(Resultado(i, "sozinho", MIM, cron_msg) if not agendado else
                 Resultado(i, "sozinho", FALHA, "agendado, mas sem backup nas últimas 36 h ou sem evento no núcleo (veja ~/backup-ultimo.log)"))
    R.append(Resultado(i, "integracao", *integ_backup))
    externo = ler_backup_env(conf)["externo"] if conf.exists() else ""
    R.append(Resultado(i, "pc", *estado_backup_externo(externo, ultimo_evento("backup.externo.concluido"),
                                                        ultimo_evento("backup.externo.restaurado"))))

    # 4. Motor e triagem
    i = "4. Motor e triagem"
    R.append(por_comando(i, "pc", ["just", "triagem", "atendimento no WhatsApp com fila", "--nucleo", "nao", "--integra", "nao"]))
    R.append(por_comando(i, "pc", ["just", "motor", "calcular o rateio"]))
    R.append(Resultado(i, "sozinho", OK if linha_agendada("resumo-manha", cron) else MIM,
                       "" if linha_agendada("resumo-manha", cron) else cron_msg))
    ollama, litellm = http_ok("http://localhost:11434/api/tags"), http_ok("http://localhost:4000/health/liveliness")
    R.append(Resultado(i, "integracao", OK if ollama else MIM, "" if ollama else "Ollama fora do ar: just ligar"))
    R.append(exigir(i, "integracao", "docker-ia-litellm", litellm, "LiteLLM fora do ar: just ligar (precisa do Docker)", dec))

    # 5. Núcleo
    i = "5. Núcleo"
    db = banco_nucleo()
    if db.exists():
        rc, ult = rodar(["sqlite3", str(db), "pragma integrity_check;"], 60) if tem("sqlite3") else (0, "ok")
        R.append(Resultado(i, "pc", OK if rc == 0 and "ok" in ult else FALHA, "" if rc == 0 else ult))
    else:
        R.append(Resultado(i, "pc", MIM, "python3 tools/nucleo/nucleo.py iniciar"))
    R.append(por_comando(i, "pc", ["just", "agora"]))
    n_cron = sum(1 for l in (cron or "").splitlines() if "# amtech-setup" in l)
    timer = rodar("systemctl --user is-active amtech-conteudo.timer", 20)[0] == 0
    R.append(Resultado(i, "sozinho", OK if n_cron >= 3 else MIM, "" if n_cron >= 3 else f"{n_cron}/3 rotinas no cron; {cron_msg}"))
    R.append(exigir(i, "sozinho", "svc-pipeline", timer, "timer do pipeline parado: bash scripts/wsl/ativar-pipeline.sh", dec))
    R.append(Resultado(i, "integracao", NAO, "núcleo é local (PostgreSQL na VM é fase futura)"))

    # 6. Coerência e docs
    i = "6. Coerência e docs"
    if not rapido:
        R.append(por_comando(i, "pc", ["just", "check"], timeout=900))
    rc, ult = rodar([sys.executable, "tools/coerencia/coerencia.py"], 120)
    R.append(Resultado(i, "pc", OK if rc == 0 else FALHA, "" if rc == 0 else ult))
    R.append(Resultado(i, "pc", OK if tem("gitleaks") else MIM, "" if tem("gitleaks") else "gitleaks ausente: rode o bootstrap"))
    R.append(Resultado(i, "pc", OK if hook_ligado() else MIM, "" if hook_ligado() else "hook do push desligado: git config core.hooksPath scripts/git-hooks"))
    R += ci_github(i)
    R.append(Resultado(i, "integracao", OK if github_ok() else MIM, "" if github_ok() else "GitHub não responde: gh auth login"))

    # 7. Professor e mapa
    i = "7. Professor e mapa"
    for a in ("hoje", "trilha", "cartoes"):
        R.append(por_comando(i, "pc", ["just", "professor", a]))
    mapa = Path.home() / "dev/mapa-de-estudo/MAPA.md"
    if mapa.exists():
        R.append(por_comando(i, "pc", ["just", "professor-mapa"]))
    else:
        R.append(Resultado(i, "pc", MIM, "clone o mapa-de-estudo em ~/dev"))
    R.append(Resultado(i, "sozinho", NAO, "não há agendamento do Professor (é sob demanda)"))
    vault = Path.home() / "dev/notas"
    tem_vault = (vault / ".git").exists()
    R.append(Resultado(i, "integracao", OK if tem_vault else MIM, "" if tem_vault else "clone o vault em ~/dev/notas"))

    # 8. Ferramentas (fonte única: data/ferramentas.json)
    R.extend(checar_ferramentas())
    return R


REPO = "AlanMateus17/dev-setup"


def hook_ligado(raiz: Path = RAIZ) -> bool:
    """O pre-push (just check antes do push) só vale se o Git usar a pasta de hooks do repositório."""
    p = subprocess.run(["git", "-C", str(raiz), "config", "--get", "core.hooksPath"], capture_output=True, text=True)
    return p.stdout.strip() in ("scripts/git-hooks", str(raiz / "scripts/git-hooks"))


def github_ok() -> bool:
    """REST (gh api): funciona no PC e também nas sessões na nuvem, onde o GraphQL é bloqueado."""
    return rodar(["gh", "api", f"repos/{REPO}", "-q", ".name"], 30)[0] == 0


def ci_github(item: str) -> list[Resultado]:
    if not github_ok():
        return [Resultado(item, "sozinho", MIM, "gh auth login para ler o CI")]
    p = subprocess.run(["gh", "api", f"repos/{REPO}/actions/runs?per_page=30"], capture_output=True, text=True, cwd=RAIZ)
    try:
        runs = runs_proprios(json.loads(p.stdout or "{}").get("workflow_runs", []))
    except json.JSONDecodeError:
        runs = []
    # O agendado é buscado à parte: num dia com muitos PRs, os 30 runs mais recentes não chegam até ele.
    a = subprocess.run(["gh", "api", f"repos/{REPO}/actions/workflows/vigia.yml/runs?event=schedule&per_page=1"],
                       capture_output=True, text=True, cwd=RAIZ)
    try:
        lista = json.loads(a.stdout or "{}").get("workflow_runs", [])
        agendado = lista[0] if lista else {}
    except json.JSONDecodeError:
        agendado = None
    return [avaliar_ci(item, runs, agendado)]


def runs_proprios(brutos: list[dict]) -> list[dict]:
    """Só os workflows do repositório (.github/workflows); os 'dynamic/' do Dependabot ficam de fora."""
    return [{"workflowName": r.get("name", ""), "conclusion": r.get("conclusion") or "", "event": r.get("event", "")}
            for r in brutos if str(r.get("path", "")).startswith(".github/workflows/")]


def avaliar_ci(item: str, runs: list[dict], agendado: dict | None = None, agora: float | None = None) -> Resultado:
    """O CI conta como 'roda sozinho' se o último de cada workflow passou e o agendado (vigia) rodou em 8 dias.
    agendado: o último run agendado do vigia ({} = nunca rodou; None = não deu para ler, usa só a lista de runs)."""
    if not runs:
        return Resultado(item, "sozinho", FALHA, "nenhuma execução do CI encontrada")
    ultimos: dict[str, dict] = {}
    for r in runs:  # gh devolve do mais novo para o mais velho
        ultimos.setdefault(r["workflowName"], r)
    ruins = [w for w, r in ultimos.items() if r.get("conclusion") not in ("success", "")]
    if ruins:
        return Resultado(item, "sozinho", FALHA, f"último run falhou: {', '.join(sorted(ruins))}")
    if agendado is not None:
        if not agendado:
            return Resultado(item, "sozinho", FALHA, "o vigia agendado nunca rodou")
        quando = time.mktime(time.strptime(agendado.get("created_at", "1970-01-01T00:00:00Z"), "%Y-%m-%dT%H:%M:%SZ")) - time.timezone
        dias = ((agora or time.time()) - quando) / 86400
        if dias > 8:
            return Resultado(item, "sozinho", FALHA, f"o vigia agendado não roda há {dias:.0f} dias")
        if agendado.get("conclusion") not in ("success", "", None):
            return Resultado(item, "sozinho", FALHA, f"o último vigia agendado terminou com '{agendado.get('conclusion')}'")
        return Resultado(item, "sozinho", OK)
    agendados = [r for r in runs if r.get("event") == "schedule"]
    if not agendados:
        return Resultado(item, "sozinho", FALHA, "o vigia agendado não rodou nos últimos 30 runs")
    return Resultado(item, "sozinho", OK)


# ------------------------------------------------------------------ matriz
def matriz(resultados: list[Resultado], testes_por_pasta: dict[str, tuple[str, str]]) -> dict[str, dict[str, Resultado]]:
    m: dict[str, dict[str, list[Resultado]]] = {}
    for item, pastas in CRITICO.items():
        m.setdefault(item, {c: [] for c in COLUNAS})
        if pastas:
            for p in pastas:
                st, mot = testes_por_pasta.get(p, (NAO, f"sem testes em tools/{p}"))
                m[item]["testes"].append(Resultado(item, "testes", st, f"{p}: {mot}" if mot else ""))
        else:
            m[item]["testes"].append(Resultado(item, "testes", NAO, "só scripts shell (o ensaio em 'Roda no PC' cobre)"))
    for r in resultados:
        m.setdefault(r.item, {c: [] for c in COLUNAS})[r.coluna].append(r)
    usados = {p for ps in CRITICO.values() for p in ps}
    for p, (st, mot) in sorted(testes_por_pasta.items()):
        if p not in usados:
            m[f"módulo {p}"] = {"testes": [Resultado(p, "testes", st, mot)], "pc": [], "sozinho": [], "integracao": []}
    final: dict[str, dict[str, Resultado]] = {}
    for item, cols in m.items():
        final[item] = {}
        for c in COLUNAS:
            rs = cols[c]
            if not rs:
                final[item][c] = Resultado(item, c, "—")
                continue
            st = pior([r.status for r in rs])
            motivos = "; ".join(dict.fromkeys(r.motivo for r in rs if r.status == st and r.motivo))
            final[item][c] = Resultado(item, c, st, motivos)
    return final


def imprimir(final: dict[str, dict[str, Resultado]]) -> int:
    print("| Item | " + " | ".join(TITULOS[c] for c in COLUNAS) + " |")
    print("|---|" + "---|" * len(COLUNAS))
    falhas = 0
    for item, cols in final.items():
        cel = []
        for c in COLUNAS:
            r = cols[c]
            falhas += r.status == FALHA
            cel.append(r.status + (f" ({r.motivo})" if r.motivo and r.status != OK else ""))
        print(f"| {item} | " + " | ".join(cel) + " |")
    contagem = {s: sum(1 for cols in final.values() for r in cols.values() if r.status == s) for s in PESO}
    print("\nResumo: " + ", ".join(f"{s} {n}" for s, n in contagem.items()))
    return 1 if falhas else 0


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--rapido", action="store_true", help="pula o just check")
    ap.add_argument("--restaurar", action="store_true", help="restaura o último snapshot real numa pasta temporária")
    a = ap.parse_args(argv)
    global VERBOSO
    VERBOSO = True
    print("Validando (5 a 10 min; a tabela sai no fim)…", file=sys.stderr, flush=True)
    por_pasta = {p: testes(p) for p in pastas_com_testes()}
    return imprimir(matriz(checar(a.rapido, a.restaurar), por_pasta))


if __name__ == "__main__":
    sys.exit(main())
