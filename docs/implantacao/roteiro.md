<!-- Arquivo GERADO por tools/implantacao/gerar.py a partir de data/implantacao.json. Não edite à mão. -->

# Roteiro de implantação

[← Implantação](README.md)

20 fases, 148 passos, cerca de **88 h 40 min** de trabalho no total. Cada passo tem um critério de pronto que dá para conferir. A versão para marcar o progresso é o [`acompanhamento.html`](acompanhamento.html) (e o artefato Implantação AMtech).

Legenda de quem faz: **Você** (só você pode: contas, senhas, decisões), **Script** (você roda o comando), **Claude com você** (o Claude faz pelo conector ou pelo Claude Code, com a sua aprovação).

**Cobertura:** os 324 blocos do [mapa do setup](../mapa.html) estão todos aqui: 237 entram nos passos, 9 são peças a construir, 3 não se instalam e 75 ficam para depois. O CI falha se um bloco novo do setup ficar fora do roteiro ([lista completa](#cobertura)).

**Dá para fazer hoje:** 135 dos 148 passos (75 h 30 min) só precisam do notebook e de contas grátis. Os outros dizem o que falta: comprar algo, pagar um serviço ou ter um conteúdo seu pronto.

| Fase | Objetivo | Passos | Tempo |
|---|---|---:|---:|
| [0 · Preparar](#f0) | Nada se perde, o hardware está no lugar e as contas estão protegidas antes de mexer na máquina. | 5 | 2 h 55 min |
| [1 · Windows](#f1) | Os programas do setup instalados, o navegador com o Claude e o WSL2 pronto. | 10 | 3 h 15 min |
| [2 · Linux (WSL2)](#f2) | O Ubuntu com tudo o que o código precisa, commits assinados e o ambiente versionado. | 10 | 2 h 22 min |
| [3 · GitHub e CI](#f3) | O repositório no ar, com testes automáticos verdes a cada envio e o trabalho organizado. | 5 | 55 min |
| [4 · Agentes de IA](#f4) | O Claude Code trabalhando dentro da sandbox, com as suas regras, ferramentas e memória. | 7 | 2 h 27 min |
| [5 · Backup e segurança](#f5) | Perder o notebook não faz você perder nada. | 4 | 1 h 45 min |
| [6 · Acervo: tudo o que você já tem](#f6) | Todos os seus documentos convertidos em conhecimento organizado no Obsidian, os pessoais separados e a lista do que dá para vender. | 7 | 4 h 55 min |
| [7 · Claude e assistentes](#f7) | Cada recurso do Claude e cada assistente com um papel definido no setup. | 4 | 1 h 45 min |
| [8 · Automação e medição](#f8) | n8n, banco de métricas, Grafana e Uptime Kuma rodando. | 7 | 57 min |
| [9 · Pipeline de conteúdo](#f9) | Gravou ou escreveu, as peças aparecem na fila de aprovação. | 6 | 1 h 24 min |
| [10 · Estúdio de conteúdo](#f10) | Gravar, editar e montar imagens no mesmo padrão toda semana, sem pensar. | 5 | 3 h 20 min |
| [11 · Contas, canais e sites](#f11) | Perfis, domínio, e-mail e sites prontos para receber o que o pipeline produz. | 12 | 8 h 40 min |
| [12 · Vendas e finanças no CPF](#f12) | Cada oferta pode ser vendida, recebida e declarada do jeito certo. | 20 | 12 h 10 min |
| [13 · Vendas medidas](#f13) | Cada venda chega sozinha ao banco e aparece no painel de lucro. | 4 | 2 h 40 min |
| [14 · Teste do núcleo](#f14) | Os três testes de ponta a ponta passam: daqui em diante, alimentar o sistema já faz tudo sozinho. | 4 | 1 h 00 min |
| [15 · Base dos sistemas AM](#f15) | Um sistema novo nasce pronto: arquitetura, testes, login, observabilidade e deploy. | 7 | 5 h 40 min |
| [16 · Nuvem e deploy](#f16) | As contas de nuvem criadas por código, com custo sob controle. | 7 | 6 h 15 min |
| [17 · Editora](#f17) | O livro sai de um repositório com CI, pronto para virar PDF, EPUB e impressão. | 8 | 8 h 30 min |
| [18 · Dados, IA e pendrives](#f18) | O laboratório de dados e de treino no ar, um modelo seu rodando no Ollama e os pendrives de Kali e Arch dando boot. | 12 | 16 h 20 min |
| [19 · Estudo contínuo](#f19) | As trilhas de estudo ligadas ao setup, sem copiar conteúdo de ninguém. | 4 | 1 h 25 min |

<a id="f0"></a>

## 0 · Preparar

Nada se perde, o hardware está no lugar e as contas estão protegidas antes de mexer na máquina.

### 0.1 Copiar documentos, fotos e projetos para um disco externo

**Você** · 1 h 00 min

- [ ] **Pronto quando:** Disco externo com a cópia conferida (abra alguns arquivos)
- Implanta: Disco externo

### 0.2 Montar a mesa: nobreak, base com cooler, 2º monitor, disco e SSD externos, kits de robótica

**Você** · 30 min

- [ ] **Pronto quando:** Notebook no nobreak e na base, 2º monitor funcionando, disco e SSD externos reconhecidos
- O que ainda não comprou fica anotado e não trava as próximas fases. O nobreak vem primeiro: protege o notebook e o backup de queda de energia.
- **Precisa:** comprar algo
- Implanta: Acer Nitro (32 GB, GTX 1650) · Nobreak · Base com cooler · 2º monitor · Disco externo · SSD externo (USB-C 10 Gbps) · Celular · Arduino · ESP32 · Pi

### 0.3 Atualizar o Windows, os drivers e o NitroSense

**Você** · 40 min

- [ ] **Pronto quando:** Windows Update sem pendências
- Implanta: Windows 11 Home · NitroSense + drivers AMD e NVIDIA

### 0.4 Instalar o app de 2FA no celular e ligar a verificação em duas etapas no GitHub, Google e e-mail

**Você** · 30 min

- [ ] **Pronto quando:** 2FA ativo nas três contas, com códigos de recuperação impressos
- Implanta: App 2FA (celular)

### 0.5 Rodar o inventário somente leitura do Windows

**Script** · 15 min

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\windows\inventario.ps1
```

- [ ] **Pronto quando:** Pasta inventario-AAAAMMDD gerada; decidir o que desinstalar
- Implanta: Windows 11 Home

<a id="f1"></a>

## 1 · Windows

Os programas do setup instalados, o navegador com o Claude e o WSL2 pronto.

### 1.1 Ver o que o instalador faria

**Script** · 5 min

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\windows\instalar.ps1
```

- [ ] **Pronto quando:** Lista de INSTALARIA conferida
- Implanta: Instaladores (PowerShell e bash)

### 1.2 Instalar programas, WSL2 com Ubuntu 24.04 e .wslconfig (PowerShell como Administrador)

**Script** · 1 h 00 min

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\windows\instalar.ps1 -Aplicar
```

- [ ] **Pronto quando:** Termina com 'Pronto' e sem ERRO; reinicie o Windows
- Implanta: Terminal · PowerShell · winget · VS Code · 7-Zip · PowerToys · SumatraPDF · ShareX · LibreOffice · Firefox (2º navegador) · Obsidian + Git · DBeaver · Bruno · Excalidraw / draw.io · VirtualBox · Arduino IDE 2 · .wslconfig + localhost · OBS Studio · Audacity · Canva · Krita · Inkscape · Wireshark · Syncthing · Anki

### 1.3 Criar o cofre do KeePassXC e migrar as senhas

**Você** · 45 min

- [ ] **Pronto quando:** Cofre com senha mestra forte e cópia do arquivo no disco externo
- Implanta: KeePassXC

### 1.4 Ligar a criptografia do dispositivo e guardar a chave de recuperação no KeePassXC

**Você** · 15 min

- [ ] **Pronto quando:** verificar.ps1 como Administrador mostra criptografia OK
- No Windows 11 Home a opção se chama Criptografia do dispositivo e depende do hardware. Se não aparecer, anote e siga.
- Implanta: BitLocker · TPM + Secure Boot

### 1.5 Conferir Defender e Firewall ligados

**Você** · 10 min

- [ ] **Pronto quando:** verificar.ps1 como Administrador mostra Defender OK
- Implanta: Defender + Firewall

### 1.6 Instalar as extensões do VS Code (WSL, Claude Code, .NET, LaTeX, revisão em português)

**Script** · 10 min

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\windows\extensoes-vscode.ps1 -Aplicar
```

- [ ] **Pronto quando:** Termina com 'Pronto'
- Implanta: VS Code

### 1.7 Instalar o Claude in Chrome e entrar com a sua conta

**Você** · 15 min

- [ ] **Pronto quando:** O painel do Claude abre numa aba do navegador
- O uso do computador pelo Claude fica no app do Claude para desktop; ligue só quando for usar e acompanhe o que ele faz.
- Implanta: Navegador + Claude in Chrome · Claude in Chrome + uso do computador

### 1.8 Instalar o DaVinci Resolve pelo site da Blackmagic (opcional)

**Você** · 20 min

- [ ] **Pronto quando:** Abre e reconhece a GPU
- Implanta: DaVinci Resolve ou Kdenlive

### 1.9 Decidir se Unity e Cocos ficam para as aulas de robótica

**Você** · 10 min

```bash
winget install --id Unity.UnityHub -e
```

- [ ] **Pronto quando:** Decisão anotada; se ficam, Unity Hub instalado
- Implanta: Unity · Cocos

### 1.10 Conferir o Windows

**Script** · 5 min

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\windows\verificar.ps1
```

- [ ] **Pronto quando:** verificar.ps1 termina com 'Windows pronto'
- Implanta: Verificadores

<a id="f2"></a>

## 2 · Linux (WSL2)

O Ubuntu com tudo o que o código precisa, commits assinados e o ambiente versionado.

### 2.1 Abrir 'Ubuntu 24.04' no menu Iniciar e criar seu usuário Linux

**Você** · 10 min

- [ ] **Pronto quando:** Prompt do Ubuntu aberto
- Implanta: Ubuntu (WSL2)

### 2.2 Ligar o Docker Desktop no Ubuntu: Settings > Resources > WSL integration

**Você** · 5 min

- [ ] **Pronto quando:** 'docker run hello-world' funciona dentro do Ubuntu
- Implanta: Docker + Compose

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
- Implanta: .NET 10 · Node · Python · TeX Live · gitleaks · Trivy · Git + SSH + gh · nmap · dig · curl · Whisper (local) · Pranchas TikZ e SVG · CircuiTikZ · Instaladores (PowerShell e bash)

### 2.5 Reiniciar o WSL para o systemd valer (PowerShell)

**Você** · 2 min

```powershell
wsl --shutdown
```

- [ ] **Pronto quando:** Ubuntu reabre normalmente
- Implanta: Ubuntu (WSL2)

### 2.6 Entrar no GitHub pelo terminal e cadastrar a chave SSH para login e assinatura

**Você** · 10 min

```bash
gh auth login && gh ssh-key add ~/.ssh/id_ed25519.pub --type authentication && gh ssh-key add ~/.ssh/id_ed25519.pub --type signing
```

- [ ] **Pronto quando:** 'gh auth status' mostra sua conta
- Implanta: Git + SSH + gh · Commits assinados (chave SSH)

### 2.7 Guardar os dotfiles (.bashrc, .gitconfig, .tmux.conf) num repositório privado

**Claude com você** · 30 min

- [ ] **Pronto quando:** Repositório dotfiles privado; clonar e rodar o script de links recria o terminal
- Nunca coloque chaves ou tokens nos dotfiles. O gitleaks do CI confere a cada envio.
- Implanta: dotfiles

### 2.8 Criar o cofre do Obsidian em ~/dev/notas e ligar o plugin Obsidian Git

**Você** · 20 min

```bash
bash scripts/wsl/vault.sh
```

- [ ] **Pronto quando:** Cofre aberto no Obsidian com as pastas e modelos; notas vão sozinhas para um repositório privado a cada 10 minutos
- No Obsidian do Windows, abra a pasta \\wsl.localhost\Ubuntu-24.04\home\SEU_USUARIO\dev\notas.
- Implanta: Obsidian + Git

### 2.9 Ligar o Syncthing entre o celular e o notebook para as gravações (opcional)

**Você** · 15 min

- [ ] **Pronto quando:** Vídeo gravado no celular aparece na pasta Gravacoes do Windows
- Para o pipeline pegar, mova o vídeo para ~/AMtech/entrada/aulas. Vídeo com aluno menor de idade só com autorização do responsável.
- Implanta: Syncthing · Celular

### 2.10 Conferir o Linux

**Script** · 5 min

```bash
bash scripts/wsl/verificar.sh
```

- [ ] **Pronto quando:** verificar.sh termina com 'WSL pronto'
- Implanta: Verificadores

<a id="f3"></a>

## 3 · GitHub e CI

O repositório no ar, com testes automáticos verdes a cada envio e o trabalho organizado.

### 3.1 Criar o repositório privado e enviar o setup

**Script** · 5 min

```bash
cd ~/dev/dev-setup && git init -q 2>/dev/null; git add -A && git commit -qm 'chore: setup inicial' ; gh repo create AlanMateus17/dev-setup --private --source . --push
```

- [ ] **Pronto quando:** Repositório AlanMateus17/dev-setup privado com o código
- Se você usar o zip, o histórico de commits não vem junto; o repositório começa com um commit novo, já assinado.
- Implanta: GitHub

### 3.2 Conferir o CI no GitHub

**Script** · 5 min

```bash
gh run list --limit 1
```

- [ ] **Pronto quando:** Última execução do workflow 'docs' com sucesso
- Implanta: GitHub Actions

### 3.3 Ligar Dependabot e CodeQL e proteger o branch main

**Claude com você** · 15 min

- [ ] **Pronto quando:** Dependabot e CodeQL ativos; push direto no main exige CI verde
- Peça ao Claude Code no repositório; ele faz pelo gh api com a sua aprovação.
- Implanta: Dependabot + CodeQL

### 3.4 Criar a organização grupo-amtech-digital no GitHub

**Você** · 10 min

- [ ] **Pronto quando:** Organização criada, com 2FA obrigatório para membros
- Implanta: GitHub

### 3.5 Criar o GitHub Project do setup e a pasta de decisões (ADRs)

**Claude com você** · 20 min

- [ ] **Pronto quando:** Quadro com as fases deste roteiro e docs/adr/0001 registrado
- O MkDocs publica a documentação no GitHub Pages quando você quiser tornar algo público; o setup continua privado.
- Implanta: Projects · ADRs · MkDocs

<a id="f4"></a>

## 4 · Agentes de IA

O Claude Code trabalhando dentro da sandbox, com as suas regras, ferramentas e memória.

### 4.1 Entrar no Claude Code

**Você** · 5 min

```bash
claude
```

- [ ] **Pronto quando:** 'claude doctor' sem erros
- Implanta: Claude Code

### 4.2 Testar a sandbox

**Script** · 2 min

```bash
cd ~/dev/dev-setup && ai-jail --dry-run claude
```

- [ ] **Pronto quando:** Mostra o que seria montado, sem erro
- Implanta: ai-jail

### 4.3 Criar o CLAUDE.md padrão do Aura e os comandos /commit e /novo-sistema-aura

**Claude com você** · 30 min

- [ ] **Pronto quando:** Arquivos no repositório de cada sistema
- Peça ao Claude Code: o conteúdo está em docs/pecas-autorais.md.
- Implanta: CLAUDE.md, agentes e skills (seus)

### 4.4 Baixar um modelo local de 3 a 4B no Ollama

**Você** · 15 min

```bash
ollama pull <nome do modelo escolhido no catálogo do Ollama>
```

- [ ] **Pronto quando:** verificar.ps1 mostra Ollama OK com 1 modelo
- Implanta: Ollama · Modelos locais: Qwen · Gemma · Llama

### 4.5 Ligar os servidores MCP do Claude Code: GitHub e o banco de métricas só para leitura

**Claude com você** · 20 min

- [ ] **Pronto quando:** 'claude mcp list' mostra os servidores conectados
- O banco entra com o usuário leitor do Grafana, que não apaga nada. Tokens ficam no KeePassXC e em variáveis de ambiente, nunca no repositório.
- Implanta: Servidores MCP

### 4.6 Ligar o ai-memory para o agente lembrar das decisões entre sessões

**Claude com você** · 15 min

- [ ] **Pronto quando:** Uma decisão anotada numa sessão aparece na seguinte
- Implanta: ai-memory

### 4.7 Montar a base de conhecimento das suas notas (Ollama + pgvector, ou NotebookLM e Projects)

**Claude com você** · 1 h 00 min

- [ ] **Pronto quando:** Pergunta sobre uma anotação sua volta com a resposta e a nota de origem
- Entram só as suas anotações, resumos com suas palavras, exercícios resolvidos e aulas que você gravou. Aulas da Udemy, DIO, Alura e afins não entram.
- Implanta: Base de conhecimento (RAG) das suas notas · NotebookLM

<a id="f5"></a>

## 5 · Backup e segurança

Perder o notebook não faz você perder nada.

### 5.1 Criar o repositório restic no disco externo e o primeiro backup

**Script** · 30 min

```bash
restic -r /mnt/d/backup-restic init && restic -r /mnt/d/backup-restic backup ~/dev ~/AMtech ~/.config/amtech
```

- [ ] **Pronto quando:** 'restic snapshots' lista o backup
- Troque /mnt/d pela letra do seu disco externo (D: vira /mnt/d). Guarde a senha do repositório no KeePassXC.
- Implanta: restic (backup criptografado) · Backup 3-2-1 · Disco externo

### 5.2 Criar a cópia fora de casa (Backblaze B2 ou o armazenamento do seu plano Google)

**Você** · 40 min

- [ ] **Pronto quando:** Segundo repositório restic com snapshot
- Implanta: Backblaze B2 (backup) · Backup 3-2-1

### 5.3 Testar a restauração de uma pasta

**Você** · 15 min

- [ ] **Pronto quando:** Arquivo restaurado abre normalmente
- Implanta: Backup 3-2-1

### 5.4 Agendar o backup diário

**Claude com você** · 20 min

- [ ] **Pronto quando:** Timer do backup ativo
- Implanta: restic (backup criptografado)

<a id="f6"></a>

## 6 · Acervo: tudo o que você já tem

Todos os seus documentos convertidos em conhecimento organizado no Obsidian, os pessoais separados e a lista do que dá para vender.

### 6.1 Baixar uma cópia completa do Google Drive pelo Google Takeout

**Você** · 45 min

- [ ] **Pronto quando:** Os zips do Takeout extraídos numa pasta só, por exemplo C:\Users\SEU_USUARIO\Downloads\Takeout
- Escolha só o Drive e, em formatos, Google Docs como .docx e Apresentações como .pptx. O Drive para computador mostra os Google Docs como atalhos sem conteúdo, por isso a primeira cópia vem do Takeout. Junte também os arquivos do notebook e dos pendrives na mesma pasta.
- Implanta: Google Drive (seus documentos)

### 6.2 Tirar da pasta os documentos pessoais (contracheques, extratos, IRPF, faturas)

**Você** · 30 min

- [ ] **Pronto quando:** Pasta Pessoal separada, guardada só no backup criptografado
- O acervo.py também barra esses arquivos pelo nome e pelo conteúdo e lista o que achou, mas tirar antes é mais seguro.
- Implanta: Backup 3-2-1

### 6.3 Ver o que o acervo faria, sem escrever nada

**Script** · 10 min

```bash
uv run tools/acervo/acervo.py --origem /mnt/c/Users/SEU_USUARIO/Downloads/Takeout --simular
```

- [ ] **Pronto quando:** Resumo com arquivos lidos, cópias repetidas, pessoais, de terceiros e da escola
- Implanta: Acervo (seus documentos)

### 6.4 Converter o acervo para o Obsidian e gerar o relatório de produtos

**Script** · 30 min

```bash
uv run tools/acervo/acervo.py --origem /mnt/c/Users/SEU_USUARIO/Downloads/Takeout
```

- [ ] **Pronto quando:** 30-Acervo no Obsidian com os documentos em Markdown e 40-Produtos/Produtos do acervo.md
- Roda no notebook; nada é enviado para fora. Pode rodar de novo quando chegarem documentos novos: o que já foi convertido não é refeito.
- Implanta: Acervo (seus documentos) · Obsidian + Git

### 6.5 Decidir cada alerta: dados de alunos, material de terceiros, material feito para a escola

**Você** · 1 h 30 min

- [ ] **Pronto quando:** Cada alerta com decisão anotada: apagar dados, só estudo, reescrever ou vender
- Material de terceiros (livros, cursos) não vira produto nem treino de IA. Material feito para a escola: confira os direitos antes de vender; o caminho seguro é reescrever do zero, no seu tempo, sem a identidade da escola.
- Implanta: Acervo (seus documentos)

### 6.6 Indexar o acervo e as suas notas na base de conhecimento

**Claude com você** · 30 min

- [ ] **Pronto quando:** Pergunta sobre um documento antigo volta com a resposta e o arquivo de origem
- Implanta: Base de conhecimento (RAG) das suas notas

### 6.7 Escolher no relatório os 3 primeiros produtos e levar para o portfólio de ofertas

**Claude com você** · 1 h 00 min

- [ ] **Pronto quando:** 3 ofertas novas em data/portfolio.json com estágio, preço alvo e próximo passo
- Implanta: Portfólio de ofertas · Esteira de ofertas

<a id="f7"></a>

## 7 · Claude e assistentes

Cada recurso do Claude e cada assistente com um papel definido no setup.

### 7.1 Organizar o app do Claude: um Project por frente, memória, artefatos, pesquisa e tarefas agendadas

**Você** · 30 min

- [ ] **Pronto quando:** Projects AMtech, Instituto, Editora e Setup criados; uma tarefa agendada de teste rodou
- Implanta: Claude (app) · Projects + memória · Artifacts (Docs, Slides, Sheets…) · Pesquisa aprofundada · Tarefas agendadas

### 7.2 Conferir os conectores: Google, Canva, Figma, MailerLite, Vercel, Microsoft Learn, Upwork, Lovable, Supabase, Cloudflare e vidIQ

**Você** · 30 min

- [ ] **Pronto quando:** Cada conector usado responde a um pedido simples; o da Cloudflare trocado pelo Cloudflare API MCP
- Notion, monday, GitBook e Stripe ficam de fora: repetem Obsidian, GitHub Projects, MkDocs e as plataformas de curso. Desconecte para não confundir.
- Implanta: Conector Google (Gmail, Drive…) · Conectores Canva + Figma · Conector MailerLite · Vercel · AWS · Microsoft Learn · Conector Upwork · Lovable + Supabase · Conector Cloudflare · Conector vidIQ

### 7.3 Ligar os plugins: small-business, marketing, engineering, design, finance, Hostinger, Adobe e Cloudinary

**Você** · 15 min

- [ ] **Pronto quando:** Os comandos dos plugins aparecem no Claude
- Implanta: Plugins: small- business + marketing · Plugins: engineering + design · Plugins: finance + Fiscal.ai · Plugins: Hostinger · Adobe · Cloudinary

### 7.4 Entrar nos outros assistentes (ChatGPT, Gemini, Grok, DeepSeek, Perplexity, Codex, agentes do Google) e anotar quais são pagos

**Você** · 30 min

- [ ] **Pronto quando:** Acessos no KeePassXC e assinaturas pagas lançadas na tabela ferramentas do banco de métricas
- Implanta: ChatGPT · Gemini (pago) · Grok · DeepSeek · Perplexity · Codex (OpenAI) · Agentes de código do Google

<a id="f8"></a>

## 8 · Automação e medição

n8n, banco de métricas, Grafana e Uptime Kuma rodando.

### 8.1 Gerar as senhas da stack e guardar no KeePassXC

**Script** · 5 min

```bash
cd infra/automacao && bash gerar-senhas.sh
```

- [ ] **Pronto quando:** .env criado com permissão 600
- Implanta: n8n

### 8.2 Subir a stack

**Script** · 10 min

```bash
cd infra/automacao && docker compose up -d
```

- [ ] **Pronto quando:** 'docker compose ps' com todos healthy
- Implanta: Docker + Compose · n8n · Banco de métricas (PostgreSQL) · PostgreSQL

### 8.3 Conferir os serviços

**Script** · 2 min

```bash
bash scripts/wsl/verificar.sh --servicos
```

- [ ] **Pronto quando:** verificar.sh --servicos sem FALTA na área servico
- Implanta: Verificadores

### 8.4 Entrar no Grafana (admin) e ver a fonte 'Métricas AMtech' conectada

**Você** · 10 min

```text
http://localhost:3001
```

- [ ] **Pronto quando:** Explore > Métricas AMtech > 'select 1' responde
- Implanta: Grafana

### 8.5 Criar a conta do n8n

**Você** · 5 min

```text
http://localhost:5678
```

- [ ] **Pronto quando:** Painel do n8n abre
- Implanta: n8n

### 8.6 Cadastrar no Uptime Kuma os monitores do n8n, Grafana e dos sites

**Você** · 15 min

```text
http://localhost:3002
```

- [ ] **Pronto quando:** Monitores verdes; aviso no Telegram configurado
- Implanta: Uptime Kuma

### 8.7 Decidir: Postiz agora ou agendador nativo das redes

**Você** · 10 min

- [ ] **Pronto quando:** Decisão anotada em infra/postiz/README.md
- Implanta: Postiz (agendador)

<a id="f9"></a>

## 9 · Pipeline de conteúdo

Gravou ou escreveu, as peças aparecem na fila de aprovação.

### 9.1 Preencher o guia de marca

**Você** · 40 min

- [ ] **Pronto quando:** config/marca.md sem colchetes
- O Claude pode rascunhar a partir dos documentos de marca e presença; você corrige.
- Implanta: Marca pessoal Alan Mateus

### 9.2 Criar a chave da API no console da Anthropic e colocar no conteudo.env

**Você** · 10 min

- [ ] **Pronto quando:** ANTHROPIC_API_KEY preenchida em ~/.config/amtech/conteudo.env
- A API é cobrada por uso, separada da assinatura do Claude. Defina um limite de gasto mensal no console.
- Implanta: Claude (assinatura e API)

### 9.3 Criar o bot de aviso no Telegram (opcional)

**Você** · 10 min

- [ ] **Pronto quando:** Mensagem de teste chega no celular
- Implanta: Telegram (avisos) · Aprovação no celular

### 9.4 Testar o caminho sem gastar

**Script** · 2 min

```bash
echo teste > ~/AMtech/entrada/ideias/teste.txt && touch -d '-2 min' ~/AMtech/entrada/ideias/teste.txt && python3 tools/conteudo/processar.py --uma-vez --simular
```

- [ ] **Pronto quando:** Uma pasta [SIMULADO] aparece em ~/AMtech/fila
- Implanta: Pipeline de conteúdo

### 9.5 Ligar o timer de 15 minutos

**Script** · 2 min

```bash
bash scripts/wsl/ativar-pipeline.sh
```

- [ ] **Pronto quando:** verificar.sh --servicos mostra o timer OK
- Implanta: Pipeline de conteúdo · Agente editor de conteúdo · Flywheel de conteúdo

### 9.6 Colocar uma aula gravada de verdade em ~/AMtech/entrada/aulas

**Você** · 20 min

- [ ] **Pronto quando:** Peças da aula na fila em até 15 minutos depois de transcrita
- Implanta: Whisper (local) · Flywheel de conteúdo

<a id="f10"></a>

## 10 · Estúdio de conteúdo

Gravar, editar e montar imagens no mesmo padrão toda semana, sem pensar.

### 10.1 Montar no OBS as cenas de aula, tela com rosto e vídeo vertical

**Você** · 40 min

- [ ] **Pronto quando:** Gravação de teste de 1 minuto com áudio limpo nas três cenas
- Implanta: OBS Studio

### 10.2 Criar no Audacity a cadeia de limpeza da sua voz (ruído, compressor, volume)

**Você** · 20 min

- [ ] **Pronto quando:** A mesma limpeza aplicada com um clique numa gravação nova
- Implanta: Audacity

### 10.3 Criar no DaVinci ou Kdenlive o projeto modelo com abertura, legendas e formato vertical

**Você** · 40 min

- [ ] **Pronto quando:** Um corte de 30 segundos exportado a partir do modelo
- Implanta: DaVinci Resolve ou Kdenlive

### 10.4 Criar os modelos de capa, carrossel e thumbnail com a sua marca (Canva, Krita ou Inkscape)

**Claude com você** · 40 min

- [ ] **Pronto quando:** Três modelos salvos; uma peça da fila montada com eles
- O Claude cria os modelos no Canva pelo conector, a partir do config/marca.md.
- Implanta: Canva · Krita · Inkscape · Conectores Canva + Figma

### 10.5 Clonar a sua própria voz na ElevenLabs (opcional, plano pago)

**Você** · 1 h 00 min

- [ ] **Pronto quando:** Trecho de teste com a sua voz clonada aprovado por você
- Só a sua voz, com 30 minutos ou mais de áudio limpo. Avise o público quando a voz for gerada por IA. Voz de outra pessoa, nunca.
- **Precisa:** pagar um serviço
- Implanta: Voz clonada (ElevenLabs)

<a id="f11"></a>

## 11 · Contas, canais e sites

Perfis, domínio, e-mail e sites prontos para receber o que o pipeline produz.

### 11.1 Completar Instagram, YouTube, TikTok, LinkedIn e Facebook com a mesma identidade

**Você** · 1 h 30 min

- [ ] **Pronto quando:** Foto, nome, bio e link iguais nas cinco redes
- Implanta: Instagram · YouTube · TikTok · LinkedIn · Facebook · Marca pessoal Alan Mateus

### 11.2 Configurar o WhatsApp Business com catálogo, respostas rápidas e horário

**Você** · 30 min

- [ ] **Pronto quando:** Mensagem de teste recebe a saudação automática
- Implanta: WhatsApp Business

### 11.3 Registrar o domínio no Registro.br e apontar para a Cloudflare

**Você** · 30 min

- [ ] **Pronto quando:** DNS ativo na Cloudflare
- **Precisa:** pagar um serviço
- Implanta: Domínio (Registro.br) · Cloudflare (DNS, Pages, e-mail)

### 11.4 Criar o e-mail profissional do domínio

**Você** · 30 min

- [ ] **Pronto quando:** Envia e recebe
- **Precisa:** pagar um serviço
- Implanta: E-mail profissional (enviar e receber)

### 11.5 Criar o Gerenciador de Negócios da Meta, o Pixel e a conta de anúncios

**Você** · 40 min

- [ ] **Pronto quando:** Pixel instalado na página de vendas
- Implanta: Meta Business Suite · Tags de conversão (Pixel, Google…)

### 11.6 Montar no MailerLite os grupos, o formulário da isca e a sequência de boas-vindas

**Claude com você** · 30 min

- [ ] **Pronto quando:** Inscrição de teste recebe o primeiro e-mail
- O Claude faz pelo conector do MailerLite, com a sua aprovação.
- Implanta: MailerLite · Isca grátis + sequência de e-mails · Conector MailerLite

### 11.7 Publicar o site pessoal e blog no GitHub Pages (alanmateus17.github.io)

**Claude com você** · 1 h 00 min

- [ ] **Pronto quando:** Site no ar com portfólio, blog e formulário da newsletter
- Implanta: Site pessoal + blog (Jekyll) · GitHub Pages

### 11.8 Publicar o site do Instituto AMS com a página de pré-venda na Cloudflare Pages

**Claude com você** · 1 h 00 min

- [ ] **Pronto quando:** Página no ar com o domínio e o Pixel
- Fica na Cloudflare Pages porque o plano grátis do Vercel não permite uso comercial. O Claude publica pelo conector da Cloudflare ou pelo Wrangler.
- Implanta: Instituto AMS · Cloudflare (DNS, Pages, e-mail)

### 11.9 Publicar o site do Grupo AMtech e o Catálogo do HTML

**Claude com você** · 1 h 30 min

- [ ] **Pronto quando:** Os dois sites no ar com domínio e HTTPS
- Implanta: Site Grupo AMtech · Catálogo do HTML

### 11.10 Ligar o Umami nos sites

**Claude com você** · 20 min

- [ ] **Pronto quando:** Uma visita de teste aparece no painel do Umami
- Implanta: Umami (analytics)

### 11.11 Ligar o Google Search Console no domínio e enviar o sitemap de cada site

**Você** · 10 min

- [ ] **Pronto quando:** Propriedade verificada e sitemaps lidos
- Implanta: Google Search Console · Busca Google (SEO)

### 11.12 Separar na Hostinger o espaço dos sites de clientes

**Claude com você** · 30 min

- [ ] **Pronto quando:** Auditoria da Hostinger sem pendências e um site modelo pronto para copiar
- O Claude faz a auditoria pelo plugin da Hostinger e aponta o que precisa de atenção.
- Implanta: Hostinger (clientes WP) · Sites para pequenas empresas

<a id="f12"></a>

## 12 · Vendas e finanças no CPF

Cada oferta pode ser vendida, recebida e declarada do jeito certo.

### 12.1 Subir a conta gov.br para prata ou ouro

**Você** · 20 min

- [ ] **Pronto quando:** Nível prata ou ouro aparece no app gov.br
- Implanta: gov.br (prata ou ouro)

### 12.2 Abrir a conta bancária separada para o que você vende (no CPF)

**Você** · 30 min

- [ ] **Pronto quando:** Conta aberta; todas as plataformas vão pagar nela
- Implanta: Conta bancária separada (CPF)

### 12.3 Fazer a consulta com o contador: carnê-leão e a partir de que renda abrir CNPJ

**Você** · 1 h 00 min

- [ ] **Pronto quando:** Regras do carnê-leão anotadas e o valor de virada para o CNPJ definido
- **Precisa:** pagar um serviço
- Implanta: Contador

### 12.4 Publicar termos de uso e política de privacidade (LGPD) e ter o contrato padrão de serviço

**Claude com você** · 1 h 00 min

- [ ] **Pronto quando:** Links de termos e privacidade no rodapé de todos os sites; contrato em modelo editável
- O Claude rascunha; antes de usar, peça para o contador ou um advogado revisar. Isto vem antes de coletar e-mail ou vender.
- Implanta: Termos, privacidade (LGPD) e contratos

### 12.5 Criar as contas da Hotmart e da Kiwify no CPF e cadastrar o mini-curso

**Você** · 1 h 00 min

- [ ] **Pronto quando:** Produto em rascunho nas duas
- Implanta: Hotmart · Kiwify · Mini-curso Lógica de Programação

### 12.6 Abrir as contas na Eduzz e na Udemy e publicar artigos e projetos na DIO

**Você** · 1 h 00 min

- [ ] **Pronto quando:** Contas aprovadas; formulário fiscal da Udemy enviado; primeiro artigo publicado na DIO
- Na Udemy o recebimento é por PayPal ou Payoneer e vai para o carnê-leão como renda do exterior.
- Implanta: Eduzz · Udemy · DIO (parceria)

### 12.7 Ativar o Mercado Pago para Pix e cartão das aulas e dos sites

**Você** · 20 min

- [ ] **Pronto quando:** Link de pagamento de teste pago e estornado
- Implanta: Mercado Pago

### 12.8 Criar a agenda online no Cal.com com pagamento para as aulas particulares

**Você** · 30 min

- [ ] **Pronto quando:** Horário de teste marcado e cobrado
- Implanta: Agenda online (Cal.com) · Aulas particulares

### 12.9 Criar o CRM em planilha com origem e consentimento de cada cliente

**Claude com você** · 30 min

- [ ] **Pronto quando:** Planilha com colunas de oferta, origem, consentimento LGPD e próximo passo
- Implanta: CRM simples (planilha) · CRM único + LGPD

### 12.10 Abrir a comunidade dos alunos (Discord ou grupo)

**Você** · 30 min

- [ ] **Pronto quando:** Regras publicadas e convite automático na compra
- Implanta: Comunidade (Discord ou grupo)

### 12.11 Entrar nos programas de afiliados (Amazon, Hotmart) e criar a lista de links

**Você** · 30 min

- [ ] **Pronto quando:** Links de afiliado com UTM numa nota do Obsidian
- Implanta: Afiliados (Amazon, Hotmart…)

### 12.12 Adotar o padrão de UTM em todo link

**Claude com você** · 15 min

- [ ] **Pronto quando:** Gerador de links com UTM salvo e usado no primeiro post
- Implanta: Padrão de UTM

### 12.13 Calcular o lucro por venda de cada oferta e definir as regras de corte dos anúncios

**Você** · 30 min

- [ ] **Pronto quando:** CPA de empate e CPA da margem anotados para cada oferta ativa
- Implanta: Lucro por Venda (calculadora) · Regras de corte

### 12.14 Revisar o portfólio de ofertas: estágio, próximo passo e padrão de qualidade

**Claude com você** · 45 min

- [ ] **Pronto quando:** Uma oferta em construção e uma em validação, cada uma com o checklist de pronto
- O Claude cria o comando /revisar-oferta, que confere um lançamento contra o padrão de qualidade antes de ir ao ar.
- Implanta: Portfólio de ofertas · Esteira de ofertas · Padrão de qualidade · Revisor de oferta

### 12.15 Ligar a pergunta de satisfação depois de cada compra ou serviço e o pedido de avaliação no Google

**Claude com você** · 30 min

- [ ] **Pronto quando:** Compra de teste recebe a pergunta por e-mail
- Implanta: NPS e avaliações

### 12.16 Montar a lista de parceiros e a primeira mensagem de prospecção

**Claude com você** · 45 min

- [ ] **Pronto quando:** 10 parceiros qualificados e a mensagem revisada por você
- O Claude busca e qualifica; quem envia é você.
- Implanta: Prospecção de parceiros

### 12.17 Pesquisar e pedir o registro das marcas no INPI

**Você** · 1 h 00 min

- [ ] **Pronto quando:** Pesquisa sem conflito e pedido protocolado (ou decisão de esperar, anotada)
- **Precisa:** pagar um serviço
- Implanta: Registro de marca (INPI)

### 12.18 Fazer o primeiro carnê-leão do mês e marcar o lembrete mensal

**Você** · 30 min

- [ ] **Pronto quando:** DARF gerado (ou mês sem receita registrado) e lembrete todo dia 20
- Implanta: Carnê-leão (Receita Federal)

### 12.19 Separar a pasta da declaração anual do IR

**Você** · 15 min

- [ ] **Pronto quando:** Pasta com informes e carnês do ano, guardada no backup
- Implanta: Declaração anual do IR

### 12.20 Começar o Caixa da Casa numa planilha até o sistema AM Rendara existir

**Claude com você** · 30 min

- [ ] **Pronto quando:** Entradas e saídas do mês lançadas, separando casa e vendas
- Implanta: Caixa da Casa / AM Rendara

<a id="f13"></a>

## 13 · Vendas medidas

Cada venda chega sozinha ao banco e aparece no painel de lucro.

### 13.1 Criar o túnel público para os webhooks (Cloudflare Tunnel) e preencher N8N_WEBHOOK_URL

**Você** · 40 min

- [ ] **Pronto quando:** https://n8n.seu-dominio responde fora de casa
- Só o caminho de webhook precisa ficar público; o painel do n8n fica protegido.
- **Precisa:** pagar um serviço
- Implanta: Cloudflare (DNS, Pages, e-mail) · Webhooks de venda

### 13.2 Criar no n8n o fluxo: webhook Hotmart, Kiwify e Eduzz → tabela vendas

**Claude com você** · 1 h 00 min

- [ ] **Pronto quando:** Venda de teste aparece na tabela vendas
- O Claude monta o fluxo com você no n8n; a tabela já tem a trava contra venda duplicada.
- Implanta: Webhooks de venda

### 13.3 Lançar os gastos de anúncio (manual no começo, depois pela API de cada rede)

**Você** · 15 min

- [ ] **Pronto quando:** Tabela gastos com a primeira campanha
- Implanta: Banco de métricas (PostgreSQL)

### 13.4 Montar o painel de lucro no Grafana sobre a view lucro_por_produto_mes

**Claude com você** · 45 min

- [ ] **Pronto quando:** Painel mostra receita, anúncio, lucro e CPA por produto
- Implanta: Painel de lucro (Grafana) · Grafana

<a id="f14"></a>

## 14 · Teste do núcleo

Os três testes de ponta a ponta passam: daqui em diante, alimentar o sistema já faz tudo sozinho.

### 14.1 Dev: mudar algo num repositório, commit assinado, push, CI verde

**Você** · 15 min

- [ ] **Pronto quando:** Selo Verified no commit e CI verde
- Implanta: Commits assinados (chave SSH) · GitHub Actions

### 14.2 Conteúdo: arquivo na entrada → peças na fila → aviso no Telegram

**Você** · 20 min

- [ ] **Pronto quando:** Pasta nova na fila e mensagem no celular
- Implanta: Pipeline de conteúdo

### 14.3 Venda: compra de teste na Hotmart → linha na tabela vendas → painel de lucro

**Você** · 20 min

- [ ] **Pronto quando:** Venda de teste no Grafana
- Implanta: Webhooks de venda · Painel de lucro (Grafana)

### 14.4 Rodar os três verificadores juntos

**Script** · 5 min

- [ ] **Pronto quando:** verificar.ps1, verificar.sh e verificar.sh --servicos sem FALTA
- Implanta: Verificadores · Roteiro de implantação

<a id="f15"></a>

## 15 · Base dos sistemas AM

Um sistema novo nasce pronto: arquitetura, testes, login, observabilidade e deploy.

### 15.1 Gerar o modelo de sistema com /novo-sistema-aura

**Claude com você** · 2 h 00 min

- [ ] **Pronto quando:** Sistema exemplo sobe com 'dotnet run' e passa nos testes
- Clean Architecture + DDD, EF Core com Npgsql, multi-tenant com RLS, SignalR com Redis, OpenAPI com Scalar, Next.js com o Aura Design System e Storybook, testes com xUnit, Playwright e k6.
- Implanta: Clean Arch + DDD · EF Core + Npgsql · SignalR · Multi-tenant (RLS) · API ASP.NET Core · Next.js + Aura Design System · OpenAPI + Scalar · Storybook · PostgreSQL · Redis · Testes: xUnit, Playwright, k6

### 15.2 Ligar o login: Keycloak no dev e Entra ID na nuvem

**Claude com você** · 1 h 00 min

- [ ] **Pronto quando:** Usuário de teste entra e só vê os dados da própria empresa
- Implanta: Keycloak / Entra ID

### 15.3 Ligar a observabilidade do dev: .NET Aspire, OpenTelemetry, Prometheus, Seq, Mailpit e Caddy

**Claude com você** · 1 h 00 min

- [ ] **Pronto quando:** Painel do Aspire mostra trace de uma requisição; e-mail de teste cai no Mailpit
- Implanta: .NET Aspire · OpenTelemetry · Prometheus · Seq (logs) · Mailpit · Caddy (proxy + HTTPS)

### 15.4 Criar o projeto no Sentry e ligar no modelo

**Você** · 20 min

- [ ] **Pronto quando:** Erro de teste aparece no Sentry
- Implanta: Sentry (erros)

### 15.5 Ligar o SonarQube Cloud no repositório do modelo

**Você** · 20 min

- [ ] **Pronto quando:** Nota de qualidade aparece no pull request
- O plano grátis cobre repositório público; confira o limite para privado antes de ligar.
- Implanta: SonarQube Cloud

### 15.6 Publicar a imagem Docker da API no GHCR pelo CI

**Claude com você** · 30 min

- [ ] **Pronto quando:** Imagem com a tag do commit aparece nos pacotes do GitHub
- Implanta: GHCR (imagens)

### 15.7 Separar o que do modelo pode virar template à venda

**Você** · 30 min

- [ ] **Pronto quando:** Lista de templates no portfólio de ofertas
- Implanta: Templates e código-fonte

<a id="f16"></a>

## 16 · Nuvem e deploy

As contas de nuvem criadas por código, com custo sob controle.

### 16.1 Instalar Azure CLI, Terraform, Vercel CLI e Wrangler

**Script** · 15 min

```bash
bash scripts/wsl/nuvem.sh
```

- [ ] **Pronto quando:** Termina com 'Pronto'; verificar.sh mostra as quatro ferramentas
- Implanta: Azure CLI · AWS CLI · Terraform

### 16.2 Criar a conta Azure com alerta de orçamento

**Você** · 30 min

- [ ] **Pronto quando:** 'az login' entra e o alerta de gasto está ligado
- Ligue o alerta antes de criar qualquer recurso. O Microsoft Learn do conector ajuda a escolher o serviço mais barato.
- Implanta: Azure

### 16.3 Criar com Terraform o grupo de recursos, o banco e o Key Vault do primeiro sistema

**Claude com você** · 1 h 30 min

- [ ] **Pronto quando:** 'terraform plan' sem diferenças depois do apply
- Implanta: Terraform · Azure

### 16.4 Criar o armazenamento de arquivos (R2 da Cloudflare ou Blob)

**Claude com você** · 30 min

- [ ] **Pronto quando:** Upload de teste pelo sistema exemplo
- Implanta: Armazenamento de arquivos (Blob/R2)

### 16.5 Configurar o e-mail transacional (Resend) com o domínio verificado

**Você** · 30 min

- [ ] **Pronto quando:** E-mail de confirmação de conta chega na caixa de entrada, não no spam
- Implanta: E-mail transacional (Resend, SES…)

### 16.6 Fazer o primeiro deploy do sistema exemplo

**Claude com você** · 1 h 00 min

- [ ] **Pronto quando:** Sistema no ar com HTTPS, login e erro de teste no Sentry
- Implanta: Vercel · Azure · Cloudflare (DNS, Pages, e-mail)

### 16.7 Criar o aura-status: painel de repositórios, backup e Dependabot

**Claude com você** · 2 h 00 min

- [ ] **Pronto quando:** Painel mostra o estado de todos os repositórios
- Implanta: aura-status

<a id="f17"></a>

## 17 · Editora

O livro sai de um repositório com CI, pronto para virar PDF, EPUB e impressão.

### 17.1 Entregar o seu modelo de criação e o seu método passo a passo

**Você** · 2 h 00 min

- [ ] **Pronto quando:** metodo.yaml com cada etapa, entrada, saída e critério de conclusão; template de capítulo pronto
- Implanta: Seu modelo de criação · Seu método (metodo.yaml) · Projeto do capítulo · Mapa de pré-requisitos

### 17.2 Criar o repositório do livro com fonte única, classe LaTeX, exercícios em YAML e CI

**Claude com você** · 2 h 00 min

- [ ] **Pronto quando:** Um push gera PDF, EPUB e o gabarito sem erro
- Depende do capítulo 1 e do seu modelo. O conteúdo é seu; nada de material de terceiros.
- **Precisa:** conteúdo seu pronto (livro, capítulo)
- Implanta: Repositório do livro · Fonte única (Markdown + Pandoc) · Classe LaTeX do livro · Exercícios em YAML · Pipeline do livro (CI) · Revisão automática (LanguageTool, Vale) · Errata e edições · Livro Lógica e Máquina

### 17.3 Montar a matriz de editais e o quadro de referências

**Claude com você** · 1 h 00 min

- [ ] **Pronto quando:** Cada tópico dos editais ligado a um capítulo; lacunas listadas
- Implanta: Matriz de editais · Quadro de referências

### 17.4 Definir o selo Editora AMS Silva (nome, logo e uso no CPF)

**Você** · 30 min

- [ ] **Pronto quando:** Logo aprovado e aplicado na classe LaTeX
- Implanta: Selo Editora AMS Silva

### 17.5 Comprar os ISBNs na CBL e pedir a ficha catalográfica

**Você** · 1 h 00 min

- [ ] **Pronto quando:** ISBN do impresso e do ebook, código de barras e ficha no verso da folha de rosto
- **Precisa:** pagar um serviço, conteúdo seu pronto (livro, capítulo)
- Implanta: ISBN + código de barras (CBL) · Ficha catalográfica

### 17.6 Escolher 3 a 5 leitores beta e um revisor técnico

**Você** · 30 min

- [ ] **Pronto quando:** Nomes confirmados e formulário de retorno pronto
- **Precisa:** conteúdo seu pronto (livro, capítulo)
- Implanta: Leitores beta e revisão técnica

### 17.7 Criar a conta no Amazon KDP e cadastrar o livro em rascunho

**Você** · 1 h 00 min

- [ ] **Pronto quando:** Livro em rascunho com capa, preço e prévia conferida
- **Precisa:** conteúdo seu pronto (livro, capítulo)
- Implanta: Amazon KDP

### 17.8 Enviar o depósito legal à Biblioteca Nacional até 30 dias depois de publicar

**Você** · 30 min

- [ ] **Pronto quando:** Comprovante de envio guardado
- **Precisa:** conteúdo seu pronto (livro, capítulo)
- Implanta: Depósito legal

<a id="f18"></a>

## 18 · Dados, IA e pendrives

O laboratório de dados e de treino no ar, um modelo seu rodando no Ollama e os pendrives de Kali e Arch dando boot.

### 18.1 Gravar o pendrive do Kali com persistência criptografada

**Você** · 1 h 30 min

```bash
winget install --id Rufus.Rufus -e
```

- [ ] **Pronto quando:** O Kali abre pelo F12 e um arquivo salvo continua lá depois de reiniciar
- Siga kali.org/docs/usb. Antes do primeiro boot: suspenda o BitLocker, desligue o Secure Boot e, ao voltar ao Windows, religue o Secure Boot e reative o BitLocker (veja Secure Boot e BitLocker no mapa). Só contra alvos seus ou autorizados.
- Implanta: Pendrive Kali (persistência) · Rufus (grava pendrives)

### 18.2 Instalar o Arch num pendrive rápido ou SSD USB, pelo guia oficial

**Você** · 3 h 00 min

- [ ] **Pronto quando:** O Arch portátil dá boot e abre o terminal com os seus dotfiles
- Use um pendrive para a ISO e outro (64 GB ou mais, USB 3) ou um SSD USB como disco do sistema. Mesmo cuidado com Secure Boot e BitLocker.
- **Precisa:** comprar algo
- Implanta: Pendrive Arch (instalação portátil)

### 18.3 Conferir a GPU dentro do Ubuntu

**Script** · 5 min

```bash
nvidia-smi
```

- [ ] **Pronto quando:** Aparece a GTX 1650 com o driver do Windows
- Implanta: PyTorch + CUDA (WSL2)

### 18.4 Montar o laboratório de dados e de IA

**Script** · 30 min

```bash
bash scripts/wsl/lab-ia.sh
```

- [ ] **Pronto quando:** Termina com 'Pronto' e mostra a GPU vista pelo PyTorch
- Implanta: Python de dados (Polars, Jupyter) · DuckDB + Parquet · Spark (PySpark) · PyTorch + CUDA (WSL2) · MLflow (experimentos) · llama.cpp (GGUF)

### 18.5 Rodar um modelo 8B no Ollama com parte na GPU

**Você** · 15 min

```bash
ollama run llama3.1:8b
```

- [ ] **Pronto quando:** 'ollama ps' mostra o modelo dividido entre CPU e GPU e ele responde
- Mais lento que um 3B ou 4B, que cabem inteiros na placa. Use o 8B quando a qualidade importar mais que a velocidade.
- Implanta: Modelos locais: Qwen · Gemma · Llama · Ollama

### 18.6 Fazer o Data Engineering Zoomcamp e os cursos de IA, um módulo por semana

**Você** · 1 h 00 min

- [ ] **Pronto quando:** Módulo 1 entregue no GitHub e anotado no Obsidian
- O tempo é só para começar; o curso leva 10 semanas. Para a IA vão as suas anotações, nunca o material do curso.
- Implanta: Zoomcamp de dados + cursos de IA

### 18.7 Criar o projeto dbt sobre o banco de métricas

**Claude com você** · 1 h 30 min

- [ ] **Pronto quando:** 'dbt build' verde e o painel de lucro lendo os modelos
- Implanta: dbt Core

### 18.8 Subir o Airflow e agendar o dbt todo dia

**Claude com você** · 1 h 30 min

- [ ] **Pronto quando:** A rotina diária aparece verde no Airflow por 3 dias seguidos
- Implanta: Airflow (orquestração)

### 18.9 Criar as contas do Hugging Face e do Kaggle (e do RunPod, só se precisar)

**Você** · 30 min

- [ ] **Pronto quando:** Token do Hugging Face no KeePassXC; Kaggle com telefone verificado para liberar a GPU
- No RunPod, só crédito pré-pago. Nunca ponha token em notebook público.
- Implanta: Hugging Face (modelos e Hub) · Kaggle · Colab (GPU grátis) · GPU por hora (RunPod e afins)

### 18.10 Montar o primeiro dataset só com conteúdo seu

**Claude com você** · 2 h 00 min

- [ ] **Pronto quando:** Algumas centenas de pares de pergunta e resposta revisados por você, com conjunto de teste separado
- Fontes: suas notas, exercícios, livro e aulas que você gravou. Nada de cursos de terceiros; nada de dados de alunos sem consentimento.
- Implanta: Seus datasets (só conteúdo seu) · Avaliação dos modelos

### 18.11 Primeiro fine-tuning QLoRA de um 8B no Kaggle

**Claude com você** · 3 h 00 min

- [ ] **Pronto quando:** Adaptador salvo no Hugging Face privado e o treino registrado no MLflow
- Implanta: Unsloth (QLoRA) · Kaggle · Colab (GPU grátis)

### 18.12 Avaliar contra o modelo base e levar o seu modelo para o Ollama

**Claude com você** · 1 h 30 min

- [ ] **Pronto quando:** O seu modelo ganha do base no conjunto de teste e responde no Ollama do notebook
- Implanta: Avaliação dos modelos · llama.cpp (GGUF) · Ollama

<a id="f19"></a>

## 19 · Estudo contínuo

As trilhas de estudo ligadas ao setup, sem copiar conteúdo de ninguém.

### 19.1 Pedir o GitHub Education como professor e ligar o Copilot

**Você** · 20 min

- [ ] **Pronto quando:** Benefícios aprovados e Copilot ativo no VS Code
- Implanta: GitHub Education · GitHub Copilot

### 19.2 Montar as trilhas: Microsoft Learn, AWS Skill Builder, roadmap.sh e laboratórios do TryHackMe

**Você** · 30 min

- [ ] **Pronto quando:** Uma trilha de cada em andamento, anotada no Obsidian
- Implanta: Microsoft Learn + AWS Skill Builder · roadmap.sh + Akita · TryHackMe / Hack The Box

### 19.3 Organizar as contas de aluno (Alura, Rocketseat, DIO, Udemy)

**Você** · 15 min

- [ ] **Pronto quando:** Acessos no KeePassXC e cursos em andamento listados no Obsidian
- A licença é para assistir e estudar. Para a IA vão só as suas anotações e os seus projetos.
- Implanta: Alura · Rocketseat · DIO · Udemy

### 19.4 Criar os baralhos do Anki (comandos, conceitos, certificações, concurso)

**Você** · 20 min

- [ ] **Pronto quando:** Revisão do dia feita no notebook e no celular
- Implanta: Anki

<a id="cobertura"></a>

## Cobertura do setup

Todo bloco do mapa do setup tem lugar: num passo acima, como peça a construir, como algo que não se instala ou para depois.

### Peças a construir

| Bloco | Onde e quando |
|---|---|
| Agentes da editora | Com o Claude Code, no repositório do livro, depois do capítulo 1. |
| Acervos de imagens (APIs) | Pipeline de imagens do livro: começa quando o capítulo 1 tiver a lista de figuras (figuras.yaml). |
| Busca automática de imagens | Pipeline de imagens do livro, junto com os acervos. |
| Filtro de licença e fichas | Pipeline de imagens do livro: roda antes de qualquer imagem entrar. |
| Folha de contato (artefato) | Pipeline de imagens do livro: artefato com os candidatos para você escolher. |
| Créditos e legendas | Pipeline de imagens do livro: gerados das fichas; o build falha se faltar ficha. |
| Figuras por código (Matplotlib…) | No repositório do livro, quando o capítulo 1 pedir o primeiro gráfico. |
| Geradores de tabelas | Ampliar o exemplo de tools/editora no repositório do livro. |
| Texto alternativo | Entra no CI do livro antes do primeiro EPUB; rascunho por IA, revisão sua. |

### Não se instala

| Bloco | Por quê |
|---|---|
| Alunos e ex-alunos | É público, não ferramenta: chega pelos canais e sites das fases de contas e vendas. |
| Recrutadores | É público, não ferramenta: chega pelo LinkedIn, GitHub e site pessoal. |
| Notion · monday · GitBook · Stripe | Decidido não usar: repete Obsidian, GitHub Projects, MkDocs e as plataformas de curso. |

### Para depois

Marcados como futuro no mapa: entram quando a renda, a decisão ou o negócio justificar. Cada um vira passo neste roteiro quando chegar a hora.

| Camada | Blocos |
|---|---|
| Público e canais | Google Perfil da Empresa |
| Plataformas de venda e recebimento | Pix Automático + gateway (ex.: Asaas) · YouTube (membros) |
| Marketing, automação e medição | Meta Ads (Instagram, Facebook) · Algoritmo de horário · Google e YouTube Ads · TikTok Ads · Programa de afiliados · Dublagem (YouTube + ElevenLabs) · Spotify Ad Studio · Kwai Ads · Pinterest Ads · LinkedIn Ads · Mídia nativa (Taboola, Outbrain) · Influenciadores e newsletters |
| Pessoa física: impostos e finanças | Certificado digital (e-CNPJ) · API de NFS-e (ex.: Focus NFe) · CNPJ (futuro) |
| Produtos (o que você vende) | Formações (TI, Matemática, Finanças) · Sistemas AM (SaaS) |
| Nuvem, código e entrega | Google Cloud · AWS |
| Aplicação: sistemas AM (Aura) | PostGIS + MapLibre · Serviços aura- (10) · IA: RAG + pgvector · aura-licensing · AM Kaixara (PDV e cardápio) · AM Rotara (entregas) |
| Observabilidade | Loki + Tempo |
| Containers, Kubernetes e infra como código | Kafka · kubectl · Helm · k9s · Datomic local · RabbitMQ · Kubernetes local (kind) |
| Linux (Ubuntu no WSL2, Arch no 2º disco) | Neovim · Arch + Omarchy (2º NVMe) |
| Windows 11, apps e máquinas virtuais | Tailscale (VPN) · Gerenciador de boot · VMs: Kali · Arch · Servidores |
| Segurança e cofre | Chave física (YubiKey) |
| Hardware | SSD SATA 2,5" · 2º NVMe (1–4 TB) · Microfone + câmera · Servidor caseiro (NAS + serviços) · Workstation com GPU |
| Editora AMS Silva (produção de livros) | Gráfica sob demanda (Brasil) · Kit edição especial · Curso por seção · Edição do professor · Traduções (espanhol, inglês) · Manim (animações) |
| Negócios do grupo (Barbacena) | AMtech Software (projetos e SaaS) · Loja AMtech (assistência) · Peças sem estoque (sob encomenda) · Ponto de retirada (Shopee e ML) · AMtech Maker (robótica) · AM Entregas (moto e carro) · Mercado Envios Flex · AM Delivery (várias empresas) · Sushi (delivery) · Cafeteria · Padaria + café da manhã + almoço · 3 CNPJs por frente · Planejador do Grupo · iFood (canal de descoberta) · Vigilância sanitária (RDC 216) · Anatel e Inmetro |
| Operação do grupo (esteira, marca, qualidade) | Canal build in public · Agente atendente (WhatsApp) · Agente orçamentista · Agente cobrador · Agente pós-venda · Analista semanal · Organizador fiscal · Agente comprador |
