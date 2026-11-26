#!/usr/bin/env bash
# Grava no Windows (variável de usuário) o OLLAMA_HOST do Ollama do Windows: só 127.0.0.1, na porta de data/portas.json
# (id ollama-windows, 11435). A 11434 fica para o Ollama do WSL, que o wslrelay publica no Windows (ADR 0022).
# Seguro para rodar várias vezes: se já estiver certo, não muda nada. Não precisa de administrador.
#   bash scripts/wsl/ollama-windows.sh --simular   # mostra o valor atual e o que gravaria
#   bash scripts/wsl/ollama-windows.sh             # grava (vale na próxima vez que o Ollama do Windows abrir)
set -euo pipefail
RAIZ="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
SIMULAR=0
for a in "$@"; do
  case "$a" in
    --simular) SIMULAR=1 ;;
    -h|--help) sed -n '2,6p' "$0"; exit 0 ;;
    *) echo "Opção desconhecida: $a" >&2; exit 64 ;;
  esac
done
command -v powershell.exe >/dev/null 2>&1 || { echo "Sem powershell.exe: rode no Ubuntu do WSL, com o Windows."; exit 1; }

DESEJADO="$(python3 "$RAIZ/tools/ferramentas/ferramentas.py" --ollama-windows-host)"
ATUAL="$(powershell.exe -NoProfile -Command "[Environment]::GetEnvironmentVariable('OLLAMA_HOST','User')" | tr -d '\r')"
echo "OLLAMA_HOST do usuário no Windows: ${ATUAL:-(vazio)}; o certo é $DESEJADO."
if [[ "$ATUAL" == "$DESEJADO" ]]; then echo "Já está certo."; exit 0; fi
if [[ $SIMULAR -eq 1 ]]; then echo "Simulação: gravaria OLLAMA_HOST=$DESEJADO. Rode sem --simular."; exit 0; fi
powershell.exe -NoProfile -Command "[Environment]::SetEnvironmentVariable('OLLAMA_HOST','$DESEJADO','User')" >/dev/null
ATUAL="$(powershell.exe -NoProfile -Command "[Environment]::GetEnvironmentVariable('OLLAMA_HOST','User')" | tr -d '\r')"
[[ "$ATUAL" == "$DESEJADO" ]] || { echo "ERRO: o Windows não gravou (ficou: ${ATUAL:-vazio})."; exit 1; }
echo "Gravado. Se o Ollama do Windows estiver aberto, feche e abra de novo para valer."
