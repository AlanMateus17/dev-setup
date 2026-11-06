#!/usr/bin/env bash
# Manutenção semanal do lado Linux. Por padrão SIMULA; com --aplicar executa.
#   bash scripts/wsl/manutencao-semanal.sh             # mostra o que faria
#   bash scripts/wsl/manutencao-semanal.sh --aplicar   # atualiza pacotes, limpa caches e confere tudo
# Nunca apaga seus arquivos: só caches de pacotes e imagens Docker sem uso.
set -uo pipefail
RAIZ="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
APLICAR=0; [[ "${1:-}" == "--aplicar" ]] && APLICAR=1
passo() { echo; echo "== $1"; }
rodar() { if [[ "$APLICAR" == 1 ]]; then echo "+ $*"; "$@"; else echo "(simulação) $*"; fi; }

passo "Pacotes do Ubuntu"
rodar sudo apt-get update -qq
rodar sudo apt-get upgrade -y
rodar sudo apt-get autoremove -y
passo "Docker: imagens e build cache sem uso"
command -v docker >/dev/null 2>&1 && rodar docker system prune -f
passo "Ferramentas do usuário"
{ command -v mise >/dev/null 2>&1 || command -v fnm >/dev/null 2>&1; } && echo "Node: $(node -v 2>/dev/null)"
command -v dotnet >/dev/null 2>&1 && rodar dotnet workload update
passo "Repositórios: buscar atualizações (sem mexer nos seus arquivos)"
while IFS= read -r g; do rodar git -C "$(dirname "$g")" fetch --quiet --all; done < <(find "$HOME/dev" -maxdepth 2 -name .git -type d 2>/dev/null)
passo "Conferência do setup"
bash "$RAIZ/scripts/wsl/verificar.sh" || echo "Há itens a corrigir (veja acima)."
passo "Resumo"
bash "$RAIZ/scripts/wsl/resumo-manha.sh"
