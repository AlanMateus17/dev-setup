<!-- Arquivo GERADO por tools/ferramentas/ferramentas.py a partir de data/ferramentas.json. Não edite à mão. -->

# Ferramentas do setup

[← Índice da documentação](../README.md) · Fonte: [`data/ferramentas.json`](../../data/ferramentas.json) · Conferir no PC: `python3 tools/ferramentas/ferramentas.py --estado`

**188 ferramentas.** Obrigatória = o setup conta com ela. Decisão *parada* ou *adiada* = escolha do Alan; não conta como falta no `just validar`.

| Tipo | Total | Obrigatórias | Paradas ou adiadas |
|---|---|---|---|
| Programas do Windows | 33 | 13 | 1 |
| Extensões do VS Code | 16 | 2 | 0 |
| Pacotes do Ubuntu (apt) | 45 | 27 | 0 |
| CLIs do Ubuntu | 49 | 9 | 1 |
| Serviços do Ubuntu | 5 | 2 | 0 |
| Serviços Docker | 40 | 0 | 0 |

## Programas do Windows

| Ferramenta | Grupo | Código aberto | Obrigatória | Para quê | Decisão | Instalar |
|---|---|---|---|---|---|---|
| Windows Terminal | Base e terminal | sim | sim | Terminal do Windows com abas para PowerShell e Ubuntu |  | `winget install --id Microsoft.WindowsTerminal -e` |
| PowerShell 7 | Base e terminal | sim | sim | PowerShell 7, usado pelos scripts de scripts/windows |  | `winget install --id Microsoft.PowerShell -e` |
| Git for Windows | Base e terminal | sim | sim | Git do lado do Windows |  | `winget install --id Git.Git -e` |
| GitHub CLI | Base e terminal | sim | sim | gh: PRs e repositórios do GitHub pelo terminal |  | `winget install --id GitHub.cli -e` |
| VS Code | Base e terminal | não | sim | Editor principal, abre o Ubuntu pelo Remote WSL |  | `winget install --id Microsoft.VisualStudioCode -e` |
| Docker Desktop | Base e terminal | não | sim | Motor do Docker usado pelo Ubuntu (integração WSL) |  | `winget install --id Docker.DockerDesktop -e` |
| 7-Zip | Base e terminal | sim | sim | Compactar e extrair arquivos |  | `winget install --id 7zip.7zip -e` |
| PowerToys | Base e terminal | sim | — | Utilitários do Windows (atalhos, FancyZones) |  | `winget install --id Microsoft.PowerToys -e` |
| KeePassXC | Segurança e rede | sim | — | Cofre de senhas offline |  | `winget install --id KeePassXCTeam.KeePassXC -e` |
| Yubico Authenticator | Segurança e rede | sim | — | Códigos 2FA da YubiKey |  | `winget install --id Yubico.Authenticator -e` |
| Tailscale | Segurança e rede | sim | — | Rede privada para alcançar o notebook pelo celular |  | `winget install --id Tailscale.Tailscale -e` |
| Syncthing | Segurança e rede | sim | — | Sincroniza pastas entre aparelhos, sem nuvem |  | `winget install --id Syncthing.Syncthing -e` |
| Wireshark | Segurança e rede | sim | — | Captura e análise de tráfego de rede |  | `winget install --id WiresharkFoundation.Wireshark -e` |
| Rufus (pendrives do Kali e do Arch) | Segurança e rede | sim | — | Grava pendrives de instalação (Kali, Arch) |  | `winget install --id Rufus.Rufus -e` |
| DBeaver Community | Desenvolvimento | sim | sim | Cliente de banco de dados com interface |  | `winget install --id DBeaver.DBeaver.Community -e` |
| Bruno (testar APIs) | Desenvolvimento | sim | sim | Testar APIs (coleções em arquivo, no Git) |  | `winget install --id Bruno.Bruno -e` |
| draw.io | Desenvolvimento | sim | — | draw.io: diagramas offline |  | `winget install --id JGraph.Draw -e` |
| VirtualBox (Arch, Kali e servidores em VM) | Desenvolvimento | sim | — | Máquinas virtuais (Arch, Kali, servidores) |  | `winget install --id Oracle.VirtualBox -e` |
| Arduino IDE 2 | Desenvolvimento | sim | — | Programar Arduino e ESP32 |  | `winget install --id ArduinoSA.IDE.stable -e` |
| Ollama (IA local na GTX 1650) | Desenvolvimento | sim | — | IA local no Windows (duplica o Ollama do WSL) |  | `winget install --id Ollama.Ollama -e` |
| Obsidian | Estudo e documentos | não | sim | Notas e estudo (vault em C:\Users\alanmateus\vault) |  | `winget install --id Obsidian.Obsidian -e` |
| Anki | Estudo e documentos | sim | sim | Repetição espaçada dos cartões do Professor |  | `winget install --id Anki.Anki -e` |
| SumatraPDF | Estudo e documentos | sim | — | Leitor de PDF leve |  | `winget install --id SumatraPDF.SumatraPDF -e` |
| LibreOffice | Estudo e documentos | sim | — | Documentos, planilhas e apresentações |  | `winget install --id TheDocumentFoundation.LibreOffice -e` |
| Firefox | Estudo e documentos | sim | — | Navegador |  | `winget install --id Mozilla.Firefox -e` |
| OBS Studio | Conteúdo | sim | sim | Gravar aulas e vídeos |  | `winget install --id OBSProject.OBSStudio -e` |
| Audacity | Conteúdo | sim | sim | Editar áudio |  | `winget install --id Audacity.Audacity -e` |
| Kdenlive | Conteúdo | sim | — | Editar vídeo |  | `winget install --id KDE.Kdenlive -e` |
| Krita | Conteúdo | sim | — | Desenho e pintura digital |  | `winget install --id KDE.Krita -e` |
| Inkscape | Conteúdo | sim | — | Desenho vetorial (SVG, logos) |  | `winget install --id Inkscape.Inkscape -e` |
| ShareX | Conteúdo | sim | — | Capturas de tela e GIFs |  | `winget install --id ShareX.ShareX -e` |
| Telegram (aprovação dos posts) | Conteúdo | não | — | Telegram (aprovação dos posts e bot) |  | `winget install --id Telegram.TelegramDesktop -e` |
| cloudflared | Segurança e rede | sim | — | Túnel da Cloudflare; instalado fora do pacotes.json | parada | `(desinstalado; voltar só por decisão: ADR 0022)` |

## Extensões do VS Code

| Ferramenta | Grupo | Código aberto | Obrigatória | Para quê | Decisão | Instalar |
|---|---|---|---|---|---|---|
| ms-vscode-remote.remote-wsl | Extensões do VS Code | sim | sim | Abre o Ubuntu do WSL no VS Code |  | `code --install-extension ms-vscode-remote.remote-wsl` |
| anthropic.claude-code | Extensões do VS Code | não | sim | Claude Code dentro do VS Code |  | `code --install-extension anthropic.claude-code` |
| editorconfig.editorconfig | Extensões do VS Code | sim | — | Aplica o .editorconfig |  | `code --install-extension editorconfig.editorconfig` |
| redhat.vscode-yaml | Extensões do VS Code | sim | — | YAML com validação (compose, CI) |  | `code --install-extension redhat.vscode-yaml` |
| ms-vscode.powershell | Extensões do VS Code | sim | — | Scripts PowerShell |  | `code --install-extension ms-vscode.powershell` |
| timonwong.shellcheck | Extensões do VS Code | sim | — | ShellCheck nos scripts bash |  | `code --install-extension timonwong.shellcheck` |
| ms-dotnettools.csdevkit | Extensões do VS Code | não | — | C#/.NET (carta de reserva) |  | `code --install-extension ms-dotnettools.csdevkit` |
| dbaeumer.vscode-eslint | Extensões do VS Code | sim | — | ESLint (TypeScript/JavaScript) |  | `code --install-extension dbaeumer.vscode-eslint` |
| esbenp.prettier-vscode | Extensões do VS Code | sim | — | Formatação Prettier |  | `code --install-extension esbenp.prettier-vscode` |
| bradlc.vscode-tailwindcss | Extensões do VS Code | sim | — | Tailwind CSS |  | `code --install-extension bradlc.vscode-tailwindcss` |
| ms-azuretools.vscode-docker | Extensões do VS Code | sim | — | Docker e compose |  | `code --install-extension ms-azuretools.vscode-docker` |
| hashicorp.terraform | Extensões do VS Code | sim | — | Terraform |  | `code --install-extension hashicorp.terraform` |
| ms-python.python | Extensões do VS Code | sim | — | Python |  | `code --install-extension ms-python.python` |
| james-yu.latex-workshop | Extensões do VS Code | sim | — | LaTeX do livro |  | `code --install-extension james-yu.latex-workshop` |
| bierner.markdown-mermaid | Extensões do VS Code | sim | — | Diagramas Mermaid no Markdown |  | `code --install-extension bierner.markdown-mermaid` |
| ltex-plus.vscode-ltex-plus | Extensões do VS Code | sim | — | Revisão de português (LanguageTool) |  | `code --install-extension ltex-plus.vscode-ltex-plus` |

## Pacotes do Ubuntu (apt)

| Ferramenta | Grupo | Código aberto | Obrigatória | Para quê | Decisão | Instalar |
|---|---|---|---|---|---|---|
| build-essential | Base (bootstrap) | sim | sim | Compiladores C/C++ e make |  | `bash scripts/wsl/bootstrap.sh` |
| curl | Base (bootstrap) | sim | sim | Baixar pela linha de comando |  | `bash scripts/wsl/bootstrap.sh` |
| wget | Base (bootstrap) | sim | sim | Baixar arquivos |  | `bash scripts/wsl/bootstrap.sh` |
| git | Base (bootstrap) | sim | sim | Controle de versão |  | `bash scripts/wsl/bootstrap.sh` |
| unzip | Base (bootstrap) | sim | sim | Extrair .zip |  | `bash scripts/wsl/bootstrap.sh` |
| zip | Base (bootstrap) | sim | sim | Criar .zip |  | `bash scripts/wsl/bootstrap.sh` |
| zstd | Base (bootstrap) | sim | sim | Compressão zstd (instalador do Ollama) |  | `bash scripts/wsl/bootstrap.sh` |
| jq | Base (bootstrap) | sim | sim | Ler e filtrar JSON |  | `bash scripts/wsl/bootstrap.sh` |
| ripgrep | Base (bootstrap) | sim | sim | Busca rápida em arquivos (rg) |  | `bash scripts/wsl/bootstrap.sh` |
| fzf | Base (bootstrap) | sim | sim | Busca interativa no terminal |  | `bash scripts/wsl/bootstrap.sh` |
| tmux | Base (bootstrap) | sim | sim | Várias janelas no terminal |  | `bash scripts/wsl/bootstrap.sh` |
| zsh | Base (bootstrap) | sim | — | Shell alternativo |  | `bash scripts/wsl/bootstrap.sh` |
| ca-certificates | Base (bootstrap) | sim | sim | Certificados raiz |  | `bash scripts/wsl/bootstrap.sh` |
| gnupg | Base (bootstrap) | sim | sim | Assinatura e criptografia GPG |  | `bash scripts/wsl/bootstrap.sh` |
| bubblewrap | Base (bootstrap) | sim | sim | Sandbox do Claude Code e do ai-jail |  | `bash scripts/wsl/bootstrap.sh` |
| restic | Base (bootstrap) | sim | sim | Backup diário |  | `bash scripts/wsl/bootstrap.sh` |
| pandoc | Base (bootstrap) | sim | sim | Converter documentos (Markdown, DOCX, PDF) |  | `bash scripts/wsl/bootstrap.sh` |
| sqlite3 | Base (bootstrap) | sim | sim | Banco do núcleo pela linha de comando |  | `bash scripts/wsl/bootstrap.sh` |
| postgresql-client | Base (bootstrap) | sim | sim | psql |  | `bash scripts/wsl/bootstrap.sh` |
| python3-venv | Base (bootstrap) | sim | sim | Ambientes virtuais Python |  | `bash scripts/wsl/bootstrap.sh` |
| shellcheck | Base (bootstrap) | sim | sim | Conferir scripts bash |  | `bash scripts/wsl/bootstrap.sh` |
| openssh-client | Base (bootstrap) | sim | sim | SSH |  | `bash scripts/wsl/bootstrap.sh` |
| nmap | Base (bootstrap) | sim | — | Varredura de rede (só laboratório) |  | `bash scripts/wsl/bootstrap.sh` |
| bind9-dnsutils | Base (bootstrap) | sim | — | dig e nslookup |  | `bash scripts/wsl/bootstrap.sh` |
| just | Terminal (bootstrap) | sim | sim | Receitas do setup (just check, just ligar…) |  | `bash scripts/wsl/bootstrap.sh` |
| zoxide | Terminal (bootstrap) | sim | sim | cd que aprende |  | `bash scripts/wsl/bootstrap.sh` |
| eza | Terminal (bootstrap) | sim | sim | ls moderno |  | `bash scripts/wsl/bootstrap.sh` |
| fd-find | Terminal (bootstrap) | sim | sim | find moderno |  | `bash scripts/wsl/bootstrap.sh` |
| btop | Terminal (bootstrap) | sim | sim | Monitor de recursos |  | `bash scripts/wsl/bootstrap.sh` |
| hyperfine | Terminal (bootstrap) | sim | sim | Medir tempo de comandos |  | `bash scripts/wsl/bootstrap.sh` |
| tio | Terminal (bootstrap) | sim | — | Terminal serial (ESP32, Arduino) |  | `bash scripts/wsl/bootstrap.sh` |
| tcpdump | Terminal (bootstrap) | sim | — | Captura de pacotes |  | `bash scripts/wsl/bootstrap.sh` |
| podman | Extras | sim | — | Containers sem daemon |  | `bash scripts/wsl/extras.sh` |
| git-lfs | Extras | sim | — | Arquivos grandes no Git |  | `bash scripts/wsl/extras.sh` |
| hledger | Extras | sim | — | Contabilidade em texto |  | `bash scripts/wsl/extras.sh` |
| neovim | Extras | sim | — | Editor no terminal |  | `bash scripts/wsl/extras.sh` |
| gdb | Engenharia reversa | sim | — | Depurador |  | `bash scripts/wsl/ferramentas-re.sh` |
| binutils | Engenharia reversa | sim | — | objdump, readelf, strings |  | `bash scripts/wsl/ferramentas-re.sh` |
| strace | Engenharia reversa | sim | — | Chamadas de sistema |  | `bash scripts/wsl/ferramentas-re.sh` |
| ltrace | Engenharia reversa | sim | — | Chamadas de biblioteca |  | `bash scripts/wsl/ferramentas-re.sh` |
| xxd | Engenharia reversa | sim | — | Ver bytes em hexadecimal |  | `bash scripts/wsl/ferramentas-re.sh` |
| file | Engenharia reversa | sim | — | Tipo de arquivo |  | `bash scripts/wsl/ferramentas-re.sh` |
| openjdk-21-jdk | Engenharia reversa | sim | — | Java 21 (Ghidra) |  | `bash scripts/wsl/ferramentas-re.sh` |
| radare2 | Engenharia reversa | sim | — | Engenharia reversa no terminal |  | `bash scripts/wsl/ferramentas-re.sh` |
| gocryptfs | Engenharia reversa | sim | — | Pasta criptografada para amostras |  | `bash scripts/wsl/ferramentas-re.sh` |

## CLIs do Ubuntu

| Ferramenta | Grupo | Código aberto | Obrigatória | Para quê | Decisão | Instalar |
|---|---|---|---|---|---|---|
| GitHub CLI | Base (bootstrap) | sim | sim | GitHub pelo terminal |  | `bash scripts/wsl/bootstrap.sh` |
| mise | Base (bootstrap) | sim | sim | Versões de linguagens e CLIs |  | `bash scripts/wsl/bootstrap.sh` |
| Node LTS | Base (bootstrap) | sim | sim | JavaScript/TypeScript (via mise) |  | `bash scripts/wsl/bootstrap.sh` |
| uv | Base (bootstrap) | sim | sim | Python e ferramentas Python |  | `bash scripts/wsl/bootstrap.sh` |
| gitleaks | Base (bootstrap) | sim | sim | Procura segredos nos commits (just check) |  | `bash scripts/wsl/bootstrap.sh` |
| trivy | Base (bootstrap) | sim | sim | Vulnerabilidades em imagens e dependências |  | `bash scripts/wsl/bootstrap.sh` |
| lazygit | Base (bootstrap) | sim | — | Git em tela de terminal |  | `bash scripts/wsl/bootstrap.sh` |
| lazydocker | Base (bootstrap) | sim | — | Docker em tela de terminal |  | `bash scripts/wsl/bootstrap.sh` |
| Starship | Base (bootstrap) | sim | — | Prompt do terminal |  | `bash scripts/wsl/bootstrap.sh` |
| Claude Code | Base (bootstrap) | não | sim | Agente de código |  | `bash scripts/wsl/bootstrap.sh` |
| ai-jail | Base (bootstrap) | sim | sim | Sandbox para agentes de IA |  | `bash scripts/wsl/bootstrap.sh` |
| SDK .NET 10 | Base (bootstrap) | sim | — | Carta de reserva (ADR 0017) |  | `AMTECH_DOTNET=1 bash scripts/wsl/bootstrap.sh` |
| TeX Live | Base (bootstrap) | sim | — | LaTeX do livro |  | `bash scripts/wsl/bootstrap.sh` |
| Whisper local | Base (bootstrap) | sim | — | Transcrição local de áudio |  | `bash scripts/wsl/bootstrap.sh --com-whisper` |
| go | CLIs do mise | sim | — | Linguagem Go |  | `bash scripts/wsl/extras.sh` |
| rust | CLIs do mise | sim | — | Linguagem Rust |  | `bash scripts/wsl/extras.sh` |
| zellij | CLIs do mise | sim | — | Multiplexador de terminal |  | `bash scripts/wsl/extras.sh` |
| yazi | CLIs do mise | sim | — | Gerenciador de arquivos no terminal |  | `bash scripts/wsl/extras.sh` |
| d2 | CLIs do mise | sim | — | Diagramas a partir de texto |  | `bash scripts/wsl/extras.sh` |
| vegeta | CLIs do mise | sim | — | Teste de carga HTTP |  | `bash scripts/wsl/extras.sh` |
| age | CLIs do mise | sim | — | Criptografia de arquivos |  | `bash scripts/wsl/extras.sh` |
| sops | CLIs do mise | sim | — | Segredos criptografados em arquivo |  | `bash scripts/wsl/extras.sh` |
| bore | CLIs do mise | sim | — | Túnel TCP para a internet | parada | `(desinstalado; voltar só por decisão: ADR 0022)` |
| gum | CLIs do mise | sim | — | Componentes para scripts shell |  | `bash scripts/wsl/extras.sh` |
| soft-serve | CLIs do mise | sim | — | Servidor Git no terminal |  | `bash scripts/wsl/extras.sh` |
| goreleaser | CLIs do mise | sim | — | Empacotar releases Go |  | `bash scripts/wsl/extras.sh` |
| cargo-dist | CLIs do mise | sim | — | Empacotar releases Rust |  | `bash scripts/wsl/extras.sh` |
| probe-rs | CLIs do mise | sim | — | Gravar e depurar microcontroladores |  | `bash scripts/wsl/extras.sh` |
| tree-sitter | CLIs do mise | sim | — | Parser de código |  | `bash scripts/wsl/extras.sh` |
| stripe-cli | CLIs do mise | não | — | Testar pagamentos Stripe |  | `bash scripts/wsl/extras.sh` |
| litestream | CLIs do mise | sim | — | Réplica contínua do SQLite |  | `bash scripts/wsl/extras.sh` |
| pocketbase | CLIs do mise | sim | — | Backend em um binário |  | `bash scripts/wsl/extras.sh` |
| posting | Ferramentas Python (uv) | sim | — | Testar APIs no terminal |  | `bash scripts/wsl/extras.sh` |
| harlequin | Ferramentas Python (uv) | sim | — | Cliente SQL no terminal |  | `bash scripts/wsl/extras.sh` |
| aider-chat | Ferramentas Python (uv) | sim | — | Agente de código com modelos locais |  | `bash scripts/wsl/extras.sh` |
| llm | Ferramentas Python (uv) | sim | — | LLM pela linha de comando (plugin Ollama) |  | `bash scripts/wsl/extras.sh` |
| beancount | Ferramentas Python (uv) | sim | — | Contabilidade em texto |  | `bash scripts/wsl/extras.sh` |
| fava | Ferramentas Python (uv) | sim | — | Interface web do beancount |  | `bash scripts/wsl/extras.sh` |
| chezmoi | Extras | sim | — | Dotfiles versionados |  | `bash scripts/wsl/extras.sh` |
| ghidra | Engenharia reversa | sim | — | Engenharia reversa com interface (WSLg) |  | `bash scripts/wsl/ferramentas-re.sh` |
| ilspycmd | Engenharia reversa | sim | — | Descompilar .NET |  | `bash scripts/wsl/ferramentas-re.sh` |
| az | Nuvem | sim | — | Azure CLI |  | `bash scripts/wsl/nuvem.sh` |
| terraform | Nuvem | não | — | Infraestrutura como código |  | `bash scripts/wsl/nuvem.sh` |
| vercel | Nuvem | não | — | Deploy na Vercel |  | `bash scripts/wsl/nuvem.sh` |
| wrangler | Nuvem | sim | — | Deploy na Cloudflare |  | `bash scripts/wsl/nuvem.sh` |
| Ollama (WSL) | IA | sim | — | IA local na GPU, usada pela fila e pelo LiteLLM |  | `just ligar` |
| keepassxc-cli | Segredos | sim | — | Ler segredos do cofre KeePassXC |  | `sudo apt install keepassxc` |
| ai-memory | IA | sim | sim | Memória de longo prazo entre sessões de agentes |  | `ver infra/ai-memory-hooks/README.md` |
| Projeto lab-ia | IA | sim | — | Laboratório de dados e IA (PyTorch com CUDA, ~6 GB) |  | `bash scripts/wsl/lab-ia.sh` |

## Serviços do Ubuntu

| Ferramenta | Grupo | Código aberto | Obrigatória | Para quê | Decisão | Instalar |
|---|---|---|---|---|---|---|
| Servidor ai-memory | Serviços do Ubuntu | sim | sim | Servidor da memória dos agentes em 127.0.0.1:49374 |  | `ver infra/ai-memory-hooks/README.md` |
| Fila de pedidos | Serviços do Ubuntu | sim | sim | Fila de pedidos do celular (tools/remoto/fila.py) |  | `just ligar` |
| Claude Remote Control | Serviços do Ubuntu | sim | — | Controla o Claude Code do PC pelo celular |  | `just ligar` |
| Bot do Telegram | Serviços do Ubuntu | sim | — | Comandos fixos pelo Telegram (só o chat do Alan) |  | `just ligar` |
| Pipeline de conteúdo | Serviços do Ubuntu | sim | — | Timer do pipeline de conteúdo |  | `bash scripts/wsl/ativar-pipeline.sh` |

## Serviços Docker

| Perfil | Serviços | RAM (estimada) | Imagens (estimadas) |
|---|---|---|---|
| Ligado para trabalhar (`just ligar trabalho`) | 23 | 2.6 GB | 11.5 GB |
| Só quando um trabalho pedir (`just ligar sob-demanda`) | 2 | 0.9 GB | 1.0 GB |
| Só para estudo e laboratório (`just ligar laboratorio`) | 15 | 5.3 GB | 16.5 GB |
| **Todos juntos** | 40 | 8.8 GB | 28.9 GB |

| Serviço | Grupo | Perfil | Porta | Para quê | Decisão | Ligar |
|---|---|---|---|---|---|---|
| metricas-db | infra/automacao | trabalho | 5433 | Postgres das métricas |  | `docker compose -f infra/automacao/compose.yaml up -d metricas-db` |
| n8n | infra/automacao | trabalho | 5678 | Automação de fluxos |  | `docker compose -f infra/automacao/compose.yaml up -d n8n` |
| grafana | infra/automacao | trabalho | 3001 | Painéis de métricas |  | `docker compose -f infra/automacao/compose.yaml up -d grafana` |
| uptime-kuma | infra/automacao | trabalho | 3002 | Monitor de disponibilidade |  | `docker compose -f infra/automacao/compose.yaml up -d uptime-kuma` |
| homeassistant | infra/casa | laboratorio | 8123 | Automação da casa |  | `docker compose -f infra/casa/compose.yaml up -d homeassistant` |
| paperless-redis | infra/casa | laboratorio | — | Fila do Paperless |  | `docker compose -f infra/casa/compose.yaml up -d paperless-redis` |
| paperless | infra/casa | laboratorio | 8010 | Documentos digitalizados com OCR |  | `docker compose -f infra/casa/compose.yaml up -d paperless` |
| grocy | infra/casa | laboratorio | 9283 | Estoque da casa |  | `docker compose -f infra/casa/compose.yaml up -d grocy` |
| metabase | infra/dados | sob-demanda | 3012 | Painéis de dados |  | `docker compose -f infra/dados/compose.yaml up -d metabase` |
| litellm | infra/ia | trabalho | 4000 | Gateway de modelos de IA com teto de gasto |  | `docker compose -f infra/ia/compose.yaml up -d litellm` |
| whisper | infra/jarvis | laboratorio | 10300 | Fala para texto na GPU (Jarvis) |  | `docker compose -f infra/jarvis/compose.yaml up -d whisper` |
| piper | infra/jarvis | laboratorio | 10200 | Texto para fala (Jarvis) |  | `docker compose -f infra/jarvis/compose.yaml up -d piper` |
| openwakeword | infra/jarvis | laboratorio | 10400 | Palavra de ativação (Jarvis) |  | `docker compose -f infra/jarvis/compose.yaml up -d openwakeword` |
| mosquitto | infra/jarvis | laboratorio | 1883 | MQTT |  | `docker compose -f infra/jarvis/compose.yaml up -d mosquitto` |
| zigbee2mqtt | infra/jarvis | laboratorio | 8080 | Ponte Zigbee |  | `docker compose -f infra/jarvis/compose.yaml --profile zigbee up -d zigbee2mqtt` |
| frigate | infra/jarvis | laboratorio | 8971, 8554 | Câmeras com detecção |  | `docker compose -f infra/jarvis/compose.yaml --profile cameras up -d frigate` |
| atacante | infra/lab-alvo | laboratorio | — | Container atacante do laboratório |  | `docker compose -f infra/lab-alvo/compose.yaml up -d atacante` |
| alvo | infra/lab-alvo | laboratorio | — | Alvo isolado do laboratório |  | `docker compose -f infra/lab-alvo/compose.yaml up -d alvo` |
| juice-shop | infra/lab-seguranca | laboratorio | 3100 | App vulnerável para estudo |  | `docker compose -f infra/lab-seguranca/compose.yaml up -d juice-shop` |
| webgoat | infra/lab-seguranca | laboratorio | 8180, 9090 | App vulnerável para estudo |  | `docker compose -f infra/lab-seguranca/compose.yaml up -d webgoat` |
| pocketbase | infra/pocketbase | sob-demanda | 8090 | Backend dos sites |  | `docker compose -f infra/pocketbase/compose.yaml up -d pocketbase` |
| adguard | infra/rede | laboratorio | 53, 53, 3011 | DNS com bloqueio de anúncios |  | `docker compose -f infra/rede/compose.yaml up -d adguard` |
| forgejo | infra/soberania | trabalho | 3000, 2222 | Git próprio |  | `docker compose -f infra/soberania/compose.yaml --profile forgejo up -d forgejo` |
| soft-serve | infra/soberania | trabalho | 23231 | Git pelo terminal |  | `docker compose -f infra/soberania/compose.yaml --profile soft-serve up -d soft-serve` |
| headscale | infra/soberania | trabalho | 8085 | Tailscale próprio |  | `docker compose -f infra/soberania/compose.yaml --profile headscale up -d headscale` |
| glitchtip-db | infra/soberania | trabalho | — | Postgres do GlitchTip |  | `docker compose -f infra/soberania/compose.yaml --profile glitchtip up -d glitchtip-db` |
| glitchtip-redis | infra/soberania | trabalho | — | Fila do GlitchTip |  | `docker compose -f infra/soberania/compose.yaml --profile glitchtip up -d glitchtip-redis` |
| glitchtip-web | infra/soberania | trabalho | 8001 | Erros das aplicações |  | `docker compose -f infra/soberania/compose.yaml --profile glitchtip up -d glitchtip-web` |
| glitchtip-worker | infra/soberania | trabalho | — | Trabalhador do GlitchTip |  | `docker compose -f infra/soberania/compose.yaml --profile glitchtip up -d glitchtip-worker` |
| glitchtip-migrate | infra/soberania | trabalho | — | Migração do banco do GlitchTip |  | `docker compose -f infra/soberania/compose.yaml --profile glitchtip up -d glitchtip-migrate` |
| bookstack-db | infra/soberania | trabalho | — | Banco do BookStack |  | `docker compose -f infra/soberania/compose.yaml --profile bookstack up -d bookstack-db` |
| bookstack | infra/soberania | trabalho | 6875 | Wiki da empresa |  | `docker compose -f infra/soberania/compose.yaml --profile bookstack up -d bookstack` |
| actual | infra/soberania | trabalho | 5006 | Orçamento pessoal |  | `docker compose -f infra/soberania/compose.yaml --profile actual up -d actual` |
| ghostfolio-db | infra/soberania | trabalho | — | Postgres do Ghostfolio |  | `docker compose -f infra/soberania/compose.yaml --profile ghostfolio up -d ghostfolio-db` |
| ghostfolio-redis | infra/soberania | trabalho | — | Cache do Ghostfolio |  | `docker compose -f infra/soberania/compose.yaml --profile ghostfolio up -d ghostfolio-redis` |
| ghostfolio | infra/soberania | trabalho | 3333 | Carteira de investimentos |  | `docker compose -f infra/soberania/compose.yaml --profile ghostfolio up -d ghostfolio` |
| firefly-db | infra/soberania | trabalho | — | Banco do Firefly III |  | `docker compose -f infra/soberania/compose.yaml --profile firefly up -d firefly-db` |
| firefly | infra/soberania | trabalho | 8089 | Finanças pessoais |  | `docker compose -f infra/soberania/compose.yaml --profile firefly up -d firefly` |
| akaunting-db | infra/soberania | trabalho | — | Banco do Akaunting |  | `docker compose -f infra/soberania/compose.yaml --profile akaunting up -d akaunting-db` |
| akaunting | infra/soberania | trabalho | 8091 | Contabilidade da empresa |  | `docker compose -f infra/soberania/compose.yaml --profile akaunting up -d akaunting` |

## Acesso de fora (revisão de segurança)

| Ferramenta | Tipo | O que abre |
|---|---|---|
| Tailscale | Programas do Windows | Porta de entrada do celular, por desenho; conferir ACLs e expiração das chaves |
| Syncthing | Programas do Windows | Quando ligado, escuta na rede local (22000) |
| Ollama (IA local na GTX 1650) | Programas do Windows | Deve escutar só em 127.0.0.1 (ADR 0022); a opção 'Expose Ollama to the network' fica desligada |
| cloudflared | Programas do Windows | Abre túnel do PC para a internet; regra de uso pendente |
| bore | CLIs do Ubuntu | Expõe qualquer porta local na internet com um comando; regra de uso pendente |
| Claude Remote Control | Serviços do Ubuntu | Quem entrar na conta claude.ai comanda um shell no PC; exige 2FA na conta |
| Bot do Telegram | Serviços do Ubuntu | Recebe comandos pela internet (allowlist de um chat e de comandos fixos) |
| adguard | Serviços Docker | DNS na porta 53 em todas as interfaces, por desenho |
| soft-serve | Serviços Docker | SSH do Git em 23231 (só 127.0.0.1) |
| headscale | Serviços Docker | Servidor de coordenação da rede privada (só 127.0.0.1:8085); precisa de config.yaml antes de subir |

## Paradas ou adiadas por decisão

Registro das decisões: [ADR 0022](../adr/0022-decisoes-de-25-11-2026.md). O `just validar` avisa quando a data de revisão passa.

| Ferramenta | Decisão | Motivo | Rever em |
|---|---|---|---|
| cloudflared | parada | Desinstalar por decisão do Alan (25/11/2026): abre túnel do PC para a internet (ADR 0022, mantido na emenda: regra de segurança) | 2027-01-20 |
| bore | parada | Desinstalado por decisão do Alan (25/11/2026): abre túnel do PC para a internet (ADR 0022, mantido na emenda: regra de segurança) | 2027-01-20 |
