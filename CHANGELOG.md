# Changelog

Formato baseado em [Keep a Changelog](https://keepachangelog.com/pt-BR/1.1.0/).

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
