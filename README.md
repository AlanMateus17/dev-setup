<!-- Arquivo GERADO por tools/gerar_docs.py. Edite os dados em data/ ou o gerador. -->

# dev-setup

[![docs](https://github.com/AlanMateus17/dev-setup/actions/workflows/docs.yml/badge.svg)](https://github.com/AlanMateus17/dev-setup/actions/workflows/docs.yml)

Arquitetura completa do meu ambiente de desenvolvimento e de trabalho: do hardware ao deploy na nuvem, da criação de conteúdo à venda de cursos. Cada ferramenta tem um motivo, um lugar e conexões definidas, e toda a documentação é gerada a partir de uma única fonte de dados.

| Camadas | Blocos | Conexões | Fluxos | Contas necessárias |
|---|---|---|---|---|
| 18 | 198 | 280 | 7 | 74 |

## Por onde começar

- **[Arquitetura](docs/arquitetura.md)**: a pilha inteira, camada por camada, com o diagrama de cada uma.
- **[Fluxos de ponta a ponta](docs/fluxos.md)**: codar com agente e publicar, vender um curso, laboratório de segurança e outros.
- **Diagrama interativo**: baixe [`docs/index.html`](docs/index.html) e abra no navegador. Toque em qualquer bloco para ver as conexões dele.
- **[Toda a documentação](docs/README.md)**

## A pilha

```mermaid
flowchart TB
  L_pub["18 · Público e canais"]
  L_venda["17 · Plataformas de venda e recebimento"]
  L_emp["16 · Pessoa física: impostos e finanças"]
  L_web["15 · Vitrine web (sites e domínio)"]
  L_prod["14 · Produtos (o que você vende)"]
  L_est["13 · Estudo e carreira"]
  L_cont["12 · Produção de conteúdo"]
  L_nuvem["11 · Nuvem, código e entrega"]
  L_app["10 · Aplicação: sistemas AM (Aura)"]
  L_obs["09 · Observabilidade"]
  L_cnt["08 · Containers, Kubernetes e infra como código"]
  L_clc["07 · Claude: recursos, conectores e plugins"]
  L_chat["06 · Assistentes de IA (chat, pesquisa e estudo)"]
  L_ia["05 · Agentes de IA e sandbox"]
  L_lin["04 · Linux (Ubuntu no WSL2, Arch no 2º disco)"]
  L_win["03 · Windows 11, apps e máquinas virtuais"]
  L_seg["02 · Segurança e cofre"]
  L_hw["01 · Hardware"]
  L_pub --- L_venda
  L_venda --- L_emp
  L_emp --- L_web
  L_web --- L_prod
  L_prod --- L_est
  L_est --- L_cont
  L_cont --- L_nuvem
  L_nuvem --- L_app
  L_app --- L_obs
  L_obs --- L_cnt
  L_cnt --- L_clc
  L_clc --- L_chat
  L_chat --- L_ia
  L_ia --- L_lin
  L_lin --- L_win
  L_win --- L_seg
  L_seg --- L_hw
  click L_pub "docs/camadas/18-pub.md"
  click L_venda "docs/camadas/17-venda.md"
  click L_emp "docs/camadas/16-emp.md"
  click L_web "docs/camadas/15-web.md"
  click L_prod "docs/camadas/14-prod.md"
  click L_est "docs/camadas/13-est.md"
  click L_cont "docs/camadas/12-cont.md"
  click L_nuvem "docs/camadas/11-nuvem.md"
  click L_app "docs/camadas/10-app.md"
  click L_obs "docs/camadas/09-obs.md"
  click L_cnt "docs/camadas/08-cnt.md"
  click L_clc "docs/camadas/07-clc.md"
  click L_chat "docs/camadas/06-chat.md"
  click L_ia "docs/camadas/05-ia.md"
  click L_lin "docs/camadas/04-lin.md"
  click L_win "docs/camadas/03-win.md"
  click L_seg "docs/camadas/02-seg.md"
  click L_hw "docs/camadas/01-hw.md"
  classDef cam fill:#e2ecec,stroke:#0e3a45,color:#13262b
  class L_pub,L_venda,L_emp,L_web,L_prod,L_est,L_cont,L_nuvem,L_app,L_obs,L_cnt,L_clc,L_chat,L_ia,L_lin,L_win,L_seg,L_hw cam
```

## A ideia em uma frase

O Windows cuida só do que precisa de janela, GPU e segurança; todo o trabalho de engenharia roda em Linux (Ubuntu no WSL2), em containers, e sai para a nuvem por CI/CD. Agentes de IA trabalham dentro de uma sandbox que só enxerga a pasta do projeto.

## Camadas

| # | Camada | Blocos | Destaques |
|---|---|---|---|
| 18 | [Público e canais](docs/camadas/18-pub.md) | 8 | Meta Business Suite, Instagram, YouTube, LinkedIn… |
| 17 | [Plataformas de venda e recebimento](docs/camadas/17-venda.md) | 14 | Pix Automático + gateway (ex.: Asaas), Agenda online (Cal.com), Comunidade (Discord ou grupo), Anúncios (Meta Ads)… |
| 16 | [Pessoa física: impostos e finanças](docs/camadas/16-emp.md) | 11 | Registro de marca (INPI), Termos, privacidade (LGPD) e contratos, Certificado digital (e-CNPJ), API de NFS-e (ex.: Focus NFe)… |
| 15 | [Vitrine web (sites e domínio)](docs/camadas/15-web.md) | 9 | E-mail profissional (enviar e receber), Domínio (Registro.br), Site pessoal + blog (Jekyll), Instituto AMS… |
| 14 | [Produtos (o que você vende)](docs/camadas/14-prod.md) | 7 | Mini-curso Lógica de Programação, Formações (TI, Matemática, Finanças), Templates e código-fonte, Livro Lógica e Máquina… |
| 13 | [Estudo e carreira](docs/camadas/13-est.md) | 6 | Microsoft Learn + AWS Skill Builder, TryHackMe / Hack The Box, Alura · Rocketseat · DIO · Udemy, Anki… |
| 12 | [Produção de conteúdo](docs/camadas/12-cont.md) | 6 | OBS Studio, DaVinci Resolve ou Kdenlive, Audacity, Canva · Krita · Inkscape… |
| 11 | [Nuvem, código e entrega](docs/camadas/11-nuvem.md) | 15 | Armazenamento de arquivos (Blob/R2), E-mail transacional (Resend, SES…), SonarQube Cloud, Projects · ADRs · MkDocs… |
| 10 | [Aplicação: sistemas AM (Aura)](docs/camadas/10-app.md) | 15 | OpenAPI + Scalar, PostGIS + MapLibre, Storybook, Clean Arch + DDD… |
| 09 | [Observabilidade](docs/camadas/09-obs.md) | 8 | Sentry (erros), Uptime Kuma, Seq (logs), Loki + Tempo… |
| 08 | [Containers, Kubernetes e infra como código](docs/camadas/08-cnt.md) | 13 | Caddy (proxy + HTTPS), Mailpit, Kafka, kubectl · Helm · k9s… |
| 07 | [Claude: recursos, conectores e plugins](docs/camadas/07-clc.md) | 18 | Projects + memória, Artifacts (Docs, Slides, Sheets…), Pesquisa aprofundada, Tarefas agendadas… |
| 06 | [Assistentes de IA (chat, pesquisa e estudo)](docs/camadas/06-chat.md) | 10 | Claude (app), ChatGPT, Gemini (pago), NotebookLM… |
| 05 | [Agentes de IA e sandbox](docs/camadas/05-ia.md) | 8 | Modelos locais: Qwen · Gemma · Llama, Base de conhecimento (RAG) das suas notas, Claude Code, ai-jail… |
| 04 | [Linux (Ubuntu no WSL2, Arch no 2º disco)](docs/camadas/04-lin.md) | 9 | Neovim, nmap · dig · curl · Wireshark, Ubuntu (WSL2), Git + SSH + gh… |
| 03 | [Windows 11, apps e máquinas virtuais](docs/camadas/03-win.md) | 21 | Tailscale (VPN), .wslconfig + localhost, Terminal · PowerShell · winget, Excalidraw / draw.io… |
| 02 | [Segurança e cofre](docs/camadas/02-seg.md) | 9 | Commits assinados (chave SSH), restic (backup criptografado), Chave física (YubiKey), TPM + Secure Boot… |
| 01 | [Hardware](docs/camadas/01-hw.md) | 11 | Nobreak, Base com cooler, SSD SATA 2,5", Acer Nitro (32 GB, GTX 1650)… |

## Stack fixa dos sistemas

C#/.NET 10 · ASP.NET Core (Controllers) · Clean Architecture + DDD · PostgreSQL · Redis · SignalR · TypeScript, Next.js e Tailwind · Docker · GitHub Actions. Rejeitadas de propósito: Bun, Hono, Rust, Tauri e gRPC. Decisões em [`docs/adr`](docs/adr).

## Como este repositório funciona

```mermaid
flowchart LR
  D["data/ecossistema.json<br/>data/mapa.json"] --> G["tools/gerar_docs.py"]
  G --> M["docs/*.md<br/>18 páginas de camada"]
  G --> H["docs/index.html<br/>diagrama interativo"]
  G --> R["README.md"]
  CI["GitHub Actions"] -->|"valida e confere"| G
```

1. Tudo nasce em [`data/`](data): camadas, blocos, conexões, fluxos, contas e o plano.
2. `python tools/gerar_docs.py` valida os dados (ids, conexões quebradas, rótulos) e regenera as páginas, o diagrama e este README.
3. O GitHub Actions roda `python tools/gerar_docs.py --check` a cada push: se os dados tiverem erro ou os arquivos gerados estiverem desatualizados, o build falha.

## Estrutura

```
data/                 fonte única: ecossistema.json e mapa.json
docs/
  arquitetura.md      a pilha e as ligações entre camadas
  camadas/            uma página por camada, com diagrama e conexões de cada bloco
  fluxos.md           fluxos de ponta a ponta
  contas.md, auditoria.md, nuvem.md, roteiro.md, ...
  adr/                decisões de arquitetura
  index.html          diagrama interativo (gerado)
  mapa.html           sistemas, nuvens, mercado e ordem de estudo
scripts/windows/      inventário somente leitura do Windows
tools/                gerador e template do diagrama
```

## Status

Em construção por fases. A fase 1 (Windows, WSL2, Docker e .NET) está em andamento; o restante segue o [roteiro de estudo](docs/roteiro.md).

## Licença

[MIT](LICENSE)
