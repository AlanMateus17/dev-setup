#!/usr/bin/env python3
"""Fontes de estudo: o conteúdo original (documentação oficial, livros, aulas) num acervo PRIVADO, fora do Git.

Tudo fica em ~/AMtech/estudo (ou AMTECH_ESTUDO). Nada daqui vai para repositório: o `conferir` roda no just check e
falha se algum arquivo de fonte aparecer no dev-setup. Separado da pasta ~/AMtech/entrada, que é do pipeline de conteúdo.

    python3 tools/fontes/fontes.py docs                       # as documentações oficiais cadastradas (data/fontes.json)
    python3 tools/fontes/fontes.py baixar typescript-handbook # clona só a pasta da documentação, na versão cadastrada
    python3 tools/fontes/fontes.py entrada                    # processa ~/AMtech/estudo/entrada: guarda, registra e converte
    python3 tools/fontes/fontes.py buscar "complemento de dois"   # procura nas fontes convertidas e nas documentações
    python3 tools/fontes/fontes.py citar ARQUIVO "trecho literal" # confere, letra por letra, se o trecho existe na fonte
    python3 tools/fontes/fontes.py conferir                   # (just check) nenhum arquivo de fonte dentro do repositório

A regra que impede alucinação: o guia de estudo só mostra trechos que o `citar` encontrou na fonte. A IA pode sugerir
qual trecho explica um termo, mas não consegue inventar um trecho, porque o código recusa o que não existe no arquivo.

Conversão (cada ferramenta é opcional; sem ela o arquivo fica guardado como "pendente" e nada se perde):
PDF/DOCX/PPTX → docling · EPUB/HTML/ODT → pandoc · áudio/vídeo → whisperx ou whisper-ctranslate2 · MD/TXT → cópia.
PDF de fora passa antes pelo dangerzone-cli (sanitiza numa caixa sem rede), quando ele estiver instalado.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import unicodedata
from datetime import datetime
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]
CATALOGO = RAIZ / "data" / "fontes.json"
TIPOS = {
    "pdf": {".pdf"},
    "documento": {".docx", ".pptx", ".odt", ".epub", ".html", ".htm"},
    "audio-video": {".mp3", ".m4a", ".wav", ".ogg", ".mp4", ".mkv", ".webm"},
    "texto": {".md", ".txt"},
}
# O que nunca pode estar dentro do repositório (conferido no just check)
PROIBIDO_PASTAS = re.compile(r"(^|/)(corpus|docs-oficiais|fontes-originais|AMtech)(/|$)")
PROIBIDO_EXT = {".epub", ".mobi", ".azw3", ".djvu"}
PDF_PERMITIDOS = re.compile(r"^(docs/|os/|infra/templates/)")  # PDFs gerados pelo próprio setup


def base() -> Path:
    return Path(os.environ.get("AMTECH_ESTUDO") or Path.home() / "AMtech" / "estudo")


def pastas() -> dict[str, Path]:
    b = base()
    return {"entrada": b / "entrada", "fontes": b / "fontes", "corpus": b / "corpus",
            "docs": b / "docs-oficiais", "manifesto": b / "manifesto.jsonl"}


def catalogo() -> list[dict]:
    return json.loads(CATALOGO.read_text(encoding="utf-8"))["documentacoes"]


def sha256(p: Path) -> str:
    h = hashlib.sha256()
    with p.open("rb") as f:
        for bloco in iter(lambda: f.read(1 << 20), b""):
            h.update(bloco)
    return h.hexdigest()


def tipo_de(p: Path) -> str | None:
    ext = p.suffix.lower()
    return next((t for t, exts in TIPOS.items() if ext in exts), None)


def registrar(registro: dict) -> None:
    m = pastas()["manifesto"]
    m.parent.mkdir(parents=True, exist_ok=True)
    with m.open("a", encoding="utf-8") as f:
        f.write(json.dumps(registro, ensure_ascii=False) + "\n")


def manifesto() -> list[dict]:
    m = pastas()["manifesto"]
    if not m.exists():
        return []
    return [json.loads(ln) for ln in m.read_text(encoding="utf-8").splitlines() if ln.strip()]


def tem(cmd: str) -> bool:
    return shutil.which(cmd) is not None


# ---------- documentações oficiais (Git, versão cadastrada) ----------

def baixar(doc: dict, destino_base: Path | None = None) -> dict:
    destino_base = destino_base or pastas()["docs"]
    alvo = destino_base / f"{doc['id']}@{doc['ref']}"
    if not alvo.exists():
        alvo.parent.mkdir(parents=True, exist_ok=True)
        subprocess.run(["git", "clone", "-q", "--depth", "1", "--branch", doc["ref"], "--filter=blob:none", "--sparse",
                        doc["repo"], str(alvo)], check=True)
        subprocess.run(["git", "-C", str(alvo), "sparse-checkout", "set", *doc["caminhos"]], check=True)
    commit = subprocess.run(["git", "-C", str(alvo), "rev-parse", "HEAD"], capture_output=True, text=True,
                            check=True).stdout.strip()
    reg = {"quando": datetime.now().isoformat(timespec="seconds"), "evento": "doc", "id": doc["id"], "ref": doc["ref"],
           "commit": commit, "repo": doc["repo"], "licenca": doc["licenca"], "pasta": str(alvo)}
    registrar(reg)
    return reg


# ---------- porta de entrada (livros, faculdade, aulas) ----------

def converter(origem: Path, saida: Path, tipo: str) -> str:
    """Converte para Markdown com a ferramenta disponível. Devolve o estado: convertido, pendente ou copiado."""
    saida.parent.mkdir(parents=True, exist_ok=True)
    if tipo == "texto":
        shutil.copyfile(origem, saida)
        return "copiado"
    if tipo in ("pdf", "documento") and origem.suffix.lower() in {".pdf", ".docx", ".pptx"} and tem("docling"):
        tmp = saida.parent / f".docling-{saida.stem}"
        subprocess.run(["docling", str(origem), "--to", "md", "--output", str(tmp)], check=True,
                       capture_output=True, text=True)
        gerado = next(tmp.glob("*.md"), None)
        if gerado:
            shutil.move(str(gerado), saida)
            shutil.rmtree(tmp, ignore_errors=True)
            return "convertido"
    if tipo == "documento" and tem("pandoc"):
        subprocess.run(["pandoc", str(origem), "-t", "gfm", "-o", str(saida)], check=True)
        return "convertido"
    if tipo == "audio-video":
        for cmd in ("whisperx", "whisper-ctranslate2"):
            if tem(cmd):
                tmp = saida.parent / f".whisper-{saida.stem}"
                tmp.mkdir(exist_ok=True)
                subprocess.run([cmd, str(origem), "--language", "pt", "--output_format", "srt", "--output_dir", str(tmp)],
                               check=True, capture_output=True, text=True)
                srt = next(tmp.glob("*.srt"), None)
                if srt:
                    saida.write_text(srt_para_md(srt.read_text(encoding="utf-8")), encoding="utf-8")
                    shutil.rmtree(tmp, ignore_errors=True)
                    return "convertido"
    return "pendente"


def srt_para_md(srt: str) -> str:
    """Legenda SRT → Markdown com o minuto de cada fala, para citar [t=mm:ss]."""
    linhas, tempo = [], None
    for ln in srt.splitlines():
        m = re.match(r"(\d\d):(\d\d):(\d\d)[,.]\d+ -->", ln)
        if m:
            h, mi, s = map(int, m.groups())
            tempo = f"{h * 60 + mi:02d}:{s:02d}"
        elif ln.strip() and not ln.strip().isdigit() and tempo:
            linhas.append(f"[t={tempo}] {ln.strip()}")
    return "\n".join(linhas) + "\n"


def processar_entrada(licenca: str = "desconhecida") -> list[dict]:
    p = pastas()
    p["entrada"].mkdir(parents=True, exist_ok=True)
    feitos = []
    vistos = {r["sha256"] for r in manifesto() if r.get("evento") == "fonte"}
    for arq in sorted(x for x in p["entrada"].rglob("*") if x.is_file() and not x.name.startswith(".")):
        tipo = tipo_de(arq)
        if not tipo:
            print(f"ignorado (tipo desconhecido): {arq.name}")
            continue
        h = sha256(arq)
        if h in vistos:
            print(f"já registrado (mesmo conteúdo): {arq.name}")
            arq.unlink()
            continue
        fid = f"{re.sub(r'[^a-z0-9]+', '-', unicodedata.normalize('NFKD', arq.stem).encode('ascii', 'ignore').decode().lower()).strip('-')}-{h[:8]}"
        destino = p["fontes"] / tipo / f"{fid}{arq.suffix.lower()}"
        destino.parent.mkdir(parents=True, exist_ok=True)
        sanitizado = False
        if tipo == "pdf" and tem("dangerzone-cli"):
            limpo = destino.with_name(destino.stem + "-safe.pdf")
            subprocess.run(["dangerzone-cli", str(arq), "--output-filename", str(limpo)], check=True)
            shutil.move(str(arq), destino)
            destino, sanitizado = limpo, True
        else:
            shutil.move(str(arq), destino)
        estado = converter(destino, p["corpus"] / f"{fid}.md", tipo)
        reg = {"quando": datetime.now().isoformat(timespec="seconds"), "evento": "fonte", "id": fid, "nome": arq.name,
               "tipo": tipo, "sha256": h, "sanitizado": sanitizado, "conversao": estado, "licenca": licenca,
               "original": str(destino)}
        registrar(reg)
        vistos.add(h)
        feitos.append(reg)
        aviso = "" if sanitizado or tipo != "pdf" else " (sem dangerzone: só abra PDF de fonte confiável)"
        print(f"{fid}: {estado}{aviso}")
    return feitos


# ---------- busca e citação literal ----------

def normalizar(t: str) -> str:
    t = unicodedata.normalize("NFC", t).replace("­", "")
    t = re.sub(r"-\n(\w)", r"\1", t)  # palavra quebrada no fim da linha
    return re.sub(r"\s+", " ", t).strip()


def citar(arquivo: Path, trecho: str) -> dict | None:
    """Confere se o trecho existe LITERALMENTE no arquivo (só espaços e quebras de linha são ignorados).
    Devolve a linha onde começa e o minuto mais próximo, se for transcrição; None se não existir."""
    texto = arquivo.read_text(encoding="utf-8", errors="replace")
    alvo = normalizar(trecho)
    if not alvo:
        return None
    plano = normalizar(texto)
    pos = plano.find(alvo)
    if pos < 0:
        return None
    # localiza a linha original: percorre as linhas acumulando o texto normalizado
    acumulado, linha_ini = "", 1
    for i, ln in enumerate(texto.splitlines(), 1):
        prox = normalizar(acumulado + " " + ln) if acumulado else normalizar(ln)
        if len(prox) > pos:
            linha_ini = i
            break
        acumulado = prox
    tempos = re.findall(r"\[t=(\d+:\d\d)\]", "\n".join(texto.splitlines()[:linha_ini]))
    return {"arquivo": str(arquivo), "linha": linha_ini, "t": tempos[-1] if tempos else None}


def buscar(termo: str) -> list[str]:
    p = pastas()
    alvos = [str(x) for x in (p["corpus"], p["docs"]) if x.exists()]
    if not alvos:
        return []
    if tem("rg"):
        r = subprocess.run(["rg", "-n", "-i", "--max-count", "3", "-g", "*.md", "-g", "*.mdx", "-g", "*.rst", termo, *alvos],
                           capture_output=True, text=True)
        return r.stdout.splitlines()
    achados = []
    for pasta in alvos:
        for arq in Path(pasta).rglob("*"):
            if arq.suffix in {".md", ".mdx", ".rst"} and arq.is_file():
                for i, ln in enumerate(arq.read_text(encoding="utf-8", errors="ignore").splitlines(), 1):
                    if termo.lower() in ln.lower():
                        achados.append(f"{arq}:{i}:{ln.strip()}")
    return achados


# ---------- barreira do repositório ----------

def conferir_repo(raiz: Path = RAIZ) -> list[str]:
    arquivos = subprocess.run(["git", "-C", str(raiz), "ls-files"], capture_output=True, text=True, check=True).stdout.split()
    erros = []
    for f in arquivos:
        if PROIBIDO_PASTAS.search(f):
            erros.append(f"{f}: pasta de fontes de estudo não entra no repositório (fica em ~/AMtech/estudo)")
        elif Path(f).suffix.lower() in PROIBIDO_EXT:
            erros.append(f"{f}: livro digital não entra no repositório")
        elif Path(f).suffix.lower() == ".pdf" and not PDF_PERMITIDOS.match(f):
            erros.append(f"{f}: PDF fora das pastas de documentos gerados pelo setup")
    return erros


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    s = ap.add_subparsers(dest="cmd", required=True)
    s.add_parser("docs")
    b = s.add_parser("baixar"); b.add_argument("id", nargs="?", help="sem id: todas")
    e = s.add_parser("entrada"); e.add_argument("--licenca", default="desconhecida",
                                                help="ex.: comprado-uso-pessoal, cc-by, faculdade-uso-pessoal")
    q = s.add_parser("buscar"); q.add_argument("termo")
    c = s.add_parser("citar"); c.add_argument("arquivo", type=Path); c.add_argument("trecho")
    s.add_parser("conferir")
    args = ap.parse_args(argv)
    if args.cmd == "docs":
        baixados = {r["id"]: r for r in manifesto() if r.get("evento") == "doc"}
        for d in catalogo():
            situ = f"baixada ({baixados[d['id']]['commit'][:7]})" if d["id"] in baixados else "não baixada"
            print(f"{d['id']:<22} {d['titulo']}  ·  {d['ref']}  ·  {d['licenca']}  ·  mapa {', '.join(d['assuntos'])}  ·  {situ}")
    elif args.cmd == "baixar":
        docs = [d for d in catalogo() if not args.id or d["id"] == args.id]
        if not docs:
            print(f"documentação {args.id} não está em data/fontes.json", file=sys.stderr)
            return 2
        for d in docs:
            r = baixar(d)
            print(f"{d['id']}: {r['pasta']} (commit {r['commit'][:7]})")
    elif args.cmd == "entrada":
        feitos = processar_entrada(args.licenca)
        print(f"{len(feitos)} fonte(s) nova(s). Converta as pendentes instalando a ferramenta e rode de novo."
              if feitos else f"Nada novo em {pastas()['entrada']}.")
    elif args.cmd == "buscar":
        achados = buscar(args.termo)
        print("\n".join(achados) if achados else "Nada encontrado (ou ainda não há fontes: rode baixar/entrada).")
    elif args.cmd == "citar":
        r = citar(args.arquivo, args.trecho)
        if not r:
            print("RECUSADO: o trecho não existe literalmente nesse arquivo.", file=sys.stderr)
            return 1
        print(f"OK: {r['arquivo']}, linha {r['linha']}" + (f", t={r['t']}" if r["t"] else ""))
    elif args.cmd == "conferir":
        erros = conferir_repo()
        for x in erros:
            print("ERRO:", x, file=sys.stderr)
        print("Nenhuma fonte de estudo dentro do repositório." if not erros else f"{len(erros)} problema(s).")
        return 1 if erros else 0
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
