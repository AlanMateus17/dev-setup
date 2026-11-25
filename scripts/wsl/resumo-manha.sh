#!/usr/bin/env bash
# Resumo da manhã: o que precisa da sua atenção hoje. SOMENTE LEITURA.
#   bash scripts/wsl/resumo-manha.sh            # mostra na tela
#   bash scripts/wsl/resumo-manha.sh --texto    # texto simples (usado pelo bot)
#   bash scripts/wsl/resumo-manha.sh --telegram # manda para o seu Telegram (precisa do bot configurado)
set -uo pipefail
RAIZ="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
MODO="${1:-}"
L=()
add() { L+=("$1"); }

add "Resumo de $(date '+%a %d/%m %H:%M')"
uso="$(df -h "$HOME" | awk 'NR==2 {print $5" usado, "$4" livre"}')"
add "Disco: ${uso}"
pct="$(df "$HOME" | awk 'NR==2 {gsub("%","",$5); print $5}')"
[[ "${pct:-0}" -ge 85 ]] && add "ATENÇÃO: disco acima de 85%. Rode a manutenção semanal."

ult="$(find "$HOME/backups" -maxdepth 2 -type f -printf '%T@\n' 2>/dev/null | sort -n | tail -1)"
if [[ -n "${ult:-}" ]]; then
  dias=$(( ( $(date +%s) - ${ult%.*} ) / 86400 ))
  add "Último backup local: há ${dias} dia(s)"
  [[ "$dias" -ge 8 ]] && add "ATENÇÃO: backup com mais de 7 dias."
else
  add "Backup local: nenhum em ~/backups (confira o backup do roteiro)."
fi

# Backup real (restic): o backup.sh grava o evento backup.concluido no núcleo. Sem ele em 36 h, o backup está falhando em silêncio.
BANCO="${NUCLEO_DB:-$HOME/.local/share/nucleo/nucleo.db}"
if [[ -f "$BANCO" ]]; then
  h="$(NUCLEO_DB="$BANCO" python3 "$RAIZ/tools/nucleo/nucleo.py" ultimo backup.concluido 2>/dev/null || echo erro)"
  case "$h" in
    nunca) add "ATENÇÃO: nenhum backup restic registrado no núcleo. Rode: just backup (e confira ~/.config/amtech/backup.env)." ;;
    erro|"") add "ATENÇÃO: não consegui ler o núcleo para conferir o backup." ;;
    *) if [[ "$h" -ge 36 ]]; then add "ATENÇÃO: último backup restic há ${h} h (mais de 36 h). Rode: just validar"; else add "Backup restic: há ${h} h."; fi ;;
  esac
else
  add "ATENÇÃO: núcleo não iniciado, não dá para conferir o backup restic (python3 tools/nucleo/nucleo.py iniciar)."
fi

pend=0
while IFS= read -r g; do
  d="$(dirname "$g")"
  if [[ -n "$(git -C "$d" status --porcelain 2>/dev/null)" ]]; then pend=$((pend + 1)); add "Repositório com mudanças não salvas: ${d/#$HOME/~}"; fi
done < <(find "$HOME/dev" -maxdepth 2 -name .git -type d 2>/dev/null)
[[ "$pend" -eq 0 ]] && add "Repositórios: tudo salvo."

if command -v docker >/dev/null 2>&1; then
  parados="$(docker ps -a --filter status=exited --format '{{.Names}}' 2>/dev/null | head -5 | tr '\n' ' ')"
  [[ -n "$parados" ]] && add "Serviços parados: ${parados}"
fi
[[ -f "$HOME/radar.md" ]] && add "Radar: $(grep -m1 -o '[0-9]* aprovados' "$HOME/radar.md" 2>/dev/null || echo 'sem aprovados') (radar.md)"
add "Lembrete: sono, cães e domingo são intocáveis."

TEXTO="$(printf '%s\n' "${L[@]}")"
case "$MODO" in
  --telegram) python3 "$RAIZ/tools/remoto/bot.py" --avisar "$TEXTO" ;;
  *) printf '%s\n' "$TEXTO" ;;
esac
