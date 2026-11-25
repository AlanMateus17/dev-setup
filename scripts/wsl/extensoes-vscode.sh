#!/usr/bin/env bash
# Instala no VS Code do Ubuntu (WSL) as extensões marcadas com "wsl": true em data/ferramentas.json.
# Seguro para rodar várias vezes: o que já está instalado é pulado. Na primeira vez, o próprio `code` instala o servidor
# do VS Code no Ubuntu (~/.vscode-server), sem abrir janela.
#   bash scripts/wsl/extensoes-vscode.sh --simular   # mostra o que faria
#   bash scripts/wsl/extensoes-vscode.sh             # instala o que falta (o mesmo que: just extensoes-wsl)
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

if ! command -v code >/dev/null 2>&1; then
  echo "O comando 'code' não está no PATH do Ubuntu. Instale o VS Code no Windows (winget install --id Microsoft.VisualStudioCode -e)"
  echo "e abra o Ubuntu de novo; o 'code' do Windows passa a valer dentro do WSL."
  exit 1
fi

# Fonte única: o registro diz quais extensões vão para o Ubuntu; o arquivo do servidor diz quais já estão lá.
mapfile -t FALTAM < <(python3 - "$RAIZ" <<'EOF'
import sys
sys.path.insert(0, f"{sys.argv[1]}/tools/ferramentas")
import ferramentas as f
dados = f.carregar()
instaladas = f.extensoes_wsl()
for x in dados["ferramentas"]:
    if x["tipo"] == "vscode" and x.get("wsl") and x["decisao"] == "normal" and x["conferir"]["extensao"] not in instaladas:
        print(x["nome"])
EOF
)

if [[ ${#FALTAM[@]} -eq 0 ]]; then
  echo "Extensões do VS Code no Ubuntu: todas instaladas."
  exit 0
fi
echo "Faltam ${#FALTAM[@]} extensão(ões) no VS Code do Ubuntu."
erros=0
for e in "${FALTAM[@]}"; do
  if [[ $SIMULAR -eq 1 ]]; then echo "  INSTALARIA  $e"; continue; fi
  if code --install-extension "$e" >/dev/null 2>&1; then echo "  INSTALADA   $e"; else echo "  ERRO        $e (rode: code --install-extension $e)"; erros=$((erros + 1)); fi
done
[[ $SIMULAR -eq 1 ]] && { echo "Simulação. Rode sem --simular para instalar."; exit 0; }
((erros == 0)) || exit 1
