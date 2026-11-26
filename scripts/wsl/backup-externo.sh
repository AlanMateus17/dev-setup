#!/usr/bin/env bash
# Cópia do backup para o HD externo (regra 3-2-1): copia os snapshots do repositório restic do SSD para um repositório no HD.
#   bash scripts/wsl/backup-externo.sh              # copia, limpa os antigos e confere (o mesmo que: just backup-externo)
#   bash scripts/wsl/backup-externo.sh --restaurar  # restaura o último snapshot do HD numa pasta temporária e compara com o SSD
#   bash scripts/wsl/backup-externo.sh --simular    # só diz o que faria
# Configuração: a mesma de ~/.config/amtech/backup.env, mais uma linha com o caminho do repositório no HD:
#   RESTIC_REPOSITORY_EXTERNO=/mnt/e/backup-restic
# O repositório do HD usa a MESMA senha do SSD (RESTIC_PASSWORD_FILE): uma senha só, no caderno e no KeePassXC.
# Na primeira vez cria o repositório do HD com os mesmos parâmetros de blocos do SSD (a cópia fica pequena).
set -euo pipefail
RAIZ="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
CONF="${BACKUP_CONF:-$HOME/.config/amtech/backup.env}"
MODO="copiar"
case "${1:-}" in
  "") ;;
  --restaurar) MODO="restaurar" ;;
  --simular) MODO="simular" ;;
  -h|--help) sed -n '2,9p' "$0"; exit 0 ;;
  *) echo "Opção desconhecida: $1" >&2; exit 64 ;;
esac

command -v restic >/dev/null 2>&1 || { echo "Instale o restic: sudo apt install restic"; exit 1; }
[[ -f "$CONF" ]] || { echo "Falta $CONF (copie infra/templates/backup.env.example)."; exit 1; }
# shellcheck source=/dev/null
source "$CONF"
[[ -n "${RESTIC_REPOSITORY:-}" && -f "${RESTIC_PASSWORD_FILE:-}" ]] || { echo "backup.env sem RESTIC_REPOSITORY ou sem o arquivo de senha: rode o just backup primeiro."; exit 1; }
EXT="${RESTIC_REPOSITORY_EXTERNO:-}"
if [[ -z "$EXT" ]]; then
  echo "Falta RESTIC_REPOSITORY_EXTERNO no $CONF."
  echo "Conecte o HD, veja a letra (PS C:\\> Get-Volume) e acrescente, por exemplo: RESTIC_REPOSITORY_EXTERNO=/mnt/e/backup-restic"
  exit 1
fi

# O HD precisa ser outro disco: /mnt/c é o próprio SSD, e uma pasta em /mnt/<letra> sem disco montado também é o SSD.
if [[ "$EXT" =~ ^/mnt/([a-z])(/|$) ]]; then
  letra="${BASH_REMATCH[1]}"
  [[ "$letra" != "c" ]] || { echo "RESTIC_REPOSITORY_EXTERNO está no C: (o mesmo SSD do backup). Use a letra do HD externo."; exit 1; }
  if ! mountpoint -q "/mnt/$letra"; then
    L="${letra^^}"
    echo "O HD ($L:) não está ligado ao Ubuntu. Conecte o HD; se o Windows já mostra o $L: e o Ubuntu não, rode:"
    echo "  alanmateus@...\$ sudo mkdir -p /mnt/$letra && sudo mount -t drvfs $L: /mnt/$letra"
    exit 1
  fi
fi
[[ "$EXT" != "$RESTIC_REPOSITORY" ]] || { echo "RESTIC_REPOSITORY_EXTERNO é igual ao RESTIC_REPOSITORY."; exit 1; }

# restic usa RESTIC_FROM_* como origem (o SSD) e RESTIC_REPOSITORY como destino (o HD).
export RESTIC_FROM_REPOSITORY="$RESTIC_REPOSITORY" RESTIC_FROM_PASSWORD_FILE="$RESTIC_PASSWORD_FILE"
export RESTIC_REPOSITORY="$EXT" RESTIC_PASSWORD_FILE
evento() { python3 "$RAIZ/tools/nucleo/nucleo.py" evento "$1" "$2" --fonte backup >/dev/null 2>&1 || echo "aviso: não gravei o evento $1 no núcleo"; }

if [[ "$MODO" == "simular" ]]; then
  [[ -f "$EXT/config" ]] || echo "restic init --from-repo $RESTIC_FROM_REPOSITORY --copy-chunker-params   (repositório novo em $EXT)"
  echo "restic copy --from-repo $RESTIC_FROM_REPOSITORY   (para $EXT)"
  echo "restic forget --keep-daily 7 --keep-weekly 4 --keep-monthly 12 --prune --tag diario"
  echo "restic check --read-data-subset=5%"
  exit 0
fi

if [[ "$MODO" == "restaurar" ]]; then
  [[ -f "$EXT/config" ]] || { echo "Ainda não há repositório no HD: rode just backup-externo primeiro."; exit 1; }
  tmp="$(mktemp -d)"; trap 'rm -rf "$tmp"' EXIT
  # O snapshot do HD guarda o id do snapshot de origem (campo "original"): a contagem de arquivos tem que bater com a do SSD.
  read -r snap orig < <(restic snapshots --latest 1 --json | python3 -c 'import json,sys; s=(json.load(sys.stdin) or [{}])[-1]; print(s.get("short_id",""), s.get("original") or s.get("id",""))')
  [[ -n "$snap" ]] || { echo "FALHOU: o repositório do HD não tem snapshot."; exit 1; }
  echo "== Restaurando o snapshot $snap do HD em $tmp"
  restic restore "$snap" --target "$tmp" >/dev/null
  n="$(find "$tmp" -type f | wc -l)"
  # Só arquivos (o stats --mode restore-size conta pastas também).
  esperado="$(restic -r "$RESTIC_FROM_REPOSITORY" --password-file "$RESTIC_FROM_PASSWORD_FILE" ls "$orig" --json \
    | python3 -c 'import json,sys; print(sum(1 for l in sys.stdin if l.strip() and json.loads(l).get("type") == "file"))')"
  echo "Restaurados $n arquivos ($(du -sh "$tmp" | cut -f1)); o snapshot de origem no SSD tem $esperado."
  [[ "$n" -gt 0 && "$n" == "$esperado" ]] || { echo "FALHOU: a restauração do HD não bate com o SSD."; exit 1; }
  evento backup.externo.restaurado "{\"snapshot\": \"$snap\", \"arquivos\": $n}"
  echo "TESTE OK: o backup do HD restaura e bate com o SSD."
  exit 0
fi

if [[ ! -f "$EXT/config" ]]; then
  echo "== Criando o repositório no HD ($EXT), com a mesma senha do SSD"
  mkdir -p "$EXT"
  restic init --from-repo "$RESTIC_FROM_REPOSITORY" --copy-chunker-params
fi
echo "== Copiando os snapshots do SSD para o HD"
restic copy
restic forget --keep-daily 7 --keep-weekly 4 --keep-monthly 12 --prune --tag diario
restic check --read-data-subset=5%
snap="$(restic snapshots --latest 1 --json | python3 -c 'import json,sys; s=json.load(sys.stdin) or [{}]; print(s[-1].get("short_id", ""))')"
evento backup.externo.concluido "{\"snapshot\": \"$snap\"}"
echo "OK: cópia no HD feita (último snapshot $snap). Teste a restauração: just backup-externo --restaurar"
