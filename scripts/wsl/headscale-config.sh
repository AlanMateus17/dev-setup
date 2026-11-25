#!/usr/bin/env bash
# Põe a configuração do headscale no lugar: copia infra/soberania/headscale/config.yaml.example para config.yaml.
# Seguro para rodar de novo: um config.yaml que já existe (arquivo) não é tocado.
#   bash scripts/wsl/headscale-config.sh --simular
set -euo pipefail
RAIZ="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
D="$RAIZ/infra/soberania/headscale"
if [[ -d "$D/config.yaml" ]]; then
  echo "infra/soberania/headscale/config.yaml é uma PASTA (o Docker cria uma quando o arquivo não existe na hora do up)."
  echo "Apague com: sudo rm -r $D/config.yaml   e rode este script de novo."
  exit 1
fi
if [[ -f "$D/config.yaml" ]]; then echo "config.yaml do headscale já existe: mantido."; exit 0; fi
if [[ "${1:-}" == "--simular" ]]; then echo "copiaria config.yaml.example para config.yaml"; exit 0; fi
cp "$D/config.yaml.example" "$D/config.yaml"
echo "Criado: infra/soberania/headscale/config.yaml (server_url http://127.0.0.1:8085; na VM, troque pelo endereço público)."
