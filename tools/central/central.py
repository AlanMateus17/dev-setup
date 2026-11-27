#!/usr/bin/env python3
"""Central AMtech (ADR 0023): uma tela para rodar e aprovar o que está em data/central.json.

Pelo just (ele instala as dependências fixas num ambiente isolado com o uv):
    just central-usuario alan        # cria o usuário (ou troca a senha); pede a senha aqui
    just central                     # sobe em http://127.0.0.1:8700 (só nesta máquina)

Direto (precisa de fastapi e uvicorn):
    python tools/central/central.py servir [--porta 8700]
    python tools/central/central.py usuario NOME [--papel dono|leitor]
    python tools/central/central.py verificar     # confere a corrente da auditoria
    python tools/central/central.py check         # allowlist (o mesmo do just check)

Acesso pelo celular (fase seguinte): Tailscale no Windows com `tailscale serve`, e o nome da máquina em
AMTECH_CENTRAL_HOSTS (ex.: notebook.tailnet.ts.net). A Central nunca escuta fora do 127.0.0.1.
"""
from __future__ import annotations

import argparse
import getpass
import os
import sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI))

import allowlist  # noqa: E402
import banco  # noqa: E402

RAIZ = AQUI.parents[1]


def servir(porta: int) -> int:
    erros = allowlist.checar(RAIZ)
    if erros:
        for err in erros:
            print(f"ERRO: {err}", file=sys.stderr)
        print("A Central não sobe com a allowlist inválida.", file=sys.stderr)
        return 1
    import uvicorn  # noqa: PLC0415

    from executor import Executor, avisar_telegram  # noqa: PLC0415
    from web import criar_app  # noqa: PLC0415

    caminho = banco.caminho_padrao()
    banco.migrar(caminho)
    con = banco.abrir(caminho)
    try:
        sem_usuario = con.execute("SELECT COUNT(*) FROM central_usuarios WHERE ativo = 1").fetchone()[0] == 0
    finally:
        con.close()
    if sem_usuario:
        print("Ainda não há usuário. Rode antes: just central-usuario alan", file=sys.stderr)
        return 1
    hosts = {h.strip().lower() for h in os.environ.get("AMTECH_CENTRAL_HOSTS", "").split(",") if h.strip()}
    app = criar_app(RAIZ, caminho, hosts, Executor(RAIZ, caminho, avisar=avisar_telegram(RAIZ)))
    print(f"Central AMtech em http://127.0.0.1:{porta}  (Ctrl+C para parar)  · banco: {caminho}")
    uvicorn.run(app, host="127.0.0.1", port=porta, log_level="warning", proxy_headers=False, server_header=False)
    return 0


def usuario(nome: str, papel: str) -> int:
    caminho = banco.caminho_padrao()
    banco.migrar(caminho)
    senha = getpass.getpass(f"Senha para {nome} (mínimo {banco.SENHA_MINIMA} caracteres): ")
    if senha != getpass.getpass("Repita a senha: "):
        print("As senhas não batem. Nada mudou.", file=sys.stderr)
        return 1
    con = banco.abrir(caminho)
    try:
        uid = banco.salvar_usuario(con, nome, senha, papel)
        banco.auditar(con, "usuario.salvo", origem="terminal", organizacao_id=banco.org_padrao(con), usuario_id=uid,
                      alvo=nome, resultado=papel)
    except ValueError as err:
        print(err, file=sys.stderr)
        return 1
    finally:
        con.close()
    marca = Path.home() / ".config" / "amtech"
    marca.mkdir(parents=True, exist_ok=True, mode=0o700)
    (marca / "central-usuario").touch()  # o just ligar passa a manter a Central no ar (amtech-central)
    print(f"Usuário '{nome}' pronto ({papel}). Guarde a senha no KeePassXC.")
    print("Agora: just ligar (deixa a Central sempre no ar) ou just central (só enquanto o terminal estiver aberto).")
    return 0


def verificar() -> int:
    caminho = banco.caminho_padrao()
    banco.migrar(caminho)
    con = banco.abrir(caminho)
    try:
        ok, linha = banco.verificar_auditoria(con)
    finally:
        con.close()
    print("Auditoria da Central íntegra." if ok else f"Auditoria ALTERADA a partir da linha {linha}.")
    return 0 if ok else 1


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="Central AMtech")
    sub = ap.add_subparsers(dest="cmd", required=True)
    s = sub.add_parser("servir")
    s.add_argument("--porta", type=int, default=8700)
    u = sub.add_parser("usuario")
    u.add_argument("nome")
    u.add_argument("--papel", choices=("dono", "leitor"), default="dono")
    sub.add_parser("verificar")
    sub.add_parser("check")
    a = ap.parse_args(argv)
    if a.cmd == "servir":
        return servir(a.porta)
    if a.cmd == "usuario":
        return usuario(a.nome, a.papel)
    if a.cmd == "verificar":
        return verificar()
    return allowlist.main(["--check"])


if __name__ == "__main__":
    sys.exit(main())
