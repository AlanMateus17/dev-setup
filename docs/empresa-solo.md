<!-- Escrito à mão. Como o "Contexto mestre unificado: setup e engenharia da empresa solo" entrou no dev-setup. -->

# Empresa solo: o contexto mestre dentro do setup

[← Índice da documentação](README.md)

O contexto mestre (soberania técnica, anti-Frankenstein, economia de tokens, 88 ferramentas abertas, `just architect` e `just triage`, Kamal, ARCA, ciclo comercial, estrutura legal e o cronograma de 14 dias) foi cruzado com o setup inteiro. A maior parte **já estava aqui**: o setup tinha chegado às mesmas ideias por outro caminho. O que soma entrou como bloco, passo e ADR; o que repete ou contradiz as suas regras ficou de fora, com o motivo, em [Decisões](fora-do-setup.md).

A regra que decidiu tudo é a do próprio documento: **uma ferramenta por função, e só se programa o que gera faturamento.** Aplicar 88 ferramentas de uma vez seria exatamente o Frankenstein que ele condena.

## O que mudou no setup

| O quê | Onde |
|---|---|
| `justfile` na raiz: porta única de comandos (`just check`, `just triagem`, `just arquiteto`, `just docs`, `just ci-local`, `just contexto-ia`, `just medir`) | [justfile](../justfile) |
| Motor de decisão montar / colar / construir e pacote de contexto para o arquiteto | `tools/triagem/triagem.py` (com testes) |
| Terminal moderno e o `just` no bootstrap: zoxide, eza, fd, btop, hyperfine, lazygit, lazydocker, Starship, tio e tcpdump | `scripts/wsl/bootstrap.sh` |
| Deploy em VM pelo Kamal; Coolify e Dokploy de fora | [ADR 0005](adr/0005-deploy-em-vm-com-kamal.md) · `infra/templates/kamal` |
| Contratos: OpenAPI no backend, Zod, Biome e Vitest no front | [ADR 0006](adr/0006-contratos-na-borda.md) |
| O agente não lê segredo nem lixo: `permissions.deny` em todo repositório | `infra/templates/repo-padrao/.claude/settings.json` |
| Klaro! (consentimento LGPD) antes de ligar o Pixel | passo `klaro-lgpd` |
| Bancada de eletrônica: KiCad, PulseView, tio e o analisador lógico | passos `solo-kicad` e `solo-analisador` |
| Fase nova do roteiro: **Empresa solo: o contexto mestre no setup** (9 passos, semana 5 de nov/2026) | [roteiro](implantacao/roteiro.md) |

## Correções ao documento original

Estas afirmações do contexto mestre estavam erradas ou desatualizadas e foram corrigidas aqui:

1. **`.claudeignore` não existe no Claude Code.** O que funciona são as regras `permissions.deny` do `.claude/settings.json` (o `.aiderignore` é só do Aider). Modelo no repo-padrão.
2. **"Claude 3.5 Sonnet" está obsoleto.** As rotas de modelo do setup ficam no gateway LiteLLM e em [custos.md](custos.md); nenhum documento deve fixar versão de modelo.
3. **Zod não existe em .NET.** O rigor de contrato fica no OpenAPI do backend e no Zod do front (ADR 0006), sem abrir uma segunda stack.
4. **Fator R:** os 6% do Anexo III valem só na 1ª faixa (receita de até R$ 180 mil em 12 meses), e o pró-labore de 28% tem custo próprio (INSS de 11% e IR). Hoje a decisão é vender no CPF; isso volta na fase CNPJ, com o contador.
5. **`just architect` e `just triage` não existiam.** Viraram `just arquiteto` e `just triagem`, que só montam o contexto e a decisão a partir dos dados do setup; nenhum deles "pesquisa líderes de mercado" sozinho.
6. **ai-jail e ai-memory** existem (já estavam no setup, fase Agentes de IA).
7. **O cronograma de 14 dias** pressupõe tempo integral. Com escola, restaurante e licenciatura, e com a regra de no máximo 3 rendas agora, ele foi encaixado nas ofertas que já existiam (abaixo).

## O cronograma de 14 dias, reescrito

| No documento | No setup | Quando |
|---|---|---|
| Dia 1: VPS, Coolify e Uptime Kuma | VM grátis da Oracle e Uptime Kuma (passos `op-vm` e `op-migrar`); Kamal no lugar do Coolify | Fase Operação 24 horas (dez/2026 a jan/2027) |
| Dias 2 a 7: Chatwoot vendido a 5 empresas por R$ 1.800 + R$ 350/mês | Oferta **Automação com IA para pequenos negócios** (`automacaoia`, veredito fila): 1 implantação grátis em troca de caso, depois preço (passo `of-automacao`). O WhatsApp no Chatwoot exige a API oficial da Meta, com verificação do negócio e custo por conversa: some isso ao preço | Fase Mais ofertas (2027), quando uma das 3 de agora passar no portão |
| Dias 8 a 14: micro-SaaS ARCA em SvelteKit + PocketBase | **AM Rendara começando pela planilha** (`rendara`, fila): Caixa da Casa na planilha (passo `caixa`), vender a planilha antes do sistema (passo `of-planilha`); o sistema, se vender, nasce na stack do Aura | Fases Vendas e finanças no CPF e Mais ofertas |

## As 88 ferramentas, uma por uma

**Já no setup** = o bloco já existia. **Entra** = virou bloco ou passo agora. **Fora** = repete algo ou contradiz uma regra; o motivo está em [Decisões](fora-do-setup.md).

| Grupo | Já no setup | Entra | Fora |
|---|---|---|---|
| Terminal e ergonomia (5) | — | Starship; lazy.nvim e snacks.nvim entram na configuração do Neovim (bloco que já existia, para quando você começar a usá-lo) | Ghostty, Zellij |
| Runtimes e coreutils (6) | ripgrep, fzf | zoxide, eza, fd | mise |
| Arquivos, Git e containers (4) | — | lazygit, lazydocker | yazi, Podman |
| APIs, bancos e backends (4) | Bruno | — | posting, harlequin, PocketBase |
| Automação e métricas (5) | — | just, btop, hyperfine | gum, bubbletea |
| Dotfiles e segredos (4) | gitleaks | — | chezmoi (o repositório de dotfiles já cobre), age, sops |
| Rede, túneis e backup (5) | cloudflared, restic, Headscale (reserva do Tailscale) | — | bore, Litestream |
| Deploy (3) | — | Kamal | Coolify, Dokploy |
| Custódia de código (3) | — | Git LFS (para os arquivos grandes do KiCad e do Ghidra, quando aparecerem) | Forgejo/Gitea, gocryptfs |
| Contexto de IA (2) | — | Repomix | tree-sitter avulso |
| Monetização e release (5) | — | act | Polar, Stripe CLI, GoReleaser, cargo-dist |
| Observabilidade e diagnóstico (15) | Uptime Kuma, strace, Wireshark/tshark, k6, Trivy, Penpot, Ghidra, GlitchTip (reserva do Sentry) | tcpdump (no bootstrap) | SigNoz, bpftrace (volta com o Linux nativo), vegeta, D2, Plane, Radare2 |
| Hardware e firmware (6) | FreeCAD | KiCad, InteractiveHtmlBom, tio, sigrok/PulseView | probe-rs |
| Qualidade e testes (4) | Playwright | Zod (front), Biome, Vitest | — |
| Finanças e ARCA (7) | — | — | Portfolio Performance, Ghostfolio, Beancount + Fava, hledger, ERPNext, Actual Budget, Firefly III |
| Comercial e atendimento (10) | Invoice Ninja, Cal.com, Twenty, Chatwoot, Documenso, Umami | Klaro! | BookStack, Formbricks, Logseq |
| IA (fora das 88) | Ollama, ai-jail, ai-memory, Playwright/MCP (Claude in Chrome e servidores MCP) | — | Aider, llm (CLI) |

## Delta de 06/11/2026: os 5 módulos complementares

| Módulo | Decisão |
|---|---|
| 1 · Economia de tokens | Já no setup: Repomix (`just contexto-ia`), ai-memory, roteamento local → Claude pelo LiteLLM, resposta seca no pacote do arquiteto. Corrigido: `.claudeignore` não existe (vale `permissions.deny`); Aider e `.aiderignore` ficam fora (o Claude Code é o agente); Claude 3.5 Sonnet está obsoleto; Qwen 2.5 Coder pode ser trocado pelo modelo que o `cabe.py` aprovar. |
| 2 · Custódia e engenharia reversa | Entra: padrão sala limpa no lab (alvos → specs → src, reimplementação em C# ou TypeScript) e Git LFS para firmware, Ghidra e CAD. Fora: Forgejo, Soft Serve e gocryptfs (motivos em Decisões). |
| 3 · Decisão no terminal | Já entrou como `just triagem` e `just arquiteto`. Novo: o pacote do arquiteto traz um link do grep.app com as palavras do pedido, para você abrir. Ele não gera Zod nem Vitest sozinho: quem gera é o Claude, a partir do pacote. |
| 4 · Nuvem própria | Kamal já é o caminho (ADR 0005), começando na VM grátis da Oracle. EC2 e Azure VM pagas e o monorepo único ficam fora agora. |
| 5 · Complementares | n8n já está no setup. SvelteKit, Astro, Plunk, React Email, Akaunting, HeyForm e Plausible ficam fora: cada um repete algo que já existe. |

## Topologia da máquina

O documento propõe `~/dev/commercial`, `~/dev/hardware`, `~/dev/re-lab` e `~/notes`. O setup mantém a árvore que já existe (`~/dev/<projeto>`, um repositório por sistema AM, o vault do Obsidian e `~/AMtech/entrada`), porque mudar pastas quebraria os scripts, o ai-jail e o acervo. O lab de engenharia reversa continua em `infra/lab-alvo`, isolado e sem internet; os projetos de placa entram como repositórios próprios em `~/dev` (ex.: `~/dev/sensor-agro`), com Git LFS para arquivos grandes.

## Comandos

```bash
cd ~/dev/dev-setup && just                                   # lista tudo
just check                                                   # antes de todo commit
just triagem "atendimento no WhatsApp com fila" --nucleo nao # montar, colar ou construir
just triagem "rebalancear a carteira ARCA" --nucleo sim --adr docs/adr
just arquiteto "módulo de aporte do AM Rendara" > /tmp/pacote.md
just contexto-ia tools/triagem                               # Repomix só da pasta
just medir "python3 tools/gerar_docs.py --check"             # hyperfine antes de trocar algo
```
