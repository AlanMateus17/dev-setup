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
]


def caminho_padrao() -> Path:
    return Path(os.environ.get("NUCLEO_DB") or Path.home() / ".local" / "share" / "nucleo" / "nucleo.db")


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
def _hash_auditoria(anterior: str, campos: dict) -> str:
    texto = anterior + json.dumps(campos, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(texto.encode()).hexdigest()


_CAMPOS_AUDITORIA = ("quando", "organizacao_id", "usuario_id", "origem", "acao", "alvo", "nivel", "resultado")


def auditar(con: sqlite3.Connection, acao: str, *, origem: str = "web", organizacao_id: int | None = None,
            usuario_id: int | None = None, alvo: str = "", nivel: str = "", resultado: str = "") -> None:
    con.execute("BEGIN IMMEDIATE")
    try:
        ult = con.execute("SELECT hash FROM central_auditoria ORDER BY id DESC LIMIT 1").fetchone()
        anterior = ult[0] if ult else INICIO_CORRENTE
        campos = {"quando": _iso(agora()), "organizacao_id": organizacao_id, "usuario_id": usuario_id, "origem": origem,
                  "acao": acao, "alvo": alvo[:500], "nivel": nivel, "resultado": resultado[:500]}
        con.execute(f"INSERT INTO central_auditoria ({', '.join(_CAMPOS_AUDITORIA)}, hash_anterior, hash) "
                    f"VALUES ({', '.join('?' * len(_CAMPOS_AUDITORIA))}, ?, ?)",
                    (*[campos[c] for c in _CAMPOS_AUDITORIA], anterior, _hash_auditoria(anterior, campos)))
        con.execute("COMMIT")
    except Exception:
        con.execute("ROLLBACK")
        raise


def verificar_auditoria(con: sqlite3.Connection) -> tuple[bool, int | None]:
    anterior = INICIO_CORRENTE
    for linha in con.execute("SELECT * FROM central_auditoria ORDER BY id"):
        campos = {c: linha[c] for c in _CAMPOS_AUDITORIA}
        if linha["hash_anterior"] != anterior or linha["hash"] != _hash_auditoria(anterior, campos):
            return False, linha["id"]
        anterior = linha["hash"]
    return True, None


# ------------------------------------------------------------------ aprovações
def criar_aprovacao(con: sqlite3.Connection, organizacao_id: int, receita: str, args: list[str], pedido_por: int | None,
                    origem: str, validade_min: int) -> str:
    id_ = secrets.token_hex(6)
    t = agora()
    con.execute("INSERT INTO central_aprovacoes (id, organizacao_id, receita, args, pedido_por, origem, criado, expira) "
                "VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                (id_, organizacao_id, receita, json.dumps(args, ensure_ascii=False), pedido_por, origem, _iso(t),
                 _iso(t + timedelta(minutes=validade_min))))
    return id_


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
