O headscale lê `config.yaml` desta pasta. Ele nasce do modelo `config.yaml.example` (validado com `headscale configtest` na v0.29.7):

    bash scripts/wsl/headscale-config.sh

O `just instalar trabalho` roda esse passo sozinho. O `config.yaml` não vai para o Git (fica livre para a configuração da VM); a chave
privada do servidor fica no volume `headscale-dados`, não neste arquivo. A porta é publicada só em `127.0.0.1:8085` (ADR 0022).

Se `config.yaml` virou uma **pasta** de dono root, foi o Docker que a criou quando o arquivo não existia: `sudo rm -r` nela e rode o
script de novo.
