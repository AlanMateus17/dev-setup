# dev-setup

Arquitetura completa do meu ambiente de desenvolvimento e de trabalho: do hardware ao deploy na nuvem, da criação de conteúdo à venda de cursos. Cada ferramenta tem um motivo, um lugar e conexões definidas.

**Diagrama interativo:** [`docs/index.html`](docs/index.html) · **Ordem de estudo e mercado:** [`docs/mapa.html`](docs/mapa.html). Baixe e abra no navegador; o repositório é privado, então não há GitHub Pages.

> Diagrama com 18 camadas, cerca de 200 blocos e mais de 270 conexões. Toque em um bloco para ver o que ele faz e com o que se conecta, ou escolha um fluxo pronto ("Codar com agente e publicar", "Vender o mini-curso", "Laboratório de segurança").

## A ideia em uma frase

O Windows cuida só do que precisa de janela, GPU e segurança; todo o trabalho de engenharia roda em Linux (Ubuntu no WSL2), em containers, e sai para a nuvem por CI/CD. Agentes de IA trabalham dentro de uma sandbox que só enxerga a pasta do projeto.

## Camadas

| # | Camada | Principais peças |
|---|---|---|
| 18 | Público e canais | Instagram, YouTube, LinkedIn, WhatsApp Business, SEO |
| 17 | Plataformas de venda | Hotmart, Kiwify, Eduzz, Udemy, DIO, MailerLite |
| 16 | Impostos e finanças | Carnê-leão, conta separada, CNPJ no futuro |
| 15 | Vitrine web | Domínio, site pessoal e blog, Instituto AMS, Cloudflare |
| 14 | Produtos | Mini-curso, templates, livro, aulas, sites para clientes |
| 13 | Estudo e carreira | Microsoft Learn, AWS Skill Builder, TryHackMe, Anki |
| 12 | Produção de conteúdo | OBS, DaVinci Resolve/Kdenlive, Audacity, Whisper |
| 11 | Recursos do Claude | Projects, artifacts, conectores, plugins, tarefas agendadas |
| 10 | Assistentes de IA | Claude, Gemini, NotebookLM, ChatGPT, Codex, Copilot, Perplexity |
| 9 | Nuvem e entrega | GitHub, Actions, GHCR, Azure, AWS, Cloudflare, Vercel |
| 8 | Aplicação (sistemas AM) | Next.js, ASP.NET Core, Clean Architecture + DDD, EF Core, SignalR |
| 7 | Observabilidade | OpenTelemetry, Prometheus, Grafana, Sentry, Uptime Kuma |
| 6 | Containers e IaC | Docker Compose, PostgreSQL + pgvector, Redis, RabbitMQ, Terraform, kind |
| 5 | Agentes de IA | Claude Code, ai-jail, ai-memory, MCP, Ollama, base de conhecimento (RAG) |
| 4 | Linux | Ubuntu no WSL2, .NET 10, Node, Python, TeX Live; Arch + Omarchy no futuro |
| 3 | Windows e VMs | VS Code Remote, KeePassXC, Obsidian, DBeaver, VirtualBox (Kali, servidores) |
| 2 | Segurança | TPM, BitLocker, Defender, 2FA, commits assinados, backup 3-2-1 |
| 1 | Hardware | Acer Nitro AN515-45 (Ryzen 7 5800H, 32 GB, GTX 1650), segundo monitor |

## Stack fixa dos sistemas

C#/.NET 10 · ASP.NET Core (Controllers) · Clean Architecture + DDD · PostgreSQL · Redis · SignalR · TypeScript, Next.js e Tailwind · Docker · GitHub Actions.

Rejeitadas de propósito: Bun, Hono, Rust, Tauri e gRPC. As decisões estão em [`docs/adr`](docs/adr).

## O que tem aqui

```
docs/
  index.html     diagrama interativo do ecossistema
  mapa.html      sistemas operacionais, nuvens, ordem de estudo e dados de mercado
  adr/           decisões de arquitetura do setup
scripts/
  windows/inventario.ps1   inventário somente leitura do Windows (programas, inicialização, espaço)
```

## Status

O setup está sendo montado em fases. A fase 1 (base Windows + WSL2 + Docker + .NET) está em andamento; o restante segue a ordem de estudo do mapa.

## Licença

[MIT](LICENSE)
