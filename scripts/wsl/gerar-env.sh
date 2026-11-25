#!/usr/bin/env bash
# Cria ou completa o .env de uma pasta de serviços (infra/<pasta>) a partir do modelo, sem nunca mostrar os valores.
# Seguro para rodar várias vezes: não troca valor que já existe.
#   bash scripts/wsl/gerar-env.sh automacao            # cria/completa infra/automacao/.env
#   bash scripts/wsl/gerar-env.sh casa --simular       # só diz o que faria
# Regras:
#   - copia o modelo (.env.example ou <pasta>.env.example) se o .env não existir; chmod 600 sempre;
#   - gera valor aleatório só para as chaves que a pasta declara em GERAR (abaixo); senha que vem de fora
#     (câmera, API de terceiros) nunca é inventada: fica na lista "preencha você";
#   - troca /home/SEU_USUARIO pelo seu $HOME;
#   - *_VERSAO=latest fica vazio, para valer a versão fixa do compose.yaml.
set -euo pipefail
RAIZ="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
PASTA="${1:-}"; SIMULAR=0; [[ "${2:-}" == "--simular" ]] && SIMULAR=1
declare -A GERAR=(
  [automacao]="METRICAS_SENHA GRAFANA_DB_SENHA GRAFANA_SENHA N8N_CHAVE"
  [casa]="PAPERLESS_SECRET"
  [jarvis]=""
  [ia]="LITELLM_MASTER_KEY"
)
[[ -n "$PASTA" && -v "GERAR[$PASTA]" ]] || { echo "Uso: gerar-env.sh <${!GERAR[*]}> [--simular]" >&2; exit 64; }
DIR="$RAIZ/infra/$PASTA"
MODELO=""
for m in "$DIR/.env.example" "$DIR/$PASTA.env.example"; do [[ -f "$m" ]] && { MODELO="$m"; break; }; done
[[ -n "$MODELO" ]] || { echo "infra/$PASTA não tem modelo de .env" >&2; exit 1; }
ENV="$DIR/.env"

if [[ $SIMULAR -eq 1 ]]; then
  [[ -f "$ENV" ]] && echo "infra/$PASTA/.env existe: só completaria o que falta" || echo "criaria infra/$PASTA/.env a partir de $(basename "$MODELO")"
  echo "geraria (se vazias): ${GERAR[$PASTA]:-nenhuma}"
  exit 0
fi

[[ -f "$ENV" ]] || { cp "$MODELO" "$ENV"; echo "Criado: infra/$PASTA/.env"; }
chmod 600 "$ENV"
# Chaves do modelo que faltam no .env entram vazias (o .env pode ser de uma versão antiga do modelo).
while IFS= read -r linha; do
  chave="${linha%%=*}"
  grep -qE "^${chave}=" "$ENV" || { printf '%s=\n' "$chave" >> "$ENV"; echo "Acrescentada: $chave"; }
done < <(grep -E '^[A-Z0-9_]+=' "$MODELO")

aleatoria() { head -c 48 /dev/urandom | base64 | tr -dc 'A-Za-z0-9' | head -c 32; }
for chave in ${GERAR[$PASTA]}; do
  if grep -qE "^${chave}=$" "$ENV"; then sed -i "s|^${chave}=$|${chave}=$(aleatoria)|" "$ENV"; echo "Gerada: $chave"; fi
done
sed -i "s|/home/SEU_USUARIO|${HOME}|g" "$ENV"
sed -i -E 's/^([A-Z0-9_]+_VERSAO)=latest$/\1=/' "$ENV"

mapfile -t VAZIAS < <(grep -E '^[A-Z0-9_]+=$' "$ENV" | cut -d= -f1 | grep -vE '_VERSAO$' || true)
if ((${#VAZIAS[@]})); then echo "Preencha você em infra/$PASTA/.env: ${VAZIAS[*]}"; fi
[[ -n "${GERAR[$PASTA]}" ]] && echo "Guarde no KeePassXC as chaves geradas: ${GERAR[$PASTA]}"
exit 0
