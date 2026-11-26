# CLAUDE.md: como trabalhar no dev-setup

Regras comuns a todas as IAs (quem é o Alan, o que nunca fazer, padrão de qualidade):
@infra/templates/regras-ia/regras-ia.md

Este arquivo acrescenta o que vale **só neste repositório**: os 15 papéis, como uma mudança é aprovada,
o plano em vigor e as regras de Git e de versão. Em caso de conflito, vale este arquivo.

## Os 15 papéis

Toda tarefa é vista pelos papéis que ela toca. Quando faltar algo que um papel exigiria, sugira e explique o motivo.

| # | Papel | Responsável por | Entra quando | Pronto quando (Definição de Pronto) |
|---|---|---|---|---|
| 1 | **Product Owner (PO)** | O que entra, o que sai e a ordem; critério de aceite; plano em vigor | Sempre: toda tarefa começa por ele | O pedido tem critério de aceite escrito e cabe no plano em vigor (abaixo) |
| 2 | **Arquiteto de Software** | Estrutura, fonte única, ADRs, decisões que custam caro desfazer | Ferramenta, serviço, pasta ou formato de dado novo; mudança entre módulos | Decisão registrada em ADR (`docs/adr/`) ou em `data/*.json`; sem duas fontes para a mesma coisa |
| 3 | **UX/UI Designer** | Como o Alan usa: comandos, mensagens, telas, celular | Comando novo, saída que o Alan lê, tela da Central | Mensagens diretas em pt-BR, o que fazer quando falha, cabe numa tela de celular |
| 4 | **Desenvolvedor Back-end** | Código Python/shell, APIs, integrações | Qualquer mudança em `tools/`, `scripts/` ou serviço | Funções devolvem dados (a impressão é uma camada), sem `|| true` sem comentário, testes passando |
| 5 | **Desenvolvedor Front-end** | HTML, HTMX, PWA, acessibilidade | Página gerada, painel, Central | Funciona em 390 px, contraste e foco visíveis, sem build obrigatório |
| 6 | **Administrador de Banco de Dados (DBA)** | `nucleo.db`, esquemas, migrações, backup de banco | Tabela ou coluna nova; dado que precisa sobreviver | Migração numerada, banco no backup, restauração testada |
| 7 | **QA / Testador** | Testes, `just check`, `just validar`, ponta a ponta | Toda mudança de comportamento | Teste que falha sem a mudança e passa com ela; `just check` verde; item novo no `just validar` quando for coisa que roda no PC |
| 8 | **DevOps / SRE** | Serviços, agendamentos, backup, disco, Docker, CI | Serviço, cron, tarefa do Windows, compose, CI | Sobe e para por comando, tem limite de memória, aparece no `just validar` e no resumo da manhã quando falha |
| 9 | **Segurança (inclui privacidade e LGPD)** | Segredos, portas, acesso de fora, dados pessoais, o que vai para IA na nuvem | Porta, túnel, acesso remoto, segredo, dado de aluno ou cliente, captura de IA | Só `127.0.0.1` ou Tailscale; nenhum segredo no repositório; dado sensível só local; nada exposto na rede sem decisão escrita |
| 10 | **Redator Técnico** | README, docs, CHANGELOG, ESTADO, guias | Toda mudança que o Alan precisa saber usar | Uma linha na doc certa, CHANGELOG da versão, ESTADO atualizado; nada gerado editado à mão |
| 11 | **Engenheiro de Plataforma** | A máquina refeita do zero só pelo repositório; scripts idempotentes; dotfiles | Qualquer configuração fora do repositório (`~/.config`, systemd, `settings.json`, tarefa do Windows) | Script idempotente com `--simular`, checagem no `just validar`; nada feito à mão sem script |
| 12 | **Gerente de Release / Configuração** | Versão, CHANGELOG, branches, tags, rastreio do que está instalado e configurado | Todo PR; toda configuração que pode divergir do repositório | Uma versão por PR, tag depois do merge, branch apagada, configuração conferida contra o repositório |
| 13 | **Engenheiro de IA / LLMOps** | Ollama, LiteLLM, motor, fila, ai-memory, rotas e custo de modelo | Prompt, modelo, rota, memória ou agente | Rota local para sensível testada; custo por tarefa conhecido; memória sem segredo |
| 14 | **FinOps** | Custo real (assinaturas, API, energia, disco) e teto de gasto | Assinatura, serviço novo, modelo pago, compra | Custo real medido (não estimado) e dentro do teto; entra na auditoria trimestral |
| 15 | **Analista de Negócios / Growth** | Oferta, métrica de venda, ligação do trabalho com renda | Toda tarefa: "isto ajuda a usar o setup para gerar renda?" | Métrica de negócio definida e medida toda semana |

## Como uma mudança é aprovada

- **1 responsável + 2 a 3 revisores.** Todo PR diz no corpo qual papel é o responsável e quais 2 ou 3 papéis revisaram,
  com uma linha de cada revisor ("QA: teste X cobre Y"). O responsável é o papel cujo "Entra quando" mais pesa.
- **Veto do PO.** O PO pode vetar qualquer mudança que fuja do plano em vigor, cresça o escopo sem decisão do Alan ou não tenha critério de aceite.
  Vetado, não entra, mesmo com os outros papéis a favor.
- **Merge é do Alan**, com `just aprovar N` (marca como pronto, faz o merge e só termina se o GitHub disser MERGED). O Claude nunca faz merge: `gh pr merge` e `just aprovar` estão bloqueados para ele em `.claude/settings.json`.
- **Ao fim de cada PR**, o Claude mostra só uma linha: `pronto para aprovar: ! just aprovar N`.

## Plano em vigor (desde 25/11/2026, tarde)

O congelamento de 8 semanas **saiu** por decisão do Alan (emenda da [ADR 0022](docs/adr/0022-decisoes-de-25-11-2026.md)). O objetivo agora é:

1. **Instalar e configurar todas as ferramentas de `data/ferramentas.json`**, menos os túneis para a internet (bore e cloudflared), que
   continuam fora pela regra de segurança.
2. **Criar a Central** como interface para usar 100% do setup, **do notebook e do celular** (pelo Tailscale), com login, CSRF,
   auditoria e PWA desde o começo, e **usuários e permissões no banco desde a v1**, para atender clientes depois sem reescrever (`organizacao_id` desde a v1, aprovado).

Ordem, em PRs pequenos, cada um com uma versão e merge do Alan: PR 4 (perfis no `just ligar`) → PR 5 (extensões do VS Code no WSL) →
PR 6 (`just instalar`) → instalar e testar perfil por perfil (sempre, trabalho, laboratório) → ADR da arquitetura da Central e plano das
telas. As regras de segurança, de Git e de versão abaixo continuam valendo.

## Git: só o Claude mexe, o merge é do Alan

- O Claude cria branch, faz commit, push e abre o PR (em rascunho até o CI passar). O Alan não precisa rodar Git.
- O hook `scripts/git-hooks/pre-push` roda o `just check` e bloqueia o push com falha. Nunca `--no-verify` (bloqueado).
- Nunca na `main` direto, nunca `push --force`, nunca `reset --hard`.
- Branch: `setup/AAAA-MM-DD-assunto` (ou `avaliacao/`, `validacao/`).
- Depois do merge, e só depois de conferir no GitHub que o estado é MERGED, o Claude atualiza a `main` local, cria a tag `vX.Y.Z` no commit do merge, envia a tag e apaga a branch (local e remota).
- Commits terminam com a linha de coautoria do Claude.

## Versão: uma por PR

- Todo PR leva **exatamente uma** versão nova: uma seção no `CHANGELOG.md` e uma linha no `ESTADO.md`. Nenhum PR sem versão, nenhum PR com duas.
- A versão é a próxima livre **no momento de abrir o PR**. Se outro PR entrar antes, o PR que entra depois troca para a próxima livre ao resolver o conflito.
- Correção: `Z` (2.46.1 → 2.46.2). Funcionalidade ou documento novo: `Y` (2.46 → 2.47). `X` só por decisão do Alan.

## Decisões em vigor

Registro completo e motivos: [ADR 0022](docs/adr/0022-decisoes-de-25-11-2026.md). **Não pergunte de novo o que está aqui**; para
mudar, o Alan decide e a ADR ganha uma nova. Ferramentas paradas ou adiadas têm `decisao`, `motivo` e `rever_em` em
`data/ferramentas.json`, e o `just validar` avisa quando a data passa.

| Assunto | Decisão (25/11/2026) |
|---|---|
| Painel | Só a Central, sem Homepage nem OliveTin; roda no notebook (VM depois da primeira renda); acesso do notebook e do celular pelo Tailscale na v1; **usuários, permissões e `organizacao_id` no banco desde a v1**, para virar ferramenta de clientes depois sem reescrever |
| Plano | **Sem congelamento** (saiu em 25/11): instalar e configurar todas as ferramentas, menos bore e cloudflared; depois a Central |
| Senhas | KeePassXC **volta** (25/11, tarde): `keepassxc-cli`, cofre `.kdbx` e `segredos.sh` voltam a ser requisito. A senha do restic continua no caderno e também vai para o cofre |
| Segredos em arquivo | `sops` **volta** |
| Backup | restic em `C:\Users\alanmateus\backup-restic`; o antigo, sem senha, em `backup-restic-senha-perdida` (não apagar); cópia no HD externo por `just backup-externo` (mesma senha), falta conectar o HD |
| Vault | `C:\Users\alanmateus\vault` (clone do GitHub); `~/dev/notas` é symlink para ele |
| IA | LiteLLM **volta**; o Ollama do setup é o do WSL; o Ollama do Windows fica só em `127.0.0.1:11435` (`scripts/wsl/ollama-windows.sh`), fechado e fora da inicialização; a 11434 é do Ollama do WSL |
| Conteúdo | Timer do pipeline **parado** por custo: precisa de chave de API paga, que o Alan não vai criar (FinOps); rever em 2027-01-20 |
| Ligar | `just ligar` = perfil sempre; `just ligar trabalho`, `sob-demanda` ou `laboratorio` sobe também o Docker do perfil (`data/ferramentas.json`); o que está parado por decisão nunca sobe |
| Rede | headscale **volta** (precisa do `config.yaml` antes de subir); bore e cloudflared **continuam desinstalados** (túnel para a internet, regra de segurança) |
| AMKaixara | Postgres, Redis e API só em `127.0.0.1`, Redis com volume nomeado (am-kaixara#26, juntado em 25/11). Postgres e Redis religados com os mesmos dados; a API não foi religada. Os 22 `.cs` apagados localmente ficam como estão até o Alan decidir |
