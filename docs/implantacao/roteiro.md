<!-- Arquivo GERADO por tools/implantacao/gerar.py a partir de data/implantacao.json. Não edite à mão. -->

# Roteiro de implantação

[← Implantação](README.md)

30 fases, 207 passos, cerca de **919 h 30 min** de trabalho no total. Cada passo tem um critério de pronto que dá para conferir. A versão para marcar o progresso é o [`acompanhamento.html`](acompanhamento.html) (e o artefato Implantação AMtech).

Legenda de quem faz: **Você** (só você pode: contas, senhas, decisões), **Script** (você roda o comando), **Claude com você** (o Claude faz pelo conector ou pelo Claude Code, com a sua aprovação).

**Todo o planejamento está aqui:** os 325 blocos do [mapa do setup](../mapa.html), de todas as 23 camadas, entram em algum passo, com a data ou o gatilho de quando. Nada fica de fora; o CI falha se um bloco novo não tiver passo ([quando entra cada bloco](#quando-entra-cada-bloco)).

**Dá para fazer hoje:** 143 dos 207 passos (142 h 20 min) só precisam do notebook e de contas grátis. Os outros dizem o que falta: comprar algo, pagar um serviço, ter um conteúdo seu pronto ou esperar o gatilho da fase.

| Fase | Quando | Passos | Tempo |
|---|---|---:|---:|
| [0 · Preparar](#f0) | Semana 1 · out/2026 | 5 | 2 h 55 min |
| [1 · Windows](#f1) | Semana 1 · out/2026 | 10 | 3 h 15 min |
| [2 · Linux (WSL2)](#f2) | Semana 2 · nov/2026 | 10 | 2 h 22 min |
| [3 · GitHub e CI](#f3) | Semana 2 · nov/2026 | 5 | 55 min |
| [4 · Agentes de IA](#f4) | Semana 2 · nov/2026 | 7 | 2 h 27 min |
| [5 · Backup e segurança](#f5) | Semana 3 · nov/2026 | 4 | 1 h 45 min |
| [6 · Acervo: tudo o que você já tem](#f6) | Semanas 3 e 4 · nov/2026 | 7 | 4 h 55 min |
| [7 · Claude e assistentes](#f7) | Semana 4 · nov/2026 | 4 | 1 h 45 min |
| [8 · Automação e medição](#f8) | Semana 4 · nov/2026 | 7 | 57 min |
| [9 · Pipeline de conteúdo](#f9) | Semana 5 · nov/2026 | 6 | 1 h 24 min |
| [10 · Estúdio de conteúdo](#f10) | Semana 5 · dez/2026 | 5 | 3 h 20 min |
| [11 · Contas, canais e sites](#f11) | Semanas 6 e 7 · dez/2026 | 13 | 9 h 00 min |
| [12 · Vendas e finanças no CPF](#f12) | Semanas 8 a 10 · dez/2026 a jan/2027 | 20 | 12 h 10 min |
| [13 · Vendas medidas](#f13) | Semana 11 · jan/2027 | 4 | 2 h 40 min |
| [14 · Teste do núcleo](#f14) | Semana 11 · jan/2027 | 4 | 1 h 00 min |
| [15 · Base dos sistemas AM](#f15) | Jan a fev/2027 | 8 | 7 h 40 min |
| [16 · Nuvem e deploy](#f16) | Fev a abr/2027 | 7 | 6 h 15 min |
| [17 · Editora](#f17) | Quando o capítulo 1 estiver pronto · **gatilho:** O capítulo 1 e o seu modelo de criação prontos | 11 | 18 h 30 min |
| [18 · Dados, IA e pendrives](#f18) | Pendrives e laboratório a partir da semana 2; dados de fev a jun/2027; treino de ago a dez/2027 | 12 | 16 h 20 min |
| [19 · Marketing pago e crescimento](#f19) | A partir de fev/2027 · **gatilho:** O mini-curso vendeu sem anúncio (por exemplo, 10 vendas) e o painel de lucro está no ar | 10 | 37 h 30 min |
| [20 · Linux nativo e laboratório completo](#f20) | 2027, conforme cada compra | 6 | 18 h 00 min |
| [21 · IA dentro dos sistemas AM](#f21) | Mai a jul/2027 | 1 | 8 h 00 min |
| [22 · Sistemas AM à venda](#f22) | 2027 · **gatilho:** O primeiro sistema AM pronto e testado com um cliente | 4 | 100 h 00 min |
| [23 · CNPJ e formalização](#f23) | Quando a renda pedir · **gatilho:** A renda passou do valor de virada definido com o contador | 4 | 13 h 00 min |
| [24 · Agentes do grupo](#f24) | Junto com o primeiro CNPJ · **gatilho:** Clientes e vendas recorrentes | 7 | 18 h 00 min |
| [25 · Editora: depois do primeiro livro](#f25) | Depois do primeiro livro · **gatilho:** O primeiro livro publicado | 5 | 56 h 00 min |
| [26 · Distribuído, plataforma e segunda nuvem](#f26) | 2028 | 6 | 69 h 00 min |
| [27 · Infraestrutura própria](#f27) | 2028, quando o grupo pedir | 3 | 17 h 00 min |
| [28 · Negócios do grupo em Barbacena](#f28) | Fase A: 12 a 18 meses; B: mais 12 a 18; C: a partir do 3º ou 4º ano · **gatilho:** Os 5 portões do planejador: negócio anterior se pagando há 3 meses, capital em caixa, alguém de confiança tocando, sistema AM rodando e a sua reserva intacta | 8 | 482 h 00 min |
| [29 · Estudo contínuo](#f29) | Contínuo, desde a semana 2 | 4 | 1 h 25 min |

<a id="f0"></a>

## 0 · Preparar

Nada se perde, o hardware está no lugar e as contas estão protegidas antes de mexer na máquina.

**Quando:** Semana 1 · out/2026

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

**Quando:** Semana 1 · out/2026

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

```powershell
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

**Quando:** Semana 2 · nov/2026

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

**Quando:** Semana 2 · nov/2026

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

**Quando:** Semana 2 · nov/2026

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

**Quando:** Semana 3 · nov/2026

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

**Quando:** Semanas 3 e 4 · nov/2026

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

**Quando:** Semana 4 · nov/2026

### 7.1 Organizar o app do Claude: um Project por frente, memória, artefatos, pesquisa e tarefas agendadas

**Você** · 30 min

- [ ] **Pronto quando:** Projects AMtech, Instituto, Editora e Setup criados; uma tarefa agendada de teste rodou
- Implanta: Claude (app) · Projects + memória · Artifacts (Docs, Slides, Sheets…) · Pesquisa aprofundada · Tarefas agendadas

### 7.2 Conferir os conectores: Google, Canva, Figma, MailerLite, Vercel, Microsoft Learn, Upwork, Lovable, Supabase, Cloudflare e vidIQ

**Você** · 30 min

- [ ] **Pronto quando:** Cada conector usado responde a um pedido simples; o da Cloudflare trocado pelo Cloudflare API MCP
- Notion, monday, GitBook e Stripe ficam de fora: repetem Obsidian, GitHub Projects, MkDocs e as plataformas de curso. Desconecte para não confundir.
- Implanta: Conector Google (Gmail, Drive…) · Conectores Canva + Figma · Conector MailerLite · Vercel · AWS · Microsoft Learn · Conector Upwork · Lovable + Supabase · Conector Cloudflare · Conector vidIQ · Notion · monday · GitBook · Stripe

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

**Quando:** Semana 4 · nov/2026

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

**Quando:** Semana 5 · nov/2026

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

**Quando:** Semana 5 · dez/2026

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

**Quando:** Semanas 6 e 7 · dez/2026

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

### 11.10 Mostrar o Catálogo do HTML aos alunos e ex-alunos

**Você** · 20 min

- [ ] **Pronto quando:** Alunos publicando os próprios sites pelo Catálogo
- É material grátis da escola, não venda. Nada de oferecer produto pago a aluno menor de idade; ex-alunos adultos podem seguir as redes.
- Implanta: Alunos e ex-alunos

### 11.11 Ligar o Umami nos sites

**Claude com você** · 20 min

- [ ] **Pronto quando:** Uma visita de teste aparece no painel do Umami
- Implanta: Umami (analytics)

### 11.12 Ligar o Google Search Console no domínio e enviar o sitemap de cada site

**Você** · 10 min

- [ ] **Pronto quando:** Propriedade verificada e sitemaps lidos
- Implanta: Google Search Console · Busca Google (SEO)

### 11.13 Separar na Hostinger o espaço dos sites de clientes

**Claude com você** · 30 min

- [ ] **Pronto quando:** Auditoria da Hostinger sem pendências e um site modelo pronto para copiar
- O Claude faz a auditoria pelo plugin da Hostinger e aponta o que precisa de atenção.
- Implanta: Hostinger (clientes WP) · Sites para pequenas empresas

<a id="f12"></a>

## 12 · Vendas e finanças no CPF

Cada oferta pode ser vendida, recebida e declarada do jeito certo.

**Quando:** Semanas 8 a 10 · dez/2026 a jan/2027

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

**Quando:** Semana 11 · jan/2027

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

**Quando:** Semana 11 · jan/2027

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

**Quando:** Jan a fev/2027

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

### 15.8 Candidatar-se às vagas de dev .NET com GitHub, LinkedIn e site prontos

**Você** · 2 h 00 min

- [ ] **Pronto quando:** 10 candidaturas enviadas com o portfólio do sistema exemplo
- Implanta: Recrutadores

<a id="f16"></a>

## 16 · Nuvem e deploy

As contas de nuvem criadas por código, com custo sob controle.

**Quando:** Fev a abr/2027

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

**Quando:** Quando o capítulo 1 estiver pronto

**Começa quando:** O capítulo 1 e o seu modelo de criação prontos

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

### 17.3 Construir o pipeline de imagens do livro: busca nos acervos, filtro de licença, folha de contato e créditos

**Claude com você** · 4 h 00 min

- [ ] **Pronto quando:** Uma figura do capítulo 1 sai com licença conferida, ficha e crédito; o build falha se faltar ficha
- Implanta: Acervos de imagens (APIs) · Busca automática de imagens · Filtro de licença e fichas · Folha de contato (artefato) · Créditos e legendas

### 17.4 Figuras, tabelas e texto alternativo gerados por código

**Claude com você** · 3 h 00 min

- [ ] **Pronto quando:** Gráficos e tabelas do capítulo 1 gerados no build, com texto alternativo revisado por você
- Implanta: Figuras por código (Matplotlib…) · Geradores de tabelas · Texto alternativo

### 17.5 Criar os agentes da editora: revisor técnico, gabarito, leitor iniciante e consistência

**Claude com você** · 3 h 00 min

- [ ] **Pronto quando:** Os agentes apontam problemas reais no capítulo 1 e você corrige
- Implanta: Agentes da editora

### 17.6 Montar a matriz de editais e o quadro de referências

**Claude com você** · 1 h 00 min

- [ ] **Pronto quando:** Cada tópico dos editais ligado a um capítulo; lacunas listadas
- Implanta: Matriz de editais · Quadro de referências

### 17.7 Definir o selo Editora AMS Silva (nome, logo e uso no CPF)

**Você** · 30 min

- [ ] **Pronto quando:** Logo aprovado e aplicado na classe LaTeX
- Implanta: Selo Editora AMS Silva

### 17.8 Comprar os ISBNs na CBL e pedir a ficha catalográfica

**Você** · 1 h 00 min

- [ ] **Pronto quando:** ISBN do impresso e do ebook, código de barras e ficha no verso da folha de rosto
- **Precisa:** pagar um serviço, conteúdo seu pronto (livro, capítulo)
- Implanta: ISBN + código de barras (CBL) · Ficha catalográfica

### 17.9 Escolher 3 a 5 leitores beta e um revisor técnico

**Você** · 30 min

- [ ] **Pronto quando:** Nomes confirmados e formulário de retorno pronto
- **Precisa:** conteúdo seu pronto (livro, capítulo)
- Implanta: Leitores beta e revisão técnica

### 17.10 Criar a conta no Amazon KDP e cadastrar o livro em rascunho

**Você** · 1 h 00 min

- [ ] **Pronto quando:** Livro em rascunho com capa, preço e prévia conferida
- **Precisa:** conteúdo seu pronto (livro, capítulo)
- Implanta: Amazon KDP

### 17.11 Enviar o depósito legal à Biblioteca Nacional até 30 dias depois de publicar

**Você** · 30 min

- [ ] **Pronto quando:** Comprovante de envio guardado
- **Precisa:** conteúdo seu pronto (livro, capítulo)
- Implanta: Depósito legal

<a id="f18"></a>

## 18 · Dados, IA e pendrives

O laboratório de dados e de treino no ar, um modelo seu rodando no Ollama e os pendrives de Kali e Arch dando boot.

**Quando:** Pendrives e laboratório a partir da semana 2; dados de fev a jun/2027; treino de ago a dez/2027

### 18.1 Gravar o pendrive do Kali com persistência criptografada

**Você** · 1 h 30 min

```powershell
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

## 19 · Marketing pago e crescimento

Pôr dinheiro em anúncio só quando a venda orgânica provou a oferta.

**Quando:** A partir de fev/2027

**Começa quando:** O mini-curso vendeu sem anúncio (por exemplo, 10 vendas) e o painel de lucro está no ar

### 19.1 Primeira campanha na Meta com orçamento de teste

**Você** · 2 h 00 min

- [ ] **Pronto quando:** Campanha com CPA abaixo do de empate por 2 semanas
- **Precisa:** pagar um serviço
- Implanta: Meta Ads (Instagram, Facebook)

### 19.2 Google e YouTube Ads, depois TikTok Ads

**Você** · 3 h 00 min

- [ ] **Pronto quando:** Cada canal com a primeira campanha medida no painel
- **Precisa:** pagar um serviço
- Implanta: Google e YouTube Ads · TikTok Ads

### 19.3 Kwai, Pinterest, LinkedIn, Spotify e mídia nativa, um por vez

**Você** · 4 h 00 min

- [ ] **Pronto quando:** Cada canal testado e mantido ou cortado pelas regras
- **Precisa:** pagar um serviço
- Implanta: Kwai Ads · Pinterest Ads · LinkedIn Ads · Spotify Ad Studio · Mídia nativa (Taboola, Outbrain)

### 19.4 Influenciadores e newsletters parceiras com cupom

**Você** · 2 h 00 min

- [ ] **Pronto quando:** Primeira parceria medida por cupom e UTM
- **Precisa:** pagar um serviço
- Implanta: Influenciadores e newsletters

### 19.5 Abrir o programa de afiliados do mini-curso

**Você** · 1 h 00 min

- [ ] **Pronto quando:** Primeiro afiliado vendendo
- Implanta: Programa de afiliados

### 19.6 Ligar o algoritmo de horário com 3 meses de dados de publicação

**Claude com você** · 2 h 00 min

- [ ] **Pronto quando:** 80% dos posts nas melhores faixas, 20% testando
- Implanta: Algoritmo de horário

### 19.7 Canal build in public: um vídeo por semana das decisões reais

**Você** · 1 h 00 min

- [ ] **Pronto quando:** 4 vídeos seguidos publicados
- Implanta: Canal build in public

### 19.8 Dublar os melhores vídeos para outros idiomas

**Você** · 2 h 00 min

- [ ] **Pronto quando:** Um vídeo com faixa de áudio em inglês ou espanhol
- **Precisa:** pagar um serviço
- Implanta: Dublagem (YouTube + ElevenLabs)

### 19.9 Membros do YouTube quando o canal for elegível

**Você** · 30 min

- [ ] **Pronto quando:** Assinatura de membros ativa
- Implanta: YouTube (membros)

### 19.10 Primeira formação completa (TI, Matemática ou Finanças)

**Você** · 20 h 00 min

- [ ] **Pronto quando:** Formação gravada e à venda
- Implanta: Formações (TI, Matemática, Finanças)

<a id="f20"></a>

## 20 · Linux nativo e laboratório completo

Arch com boot próprio, VMs de laboratório e a segurança física em dia.

**Quando:** 2027, conforme cada compra

### 20.1 Instalar o 2º NVMe e o Arch + Omarchy com boot próprio

**Você** · 5 h 00 min

- [ ] **Pronto quando:** Escolha entre Windows e Arch ao ligar, cada um no seu disco
- **Precisa:** comprar algo
- Implanta: 2º NVMe (1–4 TB) · Arch + Omarchy (2º NVMe) · Gerenciador de boot

### 20.2 Aprender o Neovim aos poucos

**Você** · 5 h 00 min

- [ ] **Pronto quando:** Uma semana editando só no Neovim
- Implanta: Neovim

### 20.3 Montar as VMs do laboratório: Kali, Arch, Ubuntu Server, Windows Server e Rocky

**Você** · 5 h 00 min

- [ ] **Pronto quando:** Duas VMs numa rede isolada, atacante e alvo
- Implanta: VMs: Kali · Arch · Servidores

### 20.4 SSD SATA na baia livre para as VMs

**Você** · 1 h 00 min

- [ ] **Pronto quando:** VMs rodando do SSD novo
- **Precisa:** comprar algo
- Implanta: SSD SATA 2,5"

### 20.5 Chave física no GitHub, Google e Microsoft

**Você** · 1 h 00 min

- [ ] **Pronto quando:** Login com a chave nas três contas
- **Precisa:** comprar algo
- Implanta: Chave física (YubiKey)

### 20.6 Microfone e câmera

**Você** · 1 h 00 min

- [ ] **Pronto quando:** Gravação de teste com áudio limpo sem pós-produção
- **Precisa:** comprar algo
- Implanta: Microfone + câmera

<a id="f21"></a>

## 21 · IA dentro dos sistemas AM

Busca e assistente com os seus dados dentro de um sistema AM.

**Quando:** Mai a jul/2027

### 21.1 RAG com pgvector dentro do primeiro sistema AM

**Claude com você** · 8 h 00 min

- [ ] **Pronto quando:** O sistema responde perguntas com base nos dados do cliente, citando a origem
- Implanta: IA: RAG + pgvector

<a id="f22"></a>

## 22 · Sistemas AM à venda

Os sistemas viram produto por assinatura.

**Quando:** 2027

**Começa quando:** O primeiro sistema AM pronto e testado com um cliente

### 22.1 Lançar o primeiro sistema AM como SaaS, com cobrança por módulo

**Claude com você** · 10 h 00 min

- [ ] **Pronto quando:** Primeiro cliente pagando por assinatura
- Implanta: Sistemas AM (SaaS) · aura-licensing

### 22.2 AM Kaixara: PDV, cardápio, fichas técnicas e estoque

**Claude com você** · 40 h 00 min

- [ ] **Pronto quando:** Rodando num negócio real
- Implanta: AM Kaixara (PDV e cardápio)

### 22.3 AM Rotara: pedidos, rotas e mapas

**Claude com você** · 40 h 00 min

- [ ] **Pronto quando:** Entregas rastreadas no mapa em tempo real
- Implanta: AM Rotara (entregas) · PostGIS + MapLibre

### 22.4 Serviços aura- compartilhados, só quando um sistema precisar

**Claude com você** · 10 h 00 min

- [ ] **Pronto quando:** Um serviço compartilhado usado por dois sistemas
- Implanta: Serviços aura- (10) · Datomic local

<a id="f23"></a>

## 23 · CNPJ e formalização

Sair do CPF na hora certa, com nota fiscal e cobrança automáticas.

**Quando:** Quando a renda pedir

**Começa quando:** A renda passou do valor de virada definido com o contador

### 23.1 Abrir a AMtech Tecnologia (ME no Simples, sócio único)

**Você** · 4 h 00 min

- [ ] **Pronto quando:** CNPJ ativo, conta PJ aberta e contador contratado
- **Precisa:** pagar um serviço
- Implanta: CNPJ (futuro) · 3 CNPJs por frente

### 23.2 Certificado digital e-CNPJ

**Você** · 1 h 00 min

- [ ] **Pronto quando:** Certificado instalado e guardado no KeePassXC
- **Precisa:** pagar um serviço
- Implanta: Certificado digital (e-CNPJ)

### 23.3 Nota fiscal automática pela API de NFS-e

**Claude com você** · 4 h 00 min

- [ ] **Pronto quando:** Venda de teste emite nota sozinha
- Implanta: API de NFS-e (ex.: Focus NFe)

### 23.4 Cobrança recorrente por Pix Automático

**Claude com você** · 4 h 00 min

- [ ] **Pronto quando:** Assinatura de teste cobrada por Pix
- Implanta: Pix Automático + gateway (ex.: Asaas)

<a id="f24"></a>

## 24 · Agentes do grupo

Atendimento, orçamento, cobrança e análise rodando com a sua aprovação.

**Quando:** Junto com o primeiro CNPJ

**Começa quando:** Clientes e vendas recorrentes

### 24.1 Analista semanal: o que funcionou e o que mudar

**Claude com você** · 2 h 00 min

- [ ] **Pronto quando:** Relatório toda segunda no Telegram
- Implanta: Analista semanal

### 24.2 Atendente do WhatsApp com passagem para você

**Claude com você** · 4 h 00 min

- [ ] **Pronto quando:** Dúvida comum respondida sozinha; o resto chega para você
- Implanta: Agente atendente (WhatsApp)

### 24.3 Orçamentista de sites e sistemas

**Claude com você** · 3 h 00 min

- [ ] **Pronto quando:** Rascunho de orçamento em 5 minutos, revisado por você
- Implanta: Agente orçamentista

### 24.4 Cobrador educado (lembrete antes e depois do vencimento)

**Claude com você** · 2 h 00 min

- [ ] **Pronto quando:** Atraso cai pela metade
- Implanta: Agente cobrador

### 24.5 Pós-venda: NPS e pedido de avaliação

**Claude com você** · 2 h 00 min

- [ ] **Pronto quando:** NPS medido em cada venda
- Implanta: Agente pós-venda

### 24.6 Organizador fiscal para o contador

**Claude com você** · 2 h 00 min

- [ ] **Pronto quando:** Pasta do mês pronta no dia 5
- Implanta: Organizador fiscal

### 24.7 Comprador com estoque mínimo

**Claude com você** · 3 h 00 min

- [ ] **Pronto quando:** Pedido de reposição sugerido antes de faltar
- Implanta: Agente comprador

<a id="f25"></a>

## 25 · Editora: depois do primeiro livro

O mesmo livro em mais formatos, públicos e idiomas.

**Quando:** Depois do primeiro livro

**Começa quando:** O primeiro livro publicado

### 25.1 Gráfica sob demanda no Brasil

**Você** · 2 h 00 min

- [ ] **Pronto quando:** Cópia de prova aprovada
- **Precisa:** pagar um serviço
- Implanta: Gráfica sob demanda (Brasil)

### 25.2 Kit edição especial

**Você** · 4 h 00 min

- [ ] **Pronto quando:** Primeira tiragem vendida
- **Precisa:** pagar um serviço
- Implanta: Kit edição especial

### 25.3 Curso por seção do livro, com animações

**Você** · 20 h 00 min

- [ ] **Pronto quando:** Primeira seção gravada e à venda
- Implanta: Curso por seção · Manim (animações)

### 25.4 Edição do professor com licença para escolas

**Claude com você** · 10 h 00 min

- [ ] **Pronto quando:** Primeira escola licenciada
- Implanta: Edição do professor

### 25.5 Traduções para espanhol e inglês

**Claude com você** · 20 h 00 min

- [ ] **Pronto quando:** Primeiro volume traduzido e revisado
- **Precisa:** pagar um serviço
- Implanta: Traduções (espanhol, inglês)

<a id="f26"></a>

## 26 · Distribuído, plataforma e segunda nuvem

O que pesa em vaga pleno e sênior.

**Quando:** 2028

### 26.1 RabbitMQ e depois Kafka entre dois sistemas AM

**Claude com você** · 10 h 00 min

- [ ] **Pronto quando:** Evento de um sistema chega no outro sem chamada direta
- Implanta: RabbitMQ · Kafka

### 26.2 Kubernetes local com kind, kubectl, Helm e k9s

**Você** · 10 h 00 min

- [ ] **Pronto quando:** Um sistema AM rodando no cluster local
- Implanta: Kubernetes local (kind) · kubectl · Helm · k9s

### 26.3 Logs e rastreamento com Loki e Tempo no Grafana

**Claude com você** · 4 h 00 min

- [ ] **Pronto quando:** Uma requisição seguida de ponta a ponta
- Implanta: Loki + Tempo

### 26.4 AWS: Cloud Practitioner e o mesmo sistema rodando lá

**Você** · 20 h 00 min

- [ ] **Pronto quando:** Certificação e post comparando Azure e AWS
- **Precisa:** pagar um serviço
- Implanta: AWS

### 26.5 Google Cloud só o básico, quando um projeto de IA ou dados pedir

**Você** · 5 h 00 min

- [ ] **Pronto quando:** Um serviço usado num projeto real
- Implanta: Google Cloud

### 26.6 App mobile dos sistemas AM com .NET MAUI

**Claude com você** · 20 h 00 min

- [ ] **Pronto quando:** App publicado para teste interno
- Implanta: App mobile (.NET MAUI)

<a id="f27"></a>

## 27 · Infraestrutura própria

Servidor em casa e máquina de IA quando o grupo pedir.

**Quando:** 2028, quando o grupo pedir

### 27.1 Servidor caseiro com backup local e os serviços 24 horas

**Você** · 8 h 00 min

- [ ] **Pronto quando:** n8n, banco e painel rodando no servidor; notebook livre
- **Precisa:** comprar algo
- Implanta: Servidor caseiro (NAS + serviços)

### 27.2 Tailscale entre notebook, celular e servidor

**Você** · 1 h 00 min

- [ ] **Pronto quando:** Acesso ao servidor de fora de casa sem abrir porta
- Implanta: Tailscale (VPN)

### 27.3 Workstation com GPU para treinar e gerar voz e vídeo em casa

**Você** · 8 h 00 min

- [ ] **Pronto quando:** Fine-tuning de 8B rodando local
- **Precisa:** comprar algo
- Implanta: Workstation com GPU

<a id="f28"></a>

## 28 · Negócios do grupo em Barbacena

Um negócio por vez, cada um só depois que o anterior passa no portão.

**Quando:** Fase A: 12 a 18 meses; B: mais 12 a 18; C: a partir do 3º ou 4º ano

**Começa quando:** Os 5 portões do planejador: negócio anterior se pagando há 3 meses, capital em caixa, alguém de confiança tocando, sistema AM rodando e a sua reserva intacta

### 28.1 Planejador do grupo com os números reais

**Claude com você** · 2 h 00 min

- [ ] **Pronto quando:** Capital mínimo e portões calculados com os seus dados
- Implanta: Planejador do Grupo

### 28.2 A1 · AMtech Software

**Você** · 40 h 00 min

- [ ] **Pronto quando:** 3 meses seguidos com lucro e 10 clientes pagantes
- **Precisa:** pagar um serviço
- Implanta: AMtech Software (projetos e SaaS)

### 28.3 A2 · Loja AMtech, peças sob encomenda, ponto de retirada e Maker

**Você** · 80 h 00 min

- [ ] **Pronto quando:** Loja acima do equilíbrio por 3 meses e técnico que abre e fecha sem você
- **Precisa:** comprar algo, pagar um serviço
- Implanta: Loja AMtech (assistência) · Peças sem estoque (sob encomenda) · Ponto de retirada (Shopee e ML) · AMtech Maker (robótica) · Anatel e Inmetro · Google Perfil da Empresa

### 28.4 B1 · AM Entregas e Mercado Envios Flex

**Você** · 80 h 00 min

- [ ] **Pronto quando:** 1.000 entregas por mês e 5 contratos fixos
- **Precisa:** comprar algo, pagar um serviço
- Implanta: AM Entregas (moto e carro) · Mercado Envios Flex

### 28.5 B2 · AM Delivery

**Você** · 80 h 00 min

- [ ] **Pronto quando:** 20 lojistas ativos e 1.500 pedidos por mês
- **Precisa:** pagar um serviço
- Implanta: AM Delivery (várias empresas)

### 28.6 C1 · Sushi, delivery primeiro

**Você** · 80 h 00 min

- [ ] **Pronto quando:** Lucro por 3 meses e sushiman que toca a noite sem você
- **Precisa:** comprar algo, pagar um serviço
- Implanta: Sushi (delivery) · Vigilância sanitária (RDC 216) · iFood (canal de descoberta)

### 28.7 C2 · Padaria com café da manhã e almoço

**Você** · 80 h 00 min

- [ ] **Pronto quando:** Gerente no comando e CMV dentro da meta por 3 meses
- **Precisa:** comprar algo, pagar um serviço
- Implanta: Padaria + café da manhã + almoço

### 28.8 C3 · Cafeteria

**Você** · 40 h 00 min

- [ ] **Pronto quando:** Cafeteria acima do equilíbrio
- **Precisa:** comprar algo, pagar um serviço
- Implanta: Cafeteria

<a id="f29"></a>

## 29 · Estudo contínuo

As trilhas de estudo ligadas ao setup, sem copiar conteúdo de ninguém.

**Quando:** Contínuo, desde a semana 2

### 29.1 Pedir o GitHub Education como professor e ligar o Copilot

**Você** · 20 min

- [ ] **Pronto quando:** Benefícios aprovados e Copilot ativo no VS Code
- Implanta: GitHub Education · GitHub Copilot

### 29.2 Montar as trilhas: Microsoft Learn, AWS Skill Builder, roadmap.sh e laboratórios do TryHackMe

**Você** · 30 min

- [ ] **Pronto quando:** Uma trilha de cada em andamento, anotada no Obsidian
- Implanta: Microsoft Learn + AWS Skill Builder · roadmap.sh + Akita · TryHackMe / Hack The Box

### 29.3 Organizar as contas de aluno (Alura, Rocketseat, DIO, Udemy)

**Você** · 15 min

- [ ] **Pronto quando:** Acessos no KeePassXC e cursos em andamento listados no Obsidian
- A licença é para assistir e estudar. Para a IA vão só as suas anotações e os seus projetos.
- Implanta: Alura · Rocketseat · DIO · Udemy

### 29.4 Criar os baralhos do Anki (comandos, conceitos, certificações, concurso)

**Você** · 20 min

- [ ] **Pronto quando:** Revisão do dia feita no notebook e no celular
- Implanta: Anki

<a id="quando-entra-cada-bloco"></a>

## Quando entra cada bloco

Camada por camada, na mesma ordem do mapa. O número é o passo do roteiro.

### Operação do grupo (esteira, marca, qualidade)

| Bloco | Passo | Quando |
|---|---|---|
| Portfólio de ofertas | 6.7, 12.14 | Semanas 3 e 4 · nov/2026; Semanas 8 a 10 · dez/2026 a jan/2027 |
| Esteira de ofertas | 6.7, 12.14 | Semanas 3 e 4 · nov/2026; Semanas 8 a 10 · dez/2026 a jan/2027 |
| Padrão de qualidade | 12.14 | Semanas 8 a 10 · dez/2026 a jan/2027 |
| Marca pessoal Alan Mateus | 9.1, 11.1 | Semana 5 · nov/2026; Semanas 6 e 7 · dez/2026 |
| NPS e avaliações | 12.15 | Semanas 8 a 10 · dez/2026 a jan/2027 |
| CRM único + LGPD | 12.9 | Semanas 8 a 10 · dez/2026 a jan/2027 |
| Flywheel de conteúdo | 9.5, 9.6 | Semana 5 · nov/2026 |
| Canal build in public | 19.7 | A partir de fev/2027 |
| Agente atendente (WhatsApp) | 24.2 | Junto com o primeiro CNPJ |
| Agente orçamentista | 24.3 | Junto com o primeiro CNPJ |
| Agente cobrador | 24.4 | Junto com o primeiro CNPJ |
| Agente pós-venda | 24.5 | Junto com o primeiro CNPJ |
| Agente editor de conteúdo | 9.5 | Semana 5 · nov/2026 |
| Analista semanal | 24.1 | Junto com o primeiro CNPJ |
| Organizador fiscal | 24.6 | Junto com o primeiro CNPJ |
| Revisor de oferta | 12.14 | Semanas 8 a 10 · dez/2026 a jan/2027 |
| Agente comprador | 24.7 | Junto com o primeiro CNPJ |
| Roteiro de implantação | 14.4 | Semana 11 · jan/2027 |
| Instaladores (PowerShell e bash) | 1.1, 2.4 | Semana 1 · out/2026; Semana 2 · nov/2026 |
| Verificadores | 1.10, 2.10, 8.3, 14.4 | Semana 1 · out/2026; Semana 2 · nov/2026; Semana 4 · nov/2026; Semana 11 · jan/2027 |
| Pipeline de conteúdo | 9.4, 9.5, 14.2 | Semana 5 · nov/2026; Semana 11 · jan/2027 |
| Acervo (seus documentos) | 6.3, 6.4, 6.5 | Semanas 3 e 4 · nov/2026 |

### Público e canais

| Bloco | Passo | Quando |
|---|---|---|
| Meta Business Suite | 11.5 | Semanas 6 e 7 · dez/2026 |
| Instagram | 11.1 | Semanas 6 e 7 · dez/2026 |
| YouTube | 11.1 | Semanas 6 e 7 · dez/2026 |
| LinkedIn | 11.1 | Semanas 6 e 7 · dez/2026 |
| WhatsApp Business | 11.2 | Semanas 6 e 7 · dez/2026 |
| Google Perfil da Empresa | 28.3 | Fase A: 12 a 18 meses; B: mais 12 a 18; C: a partir do 3º ou 4º ano |
| Comunidade (Discord ou grupo) | 12.10 | Semanas 8 a 10 · dez/2026 a jan/2027 |
| Busca Google (SEO) | 11.12 | Semanas 6 e 7 · dez/2026 |
| Alunos e ex-alunos | 11.10 | Semanas 6 e 7 · dez/2026 |
| Recrutadores | 15.8 | Jan a fev/2027 |
| TikTok | 11.1 | Semanas 6 e 7 · dez/2026 |
| Facebook | 11.1 | Semanas 6 e 7 · dez/2026 |

### Marketing, automação e medição

| Bloco | Passo | Quando |
|---|---|---|
| Meta Ads (Instagram, Facebook) | 19.1 | A partir de fev/2027 |
| Isca grátis + sequência de e-mails | 11.6 | Semanas 6 e 7 · dez/2026 |
| MailerLite | 11.6 | Semanas 6 e 7 · dez/2026 |
| Postiz (agendador) | 8.7 | Semana 4 · nov/2026 |
| Aprovação no celular | 9.3 | Semana 5 · nov/2026 |
| Telegram (avisos) | 9.3 | Semana 5 · nov/2026 |
| n8n | 8.1, 8.2, 8.5 | Semana 4 · nov/2026 |
| Algoritmo de horário | 19.6 | A partir de fev/2027 |
| Tags de conversão (Pixel, Google…) | 11.5 | Semanas 6 e 7 · dez/2026 |
| Padrão de UTM | 12.12 | Semanas 8 a 10 · dez/2026 a jan/2027 |
| Google e YouTube Ads | 19.2 | A partir de fev/2027 |
| TikTok Ads | 19.2 | A partir de fev/2027 |
| Regras de corte | 12.13 | Semanas 8 a 10 · dez/2026 a jan/2027 |
| Lucro por Venda (calculadora) | 12.13 | Semanas 8 a 10 · dez/2026 a jan/2027 |
| Webhooks de venda | 13.1, 13.2, 14.3 | Semana 11 · jan/2027 |
| Banco de métricas (PostgreSQL) | 8.2, 13.3 | Semana 4 · nov/2026; Semana 11 · jan/2027 |
| Painel de lucro (Grafana) | 13.4, 14.3 | Semana 11 · jan/2027 |
| Programa de afiliados | 19.5 | A partir de fev/2027 |
| Prospecção de parceiros | 12.16 | Semanas 8 a 10 · dez/2026 a jan/2027 |
| Dublagem (YouTube + ElevenLabs) | 19.8 | A partir de fev/2027 |
| Spotify Ad Studio | 19.3 | A partir de fev/2027 |
| Kwai Ads | 19.3 | A partir de fev/2027 |
| Pinterest Ads | 19.3 | A partir de fev/2027 |
| LinkedIn Ads | 19.3 | A partir de fev/2027 |
| Mídia nativa (Taboola, Outbrain) | 19.3 | A partir de fev/2027 |
| Influenciadores e newsletters | 19.4 | A partir de fev/2027 |

### Plataformas de venda e recebimento

| Bloco | Passo | Quando |
|---|---|---|
| Pix Automático + gateway (ex.: Asaas) | 23.4 | Quando a renda pedir |
| Agenda online (Cal.com) | 12.8 | Semanas 8 a 10 · dez/2026 a jan/2027 |
| CRM simples (planilha) | 12.9 | Semanas 8 a 10 · dez/2026 a jan/2027 |
| Hotmart | 12.5 | Semanas 8 a 10 · dez/2026 a jan/2027 |
| Kiwify | 12.5 | Semanas 8 a 10 · dez/2026 a jan/2027 |
| Eduzz | 12.6 | Semanas 8 a 10 · dez/2026 a jan/2027 |
| Udemy | 12.6 | Semanas 8 a 10 · dez/2026 a jan/2027 |
| DIO (parceria) | 12.6 | Semanas 8 a 10 · dez/2026 a jan/2027 |
| YouTube (membros) | 19.9 | A partir de fev/2027 |
| Mercado Pago | 12.7 | Semanas 8 a 10 · dez/2026 a jan/2027 |
| Afiliados (Amazon, Hotmart…) | 12.11 | Semanas 8 a 10 · dez/2026 a jan/2027 |

### Pessoa física: impostos e finanças

| Bloco | Passo | Quando |
|---|---|---|
| Registro de marca (INPI) | 12.17 | Semanas 8 a 10 · dez/2026 a jan/2027 |
| Termos, privacidade (LGPD) e contratos | 12.4 | Semanas 8 a 10 · dez/2026 a jan/2027 |
| Certificado digital (e-CNPJ) | 23.2 | Quando a renda pedir |
| API de NFS-e (ex.: Focus NFe) | 23.3 | Quando a renda pedir |
| CNPJ (futuro) | 23.1 | Quando a renda pedir |
| gov.br (prata ou ouro) | 12.1 | Semanas 8 a 10 · dez/2026 a jan/2027 |
| Carnê-leão (Receita Federal) | 12.18 | Semanas 8 a 10 · dez/2026 a jan/2027 |
| Declaração anual do IR | 12.19 | Semanas 8 a 10 · dez/2026 a jan/2027 |
| Conta bancária separada (CPF) | 12.2 | Semanas 8 a 10 · dez/2026 a jan/2027 |
| Contador | 12.3 | Semanas 8 a 10 · dez/2026 a jan/2027 |
| Caixa da Casa / AM Rendara | 12.20 | Semanas 8 a 10 · dez/2026 a jan/2027 |

### Vitrine web (sites e domínio)

| Bloco | Passo | Quando |
|---|---|---|
| E-mail profissional (enviar e receber) | 11.4 | Semanas 6 e 7 · dez/2026 |
| Domínio (Registro.br) | 11.3 | Semanas 6 e 7 · dez/2026 |
| Site pessoal + blog (Jekyll) | 11.7 | Semanas 6 e 7 · dez/2026 |
| Instituto AMS | 11.8 | Semanas 6 e 7 · dez/2026 |
| Site Grupo AMtech | 11.9 | Semanas 6 e 7 · dez/2026 |
| Catálogo do HTML | 11.9 | Semanas 6 e 7 · dez/2026 |
| Umami (analytics) | 11.11 | Semanas 6 e 7 · dez/2026 |
| Google Search Console | 11.12 | Semanas 6 e 7 · dez/2026 |
| Hostinger (clientes WP) | 11.13 | Semanas 6 e 7 · dez/2026 |

### Produtos (o que você vende)

| Bloco | Passo | Quando |
|---|---|---|
| Mini-curso Lógica de Programação | 12.5 | Semanas 8 a 10 · dez/2026 a jan/2027 |
| Formações (TI, Matemática, Finanças) | 19.10 | A partir de fev/2027 |
| Templates e código-fonte | 15.7 | Jan a fev/2027 |
| Livro Lógica e Máquina | 17.2 | Quando o capítulo 1 estiver pronto |
| Aulas particulares | 12.8 | Semanas 8 a 10 · dez/2026 a jan/2027 |
| Sites para pequenas empresas | 11.13 | Semanas 6 e 7 · dez/2026 |
| Sistemas AM (SaaS) | 22.1 | 2027 |

### Negócios do grupo (Barbacena)

| Bloco | Passo | Quando |
|---|---|---|
| AMtech Software (projetos e SaaS) | 28.2 | Fase A: 12 a 18 meses; B: mais 12 a 18; C: a partir do 3º ou 4º ano |
| Loja AMtech (assistência) | 28.3 | Fase A: 12 a 18 meses; B: mais 12 a 18; C: a partir do 3º ou 4º ano |
| Peças sem estoque (sob encomenda) | 28.3 | Fase A: 12 a 18 meses; B: mais 12 a 18; C: a partir do 3º ou 4º ano |
| Ponto de retirada (Shopee e ML) | 28.3 | Fase A: 12 a 18 meses; B: mais 12 a 18; C: a partir do 3º ou 4º ano |
| AMtech Maker (robótica) | 28.3 | Fase A: 12 a 18 meses; B: mais 12 a 18; C: a partir do 3º ou 4º ano |
| AM Entregas (moto e carro) | 28.4 | Fase A: 12 a 18 meses; B: mais 12 a 18; C: a partir do 3º ou 4º ano |
| Mercado Envios Flex | 28.4 | Fase A: 12 a 18 meses; B: mais 12 a 18; C: a partir do 3º ou 4º ano |
| AM Delivery (várias empresas) | 28.5 | Fase A: 12 a 18 meses; B: mais 12 a 18; C: a partir do 3º ou 4º ano |
| Sushi (delivery) | 28.6 | Fase A: 12 a 18 meses; B: mais 12 a 18; C: a partir do 3º ou 4º ano |
| Cafeteria | 28.8 | Fase A: 12 a 18 meses; B: mais 12 a 18; C: a partir do 3º ou 4º ano |
| Padaria + café da manhã + almoço | 28.7 | Fase A: 12 a 18 meses; B: mais 12 a 18; C: a partir do 3º ou 4º ano |
| 3 CNPJs por frente | 23.1 | Quando a renda pedir |
| Planejador do Grupo | 28.1 | Fase A: 12 a 18 meses; B: mais 12 a 18; C: a partir do 3º ou 4º ano |
| iFood (canal de descoberta) | 28.6 | Fase A: 12 a 18 meses; B: mais 12 a 18; C: a partir do 3º ou 4º ano |
| Vigilância sanitária (RDC 216) | 28.6 | Fase A: 12 a 18 meses; B: mais 12 a 18; C: a partir do 3º ou 4º ano |
| Anatel e Inmetro | 28.3 | Fase A: 12 a 18 meses; B: mais 12 a 18; C: a partir do 3º ou 4º ano |

### Editora AMS Silva (produção de livros)

| Bloco | Passo | Quando |
|---|---|---|
| Selo Editora AMS Silva | 17.7 | Quando o capítulo 1 estiver pronto |
| Repositório do livro | 17.2 | Quando o capítulo 1 estiver pronto |
| Seu modelo de criação | 17.1 | Quando o capítulo 1 estiver pronto |
| Fonte única (Markdown + Pandoc) | 17.2 | Quando o capítulo 1 estiver pronto |
| Exercícios em YAML | 17.2 | Quando o capítulo 1 estiver pronto |
| Pranchas TikZ e SVG | 2.4 | Semana 2 · nov/2026 |
| Classe LaTeX do livro | 17.2 | Quando o capítulo 1 estiver pronto |
| Pipeline do livro (CI) | 17.2 | Quando o capítulo 1 estiver pronto |
| Revisão automática (LanguageTool, Vale) | 17.2 | Quando o capítulo 1 estiver pronto |
| Agentes da editora | 17.5 | Quando o capítulo 1 estiver pronto |
| Leitores beta e revisão técnica | 17.9 | Quando o capítulo 1 estiver pronto |
| Errata e edições | 17.2 | Quando o capítulo 1 estiver pronto |
| ISBN + código de barras (CBL) | 17.8 | Quando o capítulo 1 estiver pronto |
| Ficha catalográfica | 17.8 | Quando o capítulo 1 estiver pronto |
| Depósito legal | 17.11 | Quando o capítulo 1 estiver pronto |
| Amazon KDP | 17.10 | Quando o capítulo 1 estiver pronto |
| Gráfica sob demanda (Brasil) | 25.1 | Depois do primeiro livro |
| Kit edição especial | 25.2 | Depois do primeiro livro |
| Curso por seção | 25.3 | Depois do primeiro livro |
| Edição do professor | 25.4 | Depois do primeiro livro |
| Traduções (espanhol, inglês) | 25.5 | Depois do primeiro livro |
| Quadro de referências | 17.6 | Quando o capítulo 1 estiver pronto |
| Matriz de editais | 17.6 | Quando o capítulo 1 estiver pronto |
| Projeto do capítulo | 17.1 | Quando o capítulo 1 estiver pronto |
| Mapa de pré-requisitos | 17.1 | Quando o capítulo 1 estiver pronto |
| Seu método (metodo.yaml) | 17.1 | Quando o capítulo 1 estiver pronto |
| Acervos de imagens (APIs) | 17.3 | Quando o capítulo 1 estiver pronto |
| Busca automática de imagens | 17.3 | Quando o capítulo 1 estiver pronto |
| Filtro de licença e fichas | 17.3 | Quando o capítulo 1 estiver pronto |
| Folha de contato (artefato) | 17.3 | Quando o capítulo 1 estiver pronto |
| Créditos e legendas | 17.3 | Quando o capítulo 1 estiver pronto |
| Figuras por código (Matplotlib…) | 17.4 | Quando o capítulo 1 estiver pronto |
| CircuiTikZ | 2.4 | Semana 2 · nov/2026 |
| Geradores de tabelas | 17.4 | Quando o capítulo 1 estiver pronto |
| Manim (animações) | 25.3 | Depois do primeiro livro |
| Texto alternativo | 17.4 | Quando o capítulo 1 estiver pronto |

### Estudo e carreira

| Bloco | Passo | Quando |
|---|---|---|
| Microsoft Learn + AWS Skill Builder | 29.2 | Contínuo, desde a semana 2 |
| TryHackMe / Hack The Box | 29.2 | Contínuo, desde a semana 2 |
| Alura · Rocketseat · DIO · Udemy | 29.3 | Contínuo, desde a semana 2 |
| Anki | 1.2, 29.4 | Semana 1 · out/2026; Contínuo, desde a semana 2 |
| roadmap.sh + Akita | 29.2 | Contínuo, desde a semana 2 |
| GitHub Education | 29.1 | Contínuo, desde a semana 2 |
| Zoomcamp de dados + cursos de IA | 18.6 | Pendrives e laboratório a partir da semana 2; dados de fev a jun/2027; treino de ago a dez/2027 |

### Produção de conteúdo

| Bloco | Passo | Quando |
|---|---|---|
| OBS Studio | 1.2, 10.1 | Semana 1 · out/2026; Semana 5 · dez/2026 |
| DaVinci Resolve ou Kdenlive | 1.8, 10.3 | Semana 1 · out/2026; Semana 5 · dez/2026 |
| Audacity | 1.2, 10.2 | Semana 1 · out/2026; Semana 5 · dez/2026 |
| Canva · Krita · Inkscape | 1.2, 10.4 | Semana 1 · out/2026; Semana 5 · dez/2026 |
| Whisper (local) | 2.4, 9.6 | Semana 2 · nov/2026; Semana 5 · nov/2026 |
| Voz clonada (ElevenLabs) | 10.5 | Semana 5 · dez/2026 |

### Nuvem, código e entrega

| Bloco | Passo | Quando |
|---|---|---|
| Armazenamento de arquivos (Blob/R2) | 16.4 | Fev a abr/2027 |
| E-mail transacional (Resend, SES…) | 16.5 | Fev a abr/2027 |
| SonarQube Cloud | 15.5 | Jan a fev/2027 |
| Projects · ADRs · MkDocs | 3.5 | Semana 2 · nov/2026 |
| Dependabot + CodeQL | 3.3 | Semana 2 · nov/2026 |
| Google Cloud | 26.5 | 2028 |
| GitHub | 3.1, 3.4 | Semana 2 · nov/2026 |
| GitHub Actions | 3.2, 14.1 | Semana 2 · nov/2026; Semana 11 · jan/2027 |
| GHCR (imagens) | 15.6 | Jan a fev/2027 |
| GitHub Pages | 11.7 | Semanas 6 e 7 · dez/2026 |
| Cloudflare (DNS, Pages, e-mail) | 11.3, 11.8, 13.1, 16.6 | Semanas 6 e 7 · dez/2026; Semana 11 · jan/2027; Fev a abr/2027 |
| Vercel | 16.6 | Fev a abr/2027 |
| Azure | 16.2, 16.3, 16.6 | Fev a abr/2027 |
| AWS | 26.4 | 2028 |
| Backblaze B2 (backup) | 5.2 | Semana 3 · nov/2026 |
| GPU por hora (RunPod e afins) | 18.9 | Pendrives e laboratório a partir da semana 2; dados de fev a jun/2027; treino de ago a dez/2027 |
| Google Drive (seus documentos) | 6.1 | Semanas 3 e 4 · nov/2026 |

### Aplicação: sistemas AM (Aura)

| Bloco | Passo | Quando |
|---|---|---|
| OpenAPI + Scalar | 15.1 | Jan a fev/2027 |
| PostGIS + MapLibre | 22.3 | 2027 |
| Storybook | 15.1 | Jan a fev/2027 |
| Clean Arch + DDD | 15.1 | Jan a fev/2027 |
| EF Core + Npgsql | 15.1 | Jan a fev/2027 |
| SignalR | 15.1 | Jan a fev/2027 |
| Multi-tenant (RLS) | 15.1 | Jan a fev/2027 |
| Testes: xUnit, Playwright, k6 | 15.1 | Jan a fev/2027 |
| Serviços aura- (10) | 22.4 | 2027 |
| Next.js + Aura Design System | 15.1 | Jan a fev/2027 |
| API ASP.NET Core | 15.1 | Jan a fev/2027 |
| Keycloak / Entra ID | 15.2 | Jan a fev/2027 |
| IA: RAG + pgvector | 21.1 | Mai a jul/2027 |
| aura-licensing | 22.1 | 2027 |
| aura-status | 16.7 | Fev a abr/2027 |
| AM Kaixara (PDV e cardápio) | 22.2 | 2027 |
| AM Rotara (entregas) | 22.3 | 2027 |
| App mobile (.NET MAUI) | 26.6 | 2028 |

### Observabilidade

| Bloco | Passo | Quando |
|---|---|---|
| Sentry (erros) | 15.4 | Jan a fev/2027 |
| Uptime Kuma | 8.6 | Semana 4 · nov/2026 |
| Seq (logs) | 15.3 | Jan a fev/2027 |
| Loki + Tempo | 26.3 | 2028 |
| OpenTelemetry | 15.3 | Jan a fev/2027 |
| Prometheus | 15.3 | Jan a fev/2027 |
| Grafana | 8.4, 13.4 | Semana 4 · nov/2026; Semana 11 · jan/2027 |
| .NET Aspire | 15.3 | Jan a fev/2027 |

### Containers, Kubernetes e infra como código

| Bloco | Passo | Quando |
|---|---|---|
| Caddy (proxy + HTTPS) | 15.3 | Jan a fev/2027 |
| Mailpit | 15.3 | Jan a fev/2027 |
| Kafka | 26.1 | 2028 |
| kubectl · Helm · k9s | 26.2 | 2028 |
| Azure CLI · AWS CLI | 16.1 | Fev a abr/2027 |
| Datomic local | 22.4 | 2027 |
| Docker + Compose | 2.2, 8.2 | Semana 2 · nov/2026; Semana 4 · nov/2026 |
| PostgreSQL | 8.2, 15.1 | Semana 4 · nov/2026; Jan a fev/2027 |
| Redis | 15.1 | Jan a fev/2027 |
| RabbitMQ | 26.1 | 2028 |
| Kubernetes local (kind) | 26.2 | 2028 |
| Terraform | 16.1, 16.3 | Fev a abr/2027 |

### Claude: recursos, conectores e plugins

| Bloco | Passo | Quando |
|---|---|---|
| Projects + memória | 7.1 | Semana 4 · nov/2026 |
| Artifacts (Docs, Slides, Sheets…) | 7.1 | Semana 4 · nov/2026 |
| Pesquisa aprofundada | 7.1 | Semana 4 · nov/2026 |
| Tarefas agendadas | 7.1 | Semana 4 · nov/2026 |
| Claude in Chrome + uso do computador | 1.7 | Semana 1 · out/2026 |
| Claude (assinatura e API) | 9.2 | Semana 5 · nov/2026 |
| Conector Google (Gmail, Drive…) | 7.2 | Semana 4 · nov/2026 |
| Conectores Canva + Figma | 7.2, 10.4 | Semana 4 · nov/2026; Semana 5 · dez/2026 |
| Conector MailerLite | 7.2, 11.6 | Semana 4 · nov/2026; Semanas 6 e 7 · dez/2026 |
| Vercel · AWS · Microsoft Learn | 7.2 | Semana 4 · nov/2026 |
| Conector Upwork | 7.2 | Semana 4 · nov/2026 |
| Lovable + Supabase | 7.2 | Semana 4 · nov/2026 |
| Notion · monday · GitBook · Stripe | 7.2 | Semana 4 · nov/2026 |
| Plugins: small- business + marketing | 7.3 | Semana 4 · nov/2026 |
| Plugins: engineering + design | 7.3 | Semana 4 · nov/2026 |
| Plugins: finance + Fiscal.ai | 7.3 | Semana 4 · nov/2026 |
| Plugins: Hostinger · Adobe · Cloudinary | 7.3 | Semana 4 · nov/2026 |
| Conector Cloudflare | 7.2 | Semana 4 · nov/2026 |
| Conector vidIQ | 7.2 | Semana 4 · nov/2026 |

### Assistentes de IA (chat, pesquisa e estudo)

| Bloco | Passo | Quando |
|---|---|---|
| Claude (app) | 7.1 | Semana 4 · nov/2026 |
| ChatGPT | 7.4 | Semana 4 · nov/2026 |
| Gemini (pago) | 7.4 | Semana 4 · nov/2026 |
| NotebookLM | 4.7 | Semana 2 · nov/2026 |
| Grok | 7.4 | Semana 4 · nov/2026 |
| DeepSeek | 7.4 | Semana 4 · nov/2026 |
| Codex (OpenAI) | 7.4 | Semana 4 · nov/2026 |
| Agentes de código do Google | 7.4 | Semana 4 · nov/2026 |
| Perplexity | 7.4 | Semana 4 · nov/2026 |
| GitHub Copilot | 29.1 | Contínuo, desde a semana 2 |

### Dados e treino de IA

| Bloco | Passo | Quando |
|---|---|---|
| Python de dados (Polars, Jupyter) | 18.4 | Pendrives e laboratório a partir da semana 2; dados de fev a jun/2027; treino de ago a dez/2027 |
| DuckDB + Parquet | 18.4 | Pendrives e laboratório a partir da semana 2; dados de fev a jun/2027; treino de ago a dez/2027 |
| dbt Core | 18.7 | Pendrives e laboratório a partir da semana 2; dados de fev a jun/2027; treino de ago a dez/2027 |
| Airflow (orquestração) | 18.8 | Pendrives e laboratório a partir da semana 2; dados de fev a jun/2027; treino de ago a dez/2027 |
| Spark (PySpark) | 18.4 | Pendrives e laboratório a partir da semana 2; dados de fev a jun/2027; treino de ago a dez/2027 |
| Seus datasets (só conteúdo seu) | 18.10 | Pendrives e laboratório a partir da semana 2; dados de fev a jun/2027; treino de ago a dez/2027 |
| PyTorch + CUDA (WSL2) | 18.3, 18.4 | Pendrives e laboratório a partir da semana 2; dados de fev a jun/2027; treino de ago a dez/2027 |
| Hugging Face (modelos e Hub) | 18.9 | Pendrives e laboratório a partir da semana 2; dados de fev a jun/2027; treino de ago a dez/2027 |
| Unsloth (QLoRA) | 18.11 | Pendrives e laboratório a partir da semana 2; dados de fev a jun/2027; treino de ago a dez/2027 |
| Kaggle · Colab (GPU grátis) | 18.9, 18.11 | Pendrives e laboratório a partir da semana 2; dados de fev a jun/2027; treino de ago a dez/2027 |
| MLflow (experimentos) | 18.4 | Pendrives e laboratório a partir da semana 2; dados de fev a jun/2027; treino de ago a dez/2027 |
| Avaliação dos modelos | 18.10, 18.12 | Pendrives e laboratório a partir da semana 2; dados de fev a jun/2027; treino de ago a dez/2027 |
| llama.cpp (GGUF) | 18.4, 18.12 | Pendrives e laboratório a partir da semana 2; dados de fev a jun/2027; treino de ago a dez/2027 |

### Agentes de IA e sandbox

| Bloco | Passo | Quando |
|---|---|---|
| Modelos locais: Qwen · Gemma · Llama | 4.4, 18.5 | Semana 2 · nov/2026; Pendrives e laboratório a partir da semana 2; dados de fev a jun/2027; treino de ago a dez/2027 |
| Base de conhecimento (RAG) das suas notas | 4.7, 6.6 | Semana 2 · nov/2026; Semanas 3 e 4 · nov/2026 |
| Claude Code | 4.1 | Semana 2 · nov/2026 |
| ai-jail | 4.2 | Semana 2 · nov/2026 |
| ai-memory | 4.6 | Semana 2 · nov/2026 |
| Servidores MCP | 4.5 | Semana 2 · nov/2026 |
| CLAUDE.md, agentes e skills (seus) | 4.3 | Semana 2 · nov/2026 |
| Ollama | 4.4, 18.5, 18.12 | Semana 2 · nov/2026; Pendrives e laboratório a partir da semana 2; dados de fev a jun/2027; treino de ago a dez/2027 |

### Linux (Ubuntu no WSL2, Arch no 2º disco)

| Bloco | Passo | Quando |
|---|---|---|
| Neovim | 20.2 | 2027, conforme cada compra |
| nmap · dig · curl | 2.4 | Semana 2 · nov/2026 |
| Ubuntu (WSL2) | 2.1, 2.5 | Semana 2 · nov/2026 |
| Git + SSH + gh | 2.4, 2.6 | Semana 2 · nov/2026 |
| .NET 10 · Node · Python | 2.4 | Semana 2 · nov/2026 |
| TeX Live | 2.4 | Semana 2 · nov/2026 |
| gitleaks · Trivy | 2.4 | Semana 2 · nov/2026 |
| dotfiles | 2.7 | Semana 2 · nov/2026 |
| Arch + Omarchy (2º NVMe) | 20.1 | 2027, conforme cada compra |

### Windows 11, apps e máquinas virtuais

| Bloco | Passo | Quando |
|---|---|---|
| Tailscale (VPN) | 27.2 | 2028, quando o grupo pedir |
| .wslconfig + localhost | 1.2 | Semana 1 · out/2026 |
| Terminal · PowerShell · winget | 1.2 | Semana 1 · out/2026 |
| Excalidraw / draw.io | 1.2 | Semana 1 · out/2026 |
| Unity · Cocos | 1.9 | Semana 1 · out/2026 |
| Gerenciador de boot | 20.1 | 2027, conforme cada compra |
| NitroSense + drivers AMD e NVIDIA | 0.3 | Semana 1 · out/2026 |
| 7-Zip | 1.2 | Semana 1 · out/2026 |
| PowerToys | 1.2 | Semana 1 · out/2026 |
| SumatraPDF | 1.2 | Semana 1 · out/2026 |
| ShareX | 1.2 | Semana 1 · out/2026 |
| LibreOffice | 1.2 | Semana 1 · out/2026 |
| Firefox (2º navegador) | 1.2 | Semana 1 · out/2026 |
| Windows 11 Home | 0.3, 0.5 | Semana 1 · out/2026 |
| VS Code | 1.2, 1.6 | Semana 1 · out/2026 |
| Obsidian + Git | 1.2, 2.8, 6.4 | Semana 1 · out/2026; Semana 2 · nov/2026; Semanas 3 e 4 · nov/2026 |
| Syncthing | 1.2, 2.9 | Semana 1 · out/2026; Semana 2 · nov/2026 |
| DBeaver · Bruno | 1.2 | Semana 1 · out/2026 |
| Navegador + Claude in Chrome | 1.7 | Semana 1 · out/2026 |
| VirtualBox | 1.2 | Semana 1 · out/2026 |
| Wireshark | 1.2 | Semana 1 · out/2026 |
| VMs: Kali · Arch · Servidores | 20.3 | 2027, conforme cada compra |
| Arduino IDE 2 | 1.2 | Semana 1 · out/2026 |
| Rufus (grava pendrives) | 18.1 | Pendrives e laboratório a partir da semana 2; dados de fev a jun/2027; treino de ago a dez/2027 |

### Segurança e cofre

| Bloco | Passo | Quando |
|---|---|---|
| Commits assinados (chave SSH) | 2.6, 14.1 | Semana 2 · nov/2026; Semana 11 · jan/2027 |
| restic (backup criptografado) | 5.1, 5.4 | Semana 3 · nov/2026 |
| Chave física (YubiKey) | 20.5 | 2027, conforme cada compra |
| TPM + Secure Boot | 1.4 | Semana 1 · out/2026 |
| BitLocker | 1.4 | Semana 1 · out/2026 |
| Defender + Firewall | 1.5 | Semana 1 · out/2026 |
| KeePassXC | 1.3 | Semana 1 · out/2026 |
| App 2FA (celular) | 0.4 | Semana 1 · out/2026 |
| Backup 3-2-1 | 5.1, 5.2, 5.3, 6.2 | Semana 3 · nov/2026; Semanas 3 e 4 · nov/2026 |

### Hardware

| Bloco | Passo | Quando |
|---|---|---|
| Nobreak | 0.2 | Semana 1 · out/2026 |
| Base com cooler | 0.2 | Semana 1 · out/2026 |
| SSD SATA 2,5" | 20.4 | 2027, conforme cada compra |
| Acer Nitro (32 GB, GTX 1650) | 0.2 | Semana 1 · out/2026 |
| 2º NVMe (1–4 TB) | 20.1 | 2027, conforme cada compra |
| 2º monitor | 0.2 | Semana 1 · out/2026 |
| Microfone + câmera | 20.6 | 2027, conforme cada compra |
| Celular | 0.2, 2.9 | Semana 1 · out/2026; Semana 2 · nov/2026 |
| Disco externo | 0.1, 0.2, 5.1 | Semana 1 · out/2026; Semana 3 · nov/2026 |
| Pendrive Kali (persistência) | 18.1 | Pendrives e laboratório a partir da semana 2; dados de fev a jun/2027; treino de ago a dez/2027 |
| Pendrive Arch (instalação portátil) | 18.2 | Pendrives e laboratório a partir da semana 2; dados de fev a jun/2027; treino de ago a dez/2027 |
| Arduino · ESP32 · Pi | 0.2 | Semana 1 · out/2026 |
| Servidor caseiro (NAS + serviços) | 27.1 | 2028, quando o grupo pedir |
| SSD externo (USB-C 10 Gbps) | 0.2 | Semana 1 · out/2026 |
| Workstation com GPU | 27.3 | 2028, quando o grupo pedir |
