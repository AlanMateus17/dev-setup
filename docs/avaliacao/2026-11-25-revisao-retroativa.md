<!-- Escrito à mão. Revisão retroativa do dia 25/11/2026 (v2.45.0 a v2.46.1, limpeza e inventário), feita a pedido do Alan com 15 papéis. -->

# Revisão retroativa de 25/11/2026 (15 papéis)

[← Índice da documentação](../README.md) · Avaliação do dia: [2026-11-25-avaliacao-completa.md](2026-11-25-avaliacao-completa.md) · Validação: [docs/operacao/validacao.md](../operacao/validacao.md)

**O que foi revisto:** tudo o que mudou em 25/11: ai-memory (PR #26), avaliação, portas, CI e backup (v2.45.0), plano de hardware (v2.46.0), tarefa que acorda o WSL (v2.46.1), backup restic novo, limpeza do PC (cerca de 24 GB no C: e 15,7 GB no Docker), vault no Windows e inventário de ferramentas.

**Papéis:** os 10 da avaliação mais 5 novos, que são o foco: **FinOps**, **Privacidade/LGPD**, **Engenheiro de IA/MLOps**, **Engenheiro de Plataforma** e **Comercial/Growth**.

**Congelamento (decisão de 25/11):** nenhum item abaixo cria área, oferta, fase ou ferramenta nova. Tudo é conserto, higiene ou execução das fases B a D já existentes.

---

## 1. Os achados que o Alan já tinha

| # | Achado | Veredito | O que a conferência mostrou |
|---|---|---|---|
| 1 | Configurações feitas à mão fora do repositório | **Confirmado, e maior** | Além de `backup.env`, symlink do vault e `settings.json` dos hooks: a unit `ai-memory.service`, o registro do MCP (`~/.claude.json`), a cópia dos hooks em `~/.local/share/ai-memory/hooks`, o repositório restic (`restic init`) e o `docker update --restart=no` de headscale e ghostfolio. Nada disso é recriado por script. |
| 2 | `backup.env.example` desatualizado (`/mnt/d`) | **Confirmado** | Aponta para `/mnt/d/backup-restic`, que no WSL é uma pasta dentro do próprio disco virtual, e inclui `$HOME/financas`, que não existe (o restic termina com erro). Falta o vault (`/mnt/c/Users/alanmateus/vault`) e `~/arquivo`. |
| 3 | Branches juntadas não apagadas | **Confirmado** | 26 branches remotas já juntadas à main (de `amtech-os-0.1` a `setup/2026-11-25-ai-memory-hooks`). Só 2 não estão juntadas. |
| 4 | `ESTADO.md` desatualizado | **Confirmado** | Diz que a v2.45.0 é "PR rascunho" e que "hoje não há backup", e repete as 3 decisões como pendentes. Já estão decididas (só a Central, congelamento de 8 semanas, Central no notebook), mas **não existe a ADR 0022**: as decisões só estão na conversa. |
| 5 | ai-memory gravando possíveis segredos | **Corrigido: risco real, sem vazamento** | As 324 capturas foram varridas por padrões de token do GitHub, chave privada, `sk-`, AWS, `Bearer` e `senha=`: 1 ocorrência, e era falso positivo (o texto `${GHOSTFOLIO_DB_SENHA:?defina…}` do compose). O risco continua: o hook captura entrada e saída de ferramentas, e um `cat` num `.env` iria para o banco. A resposta do Claude não é capturada (`capture_assistant = false`). |
| 6 | Dois Ollama | **Confirmado, e pior** | O do Windows (instalado pelo winget) roda e escuta em **todas as interfaces** (`::`, porta 11434), sem senha. O do WSL escuta só em 127.0.0.1. Os dois disputam a mesma GTX 1650. |
| 7 | Falta teste para "sensível só local" | **Parcial** | O motor tem teste (`tools/motor/test_motor.py`: texto com CPF vira sensível e ganha a restrição). Falta o teste **de ponta a ponta**: que a fila (`tools/remoto/fila.py`) mande pedido sensível só para o modelo local e que o LiteLLM nunca encaminhe esse pedido a um modelo na nuvem. |
| 8 | Custos reais não medidos | **Confirmado** | O `data/custos.json` tem decisões e estimativas (teto de US$ 20 por mês no LiteLLM, ADR 0009), mas nenhuma medição: fatura do Claude, uso do LiteLLM (fora do ar), energia do notebook ligado 24 h, espaço em disco. |
| 9 | Nenhuma oferta escolhida para as 8 semanas | **Confirmado** | A onda 0 tem 4 candidatas e nenhuma escolhida: `minicurso` (construção), `catalogo` (lançado, grátis), `rendara` (validação) e `dark` (construção). Sem a escolha, o congelamento não tem para onde apontar o tempo liberado. |

## 2. O que ainda não estava na lista

| # | Achado | Papel | Gravidade |
|---|---|---|---|
| N1 | **O `Cofre.kdbx` não muda desde 08/11.** A senha nova do restic (25/11) não está nele, ou está em outro arquivo. Sem ela, o backup não abre | Segurança, DevOps | **Crítico** |
| N2 | **O cofre de senhas não entra no backup**: `Documents\Cofre\Cofre.kdbx` fica fora do `BACKUP_PASTAS` | DevOps, Segurança | **Crítico** |
| N3 | **Backup só no mesmo SSD.** O repositório restic está em `C:\Users\alanmateus\backup-restic`: falha do disco ou roubo do notebook leva tudo. Falta a cópia fora (regra 3-2-1) | DevOps | **Crítico** |
| N4 | **AMKaixara publica Postgres (5432) e Redis (6379) em `0.0.0.0`**, alcançáveis pela rede local (compose em `aura-workspace\AMKaixara`) | Segurança | Alto |
| N5 | **O `restart=no` de headscale e ghostfolio some no próximo `up`**: o compose ainda diz `unless-stopped`, e o loop volta | DevOps | Alto |
| N6 | **headscale:** o `config.yaml` nunca entrou no repositório; o Docker criou uma pasta vazia de dono root no lugar. **ghostfolio:** `sslmode=prefer` + Prisma 7.10 exige TLS que o Postgres interno não tem | Back-end, DevOps | Médio |
| N7 | **Hooks do ai-memory em cópia manual.** A cópia em `~/.local/share` não acompanha o repositório e nada confere se as duas batem. Se o caminho quebrar, o `PreToolUse` bloqueia todas as ferramentas (aconteceu em 25/11) | Plataforma, QA | Médio |
| N8 | **O `just validar` não confere** ai-memory, hooks, MCP, tarefa "AMtech acordar backup", "temporizadores de despertar" nem a idade do último `validar --restaurar` | QA | Médio |
| N9 | **Ninguém agendou o teste de restauração.** Ele foi feito uma vez à mão; a avaliação pedia `just validar` semanal pelo cron | QA, DevOps | Médio |
| N10 | **A tarefa das 22h20 não foi testada com o WSL desligado**: o teste foi com o WSL já ligado | QA | Médio |
| N11 | **Nenhuma fonte única de ferramentas.** Windows em `pacotes.json`, extensões num `.txt`, CLIs dentro de 6 scripts, serviços em 10 compose e o `verificar.sh` com lista própria | Plataforma, Arquiteto | Médio |
| N12 | **Nenhum serviço Docker tem limite de memória**: os 40 somam cerca de 8,8 GB, para 20 GB do WSL | DevOps | Médio |
| N13 | **Programas instalados fora do inventário**: cloudflared (túnel para a internet) no Windows e o `bore` (expõe porta local na internet) no `mise`, sem regra de uso | Segurança | Médio |
| N14 | **O PR #26 (ai-memory) não ganhou versão nem entrada no CHANGELOG**, ao contrário da regra do repositório | Redator Técnico | Baixo |
| N15 | **Sobras:** `~/dev/notas.antigo-20261125`, `tools/nucleo/github_memoria.py` e `infra/soberania/ai-memory/` (da ponte antiga, fora do Git), container `focused_hawking` parado, `~/arquivo` repetido no `BACKUP_PASTAS`, vault parado na branch do PR #5 | Plataforma | Baixo |
| N16 | **O Temp volta a encher**: o instalador do Visual Studio deixa cerca de 176 MB por dia | DevOps | Baixo |
| N17 | **Processo:** numa sequência de comandos, um `git clone` falhou e os seguintes rodaram na pasta errada (mudaram o `core.filemode` do dev-setup; foi desfeito). Os scripts novos devem parar no primeiro erro | Plataforma, QA | Baixo |

## 3. Visão por papel (foco nos 5 novos)

### FinOps (novo)
- **Hoje:** nenhum custo medido; o teto do LiteLLM (US$ 20 por mês) não tem como ser conferido porque o LiteLLM está fora do ar por decisão.
- **O que faltava:** uma planilha mensal de 4 números reais: assinatura do Claude, gastos em API (zero hoje), energia (notebook 24 h na tomada) e espaço (disco usado em C: e no backup). Os 4 entram no resumo da manhã uma vez por mês.
- **Ganho de hoje para registrar:** a limpeza liberou cerca de 24 GB no C: e 15,7 GB dentro do disco do Docker (volta ao C: depois de compactar os vhdx).

### Privacidade/LGPD (novo)
- **ai-memory:** sem vazamento hoje (seção 1, item 5). Falta uma conferência semanal das capturas com os mesmos padrões e a regra escrita: **nunca** `cat`, `less` ou `grep` em `.env`, `~/.config/amtech`, `.kdbx` ou `~/.ssh` (o `permissions.deny` já bloqueia o Claude; o risco é o terminal de outro agente).
- **"Sensível só local":** falta o teste de ponta a ponta (seção 1, item 7).
- **Dados de alunos e clientes:** nada foi para a nuvem hoje. O AMKaixara expõe banco e Redis na rede local (N4): se ele tiver dado de cliente, isso é incidente de LGPD em potencial.

### Engenheiro de IA/MLOps (novo)
- **Dois Ollama** (item 6). Fica o do WSL, que é o do `just ligar`, das rotas do LiteLLM e da fila.
- **ai-memory** instalado e capturando. Falta conferir se a memória ajuda de fato (o `ai-memory doctor` e o `recent` numa sessão nova) antes de expandir para outros agentes.
- **LiteLLM e motor parados por decisão:** registrar como "parado", não como falha, para o `just validar` não acusar.

### Engenheiro de Plataforma (novo)
- **Princípio:** tudo o que foi feito à mão em 25/11 (item 1) precisa de um script idempotente e de uma checagem no `just validar`; a máquina tem de poder ser refeita do zero só pelo repositório e pelo cofre.
- **Ordem:** `backup.env.example` certo → `scripts/wsl/ai-memory.sh` (binário, unit, hooks, MCP) → `vault.sh` aceitar o vault no Windows com symlink → fonte única de ferramentas (N11).

### Comercial/Growth (novo)
- **Escolher uma oferta só para as 8 semanas** (item 9). A candidata natural é o **`minicurso`**: já está em construção, o `catalogo` (lançado e grátis) já é a isca, e o próximo passo está escrito ("gravar as 5 primeiras aulas e abrir a pré-venda"). O `dark` (3 vídeos por semana) compete pelo mesmo tempo.
- **Métrica das 8 semanas:** pré-vendas do mini-curso e inscritos vindos do catálogo, medidos toda semana.

### Os 10 papéis da avaliação, em uma linha cada
- **Product Owner:** decisões de 25/11 sem ADR (item 4) e oferta sem escolha (item 9).
- **Arquiteto:** fonte única de ferramentas (N11); a Central continua sendo o único painel.
- **UX/UI:** o caminho do vault mudou para `C:\Users\alanmateus\vault`; o `vault.sh` ainda manda abrir `\\wsl.localhost\…\dev\notas`.
- **Back-end:** ghostfolio (`sslmode`) e headscale (N6).
- **Front-end:** sem mudança hoje.
- **DBA:** `nucleo.db` já entra no backup (confirmado no snapshot `50b698a3`); o banco do ai-memory (`~/.local/share/ai-memory`) não entra.
- **QA:** N8, N9, N10 e o teste de ponta a ponta do item 7.
- **DevOps/SRE:** N1, N2, N3, N5 e N12.
- **Segurança:** Ollama do Windows (item 6), N4 e N13.
- **Redator Técnico:** ESTADO (item 4) e N14.

## 4. Itens priorizados (entram nas fases B a D, sem fase nova)

| Prioridade | Item | Fase | Quem | Pronto quando |
|---|---|---|---|---|
| **P0** | Conferir se a senha do restic está no KeePassXC (N1); se não, salvar agora | B | Alan | Entrada "restic - backup notebook" existe e o `Cofre.kdbx` tem data de hoje |
| **P0** | Cofre `.kdbx` no backup (N2) | B | Alan | `BACKUP_PASTAS` inclui `/mnt/c/Users/alanmateus/Documents/Cofre` e o snapshot mostra o arquivo |
| **P0** | Segunda cópia do backup fora deste SSD (N3) | B | Alan + Claude | `restic copy` para um HD externo ou B2, e restauração testada a partir dela |
| **P0** | Ollama do Windows: desinstalar ou `OLLAMA_HOST=127.0.0.1` (item 6) | D | Alan decide, Claude faz | `Get-NetTCPConnection -LocalPort 11434` só em 127.0.0.1 |
| **P0** | AMKaixara: Postgres e Redis em `127.0.0.1:` (N4) | D | Claude (PR no repositório do AMKaixara) | `ss`/`Get-NetTCPConnection` sem 0.0.0.0 nas portas 5432 e 6379 |
| **P1** | ADR 0022 com as 3 decisões de 25/11 e `ESTADO.md` atualizado (item 4) | C0 | Claude | ADR escrita, ESTADO sem pendência já resolvida |
| **P1** | Escolher a oferta das 8 semanas (item 9; sugestão: `minicurso`) | E | Alan | Oferta marcada no `data/portfolio.json` e métrica semanal no resumo da manhã |
| **P1** | `backup.env.example` certo (item 2) | D | Claude | Repositório em `/mnt/c/...`, sem `financas`, com vault, `~/arquivo` e cofre |
| **P1** | Compose: ghostfolio `sslmode=disable`; headscale com modelo de config ou fora do perfil padrão (N5, N6) | D | Claude | `docker compose up` não volta a entrar em loop |
| **P1** | `scripts/wsl/ai-memory.sh` idempotente + checagem no `just validar` (item 1, N7) | D | Claude | Máquina nova fica com servidor, hooks e MCP só com o script; `validar` acusa cópia dos hooks diferente do repositório |
| **P1** | `just validar --restaurar` agendado toda semana (N9) | D | Claude | Linha no cron; o resultado aparece no resumo da manhã |
| **P2** | Teste de ponta a ponta "sensível só local" na fila (item 7) | D | Claude | Teste falha se pedido com CPF chegar a modelo remoto |
| **P2** | Conferência semanal das capturas do ai-memory (Privacidade) | D | Claude | Script lê o banco só para contar e avisa se achar padrão de segredo |
| **P2** | Planilha mensal de custos reais (item 8) | D | Alan + Claude | 4 números reais por mês no `data/custos.json` |
| **P2** | `vault.sh` aceita o vault no Windows com symlink (UX) | D | Claude | `bash scripts/wsl/vault.sh --simular` reconhece o symlink e mostra o caminho certo para o Obsidian |
| **P2** | Fonte única de ferramentas e `mem_limit` nos serviços (N11, N12) | D | Claude | `data/ferramentas.json` + docs geradas + `validar`; todo serviço com limite |
| **P2** | cloudflared e `bore` com regra de uso, ou fora (N13) | D | Alan decide | Registrados no inventário com a regra, ou desinstalados |
| **P2** | Testar a tarefa das 22h20 com o WSL desligado; habilitar temporizadores de despertar (N10) | B | Alan | No dia seguinte, `just validar` com o backup OK a partir de WSL desligado |
| **P3** | Apagar as 26 branches juntadas (item 3) e as sobras (N15) | D | Alan aprova a lista, Claude apaga | `git branch -r --merged` só com a main |
| **P3** | Versão e CHANGELOG do ai-memory (N14) | D | Claude | Entrada no CHANGELOG |
| **P3** | Limpeza mensal do Temp (N16) e scripts com parada no primeiro erro (N17) | D | Claude | Agendada; scripts novos com `set -euo pipefail` |
