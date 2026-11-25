# Validação do setup de ponta a ponta

[← Operação](README.md)

Rodada de 25/11/2026 (ramo `validacao-setup`). Refaça a qualquer hora com:

```bash
cd ~/dev/dev-setup && just validar
```

`just validar --rapido` pula o `just check`; `just validar --restaurar` também restaura o último snapshot **real** do restic numa pasta temporária (demora). Nada lê nem imprime segredo.

> **Onde isto rodou:** o PC não estava ligado à sessão (nenhuma pasta compartilhada pelo Remote Control). A coluna "Roda no PC" foi rodada num **Ubuntu 24.04 na nuvem**, a mesma base do WSL. O que só existe no PC (cofre, disco do backup, cron, Ollama, Docker, vault) ficou como PRECISA DE MIM. O `just validar` no WSL fecha essas células.

Legenda: OK · FALHA (motivo) · NÃO EXISTE · PRECISA DE MIM (o que fazer).

## Matriz: caminho crítico

| Item | Testes | Roda no PC | Roda sozinho | Integração |
|---|---|---|---|---|
| 1. Instalação (`bootstrap-simular`, `verificar`, `os-simular`) | OK (implantacao, vault, sessao) | OK depois do conserto: o `just` 1.21 do apt (Ubuntu 24.04) não lia o justfile; agora `bootstrap-simular` e `os-simular` rodam (0 erros, 3 avisos). `verificar` lista 11 faltas, esperado numa máquina zerada. **PRECISA DE MIM:** `just verificar` no WSL | NÃO EXISTE (instalação é manual) | OK (GitHub pela API REST) |
| 2. Segredos (KeePassXC, sops/age) | OK (seguranca) | age cifra e decifra: OK. **PRECISA DE MIM:** `keepassxc-cli` e o cofre `.kdbx` só existem no PC; o sops entra pelo `extras.sh` | NÃO EXISTE (não se aplica) | NÃO EXISTE (sops/age na VM é fase futura, ADR 0009; nenhum script usa sops ainda) |
| 3. Backup (restic) | OK (ensaio novo em `tools/validar`; antes não havia teste) | Backup e restauração ensaiados: OK (repositório descartável). FALHA corrigida: o evento `backup.concluido` nunca chegava ao núcleo. **PRECISA DE MIM:** `~/.config/amtech/backup.env` e `just validar --restaurar` no repositório real | PRECISA DE MIM (cron das 22h30 pelo `agendar.sh --aplicar`, com o WSL aberto; ninguém viu disparar) | PRECISA DE MIM (disco do repositório restic e senha no KeePassXC) |
| 4. Motor e triagem (`triagem`, `motor`, LiteLLM, Ollama) | OK (motor, triagem, ia, remoto) | OK (`just triagem` e `just motor` rodam sem IA; o `motor-relatorio` pede `nucleo.py iniciar` antes) | PRECISA DE MIM (resumo das 6h10 no cron; a fila e o bot sobem pelo `just ligar`) | PRECISA DE MIM (Ollama e LiteLLM fora do ar: `just ligar`; o LiteLLM precisa do Docker e de `infra/ia/.env`) |
| 5. Núcleo (SQLite, eventos, agenda) | OK (nucleo) | OK (`iniciar`, `evento`, `buscar`, `agora`, `rapido`; SQLite íntegro) | PRECISA DE MIM (0 de 3 rotinas no cron; o timer `amtech-conteudo.timer` está desligado) | NÃO EXISTE (núcleo local; o PostgreSQL na VM é fase futura) |
| 6. Coerência e docs (`check`, `coerencia`, CI) | OK (coerencia, repos) | OK (`just check` verde; `just coerencia` sem trechos). FALHA corrigida: sem `~/dev`, o relatório dava traceback, escondido pelo `\|\| true`. **PRECISA DE MIM:** gitleaks (bootstrap) | OK (vigia agendado às segundas, último em 23/11 com sucesso; docs verde em todo PR; o job de grafo do Dependabot foi cancelado e não conta) | OK (GitHub responde) |
| 7. Professor e mapa (`hoje`, `trilha`, `cartoes`, `professor-mapa`) | OK (professor, registro, colher) | `hoje`, `trilha` e `cartoes`: OK. FALHA corrigida: sem MAPA.md, `professor-mapa` dava traceback; agora diz o que fazer. **PRECISA DE MIM:** mapa-de-estudo em `~/dev` | NÃO EXISTE (o Professor é sob demanda) | PRECISA DE MIM (vault e mapa-de-estudo só no PC; esta sessão não conseguiu abri-los) |

## Matriz: os outros módulos (só testes)

Todos OK (`python -m unittest discover -s tools/<pasta>`): acervo, akita, avaliador, biblioteca, carreira, cockpit, construcao, conteudo, custos, documentos, editora, empresas, fabrica, financeiro, git, investimentos, jarvis, kitsites, negocios, organizar, portfolio, radar, recrutador, recursos, roi, sites, softwares. São 41 pastas com testes no total, 0 falhas.

## O que PRECISA DE MIM, em ordem

1. **Rodar no WSL:** `cd ~/dev/dev-setup && git fetch origin validacao-setup && git switch validacao-setup && just validar`. Se preferir que eu rode, compartilhe a pasta pelo Remote Control (app Claude → Settings → Claude Code → Remote Control).
2. **Conferir o `just`:** `just --version`. Abaixo de 1.29, a `main` atual quebra em todas as receitas; este PR conserta.
3. **Backup real:** `~/.config/amtech/backup.env` (modelo em `infra/templates/backup.env.example`) e o arquivo de senha com `chmod 600`. Depois rode `just validar --restaurar`.
4. **Agendar e ver disparar:** `bash scripts/wsl/agendar.sh --aplicar` e `bash scripts/wsl/ativar-pipeline.sh`. Deixe o WSL aberto às 22h30 e rode `just validar` no dia seguinte: a coluna "Roda sozinho" confere o cron, o `~/backup-ultimo.log` (menos de 36 h) e o evento no núcleo.
5. **Segredos:** `sudo apt install keepassxc` no WSL e o cofre em `C:\Users\<você>\cofre senhas.kdbx` (ou a variável `COFRE`). Depois `bash scripts/wsl/extras.sh` para sops e age.
6. **IA local:** `just ligar` (Ollama, e LiteLLM com Docker). A chave do Gemini vai do KeePassXC para `infra/ia/.env`; não passe por aqui.
7. **gitleaks:** `bash scripts/wsl/bootstrap.sh` instala; o `just check` pula o gitleaks quando ele falta.
8. **Hostinger:** o conector não está autorizado no claude.ai. Autorize só se quiser que eu confira os sites.

## Os 5 próximos consertos, por impacto

1. **"Roda sozinho" depende do WSL aberto.** Nada do cron dispara com o notebook fechado ou o WSL parado. Para o backup das 22h30, uma tarefa do Agendador do Windows que acorda o WSL (ou o systemd do WSL ligado no `wsl.conf`) vale mais que qualquer outro conserto.
2. **Aviso de backup ausente.** Com o evento consertado, o `resumo-manha.sh` pode alertar quando não houver `backup.concluido` nas últimas 36 h. Hoje um backup que não roda fica em silêncio.
3. **Tirar os `|| true` que escondem erro.** Dois dos bugs desta rodada (evento do backup e relatório da coerência) estavam escondidos assim. Trocar por aviso explícito no `justfile` e no `backup.sh`.
4. **O bootstrap instala o `just` pelo apt.** É o 1.21 no 24.04. O `verificar.sh` deveria conferir a versão mínima, e as receitas novas não devem usar atributos de versões mais novas (o teste em `tools/validar` já barra o `[positional-arguments]`).
5. **Núcleo e IA ligados na instalação.** O `motor-relatorio` exige `nucleo.py iniciar` à mão, e Ollama e LiteLLM só sobem com `just ligar` a cada boot. O `instalar-tudo.sh` deveria iniciar o núcleo, e o `agendar.sh` poderia subir o `just ligar` no login.
