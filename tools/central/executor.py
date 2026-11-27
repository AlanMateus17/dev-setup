"""Executor da Central: roda uma receita do just como lista de argumentos, sem shell, com ambiente mínimo e tempo limite.

A saída fica num buffer em memória (para a tela ao vivo) e vai para central_execucoes no fim, cortada.
Segredos do processo da Central (token do Telegram, chaves de API, GH_TOKEN) não passam para a receita.
"""
from __future__ import annotations

import json
import os
import re
import secrets
import subprocess
import sys
import threading
import time
from dataclasses import dataclass, field
from pathlib import Path

import banco

ANSI = re.compile(r"\x1b\[[0-9;?]*[A-Za-z]")
SAIDA_MAX = 20_000
# Só o que as receitas precisam para funcionar no WSL; nada de token, chave ou senha.
AMBIENTE_PERMITIDO = ("PATH", "HOME", "USER", "LOGNAME", "LANG", "LC_ALL", "TZ", "SHELL",
                      "XDG_RUNTIME_DIR", "DBUS_SESSION_BUS_ADDRESS", "WSL_DISTRO_NAME", "WSL_INTEROP", "WSLENV",
                      "NUCLEO_DB", "FILA_DIR", "AMTECH_DEV", "DOCKER_HOST")


def ambiente_minimo(origem: dict[str, str] | None = None) -> dict[str, str]:
    origem = os.environ if origem is None else origem
    amb = {k: origem[k] for k in AMBIENTE_PERMITIDO if k in origem}
    amb.update({"TERM": "dumb", "NO_COLOR": "1", "AMTECH_CENTRAL": "1"})
    amb.setdefault("PATH", "/usr/local/bin:/usr/bin:/bin")
    return amb


@dataclass
class Execucao:
    id: str
    receita: str
    linhas: list[str] = field(default_factory=list)
    fim: bool = False
    codigo: int | None = None


class Executor:
    def __init__(self, raiz: Path, caminho_banco: Path, comando_just: list[str] | None = None,
                 max_simultaneas: int = 4, avisar=None):
        self.raiz = raiz
        self.caminho_banco = caminho_banco
        self.comando_just = comando_just or ["just"]
        self.max_simultaneas = max_simultaneas
        self.avisar = avisar  # função(texto) para o nível "avisa"; None desliga
        self._trava = threading.Lock()
        self._vivas: dict[str, Execucao] = {}

    def em_andamento(self) -> int:
        with self._trava:
            return sum(1 for e in self._vivas.values() if not e.fim)

    def iniciar(self, receita: str, args: list[str], *, nivel: str, organizacao_id: int, usuario_id: int | None,
                origem: str, timeout: int = 900, python: str | None = None) -> str:
        with self._trava:
            ativas = [e for e in self._vivas.values() if not e.fim]
            if len(ativas) >= self.max_simultaneas:
                raise RuntimeError(f"já há {len(ativas)} receitas rodando; espere uma terminar")
            if any(e.receita == receita for e in ativas):
                raise RuntimeError(f"'{receita}' já está rodando")
            ex = Execucao(secrets.token_urlsafe(9), receita)
            self._vivas[ex.id] = ex
            # guarda só as últimas 50 execuções em memória
            for velho in [k for k, v in self._vivas.items() if v.fim][:-50]:
                del self._vivas[velho]
        con = banco.abrir(self.caminho_banco)
        try:
            con.execute("INSERT INTO central_execucoes (id, organizacao_id, usuario_id, receita, args, nivel, origem, inicio) "
                        "VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                        (ex.id, organizacao_id, usuario_id, receita, json.dumps(args, ensure_ascii=False), nivel, origem,
                         banco._iso(banco.agora())))
            banco.auditar(con, "receita.inicio", origem=origem, organizacao_id=organizacao_id, usuario_id=usuario_id,
                          alvo=f"{receita} {json.dumps(args, ensure_ascii=False)}", nivel=nivel)
        finally:
            con.close()
        alvo = self._rodar_python if python else self._rodar_just
        threading.Thread(target=alvo, args=(ex, args, timeout, python, nivel, organizacao_id, usuario_id, origem),
                         daemon=True).start()
        return ex.id

    def _rodar_just(self, ex: Execucao, args, timeout, _python, nivel, org, usuario, origem) -> None:
        cmd = [*self.comando_just, "--justfile", str(self.raiz / "justfile"), "--working-directory", str(self.raiz),
               ex.receita, *args]
        inicio = time.monotonic()
        try:
            proc = subprocess.Popen(cmd, cwd=self.raiz, env=ambiente_minimo(), stdin=subprocess.DEVNULL,
                                    stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, errors="replace",
                                    bufsize=1, shell=False, start_new_session=True)
        except OSError as e:
            ex.linhas.append(f"Não consegui rodar o just: {e}")
            self._terminar(ex, 127, nivel, org, usuario, origem)
            return
        relogio = threading.Timer(timeout, self._matar, args=(proc, ex, timeout))
        relogio.start()
        try:
            for linha in proc.stdout:
                ex.linhas.append(ANSI.sub("", linha.rstrip("\n")))
            codigo = proc.wait()
        finally:
            relogio.cancel()
            proc.stdout.close()
        ex.linhas.append(f"— terminou em {time.monotonic() - inicio:.1f} s, código {codigo}")
        self._terminar(ex, codigo, nivel, org, usuario, origem)

    def _rodar_python(self, ex: Execucao, args, _timeout, python, nivel, org, usuario, origem) -> None:
        codigo = 0
        try:
            if python == "fila.adicionar":
                sys.path.insert(0, str(self.raiz / "tools" / "remoto"))
                import fila  # noqa: PLC0415
                item = fila.adicionar(args[0])
                ex.linhas.append(f"Na fila: {item['id']} ({item['repo']}). O resultado volta como PR em rascunho.")
            else:
                raise RuntimeError(f"ação Python desconhecida: {python}")
        except Exception as e:  # noqa: BLE001
            ex.linhas.append(f"Falhou: {e}")
            codigo = 1
        self._terminar(ex, codigo, nivel, org, usuario, origem)

    @staticmethod
    def _matar(proc: subprocess.Popen, ex: Execucao, timeout: int) -> None:
        ex.linhas.append(f"— tempo esgotado ({timeout} s): parando")
        try:
            os.killpg(proc.pid, 15)
        except OSError:
            proc.kill()

    def _terminar(self, ex: Execucao, codigo: int, nivel, org, usuario, origem) -> None:
        saida = "\n".join(ex.linhas)
        if len(saida) > SAIDA_MAX:
            saida = saida[:SAIDA_MAX // 2] + "\n… (cortado) …\n" + saida[-SAIDA_MAX // 2:]
        con = banco.abrir(self.caminho_banco)
        try:
            con.execute("UPDATE central_execucoes SET fim = ?, codigo = ?, saida = ? WHERE id = ?",
                        (banco._iso(banco.agora()), codigo, saida, ex.id))
            banco.auditar(con, "receita.fim", origem=origem, organizacao_id=org, usuario_id=usuario,
                          alvo=ex.receita, nivel=nivel, resultado=f"código {codigo}")
        finally:
            con.close()
        ex.codigo, ex.fim = codigo, True
        if self.avisar and (nivel == "avisa" or codigo != 0):
            try:
                self.avisar(f"Central: {ex.receita} {'ok' if codigo == 0 else f'FALHOU (código {codigo})'}")
            except Exception:  # noqa: BLE001  aviso nunca derruba a execução
                pass

    def ler(self, id_: str, desde: int) -> tuple[list[str], bool, int | None] | None:
        ex = self._vivas.get(id_)
        if ex is None:
            return None
        return ex.linhas[desde:], ex.fim, ex.codigo


def avisar_telegram(raiz: Path):
    """Usa o bot que já existe (tools/remoto/bot.py --avisar). Sem telegram.env, não faz nada."""
    def _avisar(texto: str) -> None:
        if not (Path.home() / ".config" / "amtech" / "telegram.env").exists():
            return
        subprocess.run([sys.executable, str(raiz / "tools" / "remoto" / "bot.py"), "--avisar", texto[:500]],
                       timeout=30, capture_output=True, check=False)
    return _avisar
