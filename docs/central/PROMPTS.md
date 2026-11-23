<!-- Escrito à mão. Prompts prontos para construir a Central AMtech. Contexto em README.md. -->

# Prompts da Central AMtech

[← Contexto da Central](README.md)

## Como usar

1. **Uma conversa por fase**, no Claude Code do notebook (a outra conta), dentro de `~/dev/dev-setup`, num ramo novo.
2. Cole primeiro o **Bloco fixo** (igual em todas as fases: o Claude reaproveita do cache e gasta menos) e depois o prompt da fase.
3. Modelo: **Sonnet, esforço médio** em todas as fases. **Opus** só na revisão de segurança (prompt R). Fable não é preciso aqui.
4. Terminou a fase: confira o “Pronto quando”, rode `just check`, revise o PR em rascunho e só então faça o merge.
5. Antes de começar a fase seguinte, rode o prompt P (passagem) para ter o resumo para colar na conversa nova.

| Ordem | Prompt | Modelo | Sessões |
|---|---|---|---|
| 1 | F0 · Portas, bug do coerencia e ADR 0022 | Sonnet médio | 1 |
| 2 | F1 · Portal Homepage gerado dos dados | Sonnet médio | 1 |
| 3 | F2 · OliveTin com allowlist | Sonnet médio | 1 |
| 4 | R · Revisão de segurança da F2 | **Opus alto** | 0,5 |
| 5 | F3 · Central: API de leitura e executor SSE | Sonnet médio | 2 |
| 6 | F4 · Central: as 9 telas | Sonnet médio | 2 |
| 7 | F5 · Caixa de aprovações de verdade | Sonnet médio | 1 |
| 8 | F6 · Celular, login e testes de ponta a ponta | Sonnet médio | 1 |
| 9 | R · Revisão de segurança da Central inteira | **Opus alto** | 0,5 |

---

## Bloco fixo (cole no começo de toda conversa)

```text
<contexto>
Você trabalha no repositório ~/dev/dev-setup do Alan Mateus (professor de TI em Barbacena-MG, fundador do Grupo AMtech Digital).
O dev-setup é o setup central: justfile como porta única (55 receitas), tools/*.py, data/*.json como fonte única,
documentação gerada por tools/gerar_docs.py, banco central nucleo.db (eventos, conhecimento, tarefas, auditoria, passos_feitos),
fila de pedidos (tools/remoto/fila.py), motor de decisão (tools/motor/motor.py, escada de 5 degraus), bot do Telegram.
Estamos construindo a Central AMtech: uma tela única (notebook e celular) sobre o que já existe.
Leia antes: docs/central/README.md (contexto, decisões, arquitetura, segurança, fases) e docs/central/prototipo/index.html (protótipo de referência visual e de fluxo).
</contexto>
<regras>
- Português do Brasil em tudo (código pode ter nomes em português, como o resto do repositório).
- Nada escrito à mão no que é gerado: gerador + --check no CI.
- Tudo em 127.0.0.1; acesso externo só pelo Tailscale. Nunca shell=True com texto do usuário; argumentos como lista.
- Nenhum segredo no Git (KeePassXC; sops/age só na VM). Nenhum dado de aluno.
- Poucos arquivos, organização simples. Testes pytest para toda função nova. just check precisa passar.
- Assuma padrões razoáveis e diga quais assumiu; o Alan corrige o que estiver errado.
- Se algo não for possível, diga claramente em vez de contornar.
</regras>
<entrega>
- Ramo novo e PR em rascunho (nunca merge).
- Uma linha no ESTADO.md (formato das linhas existentes) e uma entrada no CHANGELOG.md (próxima versão menor).
- No fim, responda só com: o que mudou (lista curta), como testar (comandos), o que o Alan precisa conferir pessoalmente.
</entrega>
```

---

## F0 · Portas, bug do coerencia e ADR 0022

```text
Fase 0 da Central AMtech.
1) Crie data/portas.json como fonte única das portas de todos os serviços dos infra/*/compose.yaml
   (id, nome, grupo, porta, compose, perfil, tem_tela). Resolva os conflitos com as trocas do docs/central/README.md, seção 1
   (Juice Shop 3100, AdGuard 3011, Metabase 3012, WebGoat 8180, Akaunting 8091) e reserve Portal 3010, OliveTin 1337, Central 8700.
2) Faça o just check falhar se dois serviços usarem a mesma porta do host (teste novo que lê os compose.yaml e o portas.json
   e confere que batem).
3) Corrija tools/coerencia/coerencia.py: criar a pasta do relatório antes de gravar (hoje quebra com FileNotFoundError quando ~/dev não existe).
   Teste que reproduz o erro antes da correção.
4) Escreva docs/adr/0022-central-amtech.md no formato das ADRs existentes: decisão montar (Homepage, OliveTin) + construir (Central em
   FastAPI + HTMX + SSE dentro de tools/central), por que Python e não Next.js aqui, segurança e o caminho se virar produto.
Pronto quando: just check verde, docker compose config de cada pasta sem porta repetida, ADR escrita, teste do coerencia passando.
```

## F1 · Portal Homepage gerado dos dados

```text
Fase 1 da Central AMtech: portal com o Homepage.
1) infra/portal/compose.yaml com o Homepage em versão fixada (sem :latest), porta 127.0.0.1:3010, usuário não root, volume de config.
2) tools/portal/gerar.py: gera os YAML do Homepage (services.yaml, settings.yaml, bookmarks.yaml) a partir de data/portas.json e
   data/ecossistema.json. Grupos iguais aos do portas.json. Bookmarks para os HTMLs de docs/ (cockpit, mapa, index, acompanhamento,
   portfólio, planejador) e para a Central (:8700). Widgets só onde a chave vem de variável de ambiente (Uptime Kuma, Grafana,
   Home Assistant); sem chave, só o link. Modo --check para o CI, como o tools/cockpit/gerar.py.
3) Receitas: just portal (gera e sobe) e just portal --check. Entrar no just check e no workflow docs.yml.
4) Testes: o gerador cobre todos os serviços com tela do portas.json; nenhuma chave escrita no YAML.
Pronto quando: just portal abre em http://localhost:3010 com todos os serviços agrupados; CI falha se o YAML gerado estiver velho.
Diga quais variáveis de ambiente o Alan precisa criar e onde guardar (KeePassXC).
```

## F2 · OliveTin com allowlist

```text
Fase 2 da Central AMtech: botões do just com OliveTin (reserva da Central e solução imediata).
1) infra/portal/compose.yaml ganha o OliveTin em 127.0.0.1:1337, versão fixada, sem root.
   Ele precisa rodar receitas no host: escolha o jeito mais seguro (ex.: OliveTin instalado como serviço systemd --user em vez de container
   com docker.sock montado) e explique a escolha em 3 linhas.
2) data/central.json: áreas das receitas (as mesmas do protótipo), quais pedem confirmação (README seção 4, item 4),
   e validação de cada argumento (regex para ids; texto livre só em pedir, lembrar, erro, atrito, triagem, motor).
3) tools/portal/olivetin.py gera o config.yaml do OliveTin a partir de `just --dump --dump-format json` + data/central.json.
   Receita perigosa: popup de confirmação. Receita fora do central.json: não entra (allowlist, não blocklist).
4) Testes: nenhuma receita sem entrada no central.json vira botão; nenhum argumento sem validação; --check no CI.
Pronto quando: just portal sobe o OliveTin com as receitas seguras rodando e as perigosas pedindo confirmação.
Liste para o Alan as receitas que viraram botão, para ele conferir uma por uma.
```

## F3 · Central: API de leitura e executor SSE

```text
Fase 3 da Central AMtech: backend.
Estrutura (poucos arquivos): tools/central/app.py (FastAPI, rotas), fontes.py (lê os dados chamando as funções dos tools/*.py
importadas, não o terminal), executor.py (roda receita da allowlist e transmite a saída por SSE), test_central.py.
1) Rotas de leitura do README seção 3 (API mínima): /api/hoje, /api/receitas, /api/fila, /api/servicos, /api/nucleo/buscar,
   /api/roteiro, /api/aprovacoes (por enquanto só leitura).
   Onde um tool só imprime texto, refatore o mínimo para expor uma função que devolve dados (sem mudar a saída do terminal; testes antigos passando).
2) POST /api/rodar {receita, args} → valida pelo data/central.json → subprocess com lista de argumentos, cwd do repositório,
   timeout, usuário atual → id. GET /api/rodar/{id}/saida: SSE linha a linha, com código de saída no fim.
   Toda execução vai para a tabela auditoria do nucleo.db.
3) Serviço systemd --user amtech-central em 127.0.0.1:8700 (mesmo padrão do amtech-fila) e receita just central.
4) Ainda sem login (só localhost nesta fase); deixe o ponto de encaixe pronto.
Pronto quando: curl localhost:8700/api/hoje devolve dado real; rodar `agora` pela API transmite a saída; receita fora da allowlist volta 403;
pytest cobre validação, allowlist, timeout e auditoria.
```

## F4 · Central: as 9 telas

```text
Fase 4 da Central AMtech: telas.
Use docs/central/prototipo/index.html como referência de layout, textos, cores (tokens do cockpit) e fluxos.
Implemente com HTMX + templates Jinja2 em tools/central/templates/ e um CSS só em tools/central/static/.
Telas: Hoje, Aprovar, Comandos, Pedir, Estudo, Empresas e rendas, Serviços, Núcleo, Roteiro; paleta Ctrl+K; terminal em folha com SSE.
Diferenças do protótipo: tudo vem da API real (nada de dado embutido); ações reais com confirmação onde o central.json mandar.
Celular: barra inferior com Hoje, Aprovar, Comandos, Pedir, Mais (igual ao protótipo), sem rolagem lateral em 390 px.
Acessibilidade: foco visível, rótulos nos campos, contraste nos dois temas.
Pronto quando: as 9 telas mostram dado real no notebook; marcar um passo feito grava em passos_feitos; pedir algo cria item na fila;
teste pytest de cada rota de tela (status 200 e um texto-chave).
```

## F5 · Caixa de aprovações de verdade

```text
Fase 5 da Central AMtech: a caixa “Esperando você” ligada de verdade.
Fontes: PRs em rascunho dos ramos fila/* (gh pr list --json), just akita pendentes, decisões do motor sem resultado,
agenda.py decisoes, fila de publicação do pipeline de conteúdo, compras da biblioteca.
Ações: aprovar merge (gh pr ready + gh pr merge --squash, só depois de confirmar na tela), pedir ajuste (volta para a fila com o texto),
aprovar/recusar regra do Akita (just akita aprovar ID / registro da recusa), anotar decisão (grava no núcleo e marca o passo),
motor ok/refazer. Cada ação: confirmação, auditoria e aviso pelo bot (tools/remoto/bot.py --avisar).
Nunca aprovar nada sozinho; nenhuma ação de degrau 5 sem clique do Alan.
Pronto quando: um PR de teste da fila aparece na caixa, é aprovado pela Central, entra na main e o aviso chega no Telegram;
a auditoria mostra cada passo. Testes com gh simulado (sem chamar o GitHub de verdade nos testes).
```

## F6 · Celular, login e testes de ponta a ponta

```text
Fase 6 da Central AMtech: usar pelo celular com segurança.
1) Login: senha única do Alan (hash argon2 em arquivo fora do Git, ~/.config/amtech/central.env com permissão 600),
   cookie de sessão HttpOnly + Secure + SameSite=Strict, CSRF nos POST, bloqueio depois de 5 tentativas erradas.
2) PWA: manifest e ícone, instalável no celular. Sem service worker que guarde dado sensível.
3) Acesso: `tailscale serve` apontando para 127.0.0.1:8700 (documente o comando e como desfazer). Nada de funnel público.
4) Testes de ponta a ponta com Playwright (viewport 390x844 e 1280x900): login, Hoje, rodar uma receita segura, pedir algo, aprovar item de teste.
   Rodar no just ci-local e no GitHub Actions.
5) Atualize docs/operacao/celular.md: a Central passa a ser o caminho principal; Telegram fica para avisos e /pedir rápido.
Pronto quando: o Alan abre a Central no celular fora de casa, entra com a senha e aprova um item; Playwright verde no CI.
```

## R · Revisão de segurança (Opus, esforço alto)

```text
Revise como especialista sênior em AppSec o PR da fase [NÚMERO] da Central AMtech.
Procure: execução de comando com texto do usuário, receita fora da allowlist, argumento sem validação, caminho que sai do repositório,
CSRF, sessão, XSS nos templates (autoescape), segredo em log/tela/Git, serviço escutando fora de 127.0.0.1, processo como root,
SSE que vaza saída de outra execução, ausência de auditoria.
Para cada achado: arquivo e linha, cenário concreto de ataque, gravidade (CVSS aproximado com tools/seguranca/cvss.py) e correção.
Não corrija nada: só o relatório. Se não achar nada grave, diga isso claramente.
```

## P · Passagem para a próxima conversa

```text
Gere a passagem desta conversa em até 15 linhas: fase feita, ramo e PR, o que ficou pendente, decisões tomadas e por quê,
comandos para testar e o próximo prompt a usar (de docs/central/PROMPTS.md). Sem repetir o Bloco fixo.
```
