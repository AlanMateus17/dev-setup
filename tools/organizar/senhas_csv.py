#!/usr/bin/env python3
"""Prepara a exportação de senhas do Chrome/Google para importar no KeePassXC. Roda só no seu computador.

    PowerShell do Windows: py $HOME\\dev-setup\\tools\\organizar\\senhas_csv.py "$HOME\\Downloads\\Chrome Passwords.csv"
    Ubuntu do WSL:         python3 tools/organizar/senhas_csv.py ~/Downloads/"Chrome Passwords.csv"

O que faz:
- gera um CSV no formato de importação do KeePassXC (Grupo, Título, Usuário, Senha, URL, Notas), com o título
  limpo (ex.: "github.com") e as contas agrupadas por categoria;
- junta duplicatas exatas (mesmo site, usuário e senha);
- mostra na tela SÓ nomes de sites: quais têm senha repetida em vários sites e quais têm senha curta.
  Nenhuma senha é impressa, enviada ou guardada em outro lugar.

Depois de importar no KeePassXC (Banco de dados > Importar > CSV), apague os DOIS arquivos CSV.
"""
from __future__ import annotations

import argparse
import csv
import os
import sys
import urllib.parse
from collections import defaultdict
from pathlib import Path

# A ordem importa: o primeiro grupo cuja palavra aparece no site ganha (por isso Escola vem antes de Governo).
# Os números deixam os grupos na mesma ordem no KeePassXC: 00 é a corrente de recuperação, que protege todo o resto.
GRUPOS = {
    "00 Essenciais (e-mail e contas-mãe)": ["accounts.google", "myaccount.google", "gmail", "outlook", "hotmail", "live.com",
                                            "microsoft", "apple", "icloud", "proton"],
    "01 Bancos e dinheiro": ["itau", "nubank", "pagbank", "pagseguro", "xp", "mercadopago", "paypal", "tesouro", "inter", "caixa", "bb.com",
                             "santander", "bradesco", "c6bank", "picpay", "binance", "blockchain", "rico", "clear", "btg", "b3.com"],
    "03 Escola (só os seus acessos)": ["educacao.mg", "see.mg", "sisap", "simade", "diario", "moodle", "classroom"],
    "02 Governo": ["gov.br", "receita", "fazenda", "detran", "sefaz", "inss", "esocial", "inpi"],
    "04 Grupo AMtech Digital": ["registro.br", "cloudflare", "hostinger", "business.facebook", "business.whatsapp", "whatsapp", "cal.com",
                                "zoho", "resend", "upwork", "canva"],
    "05 Instituto e Editora": ["hotmart", "kiwify", "eduzz", "udemy", "mailerlite", "amazon.com.br/kdp", "kdp", "clubedeautores", "isbn",
                               "cbl.org"],
    "06 Código e nuvem": ["github", "gitlab", "vercel", "supabase", "azure", "aws", "cloud.google", "docker", "npmjs", "nuget", "oracle",
                          "backblaze", "tailscale", "sonarcloud", "sentry"],
    "07 IA": ["claude", "anthropic", "openai", "chatgpt", "gemini", "perplexity", "huggingface", "cursor", "deepseek", "grok", "x.ai",
              "elevenlabs", "notebooklm"],
    "08 Redes": ["facebook", "instagram", "tiktok", "linkedin", "youtube", "twitter", "x.com", "kwai", "discord", "telegram", "threads"],
    "09 Estudo": ["alura", "rocketseat", "dio.me", "estacio", "roadmap", "tryhackme", "hackthebox", "coursera", "ankiweb", "kaggle", "duolingo"],
    "10 Compras e assinaturas": ["mercadolivre", "shopee", "amazon", "aliexpress", "magazineluiza", "netflix", "spotify", "ifood", "uber"],
}

OUTROS = "11 Outros (revisar)"


def dominio(url: str) -> str:
    h = urllib.parse.urlparse(url if "://" in url else "https://" + url).hostname or url
    return h[4:] if h.startswith("www.") else h


def grupo(dom: str) -> str:
    d = dom.lower()
    for g, chaves in GRUPOS.items():
        if any(c in d for c in chaves):
            return g
    return OUTROS


def ler(caminho: Path) -> list[dict]:
    with caminho.open(encoding="utf-8-sig", newline="") as f:
        linhas = list(csv.DictReader(f))
    out = []
    for r in linhas:
        url = r.get("url") or r.get("URL") or ""
        out.append({"url": url, "usuario": r.get("username") or r.get("Username") or "",
                    "senha": r.get("password") or r.get("Password") or "", "nota": r.get("note") or r.get("Notes") or "",
                    "titulo": dominio(url) if url else (r.get("name") or "sem site")})
    return out


def processar(linhas: list[dict]) -> tuple[list[dict], dict]:
    vistos, unicas = set(), []
    for r in linhas:
        k = (r["titulo"], r["usuario"], r["senha"])
        if k not in vistos:
            vistos.add(k)
            unicas.append(r)
    por_senha = defaultdict(set)
    for r in unicas:
        if r["senha"]:
            por_senha[r["senha"]].add(r["titulo"])
    repetidas = sorted({s for sites in por_senha.values() if len(sites) > 1 for s in sites})
    curtas = sorted({r["titulo"] for r in unicas if 0 < len(r["senha"]) < 12})
    vazias = sorted({r["titulo"] for r in unicas if not r["senha"]})
    return unicas, {"duplicatas_removidas": len(linhas) - len(unicas), "repetidas": repetidas, "curtas": curtas, "vazias": vazias}


def nota_com_alerta(r: dict, rel: dict) -> str:
    """Marca na nota o que precisa de troca, para achar no KeePassXC buscando TROCAR."""
    alertas = []
    if r["titulo"] in rel["repetidas"]:
        alertas.append("TROCAR: senha repetida em outro site")
    if r["titulo"] in rel["curtas"]:
        alertas.append("TROCAR: senha curta")
    return "\n".join(alertas + ([r["nota"]] if r["nota"] else []))


def escrever(unicas: list[dict], saida: Path, rel: dict | None = None) -> None:
    rel = rel or {"repetidas": [], "curtas": []}
    fd = os.open(saida, os.O_WRONLY | os.O_CREAT | os.O_TRUNC, 0o600)
    with os.fdopen(fd, "w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(["Group", "Title", "Username", "Password", "URL", "Notes"])
        for r in sorted(unicas, key=lambda r: (grupo(r["titulo"]), r["titulo"])):
            w.writerow([grupo(r["titulo"]), r["titulo"], r["usuario"], r["senha"], r["url"], nota_com_alerta(r, rel)])


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("csv")
    ap.add_argument("--saida")
    a = ap.parse_args()
    ent = Path(a.csv).expanduser()
    if not ent.exists():
        print(f"Arquivo não encontrado: {ent}", file=sys.stderr)
        return 1
    unicas, rel = processar(ler(ent))
    saida = Path(a.saida).expanduser() if a.saida else ent.with_name("keepassxc-importar.csv")
    escrever(unicas, saida, rel)
    print(f"{len(unicas)} contas prontas em {saida} ({rel['duplicatas_removidas']} duplicatas juntadas).")
    print(f"Senha repetida em vários sites ({len(rel['repetidas'])}): troque primeiro, começando por bancos e e-mail.")
    for s in rel["repetidas"]:
        print("  -", s)
    print(f"Senha com menos de 12 caracteres ({len(rel['curtas'])}):")
    for s in rel["curtas"]:
        print("  -", s)
    print(f"\nSem grupo conhecido: {sum(1 for r in unicas if grupo(r['titulo']) == OUTROS)} conta(s) em '{OUTROS}'.")
    print("No KeePassXC, busque TROCAR para ver as que precisam de senha nova.")
    print("\nPróximo: KeePassXC > Banco de dados > Importar > CSV. Depois APAGUE os dois arquivos CSV (Shift+Delete).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
