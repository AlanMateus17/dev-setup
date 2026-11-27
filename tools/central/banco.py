"""Banco da Central: tabelas central_* dentro do nucleo.db (que já está no backup), com migrações numeradas.

Organizações, usuários, papéis e sessões existem desde a v1 (ADR 0022 e 0023), mesmo com um usuário só.
A auditoria é uma corrente de hash: apagar ou mudar uma linha quebra a corrente e `verificar_auditoria` aponta onde.
Só biblioteca padrão.
"""
from __future__ import annotations

import hashlib
import hmac
import json
import os
import secrets
import sqlite3
import tempfile
from datetime import datetime, timedelta
from pathlib import Path

INICIO_CORRENTE = "0" * 64
SESSAO_OCIOSA = timedelta(hours=12)
SESSAO_MAXIMA = timedelta(days=7)
FALHAS_ATE_BLOQUEIO = 5
BLOQUEIO = timedelta(minutes=15)
SENHA_MINIMA = 12
_SCRYPT = {"n": 2**14, "r": 8, "p": 1, "dklen": 32}

MIGRACOES: list[str] = [
    # 1 · v1 da Central
    """
    CREATE TABLE central_organizacoes (
      id INTEGER PRIMARY KEY, nome TEXT NOT NULL UNIQUE, criada TEXT NOT NULL);
    CREATE TABLE central_papeis (
      id TEXT PRIMARY KEY, nivel_max TEXT NOT NULL CHECK (nivel_max IN ('automatico','avisa','pede-ok')),
      pode_aprovar INTEGER NOT NULL DEFAULT 0, descricao TEXT NOT NULL DEFAULT '');
    INSERT INTO central_papeis VALUES
      ('dono', 'pede-ok', 1, 'Tudo o que a allowlist permite, e aprova'),
      ('leitor', 'automatico', 0, 'Só o que roda direto; não aprova'),
      ('bot', 'pede-ok', 0, 'O bot do Telegram: pede, nunca aprova sozinho');
    CREATE TABLE central_usuarios (
      id INTEGER PRIMARY KEY, organizacao_id INTEGER NOT NULL REFERENCES central_organizacoes(id),
      nome TEXT NOT NULL, senha_hash TEXT NOT NULL, papel TEXT NOT NULL REFERENCES central_papeis(id),
      ativo INTEGER NOT NULL DEFAULT 1, criado TEXT NOT NULL, falhas INTEGER NOT NULL DEFAULT 0, bloqueado_ate TEXT,
      UNIQUE (organizacao_id, nome));
    CREATE TABLE central_sessoes (
      token_hash TEXT PRIMARY KEY, usuario_id INTEGER NOT NULL REFERENCES central_usuarios(id),
      organizacao_id INTEGER NOT NULL, csrf TEXT NOT NULL, criada TEXT NOT NULL, ultimo_uso TEXT NOT NULL, ip TEXT NOT NULL DEFAULT '');
    CREATE TABLE central_execucoes (
      id TEXT PRIMARY KEY, organizacao_id INTEGER NOT NULL, usuario_id INTEGER, receita TEXT NOT NULL,
      args TEXT NOT NULL, nivel TEXT NOT NULL, origem TEXT NOT NULL, inicio TEXT NOT NULL, fim TEXT, codigo INTEGER,
      saida TEXT NOT NULL DEFAULT '');
    CREATE TABLE central_aprovacoes (
      id TEXT PRIMARY KEY, organizacao_id INTEGER NOT NULL, receita TEXT NOT NULL, args TEXT NOT NULL,
      pedido_por INTEGER, origem TEXT NOT NULL, criado TEXT NOT NULL, expira TEXT NOT NULL,
      estado TEXT NOT NULL DEFAULT 'pendente' CHECK (estado IN ('pendente','aprovada','recusada','expirada')),
      decidido_por INTEGER, decidido_em TEXT, execucao_id TEXT);
    CREATE TABLE central_auditoria (
      id INTEGER PRIMARY KEY, quando TEXT NOT NULL, organizacao_id INTEGER, usuario_id INTEGER,
      origem TEXT NOT NULL, acao TEXT NOT NULL, alvo TEXT NOT NULL DEFAULT '', nivel TEXT NOT NULL DEFAULT '',
      resultado TEXT NOT NULL DEFAULT '', hash_anterior TEXT NOT NULL, hash TEXT NOT NULL);
    INSERT INTO central_organizacoes (nome, criada) VALUES ('Grupo AMtech', strftime('%Y-%m-%dT%H:%M:%S','now','localtime'));
    """,
    # 2 · pedidos em português (prompt): o plano, de onde veio e quanto custou; base da regra de três
    """
    CREATE TABLE central_prompts (
      id TEXT PRIMARY KEY, organizacao_id INTEGER NOT NULL, usuario_id INTEGER, texto TEXT NOT NULL,
      origem TEXT NOT NULL, plano TEXT NOT NULL, tokens INTEGER NOT NULL DEFAULT 0, criado TEXT NOT NULL,
      executado TEXT, execucoes TEXT NOT NULL DEFAULT '[]');
    CREATE INDEX central_prompts_origem ON central_prompts (organizacao_id, origem, criado);
    """,
    # 3 · auditoria assinada com HMAC (chave fora do banco) e aprovação guarda o pedido original para reconferir
    """
    ALTER TABLE central_auditoria ADD COLUMN assinatura INTEGER NOT NULL DEFAULT 1;
    ALTER TABLE central_aprovacoes ADD COLUMN pedido TEXT NOT NULL DEFAULT '';
    """,
    # 4 · marca no banco que a auditoria passou a ser assinada: depois disso, chave ou âncora sumida = alteração
    """
    CREATE TABLE central_config (chave TEXT PRIMARY KEY, valor TEXT NOT NULL);
    """,
]


def caminho_padrao() -> Path:
    return Path(os.environ.get("NUCLEO_DB") or Path.home() / ".local" / "share" / "nucleo" / "nucleo.db")


def pasta_segredos() -> Path:
    """Fora do nucleo.db e fora do Git: quem consegue mexer no banco não consegue refazer a assinatura."""
    p = Path(os.environ.get("AMTECH_CENTRAL_SEGREDOS") or Path.home() / ".config" / "amtech")
    p.mkdir(parents=True, exist_ok=True, mode=0o700)
    return p


def chave_auditoria() -> bytes:
    """Cria a chave uma vez só, mesmo com várias gravações ao mesmo tempo: escreve num temporário e liga no lugar
    (os.link falha se outro processo chegou antes, e aí vale a dele). Chave vazia ou curta é recusada."""
    pasta = pasta_segredos()
    arq = pasta / "central-auditoria.key"
    if not arq.exists():
        fd, tmp = tempfile.mkstemp(prefix=".chave-", dir=pasta)
        try:
            with os.fdopen(fd, "w") as f:
                f.write(secrets.token_hex(32))
            os.chmod(tmp, 0o600)
            try:
                os.link(tmp, arq)
            except FileExistsError:
                pass
        finally:
            os.unlink(tmp)
    chave = bytes.fromhex(arq.read_text().strip())
    if len(chave) < 32:
        raise RuntimeError(f"chave da auditoria inválida em {arq}")
    return chave


def _ancora() -> Path:
    return pasta_segredos() / "central-auditoria.ancora"


def _mac_ancora(ultimo: int, h: str, primeiro: int, chave: bytes) -> str:
    return hmac.new(chave, f"{ultimo} {h} {primeiro}".encode(), hashlib.sha256).hexdigest()


def _ler_ancora(chave: bytes) -> tuple[int, str, int] | None:
    """(último id, último hash, id da primeira linha assinada) se a âncora existir e a assinatura dela bater; senão None."""
    try:
        ultimo, h, primeiro, mac = _ancora().read_text().split()
        ultimo_i, primeiro_i = int(ultimo), int(primeiro)
    except (OSError, ValueError):
        return None
    if not hmac.compare_digest(mac, _mac_ancora(ultimo_i, h, primeiro_i, chave)):
        return None
    return ultimo_i, h, primeiro_i


def _gravar_ancora(ultimo: int, h: str, primeiro: int, chave: bytes) -> None:
    """Arquivo temporário único na mesma pasta e troca atômica: dois processos gravando ao mesmo tempo não se atrapalham."""
    pasta = pasta_segredos()
    fd, tmp = tempfile.mkstemp(prefix=".ancora-", dir=pasta)
    with os.fdopen(fd, "w") as f:
        f.write(f"{ultimo} {h} {primeiro} {_mac_ancora(ultimo, h, primeiro, chave)}\n")
    os.chmod(tmp, 0o600)
    os.replace(tmp, _ancora())


def agora() -> datetime:
    return datetime.now().replace(microsecond=0)


def _iso(t: datetime) -> str:
    return t.isoformat(timespec="seconds")


def abrir(caminho: Path) -> sqlite3.Connection:
    caminho.parent.mkdir(parents=True, exist_ok=True)
    con = sqlite3.connect(caminho, timeout=10, isolation_level=None)
    con.row_factory = sqlite3.Row
    con.execute("PRAGMA foreign_keys = ON")
    con.execute("PRAGMA busy_timeout = 10000")
    return con


def _comandos(sql: str) -> list[str]:
    """Divide um script em comandos completos (respeita ';' dentro de texto entre aspas)."""
    comandos, atual = [], ""
    for linha in sql.splitlines(keepends=True):
        atual += linha
        if sqlite3.complete_statement(atual):
            comandos.append(atual.strip())
            atual = ""
    if atual.strip():
        raise ValueError(f"migração com comando incompleto: {atual.strip()[:60]}")
    return comandos


def migrar(caminho: Path) -> int:
    con = abrir(caminho)
    try:
        con.execute("PRAGMA journal_mode = WAL")
        con.execute("CREATE TABLE IF NOT EXISTS central_migracoes (versao INTEGER PRIMARY KEY, aplicada TEXT NOT NULL)")
        feitas = {r[0] for r in con.execute("SELECT versao FROM central_migracoes")}
        for versao, sql in enumerate(MIGRACOES, 1):
            if versao in feitas:
                continue
            con.execute("BEGIN IMMEDIATE")
            try:
                for comando in _comandos(sql):
                    con.execute(comando)
                con.execute("INSERT INTO central_migracoes VALUES (?, ?)", (versao, _iso(agora())))
                con.execute("COMMIT")
            except Exception:
                con.execute("ROLLBACK")
                raise
        return len(MIGRACOES)
    finally:
        con.close()


def org_padrao(con: sqlite3.Connection) -> int:
    return con.execute("SELECT id FROM central_organizacoes ORDER BY id LIMIT 1").fetchone()[0]


# ------------------------------------------------------------------ senhas e usuários
def hash_senha(senha: str) -> str:
    sal = secrets.token_bytes(16)
    h = hashlib.scrypt(senha.encode(), salt=sal, **_SCRYPT)
    return f"scrypt${_SCRYPT['n']}${_SCRYPT['r']}${_SCRYPT['p']}${sal.hex()}${h.hex()}"


def confere_senha(senha: str, guardado: str) -> bool:
    try:
        _, n, r, p, sal, h = guardado.split("$")
        calc = hashlib.scrypt(senha.encode(), salt=bytes.fromhex(sal), n=int(n), r=int(r), p=int(p), dklen=len(h) // 2)
    except (ValueError, TypeError):
        return False
    return hmac.compare_digest(calc.hex(), h)


_HASH_FALSO = hash_senha(secrets.token_hex(16))  # iguala o tempo quando o usuário não existe


def salvar_usuario(con: sqlite3.Connection, nome: str, senha: str, papel: str = "dono") -> int:
    if len(senha) < SENHA_MINIMA:
        raise ValueError(f"a senha precisa de pelo menos {SENHA_MINIMA} caracteres")
    org = org_padrao(con)
    h = hash_senha(senha)
    linha = con.execute("SELECT id FROM central_usuarios WHERE organizacao_id = ? AND nome = ?", (org, nome)).fetchone()
    if linha:
        con.execute("UPDATE central_usuarios SET senha_hash = ?, papel = ?, falhas = 0, bloqueado_ate = NULL, ativo = 1 WHERE id = ?",
                    (h, papel, linha[0]))
        con.execute("DELETE FROM central_sessoes WHERE usuario_id = ?", (linha[0],))
        return linha[0]
    return con.execute("INSERT INTO central_usuarios (organizacao_id, nome, senha_hash, papel, criado) VALUES (?, ?, ?, ?, ?)",
                       (org, nome, h, papel, _iso(agora()))).lastrowid


def autenticar(con: sqlite3.Connection, nome: str, senha: str, quando: datetime | None = None) -> sqlite3.Row | None:
    quando = quando or agora()
    u = con.execute("SELECT * FROM central_usuarios WHERE nome = ? AND ativo = 1", (nome,)).fetchone()
    if u is None:
        confere_senha(senha, _HASH_FALSO)
        return None
    if u["bloqueado_ate"] and datetime.fromisoformat(u["bloqueado_ate"]) > quando:
        confere_senha(senha, _HASH_FALSO)
        return None
    if confere_senha(senha, u["senha_hash"]):
        con.execute("UPDATE central_usuarios SET falhas = 0, bloqueado_ate = NULL WHERE id = ?", (u["id"],))
        return u
    falhas = u["falhas"] + 1
    bloqueio = _iso(quando + BLOQUEIO) if falhas >= FALHAS_ATE_BLOQUEIO else None
    con.execute("UPDATE central_usuarios SET falhas = ?, bloqueado_ate = ? WHERE id = ?",
                (0 if bloqueio else falhas, bloqueio, u["id"]))
    return None


def papel(con: sqlite3.Connection, papel_id: str) -> sqlite3.Row:
    return con.execute("SELECT * FROM central_papeis WHERE id = ?", (papel_id,)).fetchone()


# ------------------------------------------------------------------ sessões
def _hash_token(token: str) -> str:
    return hashlib.sha256(token.encode()).hexdigest()


def criar_sessao(con: sqlite3.Connection, usuario: sqlite3.Row, ip: str = "") -> tuple[str, str]:
    token, csrf = secrets.token_urlsafe(32), secrets.token_urlsafe(32)
    t = _iso(agora())
    con.execute("INSERT INTO central_sessoes VALUES (?, ?, ?, ?, ?, ?, ?)",
                (_hash_token(token), usuario["id"], usuario["organizacao_id"], csrf, t, t, ip))
    return token, csrf


def sessao(con: sqlite3.Connection, token: str | None, quando: datetime | None = None) -> dict | None:
    if not token:
        return None
    quando = quando or agora()
    s = con.execute(
        "SELECT s.*, u.nome, u.papel FROM central_sessoes s JOIN central_usuarios u ON u.id = s.usuario_id "
        "WHERE s.token_hash = ? AND u.ativo = 1", (_hash_token(token),)).fetchone()
    if s is None:
        return None
    if quando - datetime.fromisoformat(s["ultimo_uso"]) > SESSAO_OCIOSA or quando - datetime.fromisoformat(s["criada"]) > SESSAO_MAXIMA:
        con.execute("DELETE FROM central_sessoes WHERE token_hash = ?", (s["token_hash"],))
        return None
    con.execute("UPDATE central_sessoes SET ultimo_uso = ? WHERE token_hash = ?", (_iso(quando), s["token_hash"]))
    return dict(s)


def encerrar_sessao(con: sqlite3.Connection, token: str) -> None:
    con.execute("DELETE FROM central_sessoes WHERE token_hash = ?", (_hash_token(token),))


# ------------------------------------------------------------------ auditoria
def _hash_auditoria(anterior: str, campos: dict, assinatura: int = 2, chave: bytes | None = None) -> str:
    """assinatura 1: SHA-256 puro (linhas da v1, antes da chave); 2: HMAC-SHA256 com a chave fora do banco."""
    texto = (anterior + json.dumps(campos, ensure_ascii=False, sort_keys=True, separators=(",", ":"))).encode()
    if assinatura == 1:
        return hashlib.sha256(texto).hexdigest()
    return hmac.new(chave or chave_auditoria(), texto, hashlib.sha256).hexdigest()


_CAMPOS_AUDITORIA = ("quando", "organizacao_id", "usuario_id", "origem", "acao", "alvo", "nivel", "resultado")


def auditar(con: sqlite3.Connection, acao: str, *, origem: str = "web", organizacao_id: int | None = None,
            usuario_id: int | None = None, alvo: str = "", nivel: str = "", resultado: str = "") -> None:
    """Grava a linha e a âncora dentro da mesma trava do banco (BEGIN IMMEDIATE): a âncora nunca fica para trás."""
    chave = chave_auditoria()
    con.execute("BEGIN IMMEDIATE")
    try:
        ult = con.execute("SELECT hash FROM central_auditoria ORDER BY id DESC LIMIT 1").fetchone()
        anterior = ult[0] if ult else INICIO_CORRENTE
        campos = {"quando": _iso(agora()), "organizacao_id": organizacao_id, "usuario_id": usuario_id, "origem": origem,
                  "acao": acao, "alvo": alvo[:500], "nivel": nivel, "resultado": resultado[:500]}
        h = _hash_auditoria(anterior, campos, 2, chave)
        cur = con.execute(f"INSERT INTO central_auditoria ({', '.join(_CAMPOS_AUDITORIA)}, hash_anterior, hash, assinatura) "
                          f"VALUES ({', '.join('?' * len(_CAMPOS_AUDITORIA))}, ?, ?, 2)",
                          (*[campos[c] for c in _CAMPOS_AUDITORIA], anterior, h))
        primeiro = con.execute("SELECT MIN(id) FROM central_auditoria WHERE assinatura = 2").fetchone()[0]
        con.execute("INSERT OR IGNORE INTO central_config VALUES ('auditoria_assinada_desde', ?)", (str(primeiro),))
        _gravar_ancora(cur.lastrowid, h, primeiro, chave)
        con.execute("COMMIT")
    except Exception:
        if con.in_transaction:
            con.execute("ROLLBACK")
        raise


def verificar_auditoria(con: sqlite3.Connection) -> tuple[bool, int | None]:
    """Confere a corrente inteira contra a âncora assinada.

    - A âncora (assinada com a chave) diz qual é a última linha e onde começam as linhas assinadas.
    - Linhas da v1 (SHA-256 puro) só valem antes desse ponto; dali em diante, toda linha precisa da chave.
    - Sem âncora válida, só passa uma tabela 100% da v1 sem nenhuma chave criada ainda (o primeiro uso).
    """
    linhas = con.execute("SELECT * FROM central_auditoria ORDER BY id").fetchall()
    chave_existe = (pasta_segredos() / "central-auditoria.key").exists()
    assinada = con.execute("SELECT valor FROM central_config WHERE chave = 'auditoria_assinada_desde'").fetchone()
    if not chave_existe and assinada:
        return False, int(assinada[0])  # já foi assinada e a chave sumiu: alteração
    if not chave_existe:
        anterior = INICIO_CORRENTE
        for linha in linhas:
            campos = {c: linha[c] for c in _CAMPOS_AUDITORIA}
            if linha["assinatura"] != 1 or linha["hash_anterior"] != anterior or linha["hash"] != _hash_auditoria(anterior, campos, 1):
                return False, linha["id"]
            anterior = linha["hash"]
        return True, None
    chave = chave_auditoria()
    ancora = _ler_ancora(chave)
    if ancora is None:
        return False, (linhas[0]["id"] if linhas else 0)  # âncora apagada ou falsificada
    ultimo, h_ultimo, primeiro = ancora
    anterior = INICIO_CORRENTE
    for linha in linhas:
        campos = {c: linha[c] for c in _CAMPOS_AUDITORIA}
        esperada = 2 if linha["id"] >= primeiro else 1
        if (linha["assinatura"] != esperada or linha["hash_anterior"] != anterior
                or linha["hash"] != _hash_auditoria(anterior, campos, esperada, chave)):
            return False, linha["id"]
        anterior = linha["hash"]
    if not linhas or linhas[-1]["id"] != ultimo or anterior != h_ultimo:
        return False, (linhas[-1]["id"] + 1 if linhas else ultimo)
    return True, None


def auditoria_resumo(con: sqlite3.Connection) -> bool:
    """Conferência barata (só a última linha contra a âncora assinada) para telas que abrem o tempo todo."""
    if not (pasta_segredos() / "central-auditoria.key").exists():
        return con.execute("SELECT 1 FROM central_config WHERE chave = 'auditoria_assinada_desde'").fetchone() is None
    ancora = _ler_ancora(chave_auditoria())
    ult = con.execute("SELECT id, hash FROM central_auditoria ORDER BY id DESC LIMIT 1").fetchone()
    return ancora is not None and ult is not None and (ancora[0], ancora[1]) == (ult["id"], ult["hash"])


# ------------------------------------------------------------------ aprovações
def criar_aprovacao(con: sqlite3.Connection, organizacao_id: int, receita: str, args: list[str], pedido_por: int | None,
                    origem: str, validade_min: int, pedido: dict | None = None) -> str:
    """pedido = {campos, opcoes, subcomando}: na hora de aprovar, a allowlist é conferida de novo com ele."""
    id_ = secrets.token_hex(6)
    t = agora()
    con.execute("INSERT INTO central_aprovacoes (id, organizacao_id, receita, args, pedido_por, origem, criado, expira, pedido) "
                "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
                (id_, organizacao_id, receita, json.dumps(args, ensure_ascii=False), pedido_por, origem, _iso(t),
                 _iso(t + timedelta(minutes=validade_min)), json.dumps(pedido or {}, ensure_ascii=False)))
    return id_


def devolver_aprovacao(con: sqlite3.Connection, id_: str) -> None:
    """A execução não começou (fila cheia): a aprovação volta a pendente, para não se perder."""
    con.execute("UPDATE central_aprovacoes SET estado = 'pendente', decidido_por = NULL, decidido_em = NULL "
                "WHERE id = ? AND estado = 'aprovada' AND execucao_id IS NULL", (id_,))


def expirar_aprovacoes(con: sqlite3.Connection) -> int:
    return con.execute("UPDATE central_aprovacoes SET estado = 'expirada' WHERE estado = 'pendente' AND expira < ?",
                       (_iso(agora()),)).rowcount


def decidir_aprovacao(con: sqlite3.Connection, id_: str, organizacao_id: int, usuario_id: int, aprovar: bool) -> sqlite3.Row | None:
    """Uso único: só uma decisão vence, e só dentro da validade. Devolve a aprovação decidida ou None."""
    estado = "aprovada" if aprovar else "recusada"
    cur = con.execute("UPDATE central_aprovacoes SET estado = ?, decidido_por = ?, decidido_em = ? "
                      "WHERE id = ? AND organizacao_id = ? AND estado = 'pendente' AND expira >= ?",
                      (estado, usuario_id, _iso(agora()), id_, organizacao_id, _iso(agora())))
    if cur.rowcount != 1:
        return None
    return con.execute("SELECT * FROM central_aprovacoes WHERE id = ?", (id_,)).fetchone()
