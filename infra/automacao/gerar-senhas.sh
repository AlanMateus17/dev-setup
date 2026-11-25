#!/usr/bin/env bash
# Cria ou completa o .env da automação (senhas aleatórias, sem mostrar). Mantido por compatibilidade:
# o trabalho é do scripts/wsl/gerar-env.sh, que serve a todas as pastas de serviços.
set -euo pipefail
exec bash "$(cd "$(dirname "$0")/../.." && pwd)/scripts/wsl/gerar-env.sh" automacao "$@"
