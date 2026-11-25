# Hooks do ai-memory (Claude Code)

Memória de longo prazo entre sessões e agentes: [akitaonrails/ai-memory](https://github.com/akitaonrails/ai-memory).
Instalado em 25/11/2026, versão **3.6.1**.

| Peça | Onde fica |
|---|---|
| Binário | `~/.local/bin/ai-memory` |
| Dados, token e config | `~/.local/share/ai-memory/` (token em `auth-tokens/default`, chmod 600) |
| Servidor | serviço `systemctl --user` `ai-memory.service`, em `127.0.0.1:49374` (só local) |
| Hooks | esta pasta: `_lib.sh` + `claude-code/*.sh`, ligados em `~/.claude/settings.json` |
| MCP | `ai-memory` no escopo do usuário (`claude mcp list`) |
| Projeto | `.ai-memory.toml` na raiz do repositório: workspace `amtech`, projeto `dev-setup` |

## Reinstalar do zero

```bash
gh release download v3.6.1 -R akitaonrails/ai-memory -p 'ai-memory-linux-x86_64.tar.gz*'
sha256sum -c ai-memory-linux-x86_64.tar.gz.sha256
tar xzf ai-memory-linux-x86_64.tar.gz && install -m 0755 ai-memory ~/.local/bin/
ai-memory init                       # cria dados e token
# unit: ExecStart=%h/.local/bin/ai-memory --data-dir %h/.local/share/ai-memory serve --transport http --enable-web
systemctl --user enable --now ai-memory
curl -s http://127.0.0.1:49374/healthz   # {"status":"ok"}
claude mcp add --scope user --transport stdio ai-memory -- ~/.local/bin/ai-memory mcp-bridge --server-url http://127.0.0.1:49374/mcp
```

Os hooks entram em `~/.claude/settings.json` como `sh "$HOME/dev/dev-setup/infra/ai-memory-hooks/claude-code/<evento>.sh"`.

## Testar

```bash
P='{"session_id":"teste","cwd":"'"$PWD"'","prompt":"teste"}'
printf '%s' "$P" | sh infra/ai-memory-hooks/claude-code/user-prompt-submit.sh   # imprime {}
ai-memory status          # "observations" sobe
ai-memory list-projects   # aparece amtech / dev-setup
```

## Atualizar

Troque o binário e copie `hooks/_lib.sh` e `hooks/claude-code/*.sh` do novo release para esta pasta.

## Limite conhecido

`stop.sh` descarta o evento Stop quando ele traz `last_assistant_message`, porque o script não consegue
limpar a resposta antes de enviar. Para capturar também as respostas, o próprio projeto recomenda o hook nativo
(`ai-memory hook --event stop --agent claude-code`), que dispensa estes scripts.
