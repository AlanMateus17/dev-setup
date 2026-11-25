# Validação do setup de ponta a ponta

[← Operação](README.md)

Rodada de 25/11/2026 (ramo `validacao-setup`). Refaça a qualquer hora com:

```bash
cd ~/dev/dev-setup && just validar
```

`just validar --rapido` pula o `just check`; `just validar --restaurar` também restaura o último snapshot **real** do restic numa pasta temporária (demora). Nada lê nem imprime segredo.

> **Onde isto rodou:** primeiro num Ubuntu 24.04 na nuvem (onde apareceram os 4 consertos) e depois no **PC, pelo WSL**, com `just validar`. A matriz abaixo é a do PC, de 25/11/2026.

Legenda: OK · FALHA (motivo) · NÃO EXISTE · PRECISA DE MIM (o que fazer).

## Matriz: caminho crítico (no PC)

| Item | Testes | Roda no PC | Roda sozinho | Integração |
|---|---|---|---|---|
| 1. Instalação (`bootstrap-simular`, `verificar`, `os-simular`) | OK | PRECISA DE MIM (`just verificar` aponta 1 item obrigatório faltando; simulações OK) | NÃO EXISTE (instalação é manual) | OK (GitHub) |
| 2. Segredos (KeePassXC, sops/age) | OK | PRECISA DE MIM (cofre `.kdbx` encontrado; faltam `keepassxc-cli`, age e sops no WSL) | NÃO EXISTE (não se aplica) | NÃO EXISTE (sops/age na VM é fase futura, ADR 0009) |
| 3. Backup (restic) | OK | PRECISA DE MIM (falta `~/.config/amtech/backup.env`; o ensaio com repositório descartável passou na nuvem) | **FALHA** (o cron das 22h30 está aplicado, mas não houve backup nas últimas 36 h: sem o `backup.env`, o `backup.sh` sai com erro toda noite) | PRECISA DE MIM (disco do repositório restic e senha no KeePassXC) |
| 4. Motor e triagem (`triagem`, `motor`, LiteLLM, Ollama) | OK | OK (a FALHA da rodada no PC era do próprio `validar`, que deixava a triagem esperando uma pergunta invisível; consertado) | OK (resumo das 6h10 no cron) | Ollama OK; PRECISA DE MIM: LiteLLM fora do ar (`just ligar`, precisa do Docker) |
| 5. Núcleo (SQLite, eventos, agenda) | OK | OK | PRECISA DE MIM (3 de 3 rotinas no cron OK; o timer `amtech-conteudo.timer` está parado: `bash scripts/wsl/ativar-pipeline.sh`) | NÃO EXISTE (núcleo local; o PostgreSQL na VM é fase futura) |
| 6. Coerência e docs (`check`, `coerencia`, CI) | OK | OK (`just check` verde, gitleaks presente) | OK (vigia agendado às segundas; docs verde em todo PR) | OK (GitHub) |
| 7. Professor e mapa (`hoje`, `trilha`, `cartoes`, `professor-mapa`) | OK | PRECISA DE MIM (`hoje`, `trilha` e `cartoes` OK; falta o mapa-de-estudo em `~/dev` para o `professor-mapa`) | NÃO EXISTE (o Professor é sob demanda) | OK (vault em `~/dev/notas`) |

Consertos que já estão neste PR (achados na nuvem): `just` 1.21 do apt não lia o justfile; o evento `backup.concluido` nunca chegava ao núcleo; `coerencia` e `professor-mapa` davam traceback.

## Matriz: os outros módulos (só testes)

Todos OK (`python -m unittest discover -s tools/<pasta>`): acervo, akita, avaliador, biblioteca, carreira, cockpit, construcao, conteudo, custos, documentos, editora, empresas, fabrica, financeiro, git, investimentos, jarvis, kitsites, negocios, organizar, portfolio, radar, recrutador, recursos, roi, sites, softwares. São 41 pastas com testes no total, 0 falhas.

## O que PRECISA DE MIM, em ordem

1. **Backup (urgente: hoje não existe backup).** No Ubuntu do WSL: `cp infra/templates/backup.env.example ~/.config/amtech/backup.env`, ajuste o repositório e o arquivo de senha (`chmod 600`, a mesma senha no KeePassXC), rode `just backup` uma vez e depois `just validar --restaurar`.
2. **O item que falta na instalação:** `just verificar | grep FALTA` mostra qual é.
3. **mapa-de-estudo:** `gh repo clone AlanMateus17/mapa-de-estudo ~/dev/mapa-de-estudo` e depois `just professor-mapa`.
4. **Segredos no WSL:** `sudo apt install keepassxc` e `bash scripts/wsl/extras.sh` (age e sops).
5. **Pipeline de conteúdo:** `bash scripts/wsl/ativar-pipeline.sh`.
6. **LiteLLM:** `just ligar` com o Docker aberto. A chave do Gemini vai do KeePassXC para `infra/ia/.env`; não passe por aqui.
7. **Hostinger:** o conector não está autorizado no claude.ai. Autorize só se quiser que eu confira os sites.

## Os 5 próximos consertos, por impacto

1. **Backup que falha em silêncio.** O cron roda toda noite e sai com erro (falta o `backup.env`), e ninguém percebeu. O `resumo-manha.sh` deveria alertar quando não houver `backup.concluido` nas últimas 36 h, e o aviso do Telegram precisa ser conferido.
2. **"Roda sozinho" depende do WSL aberto.** Com o notebook fechado ou o WSL parado, o cron não dispara. **Resolvido na v2.46.1:** a tarefa "AMtech acordar backup" (`scripts/windows/acordar-backup.ps1`) acorda o notebook suspenso e liga o Ubuntu às 22h20 por 30 minutos. Com o notebook desligado, ela roda assim que ele ligar. Testar: `acordar-backup.ps1 -Testar`; remover: `-Desfazer`.
3. **Tirar os `|| true` que escondem erro.** Dois bugs desta rodada (evento do backup e relatório da coerência) estavam escondidos assim.
4. **O bootstrap instala o `just` pelo apt.** É o 1.21 no 24.04. O `verificar.sh` deveria conferir a versão mínima; o teste em `tools/validar` já barra o `[positional-arguments]`.
5. **Núcleo e IA ligados na instalação.** O `instalar-tudo.sh` deveria iniciar o núcleo, e o LiteLLM deveria subir junto com o Ollama, que já está de pé.
