# Changelog

Formato baseado em [Keep a Changelog](https://keepachangelog.com/pt-BR/1.1.0/).

## [1.9.0] - 2026-10-23

### Corrigido
- O roteiro de implantação cobria só parte do setup (cerca de 176 dos 303 blocos). Agora cada passo diz quais blocos implanta e todos os 303 têm lugar: 214 em passos, 9 peças a construir, 3 que não se instalam e 77 para depois.
- Blocos n8n, banco de métricas, painel de lucro, webhooks de venda e aprovação no celular deixam de ser "futuro": a implantação já os coloca no ar.

### Adicionado
- Roteiro com 18 fases e 129 passos: hardware, Defender, Claude in Chrome, extensões do VS Code, dotfiles, Obsidian Git, Syncthing, ADRs, MCP, ai-memory, RAG, recursos do Claude, conectores e plugins, outros assistentes, estúdio de conteúdo, WhatsApp Business, sites, Umami, Hostinger, vendas e finanças no CPF (gov.br, banco, contador, LGPD, plataformas, Mercado Pago, agenda, CRM, comunidade, afiliados, UTM, ofertas, avaliações, prospecção, INPI, carnê-leão, IRPF, Caixa da Casa), base dos sistemas AM, nuvem e deploy, editora e estudo.
- `tools/implantacao/gerar.py` falha se um bloco do setup ficar fora do roteiro, se um passo citar bloco que não existe ou se um bloco estiver em dois lugares; roteiro e acompanhamento mostram o que cada passo implanta e a cobertura completa. 5 testes novos.
- `scripts/wsl/nuvem.sh`: Azure CLI, Terraform, Vercel CLI e Wrangler.
- `scripts/windows/extensoes-vscode.ps1` com `vscode-extensoes.txt` e `.vscode/extensions.json`.
- Wireshark no winget (o Unity Hub só pelo passo de decisão); nmap e dnsutils no `bootstrap.sh`; `verificar.sh` confere as ferramentas novas como opcionais.

## [1.8.0] - 2026-10-21

### Adicionado
- Implantação: `data/implantacao.json` com 11 fases e 58 passos, gerando `docs/implantacao/roteiro.md` e `acompanhamento.html`.
- `scripts/windows/instalar.ps1` e `verificar.ps1` (winget com IDs conferidos, WSL2, .wslconfig, segurança).
- `scripts/wsl/bootstrap.sh`, `verificar.sh` e `ativar-pipeline.sh` (ferramentas, .NET 10, Node, uv, gitleaks, trivy, Claude Code, ai-jail, Git assinado, pastas, timer).
- `infra/automacao/`: Docker Compose com n8n, banco de métricas (esquema, views de lucro e de melhor horário, usuário só de leitura), Grafana e Uptime Kuma; `infra/postiz/README.md`.
- `tools/conteudo/processar.py`: pipeline de conteúdo com transcrição local, guia de marca, fila de aprovação e aviso no Telegram, com 10 testes.
- `config/marca.md`: guia de marca para preencher.
- CI: job novo com ShellCheck, PSScriptAnalyzer e validação do Docker Compose.

## [1.7.1] - 2026-10-21

### Corrigido
- `docs/mapa.html` estava escrito à mão e mostrava 10 camadas e 5 fluxos antigos. Agora é gerado de `tools/mapa.template.html` com `data/ecossistema.json` e `data/mapa.json`: as 22 camadas, os 299 blocos com conexões e os 13 fluxos, conferido no CI.
- Receita do ponto de retirada corrigida de R$ 1.150 para R$ 1.140, como dá o motor financeiro.
- Os dados embutidos no planejador e no portfólio escapam `</` para não quebrar a página.

### Adicionado
- `tools/negocios/test_coerencia.py`: confere se os números escritos nos documentos batem com o motor financeiro e com o portfólio.

## [1.7.0] - 2026-10-21

### Adicionado
- `docs/operacao/`: esteira de ofertas, marca e presença, flywheel de conteúdo, automação e escala, padrão de qualidade, clientes e dados, ordem de execução.
- `data/portfolio.json` com 47 ofertas (14 fontes de renda novas) e `tools/portfolio/portfolio.py`, que valida, pontua e gera `docs/operacao/portfolio.md` e `portfolio.html`, com testes no CI.
- Camada "Operação do grupo", 18 blocos (incluindo os agentes do grupo) e o fluxo "Do trabalho ao conteúdo".

## [1.6.0] - 2026-10-21

### Adicionado
- `docs/negocios/`: os nove negócios do grupo em Barbacena (software, loja, peças, Maker, ponto de retirada, entregas e Flex, delivery, sushi, cafeteria, padaria), estrutura de CNPJs, ordem com portões, cardápios e desperdício, mínimo legal e sistemas.
- `data/negocios.json` e `tools/negocios/financas.py`: motor financeiro com Simples por anexo, ponto de equilíbrio, rampa, retorno e capital mínimo, com testes no CI.
- `docs/negocios/numeros.md` e `docs/negocios/planejador.html` (planejador interativo), gerados e conferidos no CI.
- Camada "Negócios do grupo", 18 blocos, 34 conexões e o fluxo "Abrir o próximo negócio".

## [1.5.0] - 2026-10-21

### Adicionado
- `docs/editora/10-imagens-e-figuras.md`: acervos, regras de licença, busca automática e figuras geradas por código.
- `docs/editora/11-automacao-e-metodo.md`: o método de criação dentro do pipeline e o que é automático.
- `tools/editora/tabela_verdade.py` com testes, rodando no CI.
- 11 blocos e o fluxo "Ilustrar um capítulo".

## [1.4.0] - 2026-10-21

### Adicionado
- `docs/editora/09-nivel-e-concursos.md`: caminho único, livro autocontido, matemática e física da TI, concursos PF, PRF e Forças Armadas, critério de domínio.
- Blocos Matriz de editais, Projeto do capítulo e Mapa de pré-requisitos.
- Critérios 11 a 13 na avaliação do livro; itens novos no checklist de rigor.

## [1.3.0] - 2026-10-21

### Adicionado
- Camada "Editora AMS Silva (produção de livros)" com 22 blocos: selo, repositório do livro, modelo de criação, fonte única, exercícios em YAML, pranchas TikZ, classe LaTeX, pipeline do livro, revisão automática, agentes, leitores beta, errata, ISBN, ficha catalográfica, depósito legal, KDP, gráfica sob demanda, kit, curso, edição do professor, traduções e quadro de referências.
- Fluxo "Produzir um capítulo do livro".
- Plano da editora em `docs/editora/` (8 documentos).

## [1.2.0] - 2026-10-20

### Adicionado
- `docs/marketing/11-canais-de-anuncio.md`: todos os canais de anúncio com o limite de custo de cada um.
- `docs/infra/`: vários computadores, SSD externo, NAS local e armazenamento em nuvem.
- Blocos de Spotify, Kwai, Pinterest, LinkedIn, mídia nativa e influenciadores; SSD externo, workstation, Syncthing, Backblaze B2 e GPU por hora.

### Alterado
- Servidor caseiro detalhado (NAS + serviços 24 h).

## [1.1.0] - 2026-10-20

### Adicionado
- Camada 18 "Marketing, automação e medição" (Postiz, aprovação no celular, algoritmo de horário, Pixel + CAPI, UTM, regras de corte, webhooks, banco de métricas, painel de lucro, afiliados, prospecção, dublagem).
- TikTok e Facebook na camada de público; voz clonada com ElevenLabs.
- Fluxos "Publicar automaticamente no melhor horário" e "Medir o lucro de uma campanha".
- Plano de marketing, vendas e automação em `docs/marketing/` (10 documentos).

### Alterado
- O gerador remove páginas de camada que deixaram de existir.
- Diagramas Mermaid sem cliques (o GitHub não os abre); a navegação fica nas tabelas.

## [1.0.0] - 2026-10-20

### Adicionado
- Fonte única de dados em `data/` (18 camadas, blocos, conexões, fluxos, contas, auditoria e plano de estudo).
- Gerador `tools/gerar_docs.py` com validação dos dados.
- Uma página por camada em `docs/camadas/`, com diagrama Mermaid e tabela de conexões de cada bloco.
- Arquitetura, fluxos de ponta a ponta, contas, auditoria, sistemas operacionais, nuvem, mercado, roteiro, peças autorais e cortes.
- Diagrama interativo `docs/index.html`, gerado a partir dos mesmos dados.
- ADRs 0001 a 0003.
- Script de inventário somente leitura do Windows.
- Workflow do GitHub Actions que valida os dados e confere os arquivos gerados.
