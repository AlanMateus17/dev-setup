#!/usr/bin/env bash
# Agenda as rotinas no cron do Ubuntu (idempotente: rodar de novo não duplica).
#   bash scripts/wsl/agendar.sh            # mostra o que vai agendar
#   bash scripts/wsl/agendar.sh --aplicar  # grava no crontab
#   bash scripts/wsl/agendar.sh --remover  # tira as linhas do setup
# Resumo da manhã às 6h10 no Telegram; manutenção (simulação + aviso) no domingo às 9h. O WSL precisa estar aberto.
set -euo pipefail
RAIZ="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
MARCA="# amtech-setup"
LINHAS="10 6 * * * bash $RAIZ/scripts/wsl/resumo-manha.sh --telegram >/dev/null 2>&1 $MARCA
0 9 * * 0 bash $RAIZ/scripts/wsl/manutencao-semanal.sh > \$HOME/manutencao-ultima.log 2>&1 && python3 $RAIZ/tools/remoto/bot.py --avisar 'Manutenção simulada: veja ~/manutencao-ultima.log' $MARCA"
atual="$(crontab -l 2>/dev/null | grep -v "$MARCA" || true)"
case "${1:-}" in
  --aplicar) printf '%s\n%s\n' "$atual" "$LINHAS" | sed '/^$/d' | crontab - ; echo "Agendado:"; crontab -l | grep "$MARCA" ;;
  --remover) printf '%s\n' "$atual" | sed '/^$/d' | crontab - ; echo "Linhas do setup removidas." ;;
  *) echo "Vai agendar (use --aplicar):"; echo "$LINHAS" ;;
esac
