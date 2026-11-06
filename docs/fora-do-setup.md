<!-- Arquivo GERADO por tools/gerar_docs.py a partir de data/. Edite os dados, não este arquivo. -->


# Decisões: o que entra de outro jeito e o que fica de fora

[← Índice da documentação](README.md)

Nada do planejamento foi retirado. Os quatro primeiros entram por outro caminho, com passo e data no [roteiro](implantacao/roteiro.md); os outros são decisões suas ou de segurança, e voltam se você mudar de ideia.

| Item | Decisão |
|---|---|
| Dual boot no SSD atual | Não no SSD do Windows, pelo risco de perder dados. O Arch entra do mesmo jeito: em pendrive agora e no 2º NVMe, com boot próprio, quando você comprar o disco (fase Linux nativo do roteiro). |
| Kali como sistema principal | Kali é caixa de ferramentas de pentest, não ambiente de dev. Ele entra em pendrive com persistência e em VM (fases Dados, IA e pendrives e Linux nativo). |
| Treinar um 8B na GTX 1650 | A placa tem 4 GB e o QLoRA de 8B pede 6 GB. O treino entra pelo Kaggle e por GPU alugada em 2027, e em casa quando a workstation com GPU chegar (fase Infraestrutura própria). |
| Mobile nativo (Kotlin, Swift, Flutter) | Abriria outra stack. O app mobile entra em 2028 com .NET MAUI, na mesma linguagem do Aura (fase Distribuído, plataforma e segunda nuvem). |
| OpenClaw | Histórico sério de instâncias expostas e execução de código não confiável. |
| Bun, Hono, Rust, Tauri, gRPC | Rejeitados por você para o Aura. |
| Postman, IDEs pagas, SaaS pagos | Você prefere open source; Bruno, DBeaver e VS Code cobrem. |
| Coolify e Dokploy | Um deploy só: Kamal nas VMs (ADR 0005). Três ferramentas de deploy para a mesma função é o Frankenstein que o próprio contexto mestre condena. |
| PocketBase, SvelteKit, Fastify e Go nos sistemas | Abririam uma segunda stack ao lado do .NET 10. O backend do Aura segue em ASP.NET Core com PostgreSQL; o Zod entra só no front (ADR 0006). |
| GoReleaser, cargo-dist, bubbletea e probe-rs | Ferramentas de Go e Rust, que não estão na stack. O ESP32 grava pelo ESPHome, Arduino IDE ou esptool; o probe-rs volta se entrar STM32. |
| mise | fnm (Node) e uv (Python) já isolam os runtimes. O Kamal roda pela imagem Docker oficial, sem Ruby na máquina. |
| Podman | O Docker Desktop com a integração do WSL já está instalado e funcionando; trocar o motor não muda o resultado. |
| Zellij, Ghostty, yazi e chezmoi | O tmux já vem no bootstrap, o Windows Terminal cobre as abas, o Explorer abre as pastas do WSL e o repositório de dotfiles (passo dotfiles) já versiona a configuração. O Ghostty volta com o Arch nativo no 2º NVMe. |
| age e sops (.env cifrado no Git) | Regra do setup: segredo só no KeePassXC, nunca no repositório, nem cifrado. O Kamal lê os segredos pelo keepassxc-cli. |
| Forgejo ou Gitea agora | O GitHub privado com Education, Actions e Copilot é o centro da esteira; o risco de bloqueio fica coberto pelo backup dos repositórios no restic. Servidor Git próprio volta na fase Infraestrutura própria. |
| gocryptfs no lab de engenharia reversa | O disco já é BitLocker e o lab de alvo é isolado, sem internet; cifrar a pasta de novo não muda o risco. |
| Aider, llm (CLI) e tree-sitter avulso | O Claude Code é o agente primário e o Codex a reserva; o LiteLLM já roteia para o Ollama. O Repomix (--compress) e o Claude Code já usam tree-sitter por dentro. |
| SigNoz, D2, Plane, BookStack, Logseq e Formbricks | Repetem o que já existe: OpenTelemetry com Grafana, Loki e Tempo; Mermaid e Excalidraw; GitHub Projects; MkDocs; Obsidian; perguntas do Cal.com e NPS. GlitchTip já é a reserva do Sentry. |
| posting, harlequin, vegeta, radare2, bore, gum, Litestream e Headscale | Repetem Bruno, DBeaver e o duckdb, k6, Ghidra, cloudflared e Python. Litestream é para SQLite e os sistemas usam PostgreSQL; Headscale já é a alternativa registrada do Tailscale. |
| Portfolio Performance, Ghostfolio, Beancount, hledger, Actual, Firefly III e ERPNext | financeiro.py, investimentos.py e o Caixa da Casa já fazem isso com as suas regras (cascata, ARCA e 27 metodologias); o ERPNext seria um segundo sistema de gestão concorrendo com o Aura. |
| Polar e Stripe CLI | As vendas são no CPF por Hotmart e Kiwify, e o Pix pelo Asaas. O Polar volta com a venda internacional; o Stripe só se entrar como gateway. |
| bpftrace | Entra com o Linux nativo (fase Linux nativo e laboratório completo), num kernel que é seu. |
| Cronograma de 14 dias (Estratégia do Halter) | Não cabe com escola, restaurante e licenciatura, e passa por cima da regra de no máximo 3 rendas agora. As duas frentes já estão no portfólio: Chatwoot é a Automação com IA para pequenos negócios (passo of-automacao) e o SaaS do ARCA é o AM Rendara começando pela planilha (passos caixa e of-planilha). |
| SLU e Fator R agora | Decisão atual: vender no CPF (fase CNPJ e formalização). Quando abrir: os 6% do Anexo III valem só na 1ª faixa (até R$ 180 mil em 12 meses) e o pró-labore de 28% paga INSS de 11% e IR; confirme com o contador. |
