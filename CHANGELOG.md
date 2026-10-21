# Changelog

Formato baseado em [Keep a Changelog](https://keepachangelog.com/pt-BR/1.1.0/).

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
