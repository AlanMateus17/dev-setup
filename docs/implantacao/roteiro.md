<!-- Arquivo GERADO por tools/implantacao/gerar.py a partir de data/implantacao.json. Não edite à mão. -->

# Roteiro de implantação

[← Implantação](README.md)

11 fases, 58 passos, cerca de **21 h 15 min** de trabalho no total. Cada passo tem um critério de pronto que dá para conferir. A versão para marcar o progresso é o [`acompanhamento.html`](acompanhamento.html) (e o artefato Implantação AMtech).

Legenda de quem faz: **Você** (só você pode: contas, senhas, decisões), **Script** (você roda o comando), **Claude com você** (o Claude faz pelo conector ou pelo Claude Code, com a sua aprovação).

| Fase | Objetivo | Passos | Tempo |
|---|---|---:|---:|
| [0 · Preparar](#f0) | Nada se perde e as contas estão protegidas antes de mexer na máquina. | 4 | 2 h 25 min |
| [1 · Windows](#f1) | Os programas do setup instalados e o WSL2 pronto. | 6 | 2 h 30 min |
| [2 · Linux (WSL2)](#f2) | O Ubuntu com tudo o que o código precisa, e commits assinados. | 7 | 1 h 17 min |
| [3 · GitHub e CI](#f3) | O repositório no ar, com testes automáticos verdes a cada envio. | 4 | 35 min |
| [4 · Agentes de IA](#f4) | O Claude Code trabalhando dentro da sandbox, com as regras do Aura. | 4 | 52 min |
| [5 · Automação e medição](#f5) | n8n, banco de métricas, Grafana e Uptime Kuma rodando. | 7 | 57 min |
| [6 · Pipeline de conteúdo](#f6) | Gravou ou escreveu, as peças aparecem na fila de aprovação. | 6 | 1 h 24 min |
| [7 · Contas e canais](#f7) | Os perfis e as plataformas prontos para receber o que o pipeline produz. | 8 | 5 h 50 min |
| [8 · Vendas medidas](#f8) | Cada venda chega sozinha ao banco e aparece no painel de lucro. | 4 | 2 h 40 min |
| [9 · Backup e segurança](#f9) | Perder o notebook não faz você perder nada. | 4 | 1 h 45 min |
| [10 · Teste final](#f10) | Os três testes de ponta a ponta passam. | 4 | 1 h 00 min |

<a id="f0"></a>

## 0 · Preparar

Nada se perde e as contas estão protegidas antes de mexer na máquina.

### 0.1 Copiar documentos, fotos e projetos para um disco externo

**Você** · 1 h 00 min

- [ ] **Pronto quando:** Disco externo com a cópia conferida (abra alguns arquivos)

### 0.2 Atualizar o Windows, os drivers e o NitroSense

**Você** · 40 min

- [ ] **Pronto quando:** Windows Update sem pendências

### 0.3 Ligar a verificação em duas etapas no GitHub, Google e e-mail

**Você** · 30 min

- [ ] **Pronto quando:** 2FA ativo nas três contas, com códigos de recuperação impressos

### 0.4 Rodar o inventário somente leitura do Windows

**Script** · 15 min

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\windows\inventario.ps1
```

- [ ] **Pronto quando:** Pasta inventario-AAAAMMDD gerada; decidir o que desinstalar

<a id="f1"></a>

## 1 · Windows

Os programas do setup instalados e o WSL2 pronto.

### 1.1 Ver o que o instalador faria

**Script** · 5 min

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\windows\instalar.ps1
```

- [ ] **Pronto quando:** Lista de INSTALARIA conferida

### 1.2 Instalar programas, WSL2 com Ubuntu 24.04 e .wslconfig (PowerShell como Administrador)

**Script** · 1 h 00 min

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\windows\instalar.ps1 -Aplicar
```

- [ ] **Pronto quando:** Termina com 'Pronto' e sem ERRO; reinicie o Windows

### 1.3 Criar o cofre do KeePassXC e migrar as senhas

**Você** · 45 min

- [ ] **Pronto quando:** Cofre com senha mestra forte e cópia do arquivo no disco externo

### 1.4 Ligar a criptografia do dispositivo e guardar a chave de recuperação no KeePassXC

**Você** · 15 min

- [ ] **Pronto quando:** verificar.ps1 como Administrador mostra criptografia OK
- No Windows 11 Home a opção se chama Criptografia do dispositivo e depende do hardware. Se não aparecer, anote e siga.

### 1.5 Instalar o DaVinci Resolve pelo site da Blackmagic (opcional)

**Você** · 20 min

- [ ] **Pronto quando:** Abre e reconhece a GPU

### 1.6 Conferir o Windows

**Script** · 5 min

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\windows\verificar.ps1
```

- [ ] **Pronto quando:** verificar.ps1 termina com 'Windows pronto'

<a id="f2"></a>

## 2 · Linux (WSL2)

O Ubuntu com tudo o que o código precisa, e commits assinados.

### 2.1 Abrir 'Ubuntu 24.04' no menu Iniciar e criar seu usuário Linux

**Você** · 10 min

- [ ] **Pronto quando:** Prompt do Ubuntu aberto

### 2.2 Ligar o Docker Desktop no Ubuntu: Settings > Resources > WSL integration

**Você** · 5 min

- [ ] **Pronto quando:** 'docker run hello-world' funciona dentro do Ubuntu

### 2.3 Copiar este repositório para ~/dev/dev-setup

**Você** · 5 min

```bash
mkdir -p ~/dev && cd ~/dev && unzip /mnt/c/Users/SEU_USUARIO/Downloads/dev-setup.zip
```

- [ ] **Pronto quando:** Pasta ~/dev/dev-setup com os arquivos
- Troque SEU_USUARIO pelo seu usuário do Windows. Depois que o repositório estiver no GitHub, use git clone.

### 2.4 Rodar o preparador do Linux

**Script** · 40 min

```bash
bash scripts/wsl/bootstrap.sh --nome "Alan Mateus" --email SEU_EMAIL --com-whisper
```

- [ ] **Pronto quando:** Termina com 'Pronto' e sem ERRO

### 2.5 Reiniciar o WSL para o systemd valer (PowerShell)

**Você** · 2 min

```powershell
wsl --shutdown
```

- [ ] **Pronto quando:** Ubuntu reabre normalmente

### 2.6 Entrar no GitHub pelo terminal e cadastrar a chave SSH para login e assinatura

**Você** · 10 min

```bash
gh auth login && gh ssh-key add ~/.ssh/id_ed25519.pub --type authentication && gh ssh-key add ~/.ssh/id_ed25519.pub --type signing
```

- [ ] **Pronto quando:** 'gh auth status' mostra sua conta

### 2.7 Conferir o Linux

**Script** · 5 min

```bash
bash scripts/wsl/verificar.sh
```

- [ ] **Pronto quando:** verificar.sh termina com 'WSL pronto'

<a id="f3"></a>

## 3 · GitHub e CI

O repositório no ar, com testes automáticos verdes a cada envio.

### 3.1 Criar o repositório privado e enviar o setup

**Script** · 5 min

```bash
cd ~/dev/dev-setup && git init -q 2>/dev/null; git add -A && git commit -qm 'chore: setup inicial' ; gh repo create AlanMateus17/dev-setup --private --source . --push
```

- [ ] **Pronto quando:** Repositório AlanMateus17/dev-setup privado com o código
- Se você usar o zip, o histórico de commits não vem junto; o repositório começa com um commit novo, já assinado.

### 3.2 Conferir o CI no GitHub

**Script** · 5 min

```bash
gh run list --limit 1
```

- [ ] **Pronto quando:** Última execução do workflow 'docs' com sucesso

### 3.3 Ligar Dependabot e proteger o branch main

**Claude com você** · 15 min

- [ ] **Pronto quando:** Dependabot ativo; push direto no main exige CI verde
- Peça ao Claude Code no repositório; ele faz pelo gh api com a sua aprovação.

### 3.4 Criar a organização grupo-amtech-digital no GitHub

**Você** · 10 min

- [ ] **Pronto quando:** Organização criada, com 2FA obrigatório para membros

<a id="f4"></a>

## 4 · Agentes de IA

O Claude Code trabalhando dentro da sandbox, com as regras do Aura.

### 4.1 Entrar no Claude Code

**Você** · 5 min

```bash
claude
```

- [ ] **Pronto quando:** 'claude doctor' sem erros

### 4.2 Testar a sandbox

**Script** · 2 min

```bash
cd ~/dev/dev-setup && ai-jail --dry-run claude
```

- [ ] **Pronto quando:** Mostra o que seria montado, sem erro

### 4.3 Criar o CLAUDE.md padrão do Aura e os comandos /commit e /novo-sistema-aura

**Claude com você** · 30 min

- [ ] **Pronto quando:** Arquivos no repositório de cada sistema
- Peça ao Claude Code: o conteúdo está em docs/pecas-autorais.md.

### 4.4 Baixar um modelo local de 3 a 4B no Ollama

**Você** · 15 min

```bash
ollama pull <nome do modelo escolhido no catálogo do Ollama>
```

- [ ] **Pronto quando:** verificar.ps1 mostra Ollama OK com 1 modelo

<a id="f5"></a>

## 5 · Automação e medição

n8n, banco de métricas, Grafana e Uptime Kuma rodando.

### 5.1 Gerar as senhas da stack e guardar no KeePassXC

**Script** · 5 min

```bash
cd infra/automacao && bash gerar-senhas.sh
```

- [ ] **Pronto quando:** .env criado com permissão 600

### 5.2 Subir a stack

**Script** · 10 min

```bash
cd infra/automacao && docker compose up -d
```

- [ ] **Pronto quando:** 'docker compose ps' com todos healthy

### 5.3 Conferir os serviços

**Script** · 2 min

```bash
bash scripts/wsl/verificar.sh --servicos
```

- [ ] **Pronto quando:** verificar.sh --servicos sem FALTA na área servico

### 5.4 Entrar no Grafana (admin) e ver a fonte 'Métricas AMtech' conectada

**Você** · 10 min

```text
http://localhost:3001
```

- [ ] **Pronto quando:** Explore > Métricas AMtech > 'select 1' responde

### 5.5 Criar a conta do n8n

**Você** · 5 min

```text
http://localhost:5678
```

- [ ] **Pronto quando:** Painel do n8n abre

### 5.6 Cadastrar no Uptime Kuma os monitores do n8n, Grafana e dos sites

**Você** · 15 min

```text
http://localhost:3002
```

- [ ] **Pronto quando:** Monitores verdes; aviso no Telegram configurado

### 5.7 Decidir: Postiz agora ou agendador nativo das redes

**Você** · 10 min

- [ ] **Pronto quando:** Decisão anotada em infra/postiz/README.md

<a id="f6"></a>

## 6 · Pipeline de conteúdo

Gravou ou escreveu, as peças aparecem na fila de aprovação.

### 6.1 Preencher o guia de marca

**Você** · 40 min

- [ ] **Pronto quando:** config/marca.md sem colchetes
- O Claude pode rascunhar a partir dos documentos de marca e presença; você corrige.

### 6.2 Criar a chave da API no console da Anthropic e colocar no conteudo.env

**Você** · 10 min

- [ ] **Pronto quando:** ANTHROPIC_API_KEY preenchida em ~/.config/amtech/conteudo.env
- A API é cobrada por uso, separada da assinatura do Claude. Defina um limite de gasto mensal no console.

### 6.3 Criar o bot de aviso no Telegram (opcional)

**Você** · 10 min

- [ ] **Pronto quando:** Mensagem de teste chega no celular

### 6.4 Testar o caminho sem gastar

**Script** · 2 min

```bash
echo teste > ~/AMtech/entrada/ideias/teste.txt && touch -d '-2 min' ~/AMtech/entrada/ideias/teste.txt && python3 tools/conteudo/processar.py --uma-vez --simular
```

- [ ] **Pronto quando:** Uma pasta [SIMULADO] aparece em ~/AMtech/fila

### 6.5 Ligar o timer de 15 minutos

**Script** · 2 min

```bash
bash scripts/wsl/ativar-pipeline.sh
```

- [ ] **Pronto quando:** verificar.sh --servicos mostra o timer OK

### 6.6 Colocar uma aula gravada de verdade em ~/AMtech/entrada/aulas

**Você** · 20 min

- [ ] **Pronto quando:** Peças da aula na fila em até 15 minutos depois de transcrita

<a id="f7"></a>

## 7 · Contas e canais

Os perfis e as plataformas prontos para receber o que o pipeline produz.

### 7.1 Completar Instagram, YouTube, TikTok e LinkedIn com a mesma identidade

**Você** · 1 h 30 min

- [ ] **Pronto quando:** Foto, nome, bio e link iguais nas quatro redes

### 7.2 Registrar o domínio no Registro.br e apontar para a Cloudflare

**Você** · 30 min

- [ ] **Pronto quando:** DNS ativo na Cloudflare

### 7.3 Criar o e-mail profissional do domínio

**Você** · 30 min

- [ ] **Pronto quando:** Envia e recebe

### 7.4 Montar no MailerLite os grupos, o formulário da isca e a sequência de boas-vindas

**Claude com você** · 30 min

- [ ] **Pronto quando:** Inscrição de teste recebe o primeiro e-mail
- O Claude faz pelo conector do MailerLite, com a sua aprovação.

### 7.5 Criar as contas da Hotmart e da Kiwify no CPF e cadastrar o mini-curso

**Você** · 1 h 00 min

- [ ] **Pronto quando:** Produto em rascunho nas duas

### 7.6 Criar o Gerenciador de Negócios da Meta, o Pixel e a conta de anúncios

**Você** · 40 min

- [ ] **Pronto quando:** Pixel instalado na página de vendas

### 7.7 Publicar a página de pré-venda no Vercel

**Claude com você** · 1 h 00 min

- [ ] **Pronto quando:** Página no ar com o domínio e o Pixel
- Depende de aprovar o acesso do conector do Vercel à sua equipe.

### 7.8 Ligar o Google Search Console no domínio

**Você** · 10 min

- [ ] **Pronto quando:** Propriedade verificada

<a id="f8"></a>

## 8 · Vendas medidas

Cada venda chega sozinha ao banco e aparece no painel de lucro.

### 8.1 Criar o túnel público para os webhooks (Cloudflare Tunnel) e preencher N8N_WEBHOOK_URL

**Você** · 40 min

- [ ] **Pronto quando:** https://n8n.seu-dominio responde fora de casa
- Só o caminho de webhook precisa ficar público; o painel do n8n fica protegido.

### 8.2 Criar no n8n o fluxo: webhook Hotmart e Kiwify → tabela vendas

**Claude com você** · 1 h 00 min

- [ ] **Pronto quando:** Venda de teste aparece na tabela vendas
- O Claude monta o fluxo com você no n8n; a tabela já tem a trava contra venda duplicada.

### 8.3 Lançar os gastos de anúncio (manual no começo, depois pela API de cada rede)

**Você** · 15 min

- [ ] **Pronto quando:** Tabela gastos com a primeira campanha

### 8.4 Montar o painel de lucro no Grafana sobre a view lucro_por_produto_mes

**Claude com você** · 45 min

- [ ] **Pronto quando:** Painel mostra receita, anúncio, lucro e CPA por produto

<a id="f9"></a>

## 9 · Backup e segurança

Perder o notebook não faz você perder nada.

### 9.1 Criar o repositório restic no disco externo e o primeiro backup

**Script** · 30 min

```bash
restic -r /mnt/d/backup-restic init && restic -r /mnt/d/backup-restic backup ~/dev ~/AMtech ~/.config/amtech
```

- [ ] **Pronto quando:** 'restic snapshots' lista o backup
- Troque /mnt/d pela letra do seu disco externo (D: vira /mnt/d). Guarde a senha do repositório no KeePassXC.

### 9.2 Criar a cópia fora de casa (Backblaze B2 ou o armazenamento do seu plano Google)

**Você** · 40 min

- [ ] **Pronto quando:** Segundo repositório restic com snapshot

### 9.3 Testar a restauração de uma pasta

**Você** · 15 min

- [ ] **Pronto quando:** Arquivo restaurado abre normalmente

### 9.4 Agendar o backup diário

**Claude com você** · 20 min

- [ ] **Pronto quando:** Timer do backup ativo

<a id="f10"></a>

## 10 · Teste final

Os três testes de ponta a ponta passam.

### 10.1 Dev: mudar algo num repositório, commit assinado, push, CI verde

**Você** · 15 min

- [ ] **Pronto quando:** Selo Verified no commit e CI verde

### 10.2 Conteúdo: arquivo na entrada → peças na fila → aviso no Telegram

**Você** · 20 min

- [ ] **Pronto quando:** Pasta nova na fila e mensagem no celular

### 10.3 Venda: compra de teste na Hotmart → linha na tabela vendas → painel de lucro

**Você** · 20 min

- [ ] **Pronto quando:** Venda de teste no Grafana

### 10.4 Rodar os três verificadores juntos

**Script** · 5 min

- [ ] **Pronto quando:** verificar.ps1, verificar.sh e verificar.sh --servicos sem FALTA
