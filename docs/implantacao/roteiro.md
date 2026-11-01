<!-- Arquivo GERADO por tools/implantacao/gerar.py a partir de data/implantacao.json. Não edite à mão. -->

# Roteiro de implantação

[← Implantação](README.md)

50 fases, 396 passos, cerca de **1213 h 53 min** de trabalho no total. Cada passo tem um critério de pronto que dá para conferir. A versão para marcar o progresso é o [`acompanhamento.html`](acompanhamento.html) (e o artefato Implantação AMtech).

Legenda de quem faz: **Você** (só você pode: contas, senhas, decisões), **Script** (você roda o comando), **Claude com você** (o Claude faz pelo conector ou pelo Claude Code, com a sua aprovação).

**Todo o planejamento está aqui:** os 371 blocos do [mapa do setup](../mapa.html), de todas as 23 camadas, entram em algum passo, com a data ou o gatilho de quando, e cada uma das 102 ofertas do portfólio tem o passo em que entra à venda. Nada fica de fora; o CI falha se um bloco ou uma oferta nova não tiver passo ([quando entra cada bloco](#quando-entra-cada-bloco)).

**Dá para fazer hoje:** 304 dos 396 passos (281 h 43 min) só precisam do notebook e de contas grátis. Os outros dizem o que falta: comprar algo, pagar um serviço, ter um conteúdo seu pronto ou esperar o gatilho da fase.

| Fase | Quando | Passos | Tempo |
|---|---|---:|---:|
| [0 · Diagnóstico: o que você já tem](#f0) | Antes de tudo · semana 1 (out/2026) | 6 | 1 h 40 min |
| [1 · Preparar](#f1) | Semana 1 · out/2026 | 4 | 2 h 40 min |
| [2 · Senhas: recuperar, trocar e guardar](#f2) | Semana 1 · out/2026 (o e-mail e as críticas); o resto, 5 contas por semana até dez/2026 | 16 | 7 h 05 min |
| [3 · Windows](#f3) | Semana 1 · out/2026 | 9 | 2 h 30 min |
| [4 · Linux (WSL2)](#f4) | Semana 2 · nov/2026 | 10 | 2 h 22 min |
| [5 · GitHub e CI](#f5) | Semana 2 · nov/2026 | 5 | 55 min |
| [6 · Agentes de IA](#f6) | Semana 2 · nov/2026 | 7 | 2 h 27 min |
| [7 · Backup e segurança](#f7) | Semana 3 · nov/2026 | 4 | 1 h 45 min |
| [8 · Acervo: tudo o que você já tem](#f8) | Semanas 3 e 4 · nov/2026 | 7 | 4 h 55 min |
| [9 · Claude e assistentes](#f9) | Semana 4 · nov/2026 | 4 | 1 h 45 min |
| [10 · Automação e medição](#f10) | Semana 4 · nov/2026 | 8 | 1 h 42 min |
| [11 · Arsenal de rendas: regras e as 3 de agora](#f-arsenal) | Semana 4 · nov/2026 | 8 | 7 h 50 min |
| [12 · Automações do arsenal](#f-automacoes) | Nov/2026 em diante, uma por vez, na ordem de desbloqueio | 12 | 24 h 00 min |
| [13 · Kit de sites com IA da Hostinger](#f-sites) | Semanas 4 e 5 · nov/2026 | 5 | 5 h 00 min |
| [14 · Escola: Fábrica de aulas e documentos](#f-escola) | Semanas 5 e 6 · nov/2026 | 9 | 7 h 42 min |
| [15 · Departamento financeiro pessoal](#f-financeiro) | Dez/2026 | 4 | 1 h 12 min |
| [16 · Investimentos com as suas metodologias](#f-investimentos) | Dez/2026 | 9 | 3 h 50 min |
| [17 · Rotina automatizada](#f-rotina) | Semana 4 · nov/2026 | 5 | 34 min |
| [18 · Comandos remotos pelo Telegram](#f-remoto) | Semana 5 · nov/2026 | 5 | 35 min |
| [19 · Casa e vida](#f-casa) | Dez/2026 | 6 | 2 h 55 min |
| [20 · Padrão de elite em todo repositório](#f-elite) | Semana 5 · nov/2026 | 9 | 2 h 50 min |
| [21 · Agentes e IA com qualidade medida](#f-ia-elite) | Semana 6 · nov/2026 a dez/2026 | 15 | 8 h 00 min |
| [22 · Roteador de agentes e esteira de sites](#f-agentes) | Semana 6 · nov/2026 a dez/2026 | 9 | 2 h 55 min |
| [23 · Modelos grandes sem computador maior](#f-ia-grande) | 2027, depois do primeiro fine-tuning de 8B | 6 | 23 h 00 min |
| [24 · Rede própria entre os seus computadores](#f-rede) | Semana 6 · nov/2026 | 6 | 3 h 10 min |
| [25 · Operação 24 horas](#f-247) | Dez/2026 a jan/2027 | 8 | 7 h 25 min |
| [26 · Dados e crescimento: medir, testar e vender mais](#f-crescimento) | Com a primeira página de venda no ar (jan/2027) e por etapas | 8 | 9 h 30 min |
| [27 · Pipeline de conteúdo](#f11) | Semana 5 · nov/2026 | 7 | 1 h 54 min |
| [28 · Estúdio de conteúdo](#f12) | Semana 5 · dez/2026 | 5 | 3 h 20 min |
| [29 · Contas, canais e sites](#f13) | Semanas 6 e 7 · dez/2026 | 13 | 9 h 00 min |
| [30 · Vendas e finanças no CPF](#f14) | Semanas 8 a 10 · dez/2026 a jan/2027 | 20 | 12 h 10 min |
| [31 · Vendas medidas](#f15) | Semana 11 · jan/2027 | 4 | 2 h 40 min |
| [32 · Teste do núcleo](#f16) | Semana 11 · jan/2027 | 4 | 1 h 00 min |
| [33 · Primeira venda: o mini-curso no ar](#f17) | Semanas 12 a 15 · jan a fev/2027 | 8 | 22 h 30 min |
| [34 · Base dos sistemas AM](#f18) | Junto dos Passos 4 a 6 da trilha de estudo (≈ mar a jun/2027): o modelo nasce no Passo 4 (API e login) e ganha testes e qualidade no Passo 6 | 8 | 7 h 40 min |
| [35 · Nuvem e deploy](#f19) | Com o Passo 5 da trilha de estudo (≈ abr a jun/2027) para a conta e o deploy do sistema exemplo; o deploy de produção do AM Kaixara é o Passo 10 (≈ 2028) | 7 | 6 h 15 min |
| [36 · Editora](#f20) | Quando o capítulo 1 estiver pronto · **gatilho:** O capítulo 1 e o seu modelo de criação prontos | 11 | 18 h 30 min |
| [37 · Dados, IA e pendrives](#f21) | Pendrives, GPU e laboratório a partir da semana 2; Zoomcamp, dbt e Airflow junto do IA2 da Trilha de Dados e IA do vault (depois do Passo 8, ≈ 2028); dataset e treino do 8B junto do IA6 (≈ 2029) | 12 | 16 h 20 min |
| [38 · Mais ofertas, uma por vez](#f22) | Fev a dez/2027, uma oferta por vez · **gatilho:** A primeira venda do mini-curso aconteceu | 23 | 129 h 00 min |
| [39 · Marketing pago e crescimento](#f23) | A partir de fev/2027 · **gatilho:** O mini-curso vendeu sem anúncio (por exemplo, 10 vendas) e o painel de lucro está no ar | 10 | 37 h 30 min |
| [40 · Linux nativo e laboratório completo](#f24) | 2027, conforme cada compra | 6 | 18 h 00 min |
| [41 · IA dentro dos sistemas AM](#f25) | Depois do Passo 9 e do IA0 da Trilha de Dados e IA (≈ 2028), junto do IA5 | 1 | 8 h 00 min |
| [42 · Sistemas AM à venda](#f26) | 2027 · **gatilho:** O primeiro sistema AM pronto e testado com um cliente | 5 | 120 h 00 min |
| [43 · CNPJ e formalização](#f27) | Quando a renda pedir · **gatilho:** A renda passou do valor de virada definido com o contador | 4 | 13 h 00 min |
| [44 · Agentes do grupo](#f28) | Junto com o primeiro CNPJ · **gatilho:** Clientes e vendas recorrentes | 7 | 18 h 00 min |
| [45 · Editora: depois do primeiro livro](#f29) | Depois do primeiro livro · **gatilho:** O primeiro livro publicado | 5 | 56 h 00 min |
| [46 · Distribuído, plataforma e segunda nuvem](#f30) | 2028 | 6 | 69 h 00 min |
| [47 · Infraestrutura própria](#f31) | 2028, quando o grupo pedir | 3 | 17 h 00 min |
| [48 · Negócios do grupo em Barbacena](#f32) | Fase A: 12 a 18 meses; B: mais 12 a 18; C: a partir do 3º ou 4º ano · **gatilho:** Os 5 portões do planejador: negócio anterior se pagando há 3 meses, capital em caixa, alguém de confiança tocando, sistema AM rodando e a sua reserva intacta | 10 | 483 h 00 min |
| [49 · Estudo contínuo](#f33) | Contínuo, desde a semana 2 | 13 | 3 h 50 min |

<a id="f0"></a>

## 0 · Diagnóstico: o que você já tem

Saber exatamente o que o notebook já tem de hardware, segurança, programas, contas e documentos, e começar o roteiro a partir daí.

**Quando:** Antes de tudo · semana 1 (out/2026)

### 0.1 Extrair o dev-setup.zip e deixar a pasta em C:\Users\SEU_USUARIO\dev-setup

**Você** · 5 min

No **PowerShell** do Windows (linha `PS C:\>`):

```powershell
if (Test-Path $HOME\dev-setup) { Write-Host "Ja existe $HOME\dev-setup" } else { Expand-Archive "$HOME\Downloads\dev-setup.zip" "$env:TEMP\dsx" -Force; Move-Item "$env:TEMP\dsx\dev-setup" "$HOME\dev-setup"; Remove-Item "$env:TEMP\dsx" -Recurse; Write-Host "Pronto: $HOME\dev-setup" }
```

- [ ] **Pronto quando:** Pasta C:\Users\SEU_USUARIO\dev-setup com RODAR-DIAGNOSTICO.cmd e as pastas scripts, data e docs logo dentro dela; nenhuma outra cópia em Downloads
- Botão direito no zip > Extrair tudo. O Windows costuma criar dev-setup\dev-setup: recorte a pasta de dentro (a que tem a pasta scripts) e cole em C:\Users\SEU_USUARIO, a pasta com o seu nome. Apague as cópias que sobraram em Downloads, como "dev-setup (1)". Todos os comandos do Windows deste roteiro apontam para esse lugar, então funcionam de qualquer pasta, até da System32 onde o PowerShell de Administrador abre. O comando extrai o zip que está em Downloads e põe a pasta no lugar; baixar o zip da conversa é pelo navegador.

### 0.2 Rodar o diagnóstico: botão direito em RODAR-DIAGNOSTICO.cmd > Executar como administrador

**Script** · 10 min

No **PowerShell** do Windows (linha `PS C:\>`):

```powershell
powershell -ExecutionPolicy Bypass -File $HOME\dev-setup\scripts\windows\diagnostico.ps1
```

- [ ] **Pronto quando:** Pasta diagnostico-AAAAMMDD com diagnostico.md: o que você tem e em que passo cada pendência se resolve
- Somente leitura: não instala nem apaga nada. Em vez do comando, pode clicar com o botão direito em RODAR-DIAGNOSTICO.cmd > Executar como administrador. Se o Windows avisar "O Windows protegeu o computador", clique em Mais informações > Executar assim mesmo. Mostra modelo, processador, memória e slots livres, placa de vídeo, discos e saúde, espaço livre, bateria, monitores, Secure Boot, TPM, criptografia, Defender, programas do setup que já tem e que faltam, WSL, Docker, modelos do Ollama e extensões do VS Code.
- Implanta: Diagnóstico do notebook · Acer Nitro (32 GB, GTX 1650)

### 0.3 Rodar o inventário de espaço: pastas e arquivos que mais ocupam, programas que iniciam com o Windows

**Script** · 15 min

No **PowerShell** do Windows (linha `PS C:\>`):

```powershell
powershell -ExecutionPolicy Bypass -File $HOME\dev-setup\scripts\windows\inventario.ps1
```

- [ ] **Pronto quando:** Pasta inventario-AAAAMMDD gerada; você decidiu o que desinstalar ou mover
- Implanta: Windows 11 Home

### 0.4 Listar as contas e assinaturas que você já tem, sem anotar senha

**Você** · 30 min

- **Fora do terminal:** As contas vêm do seu e-mail e da fatura: o Claude lê só os remetentes pelo conector do Gmail; os valores das assinaturas você confere no cartão.
- [ ] **Pronto quando:** Nota no Obsidian (ou papel) com quais contas do setup já existem e quais assinaturas você paga
- A lista de contas do setup está no ecossistema, em Contas que você precisa ter. Senha nunca vai para nota: só para o KeePassXC, no passo dele.
- Implanta: Windows 11 Home

### 0.5 Ver quantos documentos você já tem (só a contagem, sem abrir)

**Você** · 10 min

No **PowerShell** do Windows (linha `PS C:\>`):

```powershell
Get-ChildItem $HOME -Recurse -File -Include *.docx,*.doc,*.pdf,*.pptx,*.ppt,*.xlsx,*.odt,*.md -ErrorAction SilentlyContinue | Where-Object { $_.FullName -notmatch '\\AppData\\|\\node_modules\\|\\\.vscode\\' } | Group-Object Extension | Sort-Object Count -Descending | Select-Object Name,Count
```

- [ ] **Pronto quando:** Você sabe por alto onde estão as aulas, apostilas, provas e projetos (Drive, notebook, pendrives)
- A organização de verdade vem na fase Acervo, depois do backup.
- Implanta: Google Drive (seus documentos)

### 0.6 Mandar a pasta do diagnóstico para o Claude e ajustar o roteiro

**Claude com você** · 30 min

No **PowerShell** do Windows (linha `PS C:\>`):

```powershell
explorer (Get-ChildItem $HOME\dev-setup -Directory -Filter 'diagnostico-*' | Sort-Object Name | Select-Object -Last 1).FullName
```

- [ ] **Pronto quando:** Passos que você já cumpre marcados no acompanhamento; compras e pendências confirmadas
- Anexe na conversa os dois arquivos da pasta C:\Users\SEU_USUARIO\dev-setup\diagnostico-AAAAMMDD: diagnostico.md e diagnostico.json. Eles não têm senha nem documento seu, só hardware e programas.
- Implanta: Roteiro de implantação

<a id="f1"></a>

## 1 · Preparar

Nada se perde, o hardware está no lugar e as contas estão protegidas antes de mexer na máquina.

**Quando:** Semana 1 · out/2026

### 1.1 Copiar documentos, fotos e projetos para um disco externo

**Você** · 1 h 00 min

No **PowerShell** do Windows (linha `PS C:\>`):

```powershell
$d = 'E:'; if (-not (Test-Path "$d\")) { Write-Host "Nao existe o disco $d. Conecte o disco externo e veja a letra com: Get-Volume" } else { foreach ($p in 'Desktop','Downloads','Documents','Pictures','Videos','Music','dev','dev-setup','source') { if (Test-Path "$HOME\$p") { robocopy "$HOME\$p" "$d\backup-inicial\$p" /E /R:1 /W:1 /XJ /NFL /NDL /NP } } }
```

- [ ] **Pronto quando:** Disco externo com a cópia conferida (abra alguns arquivos)
- Troque E: pela letra do disco externo (Get-Volume lista os discos; o seu notebook só tem o C:). Acrescente à lista as pastas suas que ficam direto na pasta do usuário, como o cofre do Obsidian. O robocopy copia sem apagar nada do notebook; rodar de novo só copia o que mudou. Se as suas pastas estiverem no OneDrive, troque $HOME\$p por $HOME\OneDrive\$p.
- Implanta: Disco externo

### 1.2 Montar a mesa: nobreak, base com cooler, 2º monitor, disco e SSD externos, kits de robótica

**Você** · 30 min

- **Fora do terminal:** Montagem física da mesa. Depois o diagnóstico confere monitores e discos.
- [ ] **Pronto quando:** Notebook no nobreak e na base, 2º monitor funcionando, disco e SSD externos reconhecidos
- O que ainda não comprou fica anotado e não trava as próximas fases. O nobreak vem primeiro: protege o notebook e o backup de queda de energia.
- **Precisa:** comprar algo
- Implanta: Acer Nitro (32 GB, GTX 1650) · Nobreak · Base com cooler · 2º monitor · Disco externo · SSD externo (USB-C 10 Gbps) · Celular · Arduino · ESP32 · Pi

### 1.3 Atualizar o Windows, os drivers e o NitroSense

**Você** · 40 min

No **PowerShell** do Windows (linha `PS C:\>`):

```powershell
winget upgrade --all --accept-source-agreements --accept-package-agreements; Install-PackageProvider NuGet -Force -Scope CurrentUser | Out-Null; Install-Module PSWindowsUpdate -Force -Scope CurrentUser; Import-Module PSWindowsUpdate; Install-WindowsUpdate -MicrosoftUpdate -AcceptAll -IgnoreReboot
```

- [ ] **Pronto quando:** Windows Update sem pendências
- O PSWindowsUpdate é um módulo da PowerShell Gallery, o mais usado para isso. O NitroSense atualiza pela Microsoft Store: winget upgrade também pega ele se veio da loja. O driver da NVIDIA não vem pelo Windows Update: instale o NVIDIA App da Microsoft Store com winget install --id XP8CLZL93F5Z4P --source msstore e, nele, Drivers > Baixar > Instalação expressa. Confira com nvidia-smi.
- Implanta: Windows 11 Home · NitroSense + drivers AMD e NVIDIA

### 1.4 Instalar o app de 2FA no celular e ligar a verificação em duas etapas no GitHub, Google e e-mail

**Você** · 30 min

- **Fora do terminal:** Cada site liga a verificação em duas etapas na própria página, lendo o QR code com o celular; nenhum deixa fazer isso por terminal.
- [ ] **Pronto quando:** 2FA ativo nas três contas, com códigos de recuperação impressos
- Implanta: App 2FA (celular)

<a id="f2"></a>

## 2 · Senhas: recuperar, trocar e guardar

Toda conta com senha única guardada no KeePassXC, verificação em duas etapas nas críticas e um jeito de recuperar tudo se perder o notebook ou o celular.

**Quando:** Semana 1 · out/2026 (o e-mail e as críticas); o resto, 5 contas por semana até dez/2026

### 2.1 Instalar o KeePassXC e criar o cofre com uma senha mestra de 6 palavras

**Você** · 30 min

No **PowerShell** do Windows (linha `PS C:\>`):

```powershell
winget install --id KeePassXCTeam.KeePassXC -e; New-Item -ItemType Directory -Force "$HOME\Documents\Cofre" | Out-Null; & "$env:ProgramFiles\KeePassXC\keepassxc-cli.exe" db-create --set-password "$HOME\Documents\Cofre\Cofre.kdbx"
```

- [ ] **Pronto quando:** Arquivo Cofre.kdbx em Documentos\Cofre abre com a senha mestra; bloqueio automático depois de 5 minutos parado
- Gere a senha mestra no próprio KeePassXC (Ferramentas > Gerador de senhas > Frase-senha, 6 palavras) e decore nos primeiros dias. Ela é a única senha que você precisa saber de cor e não pode ser usada em nenhum outro lugar. Não use arquivo-chave: se perder o arquivo, perde o cofre. Ninguém, nem o Claude, precisa ver o cofre ou a senha mestra. Para gerar a senha mestra no terminal: & "$env:ProgramFiles\KeePassXC\keepassxc-cli.exe" diceware -W 6 (anote no papel do kit e rode cls para limpar a tela). O db-create pergunta a senha sem mostrar nem gravar no histórico.
- Implanta: KeePassXC

### 2.2 Montar o kit de emergência em papel

**Você** · 15 min

- **Fora do terminal:** Papel e caneta, de propósito: o kit não pode depender do computador.
- [ ] **Pronto quando:** Envelope guardado em casa (fora da carteira e da mochila) com a senha mestra, a senha do e-mail principal e os códigos de recuperação do Google
- É o que salva você se esquecer a senha mestra ou perder o notebook e o celular juntos. Papel, não foto: foto vai para a nuvem do celular.
- Implanta: KeePassXC

### 2.3 Recuperar e trocar primeiro a senha do e-mail principal (conta Google)

**Você** · 30 min

No **PowerShell** do Windows (linha `PS C:\>`):

```powershell
Start-Process 'https://myaccount.google.com/security-checkup'
```

- **Fora do terminal:** O comando abre a página; trocar a senha e ligar a verificação é no site do Google, com o celular.
- [ ] **Pronto quando:** Senha nova gerada no KeePassXC; verificação em duas etapas pelo app; telefone e e-mail de recuperação conferidos; códigos de backup salvos no cofre; aparelhos desconhecidos desconectados
- Vem antes de tudo porque todo 'Esqueci minha senha' manda o link para esse e-mail: quem controla o e-mail controla as outras contas. Faça em myaccount.google.com > Segurança e rode a Verificação de segurança no fim. Se não lembrar a senha atual, use g.co/recover no notebook e na rede de casa, onde o Google já reconhece você.
- Implanta: KeePassXC · App 2FA (celular) · Conector Google (Gmail, Drive…)

### 2.4 Preparar o CSV exportado do Chrome/Google para o KeePassXC

**Script** · 5 min

No **Ubuntu** (linha `alanmateus@...$`):

```bash
python3 ~/dev/dev-setup/tools/organizar/senhas_csv.py "/mnt/c/Users/SEU_USUARIO/Downloads/Chrome Passwords.csv"
```

- [ ] **Pronto quando:** keepassxc-importar.csv pronto e lista de senhas repetidas (só nomes de sites)
- Nenhuma senha aparece na tela. Depois de importar, apague os dois CSVs.
- Implanta: Organizadores · KeePassXC

### 2.5 Trazer para o cofre as senhas salvas no Chrome, no Edge e no Google

**Você** · 30 min

No **PowerShell** do Windows (linha `PS C:\>`):

```powershell
Start-Process chrome 'chrome://password-manager/settings'
```

- **Fora do terminal:** Os navegadores só exportam senhas pela janela de configurações, e o KeePassXC só importa CSV pela janela dele (Banco de dados > Importar).
- [ ] **Pronto quando:** Senhas importadas no KeePassXC (Banco de dados > Importar > CSV); o arquivo CSV apagado de vez; navegadores sem salvar senha
- Exporte em chrome://password-manager/settings, edge://wallet/passwords e passwords.google.com. O CSV é a lista de todas as suas senhas em texto puro: importe na hora, apague com Shift+Delete e não deixe em Downloads, no Drive, no e-mail nem no repositório. Não mande esse arquivo para ninguém, nem para o Claude. Só depois de conferir o cofre apague as senhas dos navegadores e desligue 'Oferecer para salvar senhas'.
- Implanta: KeePassXC · Navegador + Claude in Chrome

### 2.6 Ver no KeePassXC quais senhas são fracas, repetidas ou já vazaram

**Você** · 15 min

- **Fora do terminal:** A checagem de vazamento online só existe na janela do KeePassXC (Banco de dados > Relatórios).
- [ ] **Pronto quando:** Lista, em ordem, das contas para trocar (Banco de dados > Relatórios > Integridade e Have I Been Pwned)
- A checagem de vazamento manda só um pedaço do resumo da senha, nunca a senha. Senha que aparece como vazada vai para o topo da lista.
- Implanta: KeePassXC

### 2.7 Trocar as senhas críticas, uma por vez: gov.br, bancos, Microsoft, celular, WhatsApp, GitHub, Meta, Mercado Livre e plataformas de venda

**Você** · 2 h 00 min

- **Fora do terminal:** Cada serviço troca a senha no próprio site ou app; o cofre gera a senha (keepassxc-cli generate -L 24) e você cola lá.
- [ ] **Pronto quando:** Cada conta crítica com senha nova gerada no cofre, verificação em duas etapas ligada e códigos de backup salvos na entrada dela
- Para cada uma: gere a senha no KeePassXC (20 caracteres ou mais), troque no site, salve no cofre antes de fechar a página e saia de todos os outros aparelhos. Banco, troque pelo app oficial. No WhatsApp é o PIN da confirmação em duas etapas. A senha de 4 dígitos do cartão não vai para o cofre: essa você decora.
- Implanta: KeePassXC · App 2FA (celular) · gov.br (prata ou ouro) · Conta bancária separada (CPF) · GitHub

### 2.8 Recuperar as contas cuja senha você esqueceu e fechar as que não usa mais

**Você** · 1 h 00 min

- **Fora do terminal:** Recuperação de conta é sempre pelo site do serviço, com e-mail ou celular.
- [ ] **Pronto quando:** Toda conta da sua lista de contas está no cofre, foi recuperada ou foi excluída
- Use 'Esqueci minha senha' com o e-mail já protegido. Se o e-mail ou o telefone de recuperação forem antigos, cada serviço tem um formulário próprio (Meta: 'Precisa de ajuda?' na tela de login; gov.br: pelo app com reconhecimento facial ou pelo banco). Conta parada que guarda dado seu é risco: exclua.
- Implanta: KeePassXC

### 2.9 Levar o cofre para o celular (KeePassDX no Android ou KeePassium no iPhone)

**Você** · 20 min

- **Fora do terminal:** Instalar e abrir o app é no celular.
- [ ] **Pronto quando:** O cofre abre no celular com a senha mestra; uma senha criada no notebook aparece no celular
- Sincronize o arquivo Cofre.kdbx pelo Syncthing, ou pelo Drive (o arquivo vai criptografado). Edite num aparelho de cada vez para não criar cópias em conflito.
- Implanta: KeePassXC · Celular · Syncthing

### 2.10 Ligar o KeePassXC-Browser para preencher senha e código no navegador

**Você** · 15 min

- **Fora do terminal:** Extensão de navegador e a opção de integração do KeePassXC só se ligam pelas janelas deles.
- [ ] **Pronto quando:** No login de teste, o navegador preenche a senha a partir do cofre
- No KeePassXC: Configurações > Integração com navegador, marque o seu navegador e instale a extensão KeePassXC-Browser.
- Implanta: KeePassXC · Navegador + Claude in Chrome

### 2.11 Pôr o cofre no backup e testar abrir a cópia

**Você** · 15 min

No **PowerShell** do Windows (linha `PS C:\>`):

```powershell
$d = 'E:'; New-Item -ItemType Directory -Force "$d\Cofre" | Out-Null; Copy-Item "$HOME\Documents\Cofre\Cofre.kdbx" "$d\Cofre\"; & "$env:ProgramFiles\KeePassXC\keepassxc-cli.exe" db-info "$d\Cofre\Cofre.kdbx"
```

- [ ] **Pronto quando:** Cópia do Cofre.kdbx no disco externo abre com a senha mestra; quando o restic entrar, a pasta Documentos\Cofre está no backup diário
- No WSL o caminho é /mnt/c/Users/SEU_USUARIO/Documents/Cofre: acrescente ao comando do restic no passo do backup.
- Implanta: KeePassXC · Disco externo · Backup 3-2-1

### 2.12 Trocar o resto aos poucos: 5 contas por semana, das mais usadas às menos usadas

**Você** · 20 min

- **Fora do terminal:** Mesmo caso das críticas: a troca é no site de cada serviço.
- [ ] **Pronto quando:** Relatório de integridade do KeePassXC sem senha fraca, repetida ou vazada
- Implanta: KeePassXC

### 2.13 Marcar a revisão a cada 3 meses: relatório do cofre, aparelhos conectados no Google e códigos de backup

**Você** · 10 min

- **Fora do terminal:** Lembrete no calendário: peça ao Claude que crie pelo conector do Google Agenda.
- [ ] **Pronto quando:** Lembrete trimestral no calendário
- Implanta: KeePassXC

### 2.14 Usar o KeePassXC como agente SSH

**Você** · 15 min

- **Fora do terminal:** Configurações > Agente SSH, na tela do KeePassXC.
- [ ] **Pronto quando:** Chave SSH carregada pelo cofre
- Implanta: KeePassXC

### 2.15 Ativar o auto-preenchimento (Auto-Type) com atalho

**Você** · 10 min

- **Fora do terminal:** Configurações > Auto-Type, na tela do KeePassXC.
- [ ] **Pronto quando:** Login preenchido pelo atalho
- Implanta: KeePassXC

### 2.16 Avaliar arquivo-chave ou chave física como segundo fator do cofre

**Você** · 15 min

- **Fora do terminal:** Decisão sua. Perder a chave = perder o cofre: guarde cópia.
- [ ] **Pronto quando:** Decisão registrada (e cópia do arquivo-chave no pendrive, se usar)
- Implanta: KeePassXC

<a id="f3"></a>

## 3 · Windows

Os programas do setup instalados, o navegador com o Claude e o WSL2 pronto.

**Quando:** Semana 1 · out/2026

### 3.1 Ver o que o instalador faria

**Script** · 5 min

No **PowerShell** do Windows (linha `PS C:\>`):

```powershell
powershell -ExecutionPolicy Bypass -File $HOME\dev-setup\scripts\windows\instalar.ps1
```

- [ ] **Pronto quando:** Lista de INSTALARIA conferida
- Implanta: Instaladores (PowerShell e bash)

### 3.2 Instalar programas, WSL2 com Ubuntu (instala o 24.04 só se não houver nenhum) e .wslconfig (PowerShell como Administrador)

**Script** · 1 h 00 min

No **PowerShell** do Windows (linha `PS C:\>`):

```powershell
powershell -ExecutionPolicy Bypass -File $HOME\dev-setup\scripts\windows\instalar.ps1 -Aplicar
```

- [ ] **Pronto quando:** Termina com 'Pronto' e sem ERRO; reinicie o Windows
- Implanta: Terminal · PowerShell · winget · VS Code · 7-Zip · PowerToys · SumatraPDF · ShareX · LibreOffice · Firefox (2º navegador) · Obsidian + Git · DBeaver · Bruno · Excalidraw / draw.io · VirtualBox · Arduino IDE 2 · .wslconfig + localhost · OBS Studio · Audacity · Canva · Krita · Inkscape · Wireshark · Syncthing · Anki

### 3.3 Ligar a criptografia do dispositivo e guardar a chave de recuperação no KeePassXC

**Você** · 15 min

No **PowerShell** do Windows (linha `PS C:\>`):

```powershell
manage-bde -status C:; manage-bde -protectors -get C:
```

- [ ] **Pronto quando:** verificar.ps1 como Administrador mostra criptografia OK
- No Windows 11 Home a opção se chama Criptografia do dispositivo e depende do hardware. Se não aparecer, anote e siga. O segundo comando mostra a chave de recuperação (48 números): copie para uma entrada do KeePassXC. Se aparecer 'Proteção Desativada' com 'Nenhum protetor localizado', o disco já está criptografado mas sem chave: ligue em Configurações > Privacidade e segurança > Criptografia do dispositivo (pede a conta Microsoft, que guarda uma cópia da chave) e rode o comando de novo para copiar a chave para o KeePassXC.
- Implanta: BitLocker · TPM + Secure Boot

### 3.4 Conferir Defender e Firewall ligados

**Você** · 10 min

No **PowerShell** do Windows (linha `PS C:\>`):

```powershell
Get-MpComputerStatus | Select-Object AMServiceEnabled,AntivirusEnabled,RealTimeProtectionEnabled,AntivirusSignatureLastUpdated; Get-NetFirewallProfile | Select-Object Name,Enabled
```

- [ ] **Pronto quando:** verificar.ps1 como Administrador mostra Defender OK
- Implanta: Defender + Firewall

### 3.5 Instalar as extensões do VS Code (WSL, Claude Code, .NET, LaTeX, revisão em português)

**Script** · 10 min

No **PowerShell** do Windows (linha `PS C:\>`):

```powershell
powershell -ExecutionPolicy Bypass -File $HOME\dev-setup\scripts\windows\extensoes-vscode.ps1 -Aplicar
```

- [ ] **Pronto quando:** Termina com 'Pronto'
- Implanta: VS Code

### 3.6 Instalar o Claude in Chrome e entrar com a sua conta

**Você** · 15 min

- **Fora do terminal:** Extensão do Chrome se instala pela Chrome Web Store, no navegador.
- [ ] **Pronto quando:** O painel do Claude abre numa aba do navegador
- O uso do computador pelo Claude fica no app do Claude para desktop; ligue só quando for usar e acompanhe o que ele faz.
- Implanta: Navegador + Claude in Chrome · Claude in Chrome + uso do computador

### 3.7 Instalar o DaVinci Resolve pelo site da Blackmagic (opcional)

**Você** · 20 min

- **Fora do terminal:** A Blackmagic só libera o instalador depois de um cadastro no site.
- [ ] **Pronto quando:** Abre e reconhece a GPU
- Implanta: DaVinci Resolve ou Kdenlive

### 3.8 Decidir se Unity e Cocos ficam para as aulas de robótica

**Você** · 10 min

No **PowerShell** do Windows (linha `PS C:\>`):

```powershell
winget install --id Unity.UnityHub -e
```

- [ ] **Pronto quando:** Decisão anotada; se ficam, Unity Hub instalado
- Implanta: Unity · Cocos

### 3.9 Conferir o Windows

**Script** · 5 min

No **PowerShell** do Windows (linha `PS C:\>`):

```powershell
powershell -ExecutionPolicy Bypass -File $HOME\dev-setup\scripts\windows\verificar.ps1
```

- [ ] **Pronto quando:** verificar.ps1 termina com 'Windows pronto'
- Implanta: Verificadores

<a id="f4"></a>

## 4 · Linux (WSL2)

O Ubuntu com tudo o que o código precisa, commits assinados e o ambiente versionado.

**Quando:** Semana 2 · nov/2026

### 4.1 Abrir o Ubuntu do WSL e criar (ou confirmar) seu usuário Linux

**Você** · 10 min

No **PowerShell** do Windows (linha `PS C:\>`):

```powershell
wsl -l -v; wsl -d Ubuntu
```

- [ ] **Pronto quando:** Prompt do Ubuntu aberto
- Serve Ubuntu 24.04 ou mais novo (26.04 também). Se a sua distro tiver outro nome na lista, troque Ubuntu pelo nome que aparece. Se já existe usuário, o terminal abre direto nele.
- Implanta: Ubuntu (WSL2)

### 4.2 Ligar o Docker Desktop dentro do Ubuntu (integração com o WSL)

**Você** · 5 min

No **PowerShell** do Windows (linha `PS C:\>`):

```powershell
$f="$env:APPDATA\Docker\settings-store.json"; if (-not (Test-Path $f)) { Write-Host "Nao achei $f : abra o Docker Desktop uma vez e rode de novo" } else { Copy-Item $f "$f.bak" -Force; $j=Get-Content $f -Raw | ConvertFrom-Json; $j | Add-Member -Force NoteProperty EnableIntegrationWithDefaultWslDistro $true; $j | Add-Member -Force NoteProperty IntegratedWslDistros @('Ubuntu'); [IO.File]::WriteAllText($f, ($j | ConvertTo-Json -Depth 10)); Get-Process 'Docker Desktop' -ErrorAction SilentlyContinue | Stop-Process -Force; Start-Sleep 3; Start-Process "$env:ProgramFiles\Docker\Docker\Docker Desktop.exe"; $i=0; do { Start-Sleep 5; $i++; docker info *> $null } until ($LASTEXITCODE -eq 0 -or $i -ge 36); if ($LASTEXITCODE -eq 0) { Write-Host "Docker pronto com o Ubuntu ligado" } else { Write-Host "Docker nao respondeu em 3 min: veja a janela dele" } }
```

- [ ] **Pronto quando:** 'docker run hello-world' funciona dentro do Ubuntu
- Rode no PowerShell (PS C:\>), não dentro do Ubuntu. Ele guarda uma cópia da configuração (settings-store.json.bak), liga a integração com o Ubuntu e reinicia o Docker Desktop. Depois, no Ubuntu: docker run --rm hello-world. Se o nome da sua distro não for Ubuntu (wsl -l -v), troque no comando.
- Implanta: Docker + Compose

### 4.3 Copiar este repositório para ~/dev/dev-setup

**Você** · 5 min

No **Ubuntu** (linha `alanmateus@...$`):

```bash
mkdir -p ~/dev && cp -r /mnt/c/Users/SEU_USUARIO/dev-setup ~/dev/dev-setup
```

- [ ] **Pronto quando:** Pasta ~/dev/dev-setup com os arquivos
- Troque SEU_USUARIO pelo seu usuário do Windows. Depois que o repositório estiver no GitHub, use git clone.

### 4.4 Rodar o preparador do Linux

**Script** · 40 min

No **Ubuntu** (linha `alanmateus@...$`):

```bash
bash scripts/wsl/bootstrap.sh --nome "Alan Mateus" --email SEU_EMAIL --com-whisper
```

- [ ] **Pronto quando:** Termina com 'Pronto' e sem ERRO
- Implanta: .NET 10 · Node · Python · TeX Live · gitleaks · Trivy · Git + SSH + gh · nmap · dig · curl · Whisper (local) · Pranchas TikZ e SVG · CircuiTikZ · Instaladores (PowerShell e bash)

### 4.5 Reiniciar o WSL para o systemd valer (PowerShell)

**Você** · 2 min

No **PowerShell** do Windows (linha `PS C:\>`):

```powershell
wsl --shutdown
```

- [ ] **Pronto quando:** Ubuntu reabre normalmente
- Implanta: Ubuntu (WSL2)

### 4.6 Entrar no GitHub pelo terminal e cadastrar a chave SSH para login e assinatura

**Você** · 10 min

No **Ubuntu** (linha `alanmateus@...$`):

```bash
gh auth login && gh ssh-key add ~/.ssh/id_ed25519.pub --type authentication && gh ssh-key add ~/.ssh/id_ed25519.pub --type signing
```

- [ ] **Pronto quando:** 'gh auth status' mostra sua conta
- Implanta: Git + SSH + gh · Commits assinados (chave SSH)

### 4.7 Guardar os dotfiles (.bashrc, .gitconfig, .tmux.conf) num repositório privado

**Claude com você** · 30 min

No **Ubuntu** (linha `alanmateus@...$`):

```bash
cd ~ && gh repo create dotfiles --private --clone && cd dotfiles && for f in .bashrc .gitconfig .tmux.conf; do [ -f ~/$f ] && cp ~/$f .; done && git add -A && git commit -m 'dotfiles iniciais' && git push -u origin HEAD
```

- [ ] **Pronto quando:** Repositório dotfiles privado; clonar e rodar o script de links recria o terminal
- Nunca coloque chaves ou tokens nos dotfiles. O gitleaks do CI confere a cada envio.
- Implanta: dotfiles

### 4.8 Criar o cofre do Obsidian em ~/dev/notas e ligar o plugin Obsidian Git

**Você** · 20 min

No **Ubuntu** (linha `alanmateus@...$`):

```bash
bash scripts/wsl/vault.sh
```

- [ ] **Pronto quando:** Cofre aberto no Obsidian com as pastas e modelos; notas vão sozinhas para um repositório privado a cada 10 minutos
- No Obsidian do Windows, abra a pasta \\wsl.localhost\Ubuntu (ou o nome do seu Ubuntu)\home\SEU_USUARIO\dev\notas.
- Implanta: Obsidian + Git

### 4.9 Ligar o Syncthing entre o celular e o notebook para as gravações (opcional)

**Você** · 15 min

- **Fora do terminal:** Parear com o celular é lendo o QR code no app do Syncthing.
- [ ] **Pronto quando:** Vídeo gravado no celular aparece na pasta Gravacoes do Windows
- Para o pipeline pegar, mova o vídeo para ~/AMtech/entrada/aulas. Vídeo com aluno menor de idade só com autorização do responsável.
- Implanta: Syncthing · Celular

### 4.10 Conferir o Linux

**Script** · 5 min

No **Ubuntu** (linha `alanmateus@...$`):

```bash
bash scripts/wsl/verificar.sh
```

- [ ] **Pronto quando:** verificar.sh termina com 'WSL pronto'
- Implanta: Verificadores

<a id="f5"></a>

## 5 · GitHub e CI

O repositório no ar, com testes automáticos verdes a cada envio e o trabalho organizado.

**Quando:** Semana 2 · nov/2026

### 5.1 Criar o repositório privado e enviar o setup

**Script** · 5 min

No **Ubuntu** (linha `alanmateus@...$`):

```bash
cd ~/dev/dev-setup && git init -q 2>/dev/null; git add -A && git commit -qm 'chore: setup inicial' ; gh repo create AlanMateus17/dev-setup --private --source . --push
```

- [ ] **Pronto quando:** Repositório AlanMateus17/dev-setup privado com o código
- Se você usar o zip, o histórico de commits não vem junto; o repositório começa com um commit novo, já assinado.
- Implanta: GitHub

### 5.2 Conferir o CI no GitHub

**Script** · 5 min

No **Ubuntu** (linha `alanmateus@...$`):

```bash
gh run list --limit 1
```

- [ ] **Pronto quando:** Última execução do workflow 'docs' com sucesso
- Implanta: GitHub Actions

### 5.3 Ligar Dependabot e CodeQL e proteger o branch main

**Claude com você** · 15 min

No **Ubuntu** (linha `alanmateus@...$`):

```bash
cd ~/dev/dev-setup && gh api -X PUT 'repos/{owner}/{repo}/vulnerability-alerts' && gh api -X PUT 'repos/{owner}/{repo}/automated-security-fixes' && gh api -X PATCH 'repos/{owner}/{repo}/code-scanning/default-setup' -f state=configured
```

- [ ] **Pronto quando:** Dependabot e CodeQL ativos; push direto no main exige CI verde
- Peça ao Claude Code no repositório; ele faz pelo gh api com a sua aprovação. Proteger o branch main e o CodeQL em repositório privado exigem GitHub Pro; o GitHub Education de professor costuma liberar. Sem ele, o comando liga o Dependabot e o CodeQL responde que não está disponível.
- Implanta: Dependabot + CodeQL

### 5.4 Criar a organização grupo-amtech-digital no GitHub

**Você** · 10 min

- **Fora do terminal:** O GitHub só deixa criar organização pelo site.
- [ ] **Pronto quando:** Organização criada, com 2FA obrigatório para membros
- Implanta: GitHub

### 5.5 Criar o GitHub Project do setup e a pasta de decisões (ADRs)

**Claude com você** · 20 min

No **Ubuntu** (linha `alanmateus@...$`):

```bash
gh auth refresh -s project && gh project create --owner @me --title 'Setup AMtech' && mkdir -p ~/dev/dev-setup/docs/adr
```

- [ ] **Pronto quando:** Quadro com as fases deste roteiro e docs/adr/0001 registrado
- O MkDocs publica a documentação no GitHub Pages quando você quiser tornar algo público; o setup continua privado.
- Implanta: Projects · ADRs · MkDocs

<a id="f6"></a>

## 6 · Agentes de IA

O Claude Code trabalhando dentro da sandbox, com as suas regras, ferramentas e memória.

**Quando:** Semana 2 · nov/2026

### 6.1 Entrar no Claude Code

**Você** · 5 min

No **Ubuntu** (linha `alanmateus@...$`):

```bash
claude
```

- [ ] **Pronto quando:** 'claude doctor' sem erros
- Implanta: Claude Code

### 6.2 Testar a sandbox

**Script** · 2 min

No **Ubuntu** (linha `alanmateus@...$`):

```bash
cd ~/dev/dev-setup && ai-jail --dry-run claude
```

- [ ] **Pronto quando:** Mostra o que seria montado, sem erro
- Implanta: ai-jail

### 6.3 Criar o CLAUDE.md padrão do Aura e os comandos /commit e /novo-sistema-aura

**Claude com você** · 30 min

No **Ubuntu** (linha `alanmateus@...$`):

```bash
cd ~/dev/dev-setup && claude "Passo claude-md do roteiro: Criar o CLAUDE.md padrão do Aura e os comandos /commit e /novo-sistema-aura"
```

- [ ] **Pronto quando:** Arquivos no repositório de cada sistema
- Peça ao Claude Code: o conteúdo está em docs/pecas-autorais.md.
- Implanta: CLAUDE.md, agentes e skills (seus)

### 6.4 Baixar um modelo local de 3 a 4B no Ollama

**Você** · 15 min

No **Ubuntu** (linha `alanmateus@...$`):

```bash
ollama pull llama3.2:3b && ollama run llama3.2:3b 'Responda em uma frase: o que é uma variável?'
```

- [ ] **Pronto quando:** verificar.ps1 mostra Ollama OK com 1 modelo
- Implanta: Ollama · Modelos locais: Qwen · Gemma · Llama

### 6.5 Ligar os servidores MCP do Claude Code: GitHub e o banco de métricas só para leitura

**Claude com você** · 20 min

No **Ubuntu** (linha `alanmateus@...$`):

```bash
cd ~/dev/dev-setup && claude "Passo mcp do roteiro: Ligar os servidores MCP do Claude Code: GitHub e o banco de métricas só para leitura"
```

- [ ] **Pronto quando:** 'claude mcp list' mostra os servidores conectados
- O banco entra com o usuário leitor do Grafana, que não apaga nada. Tokens ficam no KeePassXC e em variáveis de ambiente, nunca no repositório.
- Implanta: Servidores MCP

### 6.6 Ligar o ai-memory para o agente lembrar das decisões entre sessões

**Claude com você** · 15 min

No **Ubuntu** (linha `alanmateus@...$`):

```bash
cd ~/dev/dev-setup && claude "Passo ai-memory do roteiro: Ligar o ai-memory para o agente lembrar das decisões entre sessões"
```

- [ ] **Pronto quando:** Uma decisão anotada numa sessão aparece na seguinte
- Implanta: ai-memory

### 6.7 Montar a base de conhecimento das suas notas (Ollama + pgvector, ou NotebookLM e Projects)

**Claude com você** · 1 h 00 min

No **Ubuntu** (linha `alanmateus@...$`):

```bash
cd ~/dev/dev-setup && claude "Passo rag do roteiro: Montar a base de conhecimento das suas notas (Ollama + pgvector, ou NotebookLM e Projects)"
```

- [ ] **Pronto quando:** Pergunta sobre uma anotação sua volta com a resposta e a nota de origem
- Entram só as suas anotações, resumos com suas palavras, exercícios resolvidos e aulas que você gravou. Aulas da Udemy, DIO, Alura e afins não entram.
- Implanta: Base de conhecimento (RAG) das suas notas · NotebookLM

<a id="f7"></a>

## 7 · Backup e segurança

Perder o notebook não faz você perder nada.

**Quando:** Semana 3 · nov/2026

### 7.1 Criar o repositório restic no disco externo e o primeiro backup

**Script** · 30 min

No **Ubuntu** (linha `alanmateus@...$`):

```bash
restic -r /mnt/d/backup-restic init && restic -r /mnt/d/backup-restic backup ~/dev ~/AMtech ~/.config/amtech
```

- [ ] **Pronto quando:** 'restic snapshots' lista o backup
- Troque /mnt/d pela letra do seu disco externo (D: vira /mnt/d). Guarde a senha do repositório no KeePassXC.
- Implanta: restic (backup criptografado) · Backup 3-2-1 · Disco externo

### 7.2 Criar a cópia fora de casa (Backblaze B2 ou o armazenamento do seu plano Google)

**Você** · 40 min

- **Fora do terminal:** Criar a conta e a chave da Backblaze é no site; depois o restic usa a chave pelo terminal.
- [ ] **Pronto quando:** Segundo repositório restic com snapshot
- Implanta: Backblaze B2 (backup) · Backup 3-2-1

### 7.3 Testar a restauração de uma pasta

**Você** · 15 min

No **Ubuntu** (linha `alanmateus@...$`):

```bash
restic -r /mnt/d/backup-restic restore latest --target /tmp/teste-restauracao --include "$HOME/dev/dev-setup/README.md" && find /tmp/teste-restauracao -name README.md
```

- [ ] **Pronto quando:** Arquivo restaurado abre normalmente
- Implanta: Backup 3-2-1

### 7.4 Agendar o backup diário

**Claude com você** · 20 min

No **Ubuntu** (linha `alanmateus@...$`):

```bash
cd ~/dev/dev-setup && claude "Passo agendar-backup do roteiro: Agendar o backup diário"
```

- [ ] **Pronto quando:** Timer do backup ativo
- Implanta: restic (backup criptografado)

<a id="f8"></a>

## 8 · Acervo: tudo o que você já tem

Todos os seus documentos convertidos em conhecimento organizado no Obsidian, os pessoais separados e a lista do que dá para vender.

**Quando:** Semanas 3 e 4 · nov/2026

### 8.1 Baixar uma cópia completa do Google Drive pelo Google Takeout

**Você** · 45 min

- **Fora do terminal:** O Google Takeout só funciona pelo site.
- [ ] **Pronto quando:** Os zips do Takeout extraídos numa pasta só, por exemplo C:\Users\SEU_USUARIO\Downloads\Takeout
- Escolha só o Drive e, em formatos, Google Docs como .docx e Apresentações como .pptx. O Drive para computador mostra os Google Docs como atalhos sem conteúdo, por isso a primeira cópia vem do Takeout. Junte também os arquivos do notebook e dos pendrives na mesma pasta.
- Implanta: Google Drive (seus documentos)

### 8.2 Tirar da pasta os documentos pessoais (contracheques, extratos, IRPF, faturas)

**Você** · 30 min

- **Fora do terminal:** Decisão sua, arquivo por arquivo; o acervo já ignora os nomes típicos de documento pessoal.
- [ ] **Pronto quando:** Pasta Pessoal separada, guardada só no backup criptografado
- O acervo.py também barra esses arquivos pelo nome e pelo conteúdo e lista o que achou, mas tirar antes é mais seguro.
- Implanta: Backup 3-2-1

### 8.3 Ver o que o acervo faria, sem escrever nada

**Script** · 10 min

No **Ubuntu** (linha `alanmateus@...$`):

```bash
uv run tools/acervo/acervo.py --origem /mnt/c/Users/SEU_USUARIO/Downloads/Takeout --simular
```

- [ ] **Pronto quando:** Resumo com arquivos lidos, cópias repetidas, pessoais, de terceiros e da escola
- Implanta: Acervo (seus documentos)

### 8.4 Converter o acervo para o Obsidian e gerar o relatório de produtos

**Script** · 30 min

No **Ubuntu** (linha `alanmateus@...$`):

```bash
uv run tools/acervo/acervo.py --origem /mnt/c/Users/SEU_USUARIO/Downloads/Takeout
```

- [ ] **Pronto quando:** 30-Acervo no Obsidian com os documentos em Markdown e 40-Produtos/Produtos do acervo.md
- Roda no notebook; nada é enviado para fora. Pode rodar de novo quando chegarem documentos novos: o que já foi convertido não é refeito.
- Implanta: Acervo (seus documentos) · Obsidian + Git

### 8.5 Decidir cada alerta: dados de alunos, material de terceiros, material feito para a escola

**Você** · 1 h 30 min

- **Fora do terminal:** Decisão sua para cada alerta.
- [ ] **Pronto quando:** Cada alerta com decisão anotada: apagar dados, só estudo, reescrever ou vender
- Material de terceiros (livros, cursos) não vira produto nem treino de IA. Material feito para a escola: confira os direitos antes de vender; o caminho seguro é reescrever do zero, no seu tempo, sem a identidade da escola.
- Implanta: Acervo (seus documentos)

### 8.6 Indexar o acervo e as suas notas na base de conhecimento

**Claude com você** · 30 min

No **Ubuntu** (linha `alanmateus@...$`):

```bash
cd ~/dev/dev-setup && claude "Passo acervo-rag do roteiro: Indexar o acervo e as suas notas na base de conhecimento"
```

- [ ] **Pronto quando:** Pergunta sobre um documento antigo volta com a resposta e o arquivo de origem
- Implanta: Base de conhecimento (RAG) das suas notas

### 8.7 Escolher no relatório os 3 primeiros produtos e levar para o portfólio de ofertas

**Claude com você** · 1 h 00 min

No **Ubuntu** (linha `alanmateus@...$`):

```bash
cd ~/dev/dev-setup && claude "Passo acervo-produtos do roteiro: Escolher no relatório os 3 primeiros produtos e levar para o portfólio de ofertas"
```

- [ ] **Pronto quando:** 3 ofertas novas em data/portfolio.json com estágio, preço alvo e próximo passo
- Implanta: Portfólio de ofertas · Esteira de ofertas

<a id="f9"></a>

## 9 · Claude e assistentes

Cada recurso do Claude e cada assistente com um papel definido no setup.

**Quando:** Semana 4 · nov/2026

### 9.1 Organizar o app do Claude: um Project por frente, memória, artefatos, pesquisa e tarefas agendadas

**Você** · 30 min

- **Fora do terminal:** Projects, memória e tarefas agendadas ficam no app do Claude.
- [ ] **Pronto quando:** Projects AMtech, Instituto, Editora e Setup criados; uma tarefa agendada de teste rodou
- Implanta: Claude (app) · Projects + memória · Artifacts (Docs, Slides, Sheets…) · Pesquisa aprofundada · Tarefas agendadas

### 9.2 Conferir os conectores: Google, Canva, Figma, MailerLite, Vercel, Microsoft Learn, Upwork, Lovable, Supabase, Cloudflare e vidIQ

**Você** · 30 min

- **Fora do terminal:** Conectores se ligam e desligam nas configurações do app do Claude.
- [ ] **Pronto quando:** Cada conector usado responde a um pedido simples; o da Cloudflare trocado pelo Cloudflare API MCP
- Notion, monday, GitBook e Stripe ficam de fora: repetem Obsidian, GitHub Projects, MkDocs e as plataformas de curso. Desconecte para não confundir.
- Implanta: Conector Google (Gmail, Drive…) · Conectores Canva + Figma · Conector MailerLite · Vercel · AWS · Microsoft Learn · Conector Upwork · Lovable + Supabase · Conector Cloudflare · Conector vidIQ · Notion · monday · GitBook · Stripe

### 9.3 Ligar os plugins: small-business, marketing, engineering, design, finance, Hostinger, Adobe e Cloudinary

**Você** · 15 min

- **Fora do terminal:** Plugins se ligam no app do Claude.
- [ ] **Pronto quando:** Os comandos dos plugins aparecem no Claude
- Implanta: Plugins: small- business + marketing · Plugins: engineering + design · Plugins: finance + Fiscal.ai · Plugins: Hostinger · Adobe · Cloudinary

### 9.4 Entrar nos outros assistentes (ChatGPT, Gemini, Grok, DeepSeek, Perplexity, Codex, agentes do Google) e anotar quais são pagos

**Você** · 30 min

- **Fora do terminal:** Cada assistente tem o próprio site ou app.
- [ ] **Pronto quando:** Acessos no KeePassXC e assinaturas pagas lançadas na tabela ferramentas do banco de métricas
- Implanta: ChatGPT · Gemini (pago) · Grok · DeepSeek · Perplexity · Codex (OpenAI) · Agentes de código do Google

<a id="f10"></a>

## 10 · Automação e medição

n8n, banco de métricas, Grafana e Uptime Kuma rodando.

**Quando:** Semana 4 · nov/2026

### 10.1 Gerar as senhas da stack e guardar no KeePassXC

**Script** · 5 min

No **Ubuntu** (linha `alanmateus@...$`):

```bash
cd infra/automacao && bash gerar-senhas.sh
```

- [ ] **Pronto quando:** .env criado com permissão 600
- Implanta: n8n

### 10.2 Subir a stack

**Script** · 10 min

No **Ubuntu** (linha `alanmateus@...$`):

```bash
cd infra/automacao && docker compose up -d
```

- [ ] **Pronto quando:** 'docker compose ps' com todos healthy
- Implanta: Docker + Compose · n8n · Banco de métricas (PostgreSQL) · PostgreSQL

### 10.3 Conferir os serviços

**Script** · 2 min

No **Ubuntu** (linha `alanmateus@...$`):

```bash
bash scripts/wsl/verificar.sh --servicos
```

- [ ] **Pronto quando:** verificar.sh --servicos sem FALTA na área servico
- Implanta: Verificadores

### 10.4 Entrar no Grafana (admin) e ver a fonte 'Métricas AMtech' conectada

**Você** · 10 min

No **navegador**:

```text
http://localhost:3001
```

- [ ] **Pronto quando:** Explore > Métricas AMtech > 'select 1' responde
- Implanta: Grafana

### 10.5 Criar a conta do n8n

**Você** · 5 min

No **navegador**:

```text
http://localhost:5678
```

- [ ] **Pronto quando:** Painel do n8n abre
- Implanta: n8n

### 10.6 Cadastrar no Uptime Kuma os monitores do n8n, Grafana e dos sites

**Você** · 15 min

No **navegador**:

```text
http://localhost:3002
```

- [ ] **Pronto quando:** Monitores verdes; aviso no Telegram configurado
- Implanta: Uptime Kuma

### 10.7 Pôr o banco de métricas e os fluxos do n8n no backup diário

**Claude com você** · 45 min

No **Ubuntu** (linha `alanmateus@...$`):

```bash
cd ~/dev/dev-setup && claude "Passo backup-banco do roteiro: Pôr o banco de métricas e os fluxos do n8n no backup diário"
```

- [ ] **Pronto quando:** Dump diário do banco e export dos fluxos em ~/AMtech/backup-dados, copiados pelo restic; uma restauração de teste funcionou
- Os dados ficam em volumes do Docker, fora das pastas que o restic copia. Sem este passo, perder o notebook leva junto o histórico de vendas.
- Implanta: Banco de métricas (PostgreSQL) · n8n · restic (backup criptografado)

### 10.8 Decidir: Postiz agora ou agendador nativo das redes

**Você** · 10 min

- **Fora do terminal:** Decisão sua.
- [ ] **Pronto quando:** Decisão anotada em infra/postiz/README.md
- Implanta: Postiz (agendador)

<a id="f-arsenal"></a>

## 11 · Arsenal de rendas: regras e as 3 de agora

Só 3 rendas ativas por vez, hora mínima de R$ 45, teto de 7 horas extras por semana e o resto em fila com portão.

**Quando:** Semana 4 · nov/2026

### 11.1 Confirmar a hora mínima (R$ 45) e o teto de 7 horas extras por semana

**Você** · 15 min

- **Fora do terminal:** Decisão sua. Se mudar o valor, peça ao Claude para trocar em data/portfolio.json.
- [ ] **Pronto quando:** Valores confirmados em data/portfolio.json (regras)

### 11.2 Pôr na Rotina o bloco de negócio (quinta 13h–16h30) e o de produção (sábado 9h30–12h30)

**Você** · 10 min

- **Fora do terminal:** A Rotina fica no Caixa da Casa (artefato), fora do terminal.
- [ ] **Pronto quando:** Os dois blocos aparecem na Rotina do Caixa da Casa

### 11.3 Cadastro e teste de entrada numa plataforma de avaliação de IA

**Você** · 1 h 30 min

- **Fora do terminal:** Cadastro no navegador. Nunca pague para entrar e nunca passe senha a ninguém.
- [ ] **Pronto quando:** Teste de entrada feito
- **Oferta:** Avaliação de respostas de IA (DataAnnotation, Outlier)

### 11.4 Oferecer site com manutenção mensal a 5 comércios

**Você** · 2 h 00 min

- **Fora do terminal:** Venda é conversa com o cliente; o setup prepara a proposta e o contrato.
- [ ] **Pronto quando:** 5 ofertas feitas e respostas anotadas no CRM
- **Oferta:** Sites e lojas para pequenas empresas

### 11.5 Criar as buscas salvas com alerta e ligar o radar de revenda

**Claude com você** · 2 h 00 min

No **Ubuntu** (linha `alanmateus@...$`):

```bash
cd ~/dev/dev-setup && claude "Passo ar-radar do roteiro: Criar as buscas salvas com alerta e ligar o radar de revenda"
```

- [ ] **Pronto quando:** Radar avisa no Telegram só itens acima da hora mínima, com checklist antigolpe
- Lê só a pasta de alertas do Gmail. Não raspa sites que proíbem coleta, não compra e não fala com vendedor.
- **Oferta:** Notebooks e PCs: comprar, consertar e revender · Celulares: comprar, consertar e revender · Livros técnicos e didáticos usados · Peças de máquinas sucateadas (RAM, SSD, placas)
- Implanta: Radar de revenda

### 11.6 Retorno por hora de cada marca no painel

**Claude com você** · 1 h 30 min

No **Ubuntu** (linha `alanmateus@...$`):

```bash
cd ~/dev/dev-setup && claude "Passo ar-retorno do roteiro: Retorno por hora de cada marca no painel"
```

- [ ] **Pronto quando:** O painel mostra R$ por hora sua de cada oferta ativa e marca as que ficaram abaixo da hora mínima
- Implanta: Painel de lucro (Grafana)

### 11.7 Conferir a fase da cascata antes de qualquer investimento

**Você** · 10 min

- **Fora do terminal:** Decisão financeira é sua; o Caixa da Casa mostra a fase.
- [ ] **Pronto quando:** Fase atual anotada no Caixa da Casa
- **Oferta:** Dividendos, FIIs e renda fixa (cascata e ARCA)

### 11.8 Revisar os descartes uma vez por trimestre

**Você** · 15 min

- **Fora do terminal:** Revisão de decisão, fora do terminal.
- [ ] **Pronto quando:** Revisão anotada; nenhum descarte volta sem motivo novo
- **Oferta:** Modelos 3D e projetos Arduino para download · Sites de nicho com anúncios · Fotos e vídeos em bancos de imagens · Jogo educativo de lógica (itch.io e Steam) · Testes de software pagos por bug · Aplicador e fiscal de provas · Edição de vídeo para lojas e criadores · Fotos de produto para lojas do Mercado Livre

<a id="f-automacoes"></a>

## 12 · Automações do arsenal

Construir uma vez as automações que várias rendas usam, na ordem de quantas rendas cada uma destrava.

**Quando:** Nov/2026 em diante, uma por vez, na ordem de desbloqueio

### 12.1 Automação: Funil de e-mails e isca gratuita

**Claude com você** · 2 h 00 min

No **Ubuntu** (linha `alanmateus@...$`):

```bash
cd ~/dev/dev-setup && claude "Passo au-funil do roteiro: Automação: Funil de e-mails e isca gratuita"
```

- [ ] **Pronto quando:** Captura o contato com consentimento e manda a sequência de e-mails até a oferta.
- Construir quando a primeira oferta que usa esta automação for ativada; a ordem está na seção Automações do portfólio.
- Implanta: n8n

### 12.2 Automação: Estudo vira produto

**Claude com você** · 2 h 00 min

No **Ubuntu** (linha `alanmateus@...$`):

```bash
cd ~/dev/dev-setup && claude "Passo au-esteira do roteiro: Automação: Estudo vira produto"
```

- [ ] **Pronto quando:** Das suas anotações de estudo, gera rascunho de aula, exercícios, cartões Anki e roteiro de vídeo para você revisar.
- Construir quando a primeira oferta que usa esta automação for ativada; a ordem está na seção Automações do portfólio.

### 12.3 Automação: Fábrica de aulas e documentos

**Claude com você** · 2 h 00 min

No **Ubuntu** (linha `alanmateus@...$`):

```bash
cd ~/dev/dev-setup && claude "Passo au-fabrica do roteiro: Automação: Fábrica de aulas e documentos"
```

- [ ] **Pronto quando:** Gera aulas e documentos da escola no modelo exigido, a partir das regras e das ementas. Dado de aluno nunca entra.
- Construir quando a primeira oferta que usa esta automação for ativada; a ordem está na seção Automações do portfólio.

### 12.4 Automação: Publicação agendada com aprovação

**Claude com você** · 2 h 00 min

No **Ubuntu** (linha `alanmateus@...$`):

```bash
cd ~/dev/dev-setup && claude "Passo au-publicacao do roteiro: Automação: Publicação agendada com aprovação"
```

- [ ] **Pronto quando:** Agenda posts, vídeos e artigos; nada vai ao ar sem o seu ok.
- Construir quando a primeira oferta que usa esta automação for ativada; a ordem está na seção Automações do portfólio.
- Implanta: n8n

### 12.5 Automação: Cortes, legendas e dublagem com a sua voz

**Claude com você** · 2 h 00 min

No **Ubuntu** (linha `alanmateus@...$`):

```bash
cd ~/dev/dev-setup && claude "Passo au-midia do roteiro: Automação: Cortes, legendas e dublagem com a sua voz"
```

- [ ] **Pronto quando:** Corta, legenda e dubla os vídeos. Só a sua voz, nunca a de alunos.
- Construir quando a primeira oferta que usa esta automação for ativada; a ordem está na seção Automações do portfólio.

### 12.6 Automação: Cobrança recorrente e controle de acesso

**Claude com você** · 2 h 00 min

No **Ubuntu** (linha `alanmateus@...$`):

```bash
cd ~/dev/dev-setup && claude "Passo au-recorrencia do roteiro: Automação: Cobrança recorrente e controle de acesso"
```

- [ ] **Pronto quando:** Cobra todo mês, corta o acesso de quem não paga e avisa antes.
- Construir quando a primeira oferta que usa esta automação for ativada; a ordem está na seção Automações do portfólio.
- Implanta: n8n

### 12.7 Automação: Atendimento de primeiro nível

**Claude com você** · 2 h 00 min

No **Ubuntu** (linha `alanmateus@...$`):

```bash
cd ~/dev/dev-setup && claude "Passo au-suporte do roteiro: Automação: Atendimento de primeiro nível"
```

- [ ] **Pronto quando:** Responde as dúvidas frequentes com base no seu material e passa para você o que não souber.
- Construir quando a primeira oferta que usa esta automação for ativada; a ordem está na seção Automações do portfólio.
- Implanta: n8n

### 12.8 Automação: Estoque, ordem de serviço e parceiros

**Claude com você** · 2 h 00 min

No **Ubuntu** (linha `alanmateus@...$`):

```bash
cd ~/dev/dev-setup && claude "Passo au-estoque do roteiro: Automação: Estoque, ordem de serviço e parceiros"
```

- [ ] **Pronto quando:** Controla compra, conserto, venda e o serviço feito por parceiros, com custo e lucro por item (Kaixara).
- Construir quando a primeira oferta que usa esta automação for ativada; a ordem está na seção Automações do portfólio.

### 12.9 Automação: Busca semanal de editais e oportunidades

**Claude com você** · 2 h 00 min

No **Ubuntu** (linha `alanmateus@...$`):

```bash
cd ~/dev/dev-setup && claude "Passo au-editais do roteiro: Automação: Busca semanal de editais e oportunidades"
```

- [ ] **Pronto quando:** Procura editais de conteudista, crédito, fomento e seleções e resume os que servem.
- Construir quando a primeira oferta que usa esta automação for ativada; a ordem está na seção Automações do portfólio.
- Implanta: n8n

### 12.10 Automação: Conciliação e relatório financeiro de clientes

**Claude com você** · 2 h 00 min

No **Ubuntu** (linha `alanmateus@...$`):

```bash
cd ~/dev/dev-setup && claude "Passo au-financeiro do roteiro: Automação: Conciliação e relatório financeiro de clientes"
```

- [ ] **Pronto quando:** Importa extratos, concilia e gera o relatório mensal de cada cliente.
- Construir quando a primeira oferta que usa esta automação for ativada; a ordem está na seção Automações do portfólio.
- Implanta: n8n

### 12.11 Automação: Registro de horas

**Claude com você** · 2 h 00 min

No **Ubuntu** (linha `alanmateus@...$`):

```bash
cd ~/dev/dev-setup && claude "Passo au-horas do roteiro: Automação: Registro de horas"
```

- [ ] **Pronto quando:** Mede as horas suas em cada renda (ActivityWatch) para calcular o retorno por hora.
- Construir quando a primeira oferta que usa esta automação for ativada; a ordem está na seção Automações do portfólio.
- Implanta: Painel de lucro (Grafana)

### 12.12 Automação: Comandos e aprovações pelo Telegram

**Claude com você** · 2 h 00 min

No **Ubuntu** (linha `alanmateus@...$`):

```bash
cd ~/dev/dev-setup && claude "Passo au-remoto do roteiro: Automação: Comandos e aprovações pelo Telegram"
```

- [ ] **Pronto quando:** Você aprova posts, vê vendas e recebe alertas pelo celular, só do seu número.
- Construir quando a primeira oferta que usa esta automação for ativada; a ordem está na seção Automações do portfólio.
- Implanta: n8n

<a id="f-sites"></a>

## 13 · Kit de sites com IA da Hostinger

Site de cliente em poucas horas, conferido por script e com mensalidade.

**Quando:** Semanas 4 e 5 · nov/2026

### 13.1 Ler o kit e definir os preços dos 3 pacotes

**Você** · 30 min

- **Fora do terminal:** Decisão sua; o kit está em docs/operacao/kit-sites.md.
- [ ] **Pronto quando:** Preços de criação e mensalidade definidos pela hora mínima
- **Oferta:** Sites e lojas para pequenas empresas
- Implanta: Kit de sites (Hostinger IA)

### 13.2 Montar o primeiro site com a ficha e o prompt do tipo de negócio

**Você** · 3 h 00 min

- **Fora do terminal:** A montagem é no editor da Hostinger, no navegador; o prompt pronto está no kit.
- [ ] **Pronto quando:** Site no ar no Website Builder ou no Horizons
- Implanta: Kit de sites (Hostinger IA)

### 13.3 Conferir o site e gerar o laudo antes de entregar

**Script** · 10 min

No **Ubuntu** (linha `alanmateus@...$`):

```bash
cd ~/dev/dev-setup && python3 tools/kitsites/conferir.py https://ENDERECO-DO-SITE --saida ~/laudo-site.md
```

- [ ] **Pronto quando:** Nota 80 ou mais no laudo
- Troque ENDERECO-DO-SITE. Com o Playwright instalado, acrescente --fotos para as fotos de celular e computador.
- Implanta: Kit de sites (Hostinger IA)

### 13.4 Levar o modelo de contrato a um advogado

**Você** · 1 h 00 min

- **Fora do terminal:** Revisão jurídica, fora do terminal. Modelo em docs/operacao/contrato-sites-modelo.md.
- [ ] **Pronto quando:** Contrato revisado e pronto para assinar
- Implanta: Kit de sites (Hostinger IA)

### 13.5 Avaliar os templates que você comprou (só se a licença permitir)

**Script** · 20 min

No **Ubuntu** (linha `alanmateus@...$`):

```bash
cd ~/dev/dev-setup && python3 tools/avaliador/avaliar.py ~/templates
```

- [ ] **Pronto quando:** avaliacao-templates.md com útil, adaptar ou descartar
- Ponha cada template (pasta ou .zip) em ~/templates. Guarde-os só num repositório PRIVADO: gh repo create templates-sites --private. O avaliador não roda código dos templates.
- Implanta: Avaliador de templates

<a id="f-escola"></a>

## 14 · Escola: Fábrica de aulas e documentos

Planejamentos e documentos da escola gerados no modelo exigido; você só revisa.

**Quando:** Semanas 5 e 6 · nov/2026

### 14.1 Criar o repositório privado 'aulas' com o esqueleto da Fábrica

**Script** · 10 min

No **Ubuntu** (linha `alanmateus@...$`):

```bash
cd ~/dev && gh repo create aulas --private --clone && cp -r ~/dev/dev-setup/infra/templates/repo-aulas/. aulas/ && cd aulas && git add -A && git commit -m 'Esqueleto da Fábrica de aulas' && git push -u origin HEAD
```

- [ ] **Pronto quando:** Repositório aulas no GitHub, privado, com regras, ementas e modelos
- Implanta: Fábrica de aulas

### 14.2 Colocar os modelos .docx da escola com os campos {{assim}}

**Você** · 40 min

- **Fora do terminal:** Os modelos são da escola; você abre no Word e escreve os campos entre chaves duplas.
- [ ] **Pronto quando:** Modelos em aulas/modelos-escola
- Implanta: Fábrica de aulas

### 14.3 Escrever a ementa da primeira disciplina

**Claude com você** · 1 h 00 min

No **Ubuntu** (linha `alanmateus@...$`):

```bash
cd ~/dev/aulas && claude "Passo fa-ementa do roteiro: escrever a ementa da primeira disciplina em ementas/, no formato de ementas/exemplo.toml, seguindo regras/alan.toml"
```

- [ ] **Pronto quando:** ementas/<disciplina>.toml com as semanas do bimestre
- Implanta: Fábrica de aulas

### 14.4 Gerar o primeiro planejamento semanal

**Script** · 10 min

No **Ubuntu** (linha `alanmateus@...$`):

```bash
cd ~/dev/aulas && python3 ~/dev/dev-setup/tools/fabrica/plano_semanal.py ementas/exemplo.toml regras/alan.toml 1 > /tmp/ctx.toml && python3 ~/dev/dev-setup/tools/fabrica/preencher.py modelos-escola/planejamento.docx /tmp/ctx.toml documentos/planejamento-s1.docx
```

- [ ] **Pronto quando:** Planejamento .docx preenchido em aulas/documentos
- Implanta: Fábrica de aulas

### 14.5 Cada correção sua vira uma regra em regras/alan.toml

**Você** · 10 min

- **Fora do terminal:** Hábito de revisão: a Fábrica aprende com o que você corrige.
- [ ] **Pronto quando:** Regras atualizadas a cada revisão
- Implanta: Fábrica de aulas

### 14.6 Conferir automaticamente cada documento antes de entregar à escola

**Script** · 2 min

No **Ubuntu** (linha `alanmateus@...$`):

```bash
python3 ~/dev/dev-setup/tools/documentos/verificar.py ~/dev/aulas/documentos/planejamento-s1.docx --perfil escola
```

- [ ] **Pronto quando:** Laudo sem itens a corrigir
- Implanta: Fábrica de aulas

### 14.7 Formatador ABNT: testar em 3 trabalhos e lançar a versão web

**Script** · 30 min

No **Ubuntu** (linha `alanmateus@...$`):

```bash
python3 ~/dev/dev-setup/tools/documentos/verificar.py ~/Downloads/trabalho.docx --corrigir
```

- [ ] **Pronto quando:** 3 trabalhos corrigidos e laudos aprovados
- Só formatação e conferência. A versão web (Horizons) usa a mesma verificação; nunca escrever o trabalho por ninguém.
- **Oferta:** Verificador e formatador ABNT automático (TCC, artigos, relatórios) · Conferência automática de documentos para coordenações e escolas
- Implanta: Fábrica de aulas

### 14.8 Revisão de fim de ano das turmas (material de revisão e avaliação, sem dados de aluno)

**Claude com você** · 2 h 00 min

No **Ubuntu** (linha `alanmateus@...$`):

```bash
cd ~/dev/aulas && claude "Passo fa-revisao-ano do roteiro: Montar a revisão de fim de ano de cada disciplina a partir das ementas, no modelo da escola, sem nenhum dado de aluno"
```

- [ ] **Pronto quando:** Material de revisão de cada disciplina pronto e conferido
- Implanta: Fábrica de aulas

### 14.9 Continuar as apostilas de Noções de Robótica depois da Aula 40, pela Fábrica

**Claude com você** · 3 h 00 min

No **Ubuntu** (linha `alanmateus@...$`):

```bash
cd ~/dev/ensino-ti && claude "Passo fa-robotica do roteiro: Continuar as apostilas de Noções de Robótica a partir da Aula 41, no mesmo padrão das anteriores, com código Arduino testado"
```

- [ ] **Pronto quando:** Apostilas do próximo bimestre no mesmo padrão visual, no repositório ensino-ti
- Implanta: Fábrica de aulas

<a id="f-financeiro"></a>

## 15 · Departamento financeiro pessoal

Extratos importados, mês resumido e a cascata aplicada pelas suas regras, com os dados só no seu PC.

**Quando:** Dez/2026

### 15.1 Criar a pasta ~/financas com os modelos

**Script** · 5 min

No **Ubuntu** (linha `alanmateus@...$`):

```bash
python3 ~/dev/dev-setup/tools/financeiro/financeiro.py iniciar
```

- [ ] **Pronto quando:** ~/financas com regras.toml, caixas.toml e politica-investimentos.md
- Implanta: Financeiro local

### 15.2 Preencher a sua Política de Investimentos e as metas da cascata

**Você** · 1 h 00 min

- **Fora do terminal:** Decisões suas; o arquivo fica em ~/financas, nunca no GitHub. Não é recomendação de investimento.
- [ ] **Pronto quando:** Política e caixas preenchidas por você
- Implanta: Financeiro local

### 15.3 Importar o extrato do mês (Nubank ou CSV)

**Script** · 5 min

No **Ubuntu** (linha `alanmateus@...$`):

```bash
python3 ~/dev/dev-setup/tools/financeiro/financeiro.py importar /mnt/c/Users/SEU_USUARIO/Downloads/extrato.csv
```

- [ ] **Pronto quando:** Lançamentos no banco local, sem duplicar
- Implanta: Financeiro local

### 15.4 Ver o resumo do mês e a cascata

**Script** · 2 min

No **Ubuntu** (linha `alanmateus@...$`):

```bash
python3 ~/dev/dev-setup/tools/financeiro/financeiro.py mes $(date +%Y-%m)
```

- [ ] **Pronto quando:** Resumo com sobra e destino de cada real
- Implanta: Financeiro local

<a id="f-investimentos"></a>

## 16 · Investimentos com as suas metodologias

Todas as metodologias ao mesmo tempo nas quatro classes do ARCA (ações, FIIs, renda fixa e internacional): consenso por ativo, ARCA em dois níveis e carteira por metodologia contra o índice. Não é recomendação: a decisão é sua.

**Quando:** Dez/2026

### 16.1 Copiar os modelos de investimento para ~/financas

**Script** · 5 min

No **Ubuntu** (linha `alanmateus@...$`):

```bash
python ~/dev/dev-setup/tools/investimentos/investimentos.py iniciar
```

- [ ] **Pronto quando:** investimentos.toml, os 4 indicadores_*.csv, carteira.csv e carteiras.csv em ~/financas
- Implanta: Caixa da Casa / AM Rendara

### 16.2 Preencher a política e o investimentos.toml (portão, ARCA por classe, metodologias por classe, limites, NTN-B do mês)

**Você** · 40 min

- **Fora do terminal:** Decisão sua; o modelo está em ~/financas/politica-investimentos.md (financeiro.py iniciar).
- [ ] **Pronto quando:** Política assinada por você e o portão refletindo o cartão e a reserva de hoje
- Implanta: Caixa da Casa / AM Rendara

### 16.3 Escrever as suas anotações das perguntas do método do Raul Sena no investimentos.toml

**Você** · 30 min

- **Fora do terminal:** O material do curso é pago: só as suas anotações vão para o arquivo, que fica fora do GitHub.
- [ ] **Pronto quando:** Lista [sena] preenchida com as suas palavras
- Implanta: Caixa da Casa / AM Rendara

### 16.4 Montar os 4 CSVs de indicadores (ações, FIIs, renda fixa, internacional) dos ativos que você acompanha

**Você** · 1 h 00 min

- **Fora do terminal:** Colunas de cada classe em docs/investimentos.md. Confira na fonte os números que decidem a compra (RI, CVM, relatório do fundo, Tesouro).
- [ ] **Pronto quando:** Planilha com os indicadores conferidos na fonte (RI da empresa ou CVM)
- Implanta: Caixa da Casa / AM Rendara

### 16.5 Rodar a avaliação das 4 classes e a divisão do aporte

**Script** · 15 min

No **Ubuntu** (linha `alanmateus@...$`):

```bash
cd ~/dev/dev-setup && for c in acoes fiis caixa internacional; do python tools/investimentos/investimentos.py avaliar $c ~/financas/indicadores_$c.csv; done && python tools/investimentos/investimentos.py aporte ~/financas/carteira.csv 800
```

- [ ] **Pronto quando:** Consenso de cada ativo e a divisão do aporte por classe e por metodologia
- Implanta: Caixa da Casa / AM Rendara

### 16.6 Criar uma carteira por metodologia e uma do índice em cada classe (reais ou simuladas)

**Você** · 30 min

- **Fora do terminal:** Simulada = anotada com preço e data, sem comprar.
- [ ] **Pronto quando:** carteiras.csv com classe, carteira, investido e valor atual, incluindo 'indice' em cada classe
- Implanta: Caixa da Casa / AM Rendara

### 16.7 Comparar as carteiras contra o índice todo mês

**Script** · 10 min

No **Ubuntu** (linha `alanmateus@...$`):

```bash
python ~/dev/dev-setup/tools/investimentos/investimentos.py comparar ~/financas/carteiras.csv
```

- [ ] **Pronto quando:** Resultado anotado no Caixa da Casa; metodologia que perder do índice por 3 anos é revista
- Implanta: Caixa da Casa / AM Rendara

### 16.8 Simular também as alocações gerais (Graham defensivo, Portfólio permanente, Bogle) contra o seu ARCA

**Você** · 20 min

- **Fora do terminal:** Todas as metodologias por classe já rodam juntas; aqui é a comparação no nível do ARCA.
- [ ] **Pronto quando:** Uma carteira simulada de cada estratégia em carteiras.csv (classe 'geral')
- Implanta: Caixa da Casa / AM Rendara

### 16.9 Marcar a prova CB da CNPI quando a verba de estudo permitir

**Você** · 20 min

- **Fora do terminal:** É ela que permite recomendar ativos no seu conteúdo de finanças. Ordem completa em docs/certificacoes.md.
- [ ] **Pronto quando:** Inscrição feita no site da Apimec

<a id="f-rotina"></a>

## 17 · Rotina automatizada

O setup se cuida sozinho e só te chama quando precisa.

**Quando:** Semana 4 · nov/2026

### 17.1 Instalar o ActivityWatch para medir as horas

**Script** · 10 min

No **PowerShell** do Windows (linha `PS C:\>`):

```powershell
winget install --id ActivityWatch.ActivityWatch -e
```

- [ ] **Pronto quando:** ActivityWatch rodando no Windows
- Implanta: ActivityWatch

### 17.2 Organizar a pasta Downloads (primeiro simula)

**Script** · 5 min

No **Ubuntu** (linha `alanmateus@...$`):

```bash
python3 ~/dev/dev-setup/tools/organizar/downloads.py
```

- [ ] **Pronto quando:** Downloads separado por tipo, nada apagado
- Confira a lista e rode de novo com --aplicar.
- Implanta: Organizadores

### 17.3 Ver o resumo da manhã

**Script** · 2 min

No **Ubuntu** (linha `alanmateus@...$`):

```bash
bash ~/dev/dev-setup/scripts/wsl/resumo-manha.sh
```

- [ ] **Pronto quando:** Resumo mostra disco, backup, repositórios e radar
- Implanta: Rotinas agendadas

### 17.4 Agendar o resumo diário e a manutenção semanal

**Script** · 2 min

No **Ubuntu** (linha `alanmateus@...$`):

```bash
bash ~/dev/dev-setup/scripts/wsl/agendar.sh --aplicar
```

- [ ] **Pronto quando:** crontab com as 2 linhas do setup
- Depois do bot do Telegram configurado. Para tirar: --remover.
- Implanta: Rotinas agendadas

### 17.5 Rodar a manutenção semanal (simula; depois --aplicar)

**Script** · 15 min

No **Ubuntu** (linha `alanmateus@...$`):

```bash
bash ~/dev/dev-setup/scripts/wsl/manutencao-semanal.sh
```

- [ ] **Pronto quando:** Manutenção sem erros
- Implanta: Rotinas agendadas

<a id="f-remoto"></a>

## 18 · Comandos remotos pelo Telegram

Status, resumo e radar no celular, respondendo só ao seu chat.

**Quando:** Semana 5 · nov/2026

### 18.1 Criar o bot no @BotFather e guardar o token no KeePassXC

**Você** · 10 min

- **Fora do terminal:** Feito no app do Telegram; o token é segredo e vai para o KeePassXC.
- [ ] **Pronto quando:** Token guardado no cofre
- Implanta: Telegram (avisos) · KeePassXC

### 18.2 Criar o arquivo de configuração do bot (permissão 600)

**Você** · 5 min

No **Ubuntu** (linha `alanmateus@...$`):

```bash
mkdir -p ~/.config/amtech && touch ~/.config/amtech/telegram.env && chmod 600 ~/.config/amtech/telegram.env && nano ~/.config/amtech/telegram.env
```

- [ ] **Pronto quando:** ~/.config/amtech/telegram.env com o token
- Escreva TELEGRAM_TOKEN=... e salve (Ctrl+O, Enter, Ctrl+X).
- Implanta: Telegram (avisos)

### 18.3 Descobrir o seu chat id e completar a configuração

**Script** · 5 min

No **Ubuntu** (linha `alanmateus@...$`):

```bash
python3 ~/dev/dev-setup/tools/remoto/bot.py
```

- [ ] **Pronto quando:** TELEGRAM_CHAT_ID preenchido
- Mande /start para o bot no celular; ele responde com o seu id. Ctrl+C no terminal para parar, ponha TELEGRAM_CHAT_ID=... no arquivo.
- Implanta: Telegram (avisos)

### 18.4 Deixar o bot rodando como serviço

**Script** · 5 min

No **Ubuntu** (linha `alanmateus@...$`):

```bash
mkdir -p ~/.config/systemd/user && printf '[Unit]\nDescription=Bot AMtech\n[Service]\nExecStart=/usr/bin/python3 %%h/dev/dev-setup/tools/remoto/bot.py\nRestart=always\n[Install]\nWantedBy=default.target\n' > ~/.config/systemd/user/amtech-bot.service && systemctl --user daemon-reload && systemctl --user enable --now amtech-bot
```

- [ ] **Pronto quando:** systemctl --user status amtech-bot ativo
- Implanta: Telegram (avisos)

### 18.5 WhatsApp Cloud API: só depois de 1 mês de Telegram estável

**Você** · 10 min

- **Fora do terminal:** Exige conta Meta Business e número próprio; decisão depois do Telegram.
- [ ] **Pronto quando:** Decisão registrada
- Implanta: Telegram (avisos)

<a id="f-casa"></a>

## 19 · Casa e vida

Casa, documentos, cães, veículos, sono e treino organizados e com aviso automático.

**Quando:** Dez/2026

### 19.1 Subir Home Assistant, Paperless e Grocy

**Script** · 20 min

No **Ubuntu** (linha `alanmateus@...$`):

```bash
cd ~/dev/dev-setup/infra/casa && cp -n casa.env.example .env && nano .env && docker compose up -d
```

- [ ] **Pronto quando:** Os três abrindo no navegador (8123, 8010, 9283)
- No .env, troque SEU_USUARIO e cole uma chave gerada por openssl rand -hex 32 (guarde no KeePassXC).
- Implanta: Home Assistant · Paperless-ngx · Grocy

### 19.2 Pôr os documentos da casa e da escola na entrada do Paperless

**Você** · 30 min

- **Fora do terminal:** Você escolhe os documentos; ficam só no seu PC.
- [ ] **Pronto quando:** Documentos com busca no texto
- Implanta: Paperless-ngx

### 19.3 Cadastrar ração, remédios e vacinas dos cães no Grocy com alerta

**Você** · 30 min

- **Fora do terminal:** Cadastro na tela do Grocy.
- [ ] **Pronto quando:** Avisos antes de acabar e antes do vencimento
- Implanta: Grocy

### 19.4 Veículos e metas de compra no Caixa da Casa

**Você** · 20 min

- **Fora do terminal:** O Caixa da Casa é um artefato; fora do terminal.
- [ ] **Pronto quando:** Veículos e metas preenchidos

### 19.5 Sono, natação e MTB na Rotina, com aviso de sono abaixo de 7 h

**Você** · 15 min

- **Fora do terminal:** Rotina do Caixa da Casa.
- [ ] **Pronto quando:** Blocos na Rotina

### 19.6 Primeira automação da casa no Home Assistant

**Você** · 1 h 00 min

- **Fora do terminal:** Configurada na tela do Home Assistant; os projetos ESP32 entram depois.
- [ ] **Pronto quando:** Uma automação funcionando
- Implanta: Home Assistant

<a id="f-elite"></a>

## 20 · Padrão de elite em todo repositório

Nenhum commit com segredo, vulnerabilidade ou teste quebrado chega ao GitHub; segredo só sai do cofre; backup testado.

**Quando:** Semana 5 · nov/2026

### 20.1 Instalar o pre-commit

**Script** · 5 min

No **Ubuntu** (linha `alanmateus@...$`):

```bash
sudo apt install -y pipx && pipx install pre-commit && pipx ensurepath
```

- [ ] **Pronto quando:** pre-commit --version responde
- Implanta: Repositório padrão

### 20.2 Aplicar o repositório padrão em todos os seus repositórios

**Script** · 10 min

No **Ubuntu** (linha `alanmateus@...$`):

```bash
cd ~/dev/dev-setup && bash scripts/wsl/padronizar-repo.sh --todos
```

- [ ] **Pronto quando:** Todos os repositórios com hooks e CI de qualidade
- Só cria o que falta. Revise com git status, faça commit e push em cada um.
- Implanta: Repositório padrão · gitleaks · Trivy

### 20.3 Varrer o histórico de todos os repositórios atrás de segredos

**Script** · 15 min

No **Ubuntu** (linha `alanmateus@...$`):

```bash
cd ~/dev && for r in */; do echo "== $r"; docker run --rm -v "$PWD/$r:/repo" zricethezav/gitleaks:latest detect -s /repo --no-banner; done
```

- [ ] **Pronto quando:** Nenhum segredo encontrado (ou trocado e removido)
- Se achar algo: troque a senha ou chave na hora (o histórico do GitHub guarda cópia).
- Implanta: gitleaks · Trivy

### 20.4 Rodar serviços com segredos vindos do KeePassXC

**Script** · 15 min

No **Ubuntu** (linha `alanmateus@...$`):

```bash
sudo apt install -y keepassxc && bash ~/dev/dev-setup/scripts/wsl/segredos.sh 'Automacao/N8N_CHAVE' N8N_CHAVE -- env | grep -c N8N_CHAVE
```

- [ ] **Pronto quando:** Um serviço sobe sem .env em texto puro
- A senha do cofre é digitada à mão. O teste deve mostrar 1.
- Implanta: Segredos do cofre (keepassxc-cli)

### 20.5 Testar a restauração do backup (todo mês)

**Script** · 15 min

No **Ubuntu** (linha `alanmateus@...$`):

```bash
bash ~/dev/dev-setup/scripts/wsl/teste-restauracao.sh
```

- [ ] **Pronto quando:** TESTE OK: o backup restaura
- Precisa de RESTIC_REPOSITORY definido. Marque na Rotina: primeiro domingo do mês.
- Implanta: Teste de restauração

### 20.6 Revisão mensal de qualidade: CI, evals, painel e backups

**Você** · 30 min

- **Fora do terminal:** Hábito de 30 minutos no primeiro sábado do mês.
- [ ] **Pronto quando:** Checklist do mês feito
- Implanta: Agente revisor de qualidade

### 20.7 Aplicar os cortes de custo agora (IAs pagas repetidas, Vercel em projeto comercial, Sonar privado)

**Você** · 30 min

- **Fora do terminal:** Cancelamentos são nas contas de cada serviço, no navegador. A lista está em docs/custos.md.
- [ ] **Pronto quando:** Assinaturas canceladas ou trocadas conforme docs/custos.md
- Implanta: Claude (assinatura e API)

### 20.8 Pedir o GitHub Education (Copilot e créditos grátis de estudante)

**Você** · 20 min

- **Fora do terminal:** Pedido no site do GitHub Education com comprovante de matrícula.
- [ ] **Pronto quando:** Pacote de estudante aprovado
- Implanta: GitHub Education · GitHub Copilot

### 20.9 Auditoria de custos a cada 3 meses

**Você** · 30 min

- **Fora do terminal:** Revisão trimestral; peça ao Claude para atualizar data/custos.json com o que mudou.
- [ ] **Pronto quando:** docs/custos.md revisado e Caixa da Casa conferido
- Implanta: Caixa da Casa / AM Rendara

<a id="f-ia-elite"></a>

## 21 · Agentes e IA com qualidade medida

Todo agente passa pelo gateway, tem testes e um revisor antes de chegar ao cliente.

**Quando:** Semana 6 · nov/2026 a dez/2026

### 21.1 Subir o gateway de modelos (LiteLLM) com teto de gasto

**Script** · 15 min

No **Ubuntu** (linha `alanmateus@...$`):

```bash
cd ~/dev/dev-setup/infra/ia && cp -n ia.env.example .env && nano .env && docker compose up -d
```

- [ ] **Pronto quando:** http://localhost:4000 responde com os modelos local, rapido e forte
- Melhor: deixe o .env vazio e suba com scripts/wsl/segredos.sh. O teto mensal está em litellm.yaml.
- Implanta: Gateway de modelos (LiteLLM)

### 21.2 Rodar os testes do primeiro agente (promptfoo)

**Script** · 15 min

No **Ubuntu** (linha `alanmateus@...$`):

```bash
cd ~/dev/dev-setup/infra/ia/evals && npx promptfoo@latest eval
```

- [ ] **Pronto quando:** Todos os casos passam
- Implanta: Evals dos agentes (promptfoo)

### 21.3 Ver quais modelos maiores cabem no seu notebook

**Script** · 5 min

No **Ubuntu** (linha `alanmateus@...$`):

```bash
python3 ~/dev/dev-setup/tools/ia/cabe.py 32 && python3 ~/dev/dev-setup/tools/ia/cabe.py 30 --ativos 3
```

- [ ] **Pronto quando:** Lista do que roda local, offload ou só alugado
- Implanta: llama.cpp (GGUF)

### 21.4 Rodar um modelo MoE ou de 14B+ quantizado que o cabe.py aprovou

**Você** · 30 min

- **Fora do terminal:** Escolha o modelo na biblioteca do Ollama pelo resultado do cabe.py; os nomes mudam com frequência.
- [ ] **Pronto quando:** Modelo respondendo no Ollama pelo gateway
- Implanta: Ollama · Modelos locais: Qwen · Gemma · Llama

### 21.5 Construir o agente revisor de qualidade (Claude Agent SDK)

**Claude com você** · 2 h 00 min

No **Ubuntu** (linha `alanmateus@...$`):

```bash
cd ~/dev/dev-setup && claude "Passo ia-revisor do roteiro: Construir o agente revisor de qualidade com o Claude Agent SDK, usando o padrão de qualidade das ofertas e o gateway"
```

- [ ] **Pronto quando:** Revisor aprova ou devolve uma entrega com o motivo
- Implanta: Agente revisor de qualidade · Claude Agent SDK

### 21.6 Construir o MCP próprio só de leitura (portfólio, softwares, roteiro)

**Claude com você** · 1 h 30 min

No **Ubuntu** (linha `alanmateus@...$`):

```bash
cd ~/dev/dev-setup && claude "Passo ia-mcp do roteiro: Construir um servidor MCP só de leitura com data/portfolio.json, data/softwares.json e data/implantacao.json"
```

- [ ] **Pronto quando:** Claude Code consulta os seus dados pelo MCP
- Implanta: MCP próprio (seus dados) · Servidores MCP

### 21.7 Agentes do n8n passam pelo gateway e têm evals

**Claude com você** · 1 h 30 min

No **Ubuntu** (linha `alanmateus@...$`):

```bash
cd ~/dev/dev-setup && claude "Passo ia-n8n do roteiro: Ligar os agentes do n8n ao gateway LiteLLM e criar os evals de cada um"
```

- [ ] **Pronto quando:** Fluxos de agente usando local/rapido/forte, com testes
- Implanta: n8n · Gateway de modelos (LiteLLM) · Evals dos agentes (promptfoo)

### 21.8 Montar a segunda IA: Google AI Plus no lugar do Google One e ChatGPT Go grátis pelo Nubank

**Você** · 20 min

- **Fora do terminal:** Assinaturas no app do Google One e no app do Nubank. Confira antes o tamanho do seu plano atual do Google One.
- [ ] **Pronto quando:** Gemini, NotebookLM e ChatGPT Go funcionando; Google One antigo trocado
- Implanta: Gemini (pago) · ChatGPT · Google Drive (seus documentos)

### 21.9 Usar a IA certa para cada tarefa (rascunho barato, revisão no Claude)

**Você** · 10 min

- **Fora do terminal:** Hábito; a tabela está em docs/custos.md.
- [ ] **Pronto quando:** Tabela de rotas em docs/custos.md seguida por 2 semanas
- Implanta: Claude (assinatura e API) · NotebookLM

### 21.10 Mesmas regras para todas as IAs em cada repositório

**Script** · 5 min

No **Ubuntu** (linha `alanmateus@...$`):

```bash
bash ~/dev/dev-setup/scripts/wsl/regras-ia.sh ~/dev/aulas
```

- [ ] **Pronto quando:** CLAUDE.md, AGENTS.md e GEMINI.md presentes
- Implanta: CLAUDE.md, agentes e skills (seus)

### 21.11 Ligar a cota grátis do Gemini no gateway para rascunhos em lote

**Você** · 10 min

- **Fora do terminal:** Chave criada no Google AI Studio (navegador) e guardada no KeePassXC; depois suba o gateway com scripts/wsl/segredos.sh.
- [ ] **Pronto quando:** Modelo 'gratis' respondendo no gateway
- Implanta: Gateway de modelos (LiteLLM)

### 21.12 Adotar as conversas curtas: pacote de contexto no começo, ESTADO.md no fim

**Script** · 5 min

No **Ubuntu** (linha `alanmateus@...$`):

```bash
python3 ~/dev/dev-setup/tools/sessao/contexto.py --resumo | clip.exe
```

- [ ] **Pronto quando:** Uma semana de tarefas, cada uma numa conversa nova
- Cole na conversa nova. Protocolo completo em docs/operacao/sessoes-curtas.md.
- Implanta: Pacote de contexto + ESTADO.md

### 21.13 Atualizar o ai-memory para a 2.0 e reinstalar os hooks do Claude Code

**Claude com você** · 30 min

No **Ubuntu** (linha `alanmateus@...$`):

```bash
cd ~/dev/dev-setup && claude "Passo ia-memoria2 do roteiro: Atualizar o ai-memory para a versão 2.0 (github.com/akitaonrails/ai-memory) e reinstalar os hooks do Claude Code"
```

- [ ] **Pronto quando:** Sessão nova do Claude Code começa com o briefing do projeto
- Implanta: ai-memory

### 21.14 Instalar o ai-usagebar para ver o limite antes de começar

**Claude com você** · 20 min

No **Ubuntu** (linha `alanmateus@...$`):

```bash
cd ~/dev/dev-setup && claude "Passo ia-usagebar do roteiro: Instalar o ai-usagebar do Akita (github.com/akitaonrails) em modo TUI no Ubuntu do WSL"
```

- [ ] **Pronto quando:** Uso do Claude visível no terminal
- Implanta: ai-usagebar (Akita)

### 21.15 Ligar as reservas baratas no gateway (DeepSeek, OpenRouter) para rascunho em volume

**Você** · 15 min

- **Fora do terminal:** Chaves criadas no navegador e guardadas no KeePassXC; nada sensível passa por elas.
- [ ] **Pronto quando:** Modelos barato e reserva respondendo no gateway
- Implanta: Gateway de modelos (LiteLLM) · OpenRouter

<a id="f-agentes"></a>

## 22 · Roteador de agentes e esteira de sites

Cada tarefa na melhor ferramenta, com reserva e portão; sites feitos por agentes e só conferidos por você. Detalhes em docs/recursos.md.

**Quando:** Semana 6 · nov/2026 a dez/2026

### 22.1 Pedir a verificação de professor no GitHub Education (libera o Copilot Pro grátis)

**Você** · 15 min

- **Fora do terminal:** Em education.github.com, com comprovante de vínculo da escola. É o passo que mais destrava a esteira.
- [ ] **Pronto quando:** Copilot Pro ativo na sua conta
- Implanta: GitHub Education · GitHub Copilot

### 22.2 Ligar o MCP da Hostinger no Claude Code (WSL)

**Script** · 10 min

No **Ubuntu** (linha `alanmateus@...$`):

```bash
bash ~/dev/dev-setup/scripts/wsl/segredos.sh "Hostinger/API_TOKEN" HOSTINGER_API_TOKEN -- claude mcp add -s user --env HOSTINGER_API_TOKEN="$HOSTINGER_API_TOKEN" hostinger-api-mcp -- npx -y hostinger-api-mcp
```

- [ ] **Pronto quando:** O Claude Code lista os seus sites da Hostinger
- A Hostinger não está no diretório de conectores do app; o servidor oficial roda pelo npm. Crie o token no painel e guarde no KeePassXC antes.
- Implanta: Hostinger (clientes WP) · Claude (assinatura e API)

### 22.3 Criar o repositório do primeiro site a partir da esteira

**Script** · 30 min

No **Ubuntu** (linha `alanmateus@...$`):

```bash
cp -r ~/dev/dev-setup/infra/templates/esteira-site/. ~/dev/site-pessoal/ && bash ~/dev/dev-setup/scripts/wsl/regras-ia.sh ~/dev/site-pessoal
```

- [ ] **Pronto quando:** Issue com a ficha atribuída ao Copilot e PR aberto com o workflow qualidade verde
- Implanta: Esteira de sites (issue → PR → ar) · GitHub Copilot

### 22.4 Ligar prévia no Cloudflare Pages e deploy por push na Hostinger

**Claude com você** · 20 min

- **Fora do terminal:** Peça ao Claude com a skill deploy-to-hosting depois do passo ag-hostinger-mcp.
- [ ] **Pronto quando:** Merge na main publica o site; cada PR tem link de prévia
- Implanta: Esteira de sites (issue → PR → ar) · Hostinger (clientes WP) · Cloudflare (DNS, Pages, e-mail)

### 22.5 Rotina do Claude Code que revisa cada PR da esteira

**Claude com você** · 15 min

- **Fora do terminal:** Rotina com gatilho de PR no GitHub. O Pro tem 5 execuções por dia: use só nos repositórios da esteira.
- [ ] **Pronto quando:** Todo PR novo recebe a revisão contra o AGENTS.md
- Implanta: Claude Code · Esteira de sites (issue → PR → ar)

### 22.6 Trocar o conector descontinuado da Cloudflare pelo Cloudflare API MCP

**Você** · 5 min

- **Fora do terminal:** Nas configurações de conectores do Claude.
- [ ] **Pronto quando:** Conector novo responde e o antigo foi removido
- Implanta: Conector Cloudflare · Cloudflare (DNS, Pages, e-mail)

### 22.7 Ligar o modelo grátis da Cloudflare (Workers AI) no gateway

**Você** · 10 min

- **Fora do terminal:** Token com permissão só de Workers AI e o ID da conta no KeePassXC; suba com scripts/wsl/segredos.sh.
- [ ] **Pronto quando:** Modelo 'gratis-cf' respondendo no gateway
- Implanta: Gateway de modelos (LiteLLM) · Cloudflare (DNS, Pages, e-mail)

### 22.8 Pedir o Canva para Educação

**Você** · 10 min

- **Fora do terminal:** No site do Canva, com comprovante da escola.
- [ ] **Pronto quando:** Conta de professor aprovada (ou recusada: segue no grátis)
- Implanta: Canva · Krita · Inkscape

### 22.9 Testar o OpenClaw isolado na VM (só depois da esteira entregar um site)

**Você** · 1 h 00 min

- **Fora do terminal:** Versão mais recente, porta só no Tailscale, sem skills da loja, chave do gateway com teto de US$ 2. Se não trouxer ganho em 2 semanas, desligue.
- [ ] **Pronto quando:** Uma tarefa noturna rodando com relatório no Telegram, sem acesso às suas contas
- Implanta: OpenClaw (agente 24 h) · VM sempre ligada (Oracle grátis)

<a id="f-ia-grande"></a>

## 23 · Modelos grandes sem computador maior

Usar e treinar modelos muito maiores que o notebook aguenta: cluster na rede, GPU por hora, destilação e QLoRA.

**Quando:** 2027, depois do primeiro fine-tuning de 8B

### 23.1 Construir um GPT pequeno do zero no Kaggle

**Você** · 10 h 00 min

- **Fora do terminal:** Estudo guiado no Kaggle (GPU grátis); o código é seu.
- [ ] **Pronto quando:** Modelo treinado gera texto e você explica cada parte
- Implanta: GPT do zero (estudo) · Kaggle · Colab (GPU grátis)

### 23.2 Dividir um modelo entre dois computadores da sua rede (llama.cpp RPC)

**Claude com você** · 2 h 00 min

No **Ubuntu** (linha `alanmateus@...$`):

```bash
cd ~/dev/dev-setup && claude "Passo ig-cluster do roteiro: Montar o llama.cpp RPC entre o notebook e o segundo computador pelo Tailscale"
```

- [ ] **Pronto quando:** Modelo maior respondendo com as duas máquinas
- Precisa de um segundo computador na rede. A velocidade depende da rede: cabo ou Wi-Fi bom.
- Implanta: Cluster de IA na rede · Tailscale (VPN)

### 23.3 Destilar: modelo grande gera exemplos, um 8B aprende a tarefa

**Claude com você** · 4 h 00 min

No **Ubuntu** (linha `alanmateus@...$`):

```bash
cd ~/dev/dev-setup && claude "Passo ig-destilacao do roteiro: Destilação de uma tarefa do grupo para um modelo de 8B, medida pelos evals"
```

- [ ] **Pronto quando:** Modelo pequeno com nota próxima do grande nos seus evals
- Implanta: Destilação · Kaggle · Colab (GPU grátis) · Evals dos agentes (promptfoo)

### 23.4 Fine-tuning QLoRA de 32B a 70B em GPU alugada, com teto de gasto

**Você** · 4 h 00 min

- **Fora do terminal:** Aluguel de GPU por hora no navegador; defina o teto antes de ligar e desligue ao terminar.
- [ ] **Pronto quando:** Adaptador treinado e avaliado contra o modelo base
- **Precisa:** pagar um serviço
- Implanta: GPU por hora (RunPod e afins) · vLLM (GPU alugada)

### 23.5 Servir o seu modelo com vLLM na GPU alugada, pelo gateway

**Claude com você** · 1 h 00 min

No **Ubuntu** (linha `alanmateus@...$`):

```bash
cd ~/dev/dev-setup && claude "Passo ig-vllm do roteiro: Servir o modelo treinado com vLLM numa GPU por hora e ligar como gpu-alugada no LiteLLM"
```

- [ ] **Pronto quando:** gpu-alugada responde no gateway
- **Precisa:** pagar um serviço
- Implanta: vLLM (GPU alugada) · Gateway de modelos (LiteLLM)

### 23.6 Strata: rodar um MoE de 125B em casa quando tiver GPU de 12 GB ou mais

**Você** · 2 h 00 min

- **Fora do terminal:** Depende da workstation (a GTX 1650 de 4 GB está abaixo do mínimo testado). Repositório: github.com/Niko1221/Strata.
- [ ] **Pronto quando:** Modelo respondendo pela API local, ligado ao gateway
- Implanta: Strata (MoE grande) · Workstation com GPU

<a id="f-rede"></a>

## 24 · Rede própria entre os seus computadores

Seus aparelhos numa rede privada criptografada, com arquivos sincronizados e DNS próprio, sem nada exposto na internet.

**Quando:** Semana 6 · nov/2026

### 24.1 Instalar o Tailscale no Windows e no celular

**Script** · 15 min

No **PowerShell** do Windows (linha `PS C:\>`):

```powershell
winget install --id Tailscale.Tailscale -e
```

- [ ] **Pronto quando:** Notebook e celular aparecem no painel do Tailscale
- O login é no navegador; no celular, app Tailscale. O Ubuntu do WSL usa a rede do Windows.
- Implanta: Tailscale (VPN)

### 24.2 Ligar MagicDNS e escrever as regras de acesso (ACL)

**Você** · 20 min

- **Fora do terminal:** Painel do Tailscale, no navegador. Modelo das regras em docs/rede/README.md.
- [ ] **Pronto quando:** Celular acessa só o que precisa
- Implanta: Tailscale (VPN)

### 24.3 Sincronizar uma pasta entre notebook e celular com o Syncthing

**Script** · 20 min

No **PowerShell** do Windows (linha `PS C:\>`):

```powershell
winget install --id Syncthing.Syncthing -e
```

- [ ] **Pronto quando:** Pasta de teste sincronizando nos dois
- Implanta: Syncthing

### 24.4 Subir o AdGuard Home como DNS da casa

**Script** · 15 min

No **Ubuntu** (linha `alanmateus@...$`):

```bash
cd ~/dev/dev-setup/infra/rede && docker compose up -d
```

- [ ] **Pronto quando:** Configuração inicial em http://localhost:3001
- Para usar no celular fora de casa, aponte o DNS do Tailscale para o notebook.
- Implanta: AdGuard Home (DNS)

### 24.5 Montar o laboratório de redes (Packet Tracer)

**Você** · 1 h 00 min

- **Fora do terminal:** Conta gratuita na Cisco Networking Academy e download do Packet Tracer.
- [ ] **Pronto quando:** Primeira topologia com 2 VLANs funcionando
- Implanta: Laboratório de redes

### 24.6 Montar um túnel WireGuard à mão entre o WSL e o celular

**Claude com você** · 1 h 00 min

No **Ubuntu** (linha `alanmateus@...$`):

```bash
cd ~/dev/dev-setup && claude "Passo rd-wireguard do roteiro: Montar um túnel WireGuard à mão entre o Ubuntu do WSL e o celular, explicando cada chave e cada linha"
```

- [ ] **Pronto quando:** Ping pelo túnel funcionando
- Implanta: WireGuard (na mão)

<a id="f-247"></a>

## 25 · Operação 24 horas

O que pode rodar sozinho roda o tempo todo: vigia, avisos, prospecção com aprovação, lucro por ferramenta. Sem gastar com o que não dá retorno.

**Quando:** Dez/2026 a jan/2027

### 25.1 Entender o que roda onde: notebook, GitHub e VM

**Você** · 10 min

- **Fora do terminal:** Leitura: docs/operacao/24-horas no fim deste passo. Notebook desligado = WSL, n8n local e cron parados; GitHub Actions e a VM continuam.
- [ ] **Pronto quando:** Você sabe o que para quando o notebook desliga
- Implanta: Vigia semanal (GitHub Actions) · VM sempre ligada (Oracle grátis)

### 25.2 Ligar o vigia semanal no GitHub (sites dos clientes e segredos)

**Você** · 10 min

- **Fora do terminal:** Já está no repositório. Coloque as URLs dos sites dos clientes em data/vigia.json e rode em Actions > vigia > Run workflow.
- [ ] **Pronto quando:** Execução manual do workflow 'vigia' verde
- Implanta: Vigia semanal (GitHub Actions)

### 25.3 Preencher o lucro do mês e ver o resultado de cada ferramenta

**Script** · 15 min

No **Ubuntu** (linha `alanmateus@...$`):

```bash
mkdir -p ~/financas && cp -n ~/dev/dev-setup/tools/roi/roi.example.toml ~/financas/roi.toml && nano ~/financas/roi.toml && python3 ~/dev/dev-setup/tools/roi/roi.py
```

- [ ] **Pronto quando:** Relatório com prejuízos marcados
- Todo dia 1: receita, custos e horas (do ActivityWatch) de cada renda. Ferramenta no prejuízo por 2 meses: cortar, trocar ou adiar.
- Implanta: Lucro por ferramenta

### 25.4 Criar a VM grátis da Oracle (2 núcleos, 12 GB) e pôr no Tailscale

**Você** · 1 h 00 min

- **Fora do terminal:** Cadastro no navegador (pede cartão para verificação; o plano Always Free não cobra). A Oracle reduziu o limite grátis em jun/2026: confira antes.
- [ ] **Pronto quando:** VM acessível pelo Tailscale, sem porta aberta na internet
- Implanta: VM sempre ligada (Oracle grátis) · Tailscale (VPN)

### 25.5 Levar n8n, bot do Telegram, Uptime Kuma e gateway para a VM

**Claude com você** · 3 h 00 min

No **Ubuntu** (linha `alanmateus@...$`):

```bash
cd ~/dev/dev-setup && claude "Passo op-migrar do roteiro: Levar n8n, bot do Telegram, Uptime Kuma e LiteLLM para a VM da Oracle pelo Tailscale, com backup e segredos do KeePassXC"
```

- [ ] **Pronto quando:** Avisos e automações funcionando com o notebook desligado
- Implanta: VM sempre ligada (Oracle grátis) · n8n · Telegram (avisos) · Uptime Kuma · Gateway de modelos (LiteLLM)

### 25.6 Prospector: lista de negócios de dados públicos e abordagem para você aprovar

**Claude com você** · 2 h 00 min

No **Ubuntu** (linha `alanmateus@...$`):

```bash
cd ~/dev/dev-setup && claude "Passo op-prospector do roteiro: Construir o prospector: lista de negócios locais a partir de dados públicos, rascunho de abordagem, aprovação manual e registro no CRM com base legal LGPD"
```

- [ ] **Pronto quando:** Lista semanal com 20 negócios e rascunhos; nada enviado sem você
- Nada de disparo em massa no WhatsApp: viola as regras e bloqueia o número. Contato um a um, com opção de não receber mais.
- Implanta: Prospector com aprovação · CRM único + LGPD

### 25.7 Manter os agentes afiados: reindexar as notas e rodar os evals todo mês

**Você** · 30 min

- **Fora do terminal:** Hábito mensal. Treino (fine-tuning) só a cada trimestre e só se os evals mostrarem ganho.
- [ ] **Pronto quando:** Evals do mês iguais ou melhores
- Implanta: Evals dos agentes (promptfoo) · Base de conhecimento (RAG) das suas notas

### 25.8 Escolher no máximo 2 tarefas agendadas do Claude (ex.: analista semanal)

**Você** · 20 min

- **Fora do terminal:** Tarefas agendadas gastam o mesmo limite do Claude: só as que pagam o próprio gasto. Peça numa conversa nova para criar.
- [ ] **Pronto quando:** Tarefas criadas e com resultado útil
- Implanta: Tarefas agendadas

<a id="f-crescimento"></a>

## 26 · Dados e crescimento: medir, testar e vender mais

Saber onde o cliente desiste, testar a página que vende mais, conhecer cada cliente e atender rápido, com ferramentas abertas.

**Quando:** Com a primeira página de venda no ar (jan/2027) e por etapas

### 26.1 Subir o Metabase e criar o painel de vendas e clientes

**Script** · 30 min

No **Ubuntu** (linha `alanmateus@...$`):

```bash
cd ~/dev/dev-setup/infra/dados && docker compose up -d
```

- [ ] **Pronto quando:** Painel com receita por renda, ticket médio e clientes novos
- Conecte ao banco de métricas (PostgreSQL da automação) pela tela do Metabase.
- Implanta: Metabase (painéis)

### 26.2 Ligar o PostHog nas páginas de venda (funil e gravações)

**Você** · 30 min

- **Fora do terminal:** Conta no plano de nuvem com cota grátis e o script na página; respeite o aviso de cookies (LGPD).
- [ ] **Pronto quando:** Funil visita → checkout → compra visível
- Implanta: PostHog (funil e gravações)

### 26.3 Primeiro teste A/B da página do mini-curso

**Claude com você** · 1 h 00 min

No **Ubuntu** (linha `alanmateus@...$`):

```bash
cd ~/dev/dev-setup && claude "Passo cr-ab do roteiro: Primeiro teste A/B da página do mini-curso com GrowthBook e PostHog, com hipótese, meta e tamanho mínimo de amostra"
```

- [ ] **Pronto quando:** Teste rodando com meta e tamanho de amostra definidos
- Implanta: GrowthBook (testes A/B) · PostHog (funil e gravações)

### 26.4 Análises de cliente: RFM, LTV, churn e previsão de receita

**Claude com você** · 2 h 00 min

No **Ubuntu** (linha `alanmateus@...$`):

```bash
cd ~/dev/dev-setup && claude "Passo cr-analises do roteiro: Criar as análises de cliente (RFM, LTV, churn e previsão de receita) em Python com DuckDB sobre o banco de métricas"
```

- [ ] **Pronto quando:** Relatório mensal com os 3 números que mudam decisão
- Implanta: Análises de cliente (RFM, LTV, churn) · DuckDB + Parquet

### 26.5 Atendimento numa caixa só com o Chatwoot e o agente atendente

**Claude com você** · 2 h 00 min

No **Ubuntu** (linha `alanmateus@...$`):

```bash
cd ~/dev/dev-setup && claude "Passo cr-chatwoot do roteiro: Subir o Chatwoot na VM e ligar o agente atendente pelo gateway, com passagem para humano"
```

- [ ] **Pronto quando:** WhatsApp, Instagram e site respondidos no mesmo lugar
- Entra com 3 clientes de sites ou o primeiro curso vendendo.
- Implanta: Chatwoot (atendimento) · Agente atendente (WhatsApp)

### 26.6 Trocar a planilha pelo Twenty CRM quando houver 20+ leads ativos

**Claude com você** · 1 h 30 min

No **Ubuntu** (linha `alanmateus@...$`):

```bash
cd ~/dev/dev-setup && claude "Passo cr-crm do roteiro: Subir o Twenty CRM e migrar a planilha de leads e clientes"
```

- [ ] **Pronto quando:** Funil de vendas no CRM, com os leads do prospector
- Implanta: Twenty (CRM aberto) · CRM único + LGPD

### 26.7 Contratos assinados online (Documenso) e orçamentos e cobranças (Invoice Ninja)

**Claude com você** · 1 h 30 min

No **Ubuntu** (linha `alanmateus@...$`):

```bash
cd ~/dev/dev-setup && claude "Passo cr-contratos do roteiro: Subir Documenso e Invoice Ninja na VM com o modelo de contrato do kit de sites"
```

- [ ] **Pronto quando:** Primeiro contrato assinado e primeira fatura enviada pelo sistema
- Implanta: Documenso (assinatura) · Invoice Ninja (orçamentos)

### 26.8 Usar o Penpot para mockups de propostas e telas dos sistemas

**Você** · 30 min

- **Fora do terminal:** Conta grátis no Penpot (navegador) ou auto-hospedado depois.
- [ ] **Pronto quando:** Primeiro mockup de proposta feito no Penpot
- Implanta: Penpot (design)

<a id="f11"></a>

## 27 · Pipeline de conteúdo

Gravou ou escreveu, as peças aparecem na fila de aprovação.

**Quando:** Semana 5 · nov/2026

### 27.1 Preencher o guia de marca

**Você** · 40 min

No **Ubuntu** (linha `alanmateus@...$`):

```bash
code ~/dev/dev-setup/config/marca.md
```

- [ ] **Pronto quando:** config/marca.md sem colchetes
- O Claude pode rascunhar a partir dos documentos de marca e presença; você corrige.
- Implanta: Marca pessoal Alan Mateus

### 27.2 Criar a chave da API no console da Anthropic e colocar no conteudo.env

**Você** · 10 min

- **Fora do terminal:** A chave é criada no site console.anthropic.com; colar no arquivo: nano ~/.config/amtech/conteudo.env.
- [ ] **Pronto quando:** ANTHROPIC_API_KEY preenchida em ~/.config/amtech/conteudo.env
- A API é cobrada por uso, separada da assinatura do Claude. Defina um limite de gasto mensal no console.
- Implanta: Claude (assinatura e API)

### 27.3 Criar o bot de aviso no Telegram (opcional)

**Você** · 10 min

- **Fora do terminal:** O bot é criado conversando com o @BotFather no app do Telegram.
- [ ] **Pronto quando:** Mensagem de teste chega no celular
- Implanta: Telegram (avisos) · Aprovação no celular

### 27.4 Testar o caminho sem gastar

**Script** · 2 min

No **Ubuntu** (linha `alanmateus@...$`):

```bash
echo teste > ~/AMtech/entrada/ideias/teste.txt && touch -d '-2 min' ~/AMtech/entrada/ideias/teste.txt && python3 tools/conteudo/processar.py --uma-vez --simular
```

- [ ] **Pronto quando:** Uma pasta [SIMULADO] aparece em ~/AMtech/fila
- Implanta: Pipeline de conteúdo

### 27.5 Ligar o timer de 15 minutos

**Script** · 2 min

No **Ubuntu** (linha `alanmateus@...$`):

```bash
bash scripts/wsl/ativar-pipeline.sh
```

- [ ] **Pronto quando:** verificar.sh --servicos mostra o timer OK
- Implanta: Pipeline de conteúdo · Agente editor de conteúdo · Flywheel de conteúdo

### 27.6 Colocar uma aula gravada de verdade em ~/AMtech/entrada/aulas

**Você** · 20 min

No **Ubuntu** (linha `alanmateus@...$`):

```bash
cp /mnt/c/Users/SEU_USUARIO/Videos/NOME-DA-AULA.mp4 ~/AMtech/entrada/aulas/
```

- [ ] **Pronto quando:** Peças da aula na fila em até 15 minutos depois de transcrita
- Implanta: Whisper (local) · Flywheel de conteúdo

### 27.7 Revisar e publicar os posts sobre o setup (feed, story e capa do blog)

**Você** · 30 min

- **Fora do terminal:** As imagens estão no artefato de design 'Post: montando meu setup'. Publicação só com a sua aprovação, sem revelar a arquitetura do setup.
- [ ] **Pronto quando:** Posts revisados por você e publicados nas suas redes e no blog
- Implanta: Pipeline de conteúdo

<a id="f12"></a>

## 28 · Estúdio de conteúdo

Gravar, editar e montar imagens no mesmo padrão toda semana, sem pensar.

**Quando:** Semana 5 · dez/2026

### 28.1 Montar no OBS as cenas de aula, tela com rosto e vídeo vertical

**Você** · 40 min

- **Fora do terminal:** Feito dentro do programa (OBS, Audacity, DaVinci), que não tem modo terminal para isso.
- [ ] **Pronto quando:** Gravação de teste de 1 minuto com áudio limpo nas três cenas
- Implanta: OBS Studio

### 28.2 Criar no Audacity a cadeia de limpeza da sua voz (ruído, compressor, volume)

**Você** · 20 min

- **Fora do terminal:** Feito dentro do programa (OBS, Audacity, DaVinci), que não tem modo terminal para isso.
- [ ] **Pronto quando:** A mesma limpeza aplicada com um clique numa gravação nova
- Implanta: Audacity

### 28.3 Criar no DaVinci ou Kdenlive o projeto modelo com abertura, legendas e formato vertical

**Você** · 40 min

- **Fora do terminal:** Feito dentro do programa (OBS, Audacity, DaVinci), que não tem modo terminal para isso.
- [ ] **Pronto quando:** Um corte de 30 segundos exportado a partir do modelo
- Implanta: DaVinci Resolve ou Kdenlive

### 28.4 Criar os modelos de capa, carrossel e thumbnail com a sua marca (Canva, Krita ou Inkscape)

**Claude com você** · 40 min

No **Ubuntu** (linha `alanmateus@...$`):

```bash
cd ~/dev/dev-setup && claude "Passo imagens-modelos do roteiro: Criar os modelos de capa, carrossel e thumbnail com a sua marca (Canva, Krita ou Inkscape)"
```

- [ ] **Pronto quando:** Três modelos salvos; uma peça da fila montada com eles
- O Claude cria os modelos no Canva pelo conector, a partir do config/marca.md.
- Implanta: Canva · Krita · Inkscape · Conectores Canva + Figma

### 28.5 Clonar a sua própria voz na ElevenLabs (opcional, plano pago)

**Você** · 1 h 00 min

- **Fora do terminal:** Cadastro no site ou app do serviço, com documento e confirmação no celular; nenhum deles deixa criar conta por terminal.
- [ ] **Pronto quando:** Trecho de teste com a sua voz clonada aprovado por você
- Só a sua voz, com 30 minutos ou mais de áudio limpo. Avise o público quando a voz for gerada por IA. Voz de outra pessoa, nunca.
- **Precisa:** pagar um serviço
- Implanta: Voz clonada (ElevenLabs)

<a id="f13"></a>

## 29 · Contas, canais e sites

Perfis, domínio, e-mail e sites prontos para receber o que o pipeline produz.

**Quando:** Semanas 6 e 7 · dez/2026

### 29.1 Completar Instagram, YouTube, TikTok, LinkedIn e Facebook com a mesma identidade

**Você** · 1 h 30 min

- **Fora do terminal:** Cadastro no site ou app do serviço, com documento e confirmação no celular; nenhum deles deixa criar conta por terminal.
- [ ] **Pronto quando:** Foto, nome, bio e link iguais nas cinco redes
- Implanta: Instagram · YouTube · TikTok · LinkedIn · Facebook · Marca pessoal Alan Mateus

### 29.2 Configurar o WhatsApp Business com catálogo, respostas rápidas e horário

**Você** · 30 min

- **Fora do terminal:** Cadastro no site ou app do serviço, com documento e confirmação no celular; nenhum deles deixa criar conta por terminal.
- [ ] **Pronto quando:** Mensagem de teste recebe a saudação automática
- Implanta: WhatsApp Business

### 29.3 Registrar o domínio no Registro.br e apontar para a Cloudflare

**Você** · 30 min

- **Fora do terminal:** Cadastro no site ou app do serviço, com documento e confirmação no celular; nenhum deles deixa criar conta por terminal.
- [ ] **Pronto quando:** DNS ativo na Cloudflare
- **Precisa:** pagar um serviço
- Implanta: Domínio (Registro.br) · Cloudflare (DNS, Pages, e-mail)

### 29.4 Criar o e-mail profissional do domínio

**Você** · 30 min

- **Fora do terminal:** Cadastro no site ou app do serviço, com documento e confirmação no celular; nenhum deles deixa criar conta por terminal.
- [ ] **Pronto quando:** Envia e recebe
- **Precisa:** pagar um serviço
- Implanta: E-mail profissional (enviar e receber)

### 29.5 Criar o Gerenciador de Negócios da Meta, o Pixel e a conta de anúncios

**Você** · 40 min

- **Fora do terminal:** Cadastro no site ou app do serviço, com documento e confirmação no celular; nenhum deles deixa criar conta por terminal.
- [ ] **Pronto quando:** Pixel instalado na página de vendas
- Implanta: Meta Business Suite · Tags de conversão (Pixel, Google…)

### 29.6 Montar no MailerLite os grupos, o formulário da isca e a sequência de boas-vindas

**Claude com você** · 30 min

No **Ubuntu** (linha `alanmateus@...$`):

```bash
cd ~/dev/dev-setup && claude "Passo mailerlite do roteiro: Montar no MailerLite os grupos, o formulário da isca e a sequência de boas-vindas"
```

- [ ] **Pronto quando:** Inscrição de teste recebe o primeiro e-mail
- O Claude faz pelo conector do MailerLite, com a sua aprovação.
- Implanta: MailerLite · Isca grátis + sequência de e-mails · Conector MailerLite

### 29.7 Publicar o site pessoal e blog no GitHub Pages (alanmateus17.github.io)

**Claude com você** · 1 h 00 min

No **Ubuntu** (linha `alanmateus@...$`):

```bash
cd ~/dev/dev-setup && claude "Passo site-pessoal do roteiro: Publicar o site pessoal e blog no GitHub Pages (alanmateus17.github.io)"
```

- [ ] **Pronto quando:** Site no ar com portfólio, blog e formulário da newsletter
- Implanta: Site pessoal + blog (Jekyll) · GitHub Pages

### 29.8 Publicar o site do Instituto AMS com a página de pré-venda na Cloudflare Pages

**Claude com você** · 1 h 00 min

No **Ubuntu** (linha `alanmateus@...$`):

```bash
cd ~/dev/dev-setup && claude "Passo vercel-pagina do roteiro: Publicar o site do Instituto AMS com a página de pré-venda na Cloudflare Pages"
```

- [ ] **Pronto quando:** Página no ar com o domínio e o Pixel
- Fica na Cloudflare Pages porque o plano grátis do Vercel não permite uso comercial. O Claude publica pelo conector da Cloudflare ou pelo Wrangler.
- Implanta: Instituto AMS · Cloudflare (DNS, Pages, e-mail)

### 29.9 Publicar o site do Grupo AMtech e o Catálogo do HTML

**Claude com você** · 1 h 30 min

No **Ubuntu** (linha `alanmateus@...$`):

```bash
cd ~/dev/dev-setup && claude "Passo site-grupo do roteiro: Publicar o site do Grupo AMtech e o Catálogo do HTML"
```

- [ ] **Pronto quando:** Os dois sites no ar com domínio e HTTPS
- **Oferta:** Catálogo do HTML (gratuito)
- Implanta: Site Grupo AMtech · Catálogo do HTML

### 29.10 Mostrar o Catálogo do HTML aos alunos e ex-alunos

**Você** · 20 min

- **Fora do terminal:** Venda e relacionamento: falar com gente, publicar e atender. O Claude prepara textos e materiais; quem fala é você.
- [ ] **Pronto quando:** Alunos publicando os próprios sites pelo Catálogo
- É material grátis da escola, não venda. Nada de oferecer produto pago a aluno menor de idade; ex-alunos adultos podem seguir as redes.
- Implanta: Alunos e ex-alunos

### 29.11 Ligar o Umami nos sites

**Claude com você** · 20 min

No **Ubuntu** (linha `alanmateus@...$`):

```bash
cd ~/dev/dev-setup && claude "Passo umami do roteiro: Ligar o Umami nos sites"
```

- [ ] **Pronto quando:** Uma visita de teste aparece no painel do Umami
- Implanta: Umami (analytics)

### 29.12 Ligar o Google Search Console no domínio e enviar o sitemap de cada site

**Você** · 10 min

- **Fora do terminal:** Cadastro no site ou app do serviço, com documento e confirmação no celular; nenhum deles deixa criar conta por terminal.
- [ ] **Pronto quando:** Propriedade verificada e sitemaps lidos
- Implanta: Google Search Console · Busca Google (SEO)

### 29.13 Separar na Hostinger o espaço dos sites de clientes

**Claude com você** · 30 min

No **Ubuntu** (linha `alanmateus@...$`):

```bash
cd ~/dev/dev-setup && claude "Passo hostinger do roteiro: Separar na Hostinger o espaço dos sites de clientes"
```

- [ ] **Pronto quando:** Auditoria da Hostinger sem pendências e um site modelo pronto para copiar
- O Claude faz a auditoria pelo plugin da Hostinger e aponta o que precisa de atenção.
- **Oferta:** Sites e lojas para pequenas empresas
- Implanta: Hostinger (clientes WP) · Sites para pequenas empresas

<a id="f14"></a>

## 30 · Vendas e finanças no CPF

Cada oferta pode ser vendida, recebida e declarada do jeito certo.

**Quando:** Semanas 8 a 10 · dez/2026 a jan/2027

### 30.1 Subir a conta gov.br para prata ou ouro

**Você** · 20 min

- **Fora do terminal:** Órgão público, contador ou entidade: feito no site do governo ou com atendimento.
- [ ] **Pronto quando:** Nível prata ou ouro aparece no app gov.br
- Implanta: gov.br (prata ou ouro)

### 30.2 Abrir a conta bancária separada para o que você vende (no CPF)

**Você** · 30 min

- **Fora do terminal:** Cadastro no site ou app do serviço, com documento e confirmação no celular; nenhum deles deixa criar conta por terminal.
- [ ] **Pronto quando:** Conta aberta; todas as plataformas vão pagar nela
- Implanta: Conta bancária separada (CPF)

### 30.3 Fazer a consulta com o contador: carnê-leão e a partir de que renda abrir CNPJ

**Você** · 1 h 00 min

- **Fora do terminal:** Órgão público, contador ou entidade: feito no site do governo ou com atendimento.
- [ ] **Pronto quando:** Regras do carnê-leão anotadas e o valor de virada para o CNPJ definido
- **Precisa:** pagar um serviço
- Implanta: Contador

### 30.4 Publicar termos de uso e política de privacidade (LGPD) e ter o contrato padrão de serviço

**Claude com você** · 1 h 00 min

No **Ubuntu** (linha `alanmateus@...$`):

```bash
cd ~/dev/dev-setup && claude "Passo legal do roteiro: Publicar termos de uso e política de privacidade (LGPD) e ter o contrato padrão de serviço"
```

- [ ] **Pronto quando:** Links de termos e privacidade no rodapé de todos os sites; contrato em modelo editável
- O Claude rascunha; antes de usar, peça para o contador ou um advogado revisar. Isto vem antes de coletar e-mail ou vender.
- Implanta: Termos, privacidade (LGPD) e contratos

### 30.5 Criar as contas da Hotmart e da Kiwify no CPF e cadastrar o mini-curso

**Você** · 1 h 00 min

- **Fora do terminal:** Cadastro no site ou app do serviço, com documento e confirmação no celular; nenhum deles deixa criar conta por terminal.
- [ ] **Pronto quando:** Produto em rascunho nas duas
- Implanta: Hotmart · Kiwify · Mini-curso Lógica de Programação

### 30.6 Abrir as contas na Eduzz e na Udemy e publicar artigos e projetos na DIO

**Você** · 1 h 00 min

- **Fora do terminal:** Cadastro no site ou app do serviço, com documento e confirmação no celular; nenhum deles deixa criar conta por terminal.
- [ ] **Pronto quando:** Contas aprovadas; formulário fiscal da Udemy enviado; primeiro artigo publicado na DIO
- Na Udemy o recebimento é por PayPal ou Payoneer e vai para o carnê-leão como renda do exterior.
- **Oferta:** Parceria DIO
- Implanta: Eduzz · Udemy · DIO (parceria)

### 30.7 Ativar o Mercado Pago para Pix e cartão das aulas e dos sites

**Você** · 20 min

- **Fora do terminal:** Cadastro no site ou app do serviço, com documento e confirmação no celular; nenhum deles deixa criar conta por terminal.
- [ ] **Pronto quando:** Link de pagamento de teste pago e estornado
- Implanta: Mercado Pago

### 30.8 Criar a agenda online no Cal.com com pagamento para as aulas particulares

**Você** · 30 min

- **Fora do terminal:** Cadastro no site ou app do serviço, com documento e confirmação no celular; nenhum deles deixa criar conta por terminal.
- [ ] **Pronto quando:** Horário de teste marcado e cobrado
- **Oferta:** Aulas particulares
- Implanta: Agenda online (Cal.com) · Aulas particulares

### 30.9 Criar o CRM em planilha com origem e consentimento de cada cliente

**Claude com você** · 30 min

No **Ubuntu** (linha `alanmateus@...$`):

```bash
cd ~/dev/dev-setup && claude "Passo crm do roteiro: Criar o CRM em planilha com origem e consentimento de cada cliente"
```

- [ ] **Pronto quando:** Planilha com colunas de oferta, origem, consentimento LGPD e próximo passo
- Implanta: CRM simples (planilha) · CRM único + LGPD

### 30.10 Abrir a comunidade dos alunos (Discord ou grupo)

**Você** · 30 min

- **Fora do terminal:** Cadastro no site ou app do serviço, com documento e confirmação no celular; nenhum deles deixa criar conta por terminal.
- [ ] **Pronto quando:** Regras publicadas e convite automático na compra
- Implanta: Comunidade (Discord ou grupo)

### 30.11 Entrar nos programas de afiliados (Amazon, Hotmart) e criar a lista de links

**Você** · 30 min

- **Fora do terminal:** Cadastro no site ou app do serviço, com documento e confirmação no celular; nenhum deles deixa criar conta por terminal.
- [ ] **Pronto quando:** Links de afiliado com UTM numa nota do Obsidian
- **Oferta:** Afiliados (ferramentas, livros, equipamentos que você usa)
- Implanta: Afiliados (Amazon, Hotmart…)

### 30.12 Adotar o padrão de UTM em todo link

**Claude com você** · 15 min

No **Ubuntu** (linha `alanmateus@...$`):

```bash
cd ~/dev/dev-setup && claude "Passo utm do roteiro: Adotar o padrão de UTM em todo link"
```

- [ ] **Pronto quando:** Gerador de links com UTM salvo e usado no primeiro post
- Implanta: Padrão de UTM

### 30.13 Calcular o lucro por venda de cada oferta e definir as regras de corte dos anúncios

**Você** · 30 min

- **Fora do terminal:** Decisão sua; os números e as opções já estão no roteiro e no portfólio.
- [ ] **Pronto quando:** CPA de empate e CPA da margem anotados para cada oferta ativa
- Implanta: Lucro por Venda (calculadora) · Regras de corte

### 30.14 Revisar o portfólio de ofertas: estágio, próximo passo e padrão de qualidade

**Claude com você** · 45 min

No **Ubuntu** (linha `alanmateus@...$`):

```bash
cd ~/dev/dev-setup && claude "Passo ofertas do roteiro: Revisar o portfólio de ofertas: estágio, próximo passo e padrão de qualidade"
```

- [ ] **Pronto quando:** Uma oferta em construção e uma em validação, cada uma com o checklist de pronto
- O Claude cria o comando /revisar-oferta, que confere um lançamento contra o padrão de qualidade antes de ir ao ar.
- Implanta: Portfólio de ofertas · Esteira de ofertas · Padrão de qualidade · Revisor de oferta

### 30.15 Ligar a pergunta de satisfação depois de cada compra ou serviço e o pedido de avaliação no Google

**Claude com você** · 30 min

No **Ubuntu** (linha `alanmateus@...$`):

```bash
cd ~/dev/dev-setup && claude "Passo avaliacoes do roteiro: Ligar a pergunta de satisfação depois de cada compra ou serviço e o pedido de avaliação no Google"
```

- [ ] **Pronto quando:** Compra de teste recebe a pergunta por e-mail
- Implanta: NPS e avaliações

### 30.16 Montar a lista de parceiros e a primeira mensagem de prospecção

**Claude com você** · 45 min

No **Ubuntu** (linha `alanmateus@...$`):

```bash
cd ~/dev/dev-setup && claude "Passo prospeccao do roteiro: Montar a lista de parceiros e a primeira mensagem de prospecção"
```

- [ ] **Pronto quando:** 10 parceiros qualificados e a mensagem revisada por você
- O Claude busca e qualifica; quem envia é você.
- Implanta: Prospecção de parceiros

### 30.17 Pesquisar e pedir o registro das marcas no INPI

**Você** · 1 h 00 min

- **Fora do terminal:** Órgão público, contador ou entidade: feito no site do governo ou com atendimento.
- [ ] **Pronto quando:** Pesquisa sem conflito e pedido protocolado (ou decisão de esperar, anotada)
- **Precisa:** pagar um serviço
- Implanta: Registro de marca (INPI)

### 30.18 Fazer o primeiro carnê-leão do mês e marcar o lembrete mensal

**Você** · 30 min

- **Fora do terminal:** Órgão público, contador ou entidade: feito no site do governo ou com atendimento.
- [ ] **Pronto quando:** DARF gerado (ou mês sem receita registrado) e lembrete todo dia 20
- Implanta: Carnê-leão (Receita Federal)

### 30.19 Separar a pasta da declaração anual do IR

**Você** · 15 min

- **Fora do terminal:** Órgão público, contador ou entidade: feito no site do governo ou com atendimento.
- [ ] **Pronto quando:** Pasta com informes e carnês do ano, guardada no backup
- Implanta: Declaração anual do IR

### 30.20 Começar o Caixa da Casa numa planilha até o sistema AM Rendara existir

**Claude com você** · 30 min

No **Ubuntu** (linha `alanmateus@...$`):

```bash
cd ~/dev/dev-setup && claude "Passo caixa do roteiro: Começar o Caixa da Casa numa planilha até o sistema AM Rendara existir"
```

- [ ] **Pronto quando:** Entradas e saídas do mês lançadas, separando casa e vendas
- **Oferta:** AM Rendara (finanças), começando pela planilha
- Implanta: Caixa da Casa / AM Rendara

<a id="f15"></a>

## 31 · Vendas medidas

Cada venda chega sozinha ao banco e aparece no painel de lucro.

**Quando:** Semana 11 · jan/2027

### 31.1 Criar o túnel público para os webhooks (Cloudflare Tunnel) e preencher N8N_WEBHOOK_URL

**Você** · 40 min

No **Ubuntu** (linha `alanmateus@...$`):

```bash
curl -L https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-amd64.deb -o /tmp/cloudflared.deb && sudo dpkg -i /tmp/cloudflared.deb && cloudflared tunnel login && cloudflared tunnel create amtech-n8n && cloudflared tunnel route dns amtech-n8n n8n.SEU-DOMINIO
```

- [ ] **Pronto quando:** https://n8n.seu-dominio responde fora de casa
- Só o caminho de webhook precisa ficar público; o painel do n8n fica protegido. Troque SEU-DOMINIO pelo domínio do passo do Registro.br. O cloudflared login abre o navegador uma vez para autorizar.
- **Precisa:** pagar um serviço
- Implanta: Cloudflare (DNS, Pages, e-mail) · Webhooks de venda

### 31.2 Criar no n8n o fluxo: webhook Hotmart, Kiwify e Eduzz → tabela vendas

**Claude com você** · 1 h 00 min

No **Ubuntu** (linha `alanmateus@...$`):

```bash
cd ~/dev/dev-setup && claude "Passo fluxo-vendas do roteiro: Criar no n8n o fluxo: webhook Hotmart, Kiwify e Eduzz → tabela vendas"
```

- [ ] **Pronto quando:** Venda de teste aparece na tabela vendas
- O Claude monta o fluxo com você no n8n; a tabela já tem a trava contra venda duplicada.
- Implanta: Webhooks de venda

### 31.3 Lançar os gastos de anúncio (manual no começo, depois pela API de cada rede)

**Você** · 15 min

- **Fora do terminal:** Feito no painel da plataforma, que não tem terminal para isso.
- [ ] **Pronto quando:** Tabela gastos com a primeira campanha
- Implanta: Banco de métricas (PostgreSQL)

### 31.4 Montar o painel de lucro no Grafana sobre a view lucro_por_produto_mes

**Claude com você** · 45 min

No **Ubuntu** (linha `alanmateus@...$`):

```bash
cd ~/dev/dev-setup && claude "Passo painel-lucro do roteiro: Montar o painel de lucro no Grafana sobre a view lucro_por_produto_mes"
```

- [ ] **Pronto quando:** Painel mostra receita, anúncio, lucro e CPA por produto
- Implanta: Painel de lucro (Grafana) · Grafana

<a id="f16"></a>

## 32 · Teste do núcleo

Os três testes de ponta a ponta passam: daqui em diante, alimentar o sistema já faz tudo sozinho.

**Quando:** Semana 11 · jan/2027

### 32.1 Dev: mudar algo num repositório, commit assinado, push, CI verde

**Você** · 15 min

No **Ubuntu** (linha `alanmateus@...$`):

```bash
cd ~/dev/dev-setup && git commit --allow-empty -S -m 'teste: commit assinado' && git push && gh run watch && git log --show-signature -1
```

- [ ] **Pronto quando:** Selo Verified no commit e CI verde
- Implanta: Commits assinados (chave SSH) · GitHub Actions

### 32.2 Conteúdo: arquivo na entrada → peças na fila → aviso no Telegram

**Você** · 20 min

- **Fora do terminal:** Teste de ponta a ponta: um pedaço é no celular (aviso do Telegram) ou na plataforma (compra de teste).
- [ ] **Pronto quando:** Pasta nova na fila e mensagem no celular
- Implanta: Pipeline de conteúdo

### 32.3 Venda: compra de teste na Hotmart → linha na tabela vendas → painel de lucro

**Você** · 20 min

- **Fora do terminal:** Teste de ponta a ponta: um pedaço é no celular (aviso do Telegram) ou na plataforma (compra de teste).
- [ ] **Pronto quando:** Venda de teste no Grafana
- Implanta: Webhooks de venda · Painel de lucro (Grafana)

### 32.4 Rodar os três verificadores juntos

**Script** · 5 min

No **Ubuntu** (linha `alanmateus@...$`):

```bash
bash ~/dev/dev-setup/scripts/wsl/verificar.sh && bash ~/dev/dev-setup/scripts/wsl/verificar.sh --servicos && powershell.exe -ExecutionPolicy Bypass -File "$(wslpath -w ~/dev/dev-setup/scripts/windows/verificar.ps1)"
```

- [ ] **Pronto quando:** verificar.ps1, verificar.sh e verificar.sh --servicos sem FALTA
- Implanta: Verificadores · Roteiro de implantação

<a id="f17"></a>

## 33 · Primeira venda: o mini-curso no ar

A primeira venda real pela internet, com entrega, suporte, imposto e números no painel.

**Quando:** Semanas 12 a 15 · jan a fev/2027

### 33.1 Fechar o roteiro das 5 primeiras aulas do mini-curso a partir do acervo

**Claude com você** · 2 h 00 min

No **Ubuntu** (linha `alanmateus@...$`):

```bash
cd ~/dev/dev-setup && claude "Passo mc-roteiro do roteiro: Fechar o roteiro das 5 primeiras aulas do mini-curso a partir do acervo"
```

- [ ] **Pronto quando:** 5 aulas com objetivo, exemplo e exercício, no Obsidian
- **Oferta:** Mini-curso Lógica de Programação
- Implanta: Mini-curso Lógica de Programação

### 33.2 Gravar e editar as 5 aulas

**Você** · 10 h 00 min

- **Fora do terminal:** Conteúdo seu: gravar, escrever ou explicar o seu método.
- [ ] **Pronto quando:** 5 vídeos finais exportados no modelo do estúdio
- **Oferta:** Mini-curso Lógica de Programação
- Implanta: OBS Studio · DaVinci Resolve ou Kdenlive

### 33.3 Subir as aulas na Hotmart com preço e garantia de 7 dias

**Você** · 2 h 00 min

- **Fora do terminal:** Feito no painel da plataforma, que não tem terminal para isso.
- [ ] **Pronto quando:** Produto aprovado na Hotmart, com checkout funcionando
- A garantia de 7 dias é o direito de arrependimento do Código de Defesa do Consumidor para compra pela internet.
- **Oferta:** Mini-curso Lógica de Programação
- Implanta: Hotmart

### 33.4 Página de vendas no Instituto AMS: promessa, conteúdo, preço e garantia

**Claude com você** · 2 h 00 min

No **Ubuntu** (linha `alanmateus@...$`):

```bash
cd ~/dev/dev-setup && claude "Passo mc-pagina do roteiro: Página de vendas no Instituto AMS: promessa, conteúdo, preço e garantia"
```

- [ ] **Pronto quando:** Página no ar levando ao checkout, com Pixel e UTM
- Sem depoimento inventado: só depoimentos reais, com autorização, quando existirem.
- **Oferta:** Mini-curso Lógica de Programação
- Implanta: Instituto AMS · Tags de conversão (Pixel, Google…) · Padrão de UTM

### 33.5 Isca grátis (aula 1) com a sequência de e-mails que leva à venda

**Claude com você** · 1 h 30 min

No **Ubuntu** (linha `alanmateus@...$`):

```bash
cd ~/dev/dev-setup && claude "Passo mc-isca do roteiro: Isca grátis (aula 1) com a sequência de e-mails que leva à venda"
```

- [ ] **Pronto quando:** Inscrição de teste recebe os 5 e-mails e o último leva ao checkout
- **Oferta:** Mini-curso Lógica de Programação · Newsletter (patrocínio e vendas)
- Implanta: Isca grátis + sequência de e-mails · MailerLite

### 33.6 Abrir a pré-venda: lista de e-mail, Instagram, WhatsApp e LinkedIn

**Você** · 2 h 00 min

- **Fora do terminal:** Venda e relacionamento: falar com gente, publicar e atender. O Claude prepara textos e materiais; quem fala é você.
- [ ] **Pronto quando:** Lançamento publicado em todos os canais, com UTM
- **Oferta:** Mini-curso Lógica de Programação
- Implanta: Instagram · WhatsApp Business · LinkedIn

### 33.7 Primeira venda real: acesso, suporte, painel e carnê-leão

**Você** · 1 h 00 min

- **Fora do terminal:** Venda e relacionamento: falar com gente, publicar e atender. O Claude prepara textos e materiais; quem fala é você.
- [ ] **Pronto quando:** Venda paga, aluno com acesso, dúvida respondida em até 24 h, linha na tabela vendas e venda lançada no carnê-leão
- **Oferta:** Mini-curso Lógica de Programação
- Implanta: Hotmart · Webhooks de venda · Carnê-leão (Receita Federal)

### 33.8 Publicar o mini-curso também na Kiwify, Eduzz e Udemy

**Você** · 2 h 00 min

- **Fora do terminal:** Feito no painel da plataforma, que não tem terminal para isso.
- [ ] **Pronto quando:** Mini-curso à venda nas quatro plataformas
- **Oferta:** Mini-curso Lógica de Programação · Versões dos cursos na Udemy (português e inglês)
- Implanta: Kiwify · Eduzz · Udemy

<a id="f18"></a>

## 34 · Base dos sistemas AM

Um sistema novo nasce pronto: arquitetura, testes, login, observabilidade e deploy.

**Quando:** Junto dos Passos 4 a 6 da trilha de estudo (≈ mar a jun/2027): o modelo nasce no Passo 4 (API e login) e ganha testes e qualidade no Passo 6

### 34.1 Gerar o modelo de sistema com /novo-sistema-aura

**Claude com você** · 2 h 00 min

No **Ubuntu** (linha `alanmateus@...$`):

```bash
cd ~/dev/dev-setup && claude "Passo template-aura do roteiro: Gerar o modelo de sistema com /novo-sistema-aura"
```

- [ ] **Pronto quando:** Sistema exemplo sobe com 'dotnet run' e passa nos testes
- Clean Architecture + DDD, EF Core com Npgsql, multi-tenant com RLS, SignalR com Redis, OpenAPI com Scalar, Next.js com o Aura Design System e Storybook, testes com xUnit, Playwright e k6.
- Implanta: Clean Arch + DDD · EF Core + Npgsql · SignalR · Multi-tenant (RLS) · API ASP.NET Core · Next.js + Aura Design System · OpenAPI + Scalar · Storybook · PostgreSQL · Redis · Testes: xUnit, Playwright, k6

### 34.2 Ligar o login: Keycloak no dev e Entra ID na nuvem

**Claude com você** · 1 h 00 min

No **Ubuntu** (linha `alanmateus@...$`):

```bash
cd ~/dev/dev-setup && claude "Passo auth do roteiro: Ligar o login: Keycloak no dev e Entra ID na nuvem"
```

- [ ] **Pronto quando:** Usuário de teste entra e só vê os dados da própria empresa
- Implanta: Keycloak / Entra ID

### 34.3 Ligar a observabilidade do dev: .NET Aspire, OpenTelemetry, Prometheus, Seq, Mailpit e Caddy

**Claude com você** · 1 h 00 min

No **Ubuntu** (linha `alanmateus@...$`):

```bash
cd ~/dev/dev-setup && claude "Passo observabilidade-dev do roteiro: Ligar a observabilidade do dev: .NET Aspire, OpenTelemetry, Prometheus, Seq, Mailpit e Caddy"
```

- [ ] **Pronto quando:** Painel do Aspire mostra trace de uma requisição; e-mail de teste cai no Mailpit
- Implanta: .NET Aspire · OpenTelemetry · Prometheus · Seq (logs) · Mailpit · Caddy (proxy + HTTPS)

### 34.4 Criar o projeto no Sentry e ligar no modelo

**Você** · 20 min

- **Fora do terminal:** Cadastro no site ou app do serviço, com documento e confirmação no celular; nenhum deles deixa criar conta por terminal.
- [ ] **Pronto quando:** Erro de teste aparece no Sentry
- Implanta: Sentry (erros)

### 34.5 Ligar o SonarQube Cloud no repositório do modelo

**Você** · 20 min

- **Fora do terminal:** Cadastro no site ou app do serviço, com documento e confirmação no celular; nenhum deles deixa criar conta por terminal.
- [ ] **Pronto quando:** Nota de qualidade aparece no pull request
- O plano grátis cobre repositório público; confira o limite para privado antes de ligar.
- Implanta: SonarQube Cloud

### 34.6 Publicar a imagem Docker da API no GHCR pelo CI

**Claude com você** · 30 min

No **Ubuntu** (linha `alanmateus@...$`):

```bash
cd ~/dev/dev-setup && claude "Passo ghcr do roteiro: Publicar a imagem Docker da API no GHCR pelo CI"
```

- [ ] **Pronto quando:** Imagem com a tag do commit aparece nos pacotes do GitHub
- Implanta: GHCR (imagens)

### 34.7 Separar o que do modelo pode virar template à venda

**Você** · 30 min

- **Fora do terminal:** Decisão sua; os números e as opções já estão no roteiro e no portfólio.
- [ ] **Pronto quando:** Lista de templates no portfólio de ofertas
- **Oferta:** Templates e código-fonte
- Implanta: Templates e código-fonte

### 34.8 Candidatar-se às vagas de dev .NET com GitHub, LinkedIn e site prontos — quando o Passo 8 da trilha de estudo estiver feito (≈ jul a dez/2027)

**Você** · 2 h 00 min

- **Fora do terminal:** Venda e relacionamento: falar com gente, publicar e atender. O Claude prepara textos e materiais; quem fala é você.
- [ ] **Pronto quando:** 10 candidaturas enviadas com o portfólio do sistema exemplo
- Implanta: Recrutadores

<a id="f19"></a>

## 35 · Nuvem e deploy

As contas de nuvem criadas por código, com custo sob controle.

**Quando:** Com o Passo 5 da trilha de estudo (≈ abr a jun/2027) para a conta e o deploy do sistema exemplo; o deploy de produção do AM Kaixara é o Passo 10 (≈ 2028)

### 35.1 Instalar Azure CLI, Terraform, Vercel CLI e Wrangler

**Script** · 15 min

No **Ubuntu** (linha `alanmateus@...$`):

```bash
bash scripts/wsl/nuvem.sh
```

- [ ] **Pronto quando:** Termina com 'Pronto'; verificar.sh mostra as quatro ferramentas
- Implanta: Azure CLI · AWS CLI · Terraform

### 35.2 Criar a conta Azure com alerta de orçamento

**Você** · 30 min

No **Ubuntu** (linha `alanmateus@...$`):

```bash
az login && az account show
```

- **Fora do terminal:** Cadastro no site ou app do serviço, com documento e confirmação no celular; nenhum deles deixa criar conta por terminal.
- [ ] **Pronto quando:** 'az login' entra e o alerta de gasto está ligado
- Ligue o alerta antes de criar qualquer recurso. O Microsoft Learn do conector ajuda a escolher o serviço mais barato.
- Implanta: Azure

### 35.3 Criar com Terraform o grupo de recursos, o banco e o Key Vault do primeiro sistema

**Claude com você** · 1 h 30 min

No **Ubuntu** (linha `alanmateus@...$`):

```bash
cd ~/dev/dev-setup && claude "Passo terraform-base do roteiro: Criar com Terraform o grupo de recursos, o banco e o Key Vault do primeiro sistema"
```

- [ ] **Pronto quando:** 'terraform plan' sem diferenças depois do apply
- Implanta: Terraform · Azure

### 35.4 Criar o armazenamento de arquivos (R2 da Cloudflare ou Blob)

**Claude com você** · 30 min

No **Ubuntu** (linha `alanmateus@...$`):

```bash
cd ~/dev/dev-setup && claude "Passo arquivos-nuvem do roteiro: Criar o armazenamento de arquivos (R2 da Cloudflare ou Blob)"
```

- [ ] **Pronto quando:** Upload de teste pelo sistema exemplo
- Implanta: Armazenamento de arquivos (Blob/R2)

### 35.5 Configurar o e-mail transacional (Resend) com o domínio verificado

**Você** · 30 min

- **Fora do terminal:** Cadastro no site ou app do serviço, com documento e confirmação no celular; nenhum deles deixa criar conta por terminal.
- [ ] **Pronto quando:** E-mail de confirmação de conta chega na caixa de entrada, não no spam
- Implanta: E-mail transacional (Resend, SES…)

### 35.6 Fazer o primeiro deploy do sistema exemplo

**Claude com você** · 1 h 00 min

No **Ubuntu** (linha `alanmateus@...$`):

```bash
cd ~/dev/dev-setup && claude "Passo deploy-teste do roteiro: Fazer o primeiro deploy do sistema exemplo"
```

- [ ] **Pronto quando:** Sistema no ar com HTTPS, login e erro de teste no Sentry
- Implanta: Vercel · Azure · Cloudflare (DNS, Pages, e-mail)

### 35.7 Criar o aura-status: painel de repositórios, backup e Dependabot

**Claude com você** · 2 h 00 min

No **Ubuntu** (linha `alanmateus@...$`):

```bash
cd ~/dev/dev-setup && claude "Passo aura-status do roteiro: Criar o aura-status: painel de repositórios, backup e Dependabot"
```

- [ ] **Pronto quando:** Painel mostra o estado de todos os repositórios
- Implanta: aura-status

<a id="f20"></a>

## 36 · Editora

O livro sai de um repositório com CI, pronto para virar PDF, EPUB e impressão.

**Quando:** Quando o capítulo 1 estiver pronto

**Começa quando:** O capítulo 1 e o seu modelo de criação prontos

### 36.1 Entregar o seu modelo de criação e o seu método passo a passo

**Você** · 2 h 00 min

- **Fora do terminal:** Conteúdo seu: gravar, escrever ou explicar o seu método.
- [ ] **Pronto quando:** metodo.yaml com cada etapa, entrada, saída e critério de conclusão; template de capítulo pronto
- Implanta: Seu modelo de criação · Seu método (metodo.yaml) · Projeto do capítulo · Mapa de pré-requisitos

### 36.2 Criar o repositório do livro com fonte única, classe LaTeX, exercícios em YAML e CI

**Claude com você** · 2 h 00 min

No **Ubuntu** (linha `alanmateus@...$`):

```bash
cd ~/dev/dev-setup && claude "Passo livro-repo do roteiro: Criar o repositório do livro com fonte única, classe LaTeX, exercícios em YAML e CI"
```

- [ ] **Pronto quando:** Um push gera PDF, EPUB e o gabarito sem erro
- Depende do capítulo 1 e do seu modelo. O conteúdo é seu; nada de material de terceiros.
- **Precisa:** conteúdo seu pronto (livro, capítulo)
- Implanta: Repositório do livro · Fonte única (Markdown + Pandoc) · Classe LaTeX do livro · Exercícios em YAML · Pipeline do livro (CI) · Revisão automática (LanguageTool, Vale) · Errata e edições · Livro Lógica e Máquina

### 36.3 Construir o pipeline de imagens do livro: busca nos acervos, filtro de licença, folha de contato e créditos

**Claude com você** · 4 h 00 min

No **Ubuntu** (linha `alanmateus@...$`):

```bash
cd ~/dev/dev-setup && claude "Passo editora-imagens do roteiro: Construir o pipeline de imagens do livro: busca nos acervos, filtro de licença, folha de contato e créditos"
```

- [ ] **Pronto quando:** Uma figura do capítulo 1 sai com licença conferida, ficha e crédito; o build falha se faltar ficha
- Implanta: Acervos de imagens (APIs) · Busca automática de imagens · Filtro de licença e fichas · Folha de contato (artefato) · Créditos e legendas

### 36.4 Figuras, tabelas e texto alternativo gerados por código

**Claude com você** · 3 h 00 min

No **Ubuntu** (linha `alanmateus@...$`):

```bash
cd ~/dev/dev-setup && claude "Passo editora-figuras do roteiro: Figuras, tabelas e texto alternativo gerados por código"
```

- [ ] **Pronto quando:** Gráficos e tabelas do capítulo 1 gerados no build, com texto alternativo revisado por você
- Implanta: Figuras por código (Matplotlib…) · Geradores de tabelas · Texto alternativo

### 36.5 Criar os agentes da editora: revisor técnico, gabarito, leitor iniciante e consistência

**Claude com você** · 3 h 00 min

No **Ubuntu** (linha `alanmateus@...$`):

```bash
cd ~/dev/dev-setup && claude "Passo editora-agentes do roteiro: Criar os agentes da editora: revisor técnico, gabarito, leitor iniciante e consistência"
```

- [ ] **Pronto quando:** Os agentes apontam problemas reais no capítulo 1 e você corrige
- Implanta: Agentes da editora

### 36.6 Montar a matriz de editais e o quadro de referências

**Claude com você** · 1 h 00 min

No **Ubuntu** (linha `alanmateus@...$`):

```bash
cd ~/dev/dev-setup && claude "Passo editais do roteiro: Montar a matriz de editais e o quadro de referências"
```

- [ ] **Pronto quando:** Cada tópico dos editais ligado a um capítulo; lacunas listadas
- Implanta: Matriz de editais · Quadro de referências

### 36.7 Definir o selo Editora AMS Silva (nome, logo e uso no CPF)

**Você** · 30 min

- **Fora do terminal:** Decisão sua; os números e as opções já estão no roteiro e no portfólio.
- [ ] **Pronto quando:** Logo aprovado e aplicado na classe LaTeX
- Implanta: Selo Editora AMS Silva

### 36.8 Comprar os ISBNs na CBL e pedir a ficha catalográfica

**Você** · 1 h 00 min

- **Fora do terminal:** Órgão público, contador ou entidade: feito no site do governo ou com atendimento.
- [ ] **Pronto quando:** ISBN do impresso e do ebook, código de barras e ficha no verso da folha de rosto
- **Precisa:** pagar um serviço, conteúdo seu pronto (livro, capítulo)
- Implanta: ISBN + código de barras (CBL) · Ficha catalográfica

### 36.9 Escolher 3 a 5 leitores beta e um revisor técnico

**Você** · 30 min

- **Fora do terminal:** Decisão sua; os números e as opções já estão no roteiro e no portfólio.
- [ ] **Pronto quando:** Nomes confirmados e formulário de retorno pronto
- **Precisa:** conteúdo seu pronto (livro, capítulo)
- Implanta: Leitores beta e revisão técnica

### 36.10 Criar a conta no Amazon KDP e cadastrar o livro em rascunho

**Você** · 1 h 00 min

- **Fora do terminal:** Cadastro no site ou app do serviço, com documento e confirmação no celular; nenhum deles deixa criar conta por terminal.
- [ ] **Pronto quando:** Livro em rascunho com capa, preço e prévia conferida
- **Precisa:** conteúdo seu pronto (livro, capítulo)
- **Oferta:** Livro Lógica e Máquina
- Implanta: Amazon KDP

### 36.11 Enviar o depósito legal à Biblioteca Nacional até 30 dias depois de publicar

**Você** · 30 min

- **Fora do terminal:** Órgão público, contador ou entidade: feito no site do governo ou com atendimento.
- [ ] **Pronto quando:** Comprovante de envio guardado
- **Precisa:** conteúdo seu pronto (livro, capítulo)
- Implanta: Depósito legal

<a id="f21"></a>

## 37 · Dados, IA e pendrives

O laboratório de dados e de treino no ar, um modelo seu rodando no Ollama e os pendrives de Kali e Arch dando boot.

**Quando:** Pendrives, GPU e laboratório a partir da semana 2; Zoomcamp, dbt e Airflow junto do IA2 da Trilha de Dados e IA do vault (depois do Passo 8, ≈ 2028); dataset e treino do 8B junto do IA6 (≈ 2029)

### 37.1 Gravar o pendrive do Kali com persistência criptografada

**Você** · 1 h 30 min

No **PowerShell** do Windows (linha `PS C:\>`):

```powershell
winget install --id Rufus.Rufus -e
```

- [ ] **Pronto quando:** O Kali abre pelo F12 e um arquivo salvo continua lá depois de reiniciar
- Siga kali.org/docs/usb. Antes do primeiro boot: suspenda o BitLocker, desligue o Secure Boot e, ao voltar ao Windows, religue o Secure Boot e reative o BitLocker (veja Secure Boot e BitLocker no mapa). Só contra alvos seus ou autorizados.
- Implanta: Pendrive Kali (persistência) · Rufus (grava pendrives)

### 37.2 Instalar o Arch num pendrive rápido ou SSD USB, pelo guia oficial

**Você** · 3 h 00 min

- **Fora do terminal:** O Rufus grava o pendrive pela janela dele; a instalação do Arch é no terminal, mas no boot do pendrive, seguindo o guia oficial.
- [ ] **Pronto quando:** O Arch portátil dá boot e abre o terminal com os seus dotfiles
- Use um pendrive para a ISO e outro (64 GB ou mais, USB 3) ou um SSD USB como disco do sistema. Mesmo cuidado com Secure Boot e BitLocker.
- **Precisa:** comprar algo
- Implanta: Pendrive Arch (instalação portátil)

### 37.3 Conferir a GPU dentro do Ubuntu

**Script** · 5 min

No **Ubuntu** (linha `alanmateus@...$`):

```bash
nvidia-smi
```

- [ ] **Pronto quando:** Aparece a GTX 1650 com o driver do Windows
- Implanta: PyTorch + CUDA (WSL2)

### 37.4 Montar o laboratório de dados e de IA

**Script** · 30 min

No **Ubuntu** (linha `alanmateus@...$`):

```bash
bash scripts/wsl/lab-ia.sh
```

- [ ] **Pronto quando:** Termina com 'Pronto' e mostra a GPU vista pelo PyTorch
- Implanta: Python de dados (Polars, Jupyter) · DuckDB + Parquet · Spark (PySpark) · PyTorch + CUDA (WSL2) · MLflow (experimentos) · llama.cpp (GGUF)

### 37.5 Rodar um modelo 8B no Ollama com parte na GPU

**Você** · 15 min

No **Ubuntu** (linha `alanmateus@...$`):

```bash
ollama run llama3.1:8b
```

- [ ] **Pronto quando:** 'ollama ps' mostra o modelo dividido entre CPU e GPU e ele responde
- Mais lento que um 3B ou 4B, que cabem inteiros na placa. Use o 8B quando a qualidade importar mais que a velocidade.
- Implanta: Modelos locais: Qwen · Gemma · Llama · Ollama

### 37.6 Fazer o Data Engineering Zoomcamp e os cursos de IA, um módulo por semana

**Você** · 1 h 00 min

- **Fora do terminal:** Estudo: assistir, praticar e anotar.
- [ ] **Pronto quando:** Módulo 1 entregue no GitHub e anotado no Obsidian
- O tempo é só para começar; o curso leva 10 semanas. Para a IA vão as suas anotações, nunca o material do curso.
- Implanta: Zoomcamp de dados + cursos de IA

### 37.7 Criar o projeto dbt sobre o banco de métricas

**Claude com você** · 1 h 30 min

No **Ubuntu** (linha `alanmateus@...$`):

```bash
cd ~/dev/dev-setup && claude "Passo dbt-metricas do roteiro: Criar o projeto dbt sobre o banco de métricas"
```

- [ ] **Pronto quando:** 'dbt build' verde e o painel de lucro lendo os modelos
- Implanta: dbt Core

### 37.8 Subir o Airflow e agendar o dbt todo dia

**Claude com você** · 1 h 30 min

No **Ubuntu** (linha `alanmateus@...$`):

```bash
cd ~/dev/dev-setup && claude "Passo airflow do roteiro: Subir o Airflow e agendar o dbt todo dia"
```

- [ ] **Pronto quando:** A rotina diária aparece verde no Airflow por 3 dias seguidos
- Implanta: Airflow (orquestração)

### 37.9 Criar as contas do Hugging Face e do Kaggle (e do RunPod, só se precisar)

**Você** · 30 min

- **Fora do terminal:** Cadastro no site ou app do serviço, com documento e confirmação no celular; nenhum deles deixa criar conta por terminal.
- [ ] **Pronto quando:** Token do Hugging Face no KeePassXC; Kaggle com telefone verificado para liberar a GPU
- No RunPod, só crédito pré-pago. Nunca ponha token em notebook público.
- Implanta: Hugging Face (modelos e Hub) · Kaggle · Colab (GPU grátis) · GPU por hora (RunPod e afins)

### 37.10 Montar o primeiro dataset só com conteúdo seu

**Claude com você** · 2 h 00 min

No **Ubuntu** (linha `alanmateus@...$`):

```bash
cd ~/dev/dev-setup && claude "Passo dataset do roteiro: Montar o primeiro dataset só com conteúdo seu"
```

- [ ] **Pronto quando:** Algumas centenas de pares de pergunta e resposta revisados por você, com conjunto de teste separado
- Fontes: suas notas, exercícios, livro e aulas que você gravou. Nada de cursos de terceiros; nada de dados de alunos sem consentimento.
- Implanta: Seus datasets (só conteúdo seu) · Avaliação dos modelos

### 37.11 Primeiro fine-tuning QLoRA de um 8B no Kaggle

**Claude com você** · 3 h 00 min

No **Ubuntu** (linha `alanmateus@...$`):

```bash
cd ~/dev/dev-setup && claude "Passo fine-tune do roteiro: Primeiro fine-tuning QLoRA de um 8B no Kaggle"
```

- [ ] **Pronto quando:** Adaptador salvo no Hugging Face privado e o treino registrado no MLflow
- Implanta: Unsloth (QLoRA) · Kaggle · Colab (GPU grátis)

### 37.12 Avaliar contra o modelo base e levar o seu modelo para o Ollama

**Claude com você** · 1 h 30 min

No **Ubuntu** (linha `alanmateus@...$`):

```bash
cd ~/dev/dev-setup && claude "Passo modelo-no-ollama do roteiro: Avaliar contra o modelo base e levar o seu modelo para o Ollama"
```

- [ ] **Pronto quando:** O seu modelo ganha do base no conjunto de teste e responde no Ollama do notebook
- Implanta: Avaliação dos modelos · llama.cpp (GGUF) · Ollama

<a id="f22"></a>

## 38 · Mais ofertas, uma por vez

Cada oferta do portfólio entra na esteira na ordem da pontuação: uma em construção e uma em validação por vez.

**Quando:** Fev a dez/2027, uma oferta por vez

**Começa quando:** A primeira venda do mini-curso aconteceu

### 38.1 Página 'meu setup' com links de afiliado

**Claude com você** · 1 h 30 min

No **Ubuntu** (linha `alanmateus@...$`):

```bash
cd ~/dev/dev-setup && claude "Passo of-meu-setup do roteiro: Página 'meu setup' com links de afiliado"
```

- [ ] **Pronto quando:** Página publicada com links marcados com UTM
- **Oferta:** Afiliados (ferramentas, livros, equipamentos que você usa)
- Implanta: Site pessoal + blog (Jekyll) · Afiliados (Amazon, Hotmart…)

### 38.2 Pôr no Catálogo do HTML a chamada para o mini-curso e para a newsletter

**Claude com você** · 30 min

No **Ubuntu** (linha `alanmateus@...$`):

```bash
cd ~/dev/dev-setup && claude "Passo of-catalogo do roteiro: Pôr no Catálogo do HTML a chamada para o mini-curso e para a newsletter"
```

- [ ] **Pronto quando:** Chamadas no ar, medidas por UTM
- **Oferta:** Catálogo do HTML (gratuito)
- Implanta: Catálogo do HTML

### 38.3 Kit de aulas prontas para professores: uma disciplina que você já leciona

**Você** · 10 h 00 min

- **Fora do terminal:** Venda e relacionamento: falar com gente, publicar e atender. O Claude prepara textos e materiais; quem fala é você.
- [ ] **Pronto quando:** Kit de 1 disciplina (planos, slides, avaliações) à venda
- Material feito para a escola: reescreva do zero, no seu tempo e sem a identidade da escola, ou confirme os direitos.
- **Oferta:** Pacote de aulas prontas para professores de informática
- Implanta: Acervo (seus documentos) · Hotmart

### 38.4 Vender a planilha do Caixa da Casa antes de construir o AM Rendara

**Você** · 3 h 00 min

- **Fora do terminal:** Venda e relacionamento: falar com gente, publicar e atender. O Claude prepara textos e materiais; quem fala é você.
- [ ] **Pronto quando:** 10 planilhas vendidas
- **Oferta:** AM Rendara (finanças), começando pela planilha
- Implanta: Caixa da Casa / AM Rendara · Hotmart

### 38.5 Automação com IA para pequenos negócios: 1 implantação grátis em troca de caso

**Claude com você** · 10 h 00 min

No **Ubuntu** (linha `alanmateus@...$`):

```bash
cd ~/dev/dev-setup && claude "Passo of-automacao do roteiro: Automação com IA para pequenos negócios: 1 implantação grátis em troca de caso"
```

- [ ] **Pronto quando:** Um negócio usando a automação e um caso escrito com autorização
- **Oferta:** Automação com IA para pequenos negócios (WhatsApp, n8n, agenda)
- Implanta: n8n · Agente atendente (WhatsApp)

### 38.6 Banco de questões para concursos: 50 questões comentadas grátis para medir a procura

**Você** · 8 h 00 min

- **Fora do terminal:** Venda e relacionamento: falar com gente, publicar e atender. O Claude prepara textos e materiais; quem fala é você.
- [ ] **Pronto quando:** 50 questões publicadas e a procura medida
- **Oferta:** Banco de questões de TI para concursos (PF, PRF, Forças Armadas)
- Implanta: Exercícios em YAML

### 38.7 Baralhos Anki de TI e concursos: o primeiro, do capítulo 1

**Você** · 3 h 00 min

- **Fora do terminal:** Venda e relacionamento: falar com gente, publicar e atender. O Claude prepara textos e materiais; quem fala é você.
- [ ] **Pronto quando:** Primeiro baralho à venda
- **Oferta:** Baralhos Anki de TI e concursos
- Implanta: Anki · Exercícios em YAML

### 38.8 Newsletter com patrocínio e vendas

**Você** · 2 h 00 min

- **Fora do terminal:** Venda e relacionamento: falar com gente, publicar e atender. O Claude prepara textos e materiais; quem fala é você.
- [ ] **Pronto quando:** Edição semanal por 8 semanas e o primeiro patrocinador
- **Oferta:** Newsletter (patrocínio e vendas)
- Implanta: MailerLite

### 38.9 Presença digital para comércio local, oferecida a 5 clientes de sites

**Você** · 4 h 00 min

- **Fora do terminal:** Venda e relacionamento: falar com gente, publicar e atender. O Claude prepara textos e materiais; quem fala é você.
- [ ] **Pronto quando:** Primeiro cliente mensal
- **Oferta:** Presença digital para comércio local (Google Perfil, redes, avaliações)
- Implanta: Google Perfil da Empresa · Sites para pequenas empresas

### 38.10 Sites: 3 pacotes fixos com preço público

**Você** · 3 h 00 min

- **Fora do terminal:** Venda e relacionamento: falar com gente, publicar e atender. O Claude prepara textos e materiais; quem fala é você.
- [ ] **Pronto quando:** Pacotes publicados e primeiro cliente fechado
- **Oferta:** Sites e lojas para pequenas empresas
- Implanta: Sites para pequenas empresas · Hostinger (clientes WP)

### 38.11 Suporte remoto com plano mensal para empresas

**Você** · 4 h 00 min

- **Fora do terminal:** Venda e relacionamento: falar com gente, publicar e atender. O Claude prepara textos e materiais; quem fala é você.
- [ ] **Pronto quando:** 3 empresas no plano mensal
- **Oferta:** Suporte remoto e planos mensais para empresas
- Implanta: Tailscale (VPN)

### 38.12 Implantação de ficha técnica e engenharia de cardápio para restaurantes

**Você** · 8 h 00 min

- **Fora do terminal:** Venda e relacionamento: falar com gente, publicar e atender. O Claude prepara textos e materiais; quem fala é você.
- [ ] **Pronto quando:** Um estudo de caso, com autorização do dono
- **Oferta:** Implantação de ficha técnica e engenharia de cardápio
- Implanta: AM Kaixara (PDV e cardápio)

### 38.13 AM Mentor: banco de exercícios com correção, começando pelo capítulo 1

**Claude com você** · 20 h 00 min

No **Ubuntu** (linha `alanmateus@...$`):

```bash
cd ~/dev/dev-setup && claude "Passo of-ammentor do roteiro: AM Mentor: banco de exercícios com correção, começando pelo capítulo 1"
```

- [ ] **Pronto quando:** Primeiros alunos usando
- **Oferta:** AM Mentor: banco de exercícios com correção
- Implanta: Exercícios em YAML

### 38.14 Canais sem rosto: 3 vídeos por semana por 8 semanas e medir

**Você** · 20 h 00 min

- **Fora do terminal:** Venda e relacionamento: falar com gente, publicar e atender. O Claude prepara textos e materiais; quem fala é você.
- [ ] **Pronto quando:** 24 vídeos publicados e o resultado medido
- **Oferta:** Canais sem rosto (YouTube, TikTok, Instagram, Facebook)
- Implanta: Agente editor de conteúdo · YouTube

### 38.15 Comunidade paga do Instituto AMS

**Você** · 4 h 00 min

- **Fora do terminal:** Venda e relacionamento: falar com gente, publicar e atender. O Claude prepara textos e materiais; quem fala é você.
- [ ] **Pronto quando:** Comunidade aberta com os primeiros assinantes
- Só com 200 alunos pagantes.
- **Oferta:** Comunidade paga do Instituto AMS
- Implanta: Comunidade (Discord ou grupo)

### 38.16 Oficinas de robótica e programação para escolas: plano de 8 encontros

**Você** · 10 h 00 min

- **Fora do terminal:** Venda e relacionamento: falar com gente, publicar e atender. O Claude prepara textos e materiais; quem fala é você.
- [ ] **Pronto quando:** Primeira escola contratando
- **Oferta:** Oficinas de robótica e programação para escolas
- Implanta: Arduino · ESP32 · Pi · Arduino IDE 2

### 38.17 Sistemas sob encomenda, com 50% de entrada

**Você** · 4 h 00 min

- **Fora do terminal:** Venda e relacionamento: falar com gente, publicar e atender. O Claude prepara textos e materiais; quem fala é você.
- [ ] **Pronto quando:** Primeiro contrato assinado
- **Oferta:** Sistemas sob encomenda
- Implanta: API ASP.NET Core · Next.js + Aura Design System

### 38.18 Aula de sushi e sushiman para eventos: 2 eventos de teste

**Você** · 4 h 00 min

- **Fora do terminal:** Venda e relacionamento: falar com gente, publicar e atender. O Claude prepara textos e materiais; quem fala é você.
- [ ] **Pronto quando:** 2 eventos pagos, com as regras sanitárias conferidas
- **Oferta:** Aula de sushi e sushiman para eventos
- Implanta: Agenda online (Cal.com)

### 38.19 Workshop presencial para pequenos empresários: piloto com 10 vagas

**Você** · 8 h 00 min

- **Fora do terminal:** Venda e relacionamento: falar com gente, publicar e atender. O Claude prepara textos e materiais; quem fala é você.
- [ ] **Pronto quando:** Piloto realizado com 10 inscritos pagantes
- **Oferta:** Workshops presenciais para pequenos empresários (IA, planilhas, presença digital)
- Implanta: Agenda online (Cal.com) · Mercado Pago

### 38.20 Revisar a cada trimestre as ofertas pausadas (AM Taskoro)

**Você** · 30 min

- **Fora do terminal:** Decisão sua; os números e as opções já estão no roteiro e no portfólio.
- [ ] **Pronto quando:** Decisão anotada: retomar ou manter pausada
- **Oferta:** AM Taskoro (gestão de projetos ágeis)
- Implanta: Portfólio de ofertas

### 38.21 Fila de produtos digitais (Fábrica para professores, Setup profissional, templates e outros)

**Você** · 30 min

- **Fora do terminal:** Entra só quando uma renda ativa passar no portão (3 meses se pagando). A ordem é o ranking de facilidade do portfólio.
- [ ] **Pronto quando:** Cada uma ativada na ordem, uma de cada vez
- **Oferta:** Fábrica de documentos para professores de MG (assinatura) · Setup profissional (curso, template e configuração remota) · Templates Next.js/Tailwind em inglês · Blocos e kits de componentes de interface · Plugin WordPress com versão Pro · Templates de automação n8n · Cursos em plataformas que pagam royalties (Alura, Rocketseat, Domestika) · Cursos dublados por IA em inglês e espanhol (só a sua voz) · Licença do ByteSDCoin para escolas (sem aposta) · Camisetas e canecas sob demanda (dev e professor)

### 38.22 Fila de serviços que pagam bem por hora (conteudista, questões, ERP e outros)

**Você** · 30 min

- **Fora do terminal:** Entra só quando uma renda ativa passar no portão (3 meses se pagando). A ordem é o ranking de facilidade do portfólio.
- [ ] **Pronto quando:** Cada uma ativada na ordem, uma de cada vez
- **Oferta:** Professor conteudista EAD · Elaboração e revisão de questões · Formatação ABNT de TCC (só formatar e revisar) · Segurança digital para pequenas empresas · Freela internacional em dólar (Upwork) · Parceiro de ERP (Bling, Tiny, Omie): implantação e comissão · Português para estrangeiros (Preply, italki) · Recuperação de dados (intermediação com laboratório)

### 38.23 Fila da AMtech Economia (plano de negócios, BPO financeiro, crédito e editais, mentoria, modelos, calculadoras)

**Você** · 30 min

- **Fora do terminal:** Entra só quando uma renda ativa passar no portão (3 meses se pagando). A ordem é o ranking de facilidade do portfólio.
- [ ] **Pronto quando:** Cada uma ativada na ordem, uma de cada vez
- **Oferta:** Plano de negócios e viabilidade financeira para quem vai abrir empresa · BPO financeiro para pequenas empresas (contas, conciliação, fluxo de caixa) · Captação de crédito e editais para pequenos negócios (Pronampe, BDMG, Sebrae, FAPEMIG) · Mentoria de organização financeira e palestras em empresas (sem recomendar ativos) · Modelos financeiros para empresas (fluxo de caixa, DRE gerencial, precificação, valuation simples) · Calculadoras financeiras online (CLT x PJ, MEI, financiamento, independência financeira)

<a id="f23"></a>

## 39 · Marketing pago e crescimento

Pôr dinheiro em anúncio só quando a venda orgânica provou a oferta.

**Quando:** A partir de fev/2027

**Começa quando:** O mini-curso vendeu sem anúncio (por exemplo, 10 vendas) e o painel de lucro está no ar

### 39.1 Primeira campanha na Meta com orçamento de teste

**Você** · 2 h 00 min

- **Fora do terminal:** Campanha montada no painel de anúncios de cada rede, com cartão.
- [ ] **Pronto quando:** Campanha com CPA abaixo do de empate por 2 semanas
- **Precisa:** pagar um serviço
- Implanta: Meta Ads (Instagram, Facebook)

### 39.2 Google e YouTube Ads, depois TikTok Ads

**Você** · 3 h 00 min

- **Fora do terminal:** Campanha montada no painel de anúncios de cada rede, com cartão.
- [ ] **Pronto quando:** Cada canal com a primeira campanha medida no painel
- **Precisa:** pagar um serviço
- Implanta: Google e YouTube Ads · TikTok Ads

### 39.3 Kwai, Pinterest, LinkedIn, Spotify e mídia nativa, um por vez

**Você** · 4 h 00 min

- **Fora do terminal:** Campanha montada no painel de anúncios de cada rede, com cartão.
- [ ] **Pronto quando:** Cada canal testado e mantido ou cortado pelas regras
- **Precisa:** pagar um serviço
- Implanta: Kwai Ads · Pinterest Ads · LinkedIn Ads · Spotify Ad Studio · Mídia nativa (Taboola, Outbrain)

### 39.4 Influenciadores e newsletters parceiras com cupom

**Você** · 2 h 00 min

- **Fora do terminal:** Venda e relacionamento: falar com gente, publicar e atender. O Claude prepara textos e materiais; quem fala é você.
- [ ] **Pronto quando:** Primeira parceria medida por cupom e UTM
- **Precisa:** pagar um serviço
- Implanta: Influenciadores e newsletters

### 39.5 Abrir o programa de afiliados do mini-curso

**Você** · 1 h 00 min

- **Fora do terminal:** Venda e relacionamento: falar com gente, publicar e atender. O Claude prepara textos e materiais; quem fala é você.
- [ ] **Pronto quando:** Primeiro afiliado vendendo
- Implanta: Programa de afiliados

### 39.6 Ligar o algoritmo de horário com 3 meses de dados de publicação

**Claude com você** · 2 h 00 min

No **Ubuntu** (linha `alanmateus@...$`):

```bash
cd ~/dev/dev-setup && claude "Passo horario do roteiro: Ligar o algoritmo de horário com 3 meses de dados de publicação"
```

- [ ] **Pronto quando:** 80% dos posts nas melhores faixas, 20% testando
- Implanta: Algoritmo de horário

### 39.7 Canal build in public: um vídeo por semana das decisões reais

**Você** · 1 h 00 min

- **Fora do terminal:** Venda e relacionamento: falar com gente, publicar e atender. O Claude prepara textos e materiais; quem fala é você.
- [ ] **Pronto quando:** 4 vídeos seguidos publicados
- **Oferta:** Canal com rosto: construindo o Grupo AMtech em público
- Implanta: Canal build in public

### 39.8 Dublar os melhores vídeos para outros idiomas

**Você** · 2 h 00 min

- **Fora do terminal:** Conteúdo seu: gravar, escrever ou explicar o seu método.
- [ ] **Pronto quando:** Um vídeo com faixa de áudio em inglês ou espanhol
- **Precisa:** pagar um serviço
- Implanta: Dublagem (YouTube + ElevenLabs)

### 39.9 Membros do YouTube quando o canal for elegível

**Você** · 30 min

- **Fora do terminal:** Venda e relacionamento: falar com gente, publicar e atender. O Claude prepara textos e materiais; quem fala é você.
- [ ] **Pronto quando:** Assinatura de membros ativa
- **Oferta:** Monetização das plataformas (YouTube, Instagram)
- Implanta: YouTube (membros)

### 39.10 Primeira formação completa (TI, Matemática ou Finanças)

**Você** · 20 h 00 min

- **Fora do terminal:** Conteúdo seu: gravar, escrever ou explicar o seu método.
- [ ] **Pronto quando:** Formação gravada e à venda
- **Oferta:** Formação Téc. em Desenvolvimento de Sistemas (13 disciplinas) · Formação em Matemática · Curso de finanças pessoais (conteúdo próprio)
- Implanta: Formações (TI, Matemática, Finanças)

<a id="f24"></a>

## 40 · Linux nativo e laboratório completo

Arch com boot próprio, VMs de laboratório e a segurança física em dia.

**Quando:** 2027, conforme cada compra

### 40.1 Instalar o 2º NVMe e o Arch + Omarchy com boot próprio

**Você** · 5 h 00 min

- **Fora do terminal:** Compra e montagem física (ou instalação por janela de VM); depois os verificadores conferem pelo terminal.
- [ ] **Pronto quando:** Escolha entre Windows e Arch ao ligar, cada um no seu disco
- **Precisa:** comprar algo
- Implanta: 2º NVMe (1–4 TB) · Arch + Omarchy (2º NVMe) · Gerenciador de boot

### 40.2 Aprender o Neovim aos poucos

**Você** · 5 h 00 min

No **Ubuntu** (linha `alanmateus@...$`):

```bash
sudo apt install -y neovim && nvim +Tutor
```

- [ ] **Pronto quando:** Uma semana editando só no Neovim
- Implanta: Neovim

### 40.3 Montar as VMs do laboratório: Kali, Arch, Ubuntu Server, Windows Server e Rocky

**Você** · 5 h 00 min

- **Fora do terminal:** Compra e montagem física (ou instalação por janela de VM); depois os verificadores conferem pelo terminal.
- [ ] **Pronto quando:** Duas VMs numa rede isolada, atacante e alvo
- Implanta: VMs: Kali · Arch · Servidores

### 40.4 SSD SATA na baia livre para as VMs

**Você** · 1 h 00 min

- **Fora do terminal:** Compra e montagem física (ou instalação por janela de VM); depois os verificadores conferem pelo terminal.
- [ ] **Pronto quando:** VMs rodando do SSD novo
- **Precisa:** comprar algo
- Implanta: SSD SATA 2,5"

### 40.5 Chave física no GitHub, Google e Microsoft

**Você** · 1 h 00 min

- **Fora do terminal:** Compra e montagem física (ou instalação por janela de VM); depois os verificadores conferem pelo terminal.
- [ ] **Pronto quando:** Login com a chave nas três contas
- **Precisa:** comprar algo
- Implanta: Chave física (YubiKey)

### 40.6 Microfone e câmera

**Você** · 1 h 00 min

- **Fora do terminal:** Compra e montagem física (ou instalação por janela de VM); depois os verificadores conferem pelo terminal.
- [ ] **Pronto quando:** Gravação de teste com áudio limpo sem pós-produção
- **Precisa:** comprar algo
- Implanta: Microfone + câmera

<a id="f25"></a>

## 41 · IA dentro dos sistemas AM

Busca e assistente com os seus dados dentro de um sistema AM.

**Quando:** Depois do Passo 9 e do IA0 da Trilha de Dados e IA (≈ 2028), junto do IA5

### 41.1 RAG com pgvector dentro do primeiro sistema AM

**Claude com você** · 8 h 00 min

No **Ubuntu** (linha `alanmateus@...$`):

```bash
cd ~/dev/dev-setup && claude "Passo rag-sistema do roteiro: RAG com pgvector dentro do primeiro sistema AM"
```

- [ ] **Pronto quando:** O sistema responde perguntas com base nos dados do cliente, citando a origem
- Implanta: IA: RAG + pgvector

<a id="f26"></a>

## 42 · Sistemas AM à venda

Os sistemas viram produto por assinatura.

**Quando:** 2027

**Começa quando:** O primeiro sistema AM pronto e testado com um cliente

### 42.1 Lançar o primeiro sistema AM como SaaS, com cobrança por módulo

**Claude com você** · 10 h 00 min

No **Ubuntu** (linha `alanmateus@...$`):

```bash
cd ~/dev/dev-setup && claude "Passo saas do roteiro: Lançar o primeiro sistema AM como SaaS, com cobrança por módulo"
```

- [ ] **Pronto quando:** Primeiro cliente pagando por assinatura
- Implanta: Sistemas AM (SaaS) · aura-licensing

### 42.2 AM Kaixara: PDV, cardápio, fichas técnicas e estoque

**Claude com você** · 40 h 00 min

No **Ubuntu** (linha `alanmateus@...$`):

```bash
cd ~/dev/dev-setup && claude "Passo kaixara do roteiro: AM Kaixara: PDV, cardápio, fichas técnicas e estoque"
```

- [ ] **Pronto quando:** Rodando num negócio real
- **Oferta:** AM Kaixara (PDV, ficha técnica, cardápio)
- Implanta: AM Kaixara (PDV e cardápio)

### 42.3 AM Rotara: pedidos, rotas e mapas

**Claude com você** · 40 h 00 min

No **Ubuntu** (linha `alanmateus@...$`):

```bash
cd ~/dev/dev-setup && claude "Passo rotara do roteiro: AM Rotara: pedidos, rotas e mapas"
```

- [ ] **Pronto quando:** Entregas rastreadas no mapa em tempo real
- **Oferta:** AM Rotara (pedidos e entregas)
- Implanta: AM Rotara (entregas) · PostGIS + MapLibre

### 42.4 Serviços aura- compartilhados, só quando um sistema precisar

**Claude com você** · 10 h 00 min

No **Ubuntu** (linha `alanmateus@...$`):

```bash
cd ~/dev/dev-setup && claude "Passo servicos-aura do roteiro: Serviços aura- compartilhados, só quando um sistema precisar"
```

- [ ] **Pronto quando:** Um serviço compartilhado usado por dois sistemas
- Implanta: Serviços aura- (10) · Datomic local

### 42.5 App de delivery com a marca do restaurante (white-label)

**Claude com você** · 20 h 00 min

No **Ubuntu** (linha `alanmateus@...$`):

```bash
cd ~/dev/dev-setup && claude "Passo whitelabel do roteiro: App de delivery com a marca do restaurante (white-label)"
```

- [ ] **Pronto quando:** Primeiro restaurante usando o app com a marca dele
- Comece oferecendo a 3 restaurantes que pagam 23% ao iFood.
- **Oferta:** App de delivery com a marca do restaurante (white-label)
- Implanta: AM Rotara (entregas)

<a id="f27"></a>

## 43 · CNPJ e formalização

Sair do CPF na hora certa, com nota fiscal e cobrança automáticas.

**Quando:** Quando a renda pedir

**Começa quando:** A renda passou do valor de virada definido com o contador

### 43.1 Abrir a AMtech Tecnologia (ME no Simples, sócio único)

**Você** · 4 h 00 min

- **Fora do terminal:** Órgão público, contador ou entidade: feito no site do governo ou com atendimento.
- [ ] **Pronto quando:** CNPJ ativo, conta PJ aberta e contador contratado
- **Precisa:** pagar um serviço
- Implanta: CNPJ (futuro) · 3 CNPJs por frente

### 43.2 Certificado digital e-CNPJ

**Você** · 1 h 00 min

- **Fora do terminal:** Órgão público, contador ou entidade: feito no site do governo ou com atendimento.
- [ ] **Pronto quando:** Certificado instalado e guardado no KeePassXC
- **Precisa:** pagar um serviço
- Implanta: Certificado digital (e-CNPJ)

### 43.3 Nota fiscal automática pela API de NFS-e

**Claude com você** · 4 h 00 min

No **Ubuntu** (linha `alanmateus@...$`):

```bash
cd ~/dev/dev-setup && claude "Passo nfse-api do roteiro: Nota fiscal automática pela API de NFS-e"
```

- [ ] **Pronto quando:** Venda de teste emite nota sozinha
- Implanta: API de NFS-e (ex.: Focus NFe)

### 43.4 Cobrança recorrente por Pix Automático

**Claude com você** · 4 h 00 min

No **Ubuntu** (linha `alanmateus@...$`):

```bash
cd ~/dev/dev-setup && claude "Passo pix-automatico do roteiro: Cobrança recorrente por Pix Automático"
```

- [ ] **Pronto quando:** Assinatura de teste cobrada por Pix
- Implanta: Pix Automático + gateway (ex.: Asaas)

<a id="f28"></a>

## 44 · Agentes do grupo

Atendimento, orçamento, cobrança e análise rodando com a sua aprovação.

**Quando:** Junto com o primeiro CNPJ

**Começa quando:** Clientes e vendas recorrentes

### 44.1 Analista semanal: o que funcionou e o que mudar

**Claude com você** · 2 h 00 min

No **Ubuntu** (linha `alanmateus@...$`):

```bash
cd ~/dev/dev-setup && claude "Passo ag-analista do roteiro: Analista semanal: o que funcionou e o que mudar"
```

- [ ] **Pronto quando:** Relatório toda segunda no Telegram
- Implanta: Analista semanal

### 44.2 Atendente do WhatsApp com passagem para você

**Claude com você** · 4 h 00 min

No **Ubuntu** (linha `alanmateus@...$`):

```bash
cd ~/dev/dev-setup && claude "Passo ag-atendente do roteiro: Atendente do WhatsApp com passagem para você"
```

- [ ] **Pronto quando:** Dúvida comum respondida sozinha; o resto chega para você
- Implanta: Agente atendente (WhatsApp)

### 44.3 Orçamentista de sites e sistemas

**Claude com você** · 3 h 00 min

No **Ubuntu** (linha `alanmateus@...$`):

```bash
cd ~/dev/dev-setup && claude "Passo ag-orcamento do roteiro: Orçamentista de sites e sistemas"
```

- [ ] **Pronto quando:** Rascunho de orçamento em 5 minutos, revisado por você
- Implanta: Agente orçamentista

### 44.4 Cobrador educado (lembrete antes e depois do vencimento)

**Claude com você** · 2 h 00 min

No **Ubuntu** (linha `alanmateus@...$`):

```bash
cd ~/dev/dev-setup && claude "Passo ag-cobranca do roteiro: Cobrador educado (lembrete antes e depois do vencimento)"
```

- [ ] **Pronto quando:** Atraso cai pela metade
- Implanta: Agente cobrador

### 44.5 Pós-venda: NPS e pedido de avaliação

**Claude com você** · 2 h 00 min

No **Ubuntu** (linha `alanmateus@...$`):

```bash
cd ~/dev/dev-setup && claude "Passo ag-posvenda do roteiro: Pós-venda: NPS e pedido de avaliação"
```

- [ ] **Pronto quando:** NPS medido em cada venda
- Implanta: Agente pós-venda

### 44.6 Organizador fiscal para o contador

**Claude com você** · 2 h 00 min

No **Ubuntu** (linha `alanmateus@...$`):

```bash
cd ~/dev/dev-setup && claude "Passo ag-fiscal do roteiro: Organizador fiscal para o contador"
```

- [ ] **Pronto quando:** Pasta do mês pronta no dia 5
- Implanta: Organizador fiscal

### 44.7 Comprador com estoque mínimo

**Claude com você** · 3 h 00 min

No **Ubuntu** (linha `alanmateus@...$`):

```bash
cd ~/dev/dev-setup && claude "Passo ag-comprador do roteiro: Comprador com estoque mínimo"
```

- [ ] **Pronto quando:** Pedido de reposição sugerido antes de faltar
- Implanta: Agente comprador

<a id="f29"></a>

## 45 · Editora: depois do primeiro livro

O mesmo livro em mais formatos, públicos e idiomas.

**Quando:** Depois do primeiro livro

**Começa quando:** O primeiro livro publicado

### 45.1 Gráfica sob demanda no Brasil

**Você** · 2 h 00 min

- **Fora do terminal:** Venda e relacionamento: falar com gente, publicar e atender. O Claude prepara textos e materiais; quem fala é você.
- [ ] **Pronto quando:** Cópia de prova aprovada
- **Precisa:** pagar um serviço
- Implanta: Gráfica sob demanda (Brasil)

### 45.2 Kit edição especial

**Você** · 4 h 00 min

- **Fora do terminal:** Venda e relacionamento: falar com gente, publicar e atender. O Claude prepara textos e materiais; quem fala é você.
- [ ] **Pronto quando:** Primeira tiragem vendida
- **Precisa:** pagar um serviço
- **Oferta:** Kit do livro e edição do professor
- Implanta: Kit edição especial

### 45.3 Curso por seção do livro, com animações

**Você** · 20 h 00 min

- **Fora do terminal:** Conteúdo seu: gravar, escrever ou explicar o seu método.
- [ ] **Pronto quando:** Primeira seção gravada e à venda
- Implanta: Curso por seção · Manim (animações)

### 45.4 Edição do professor com licença para escolas

**Claude com você** · 10 h 00 min

No **Ubuntu** (linha `alanmateus@...$`):

```bash
cd ~/dev/dev-setup && claude "Passo edicao-professor do roteiro: Edição do professor com licença para escolas"
```

- [ ] **Pronto quando:** Primeira escola licenciada
- **Oferta:** Adoção do livro por escolas
- Implanta: Edição do professor

### 45.5 Traduções para espanhol e inglês

**Claude com você** · 20 h 00 min

No **Ubuntu** (linha `alanmateus@...$`):

```bash
cd ~/dev/dev-setup && claude "Passo traducoes do roteiro: Traduções para espanhol e inglês"
```

- [ ] **Pronto quando:** Primeiro volume traduzido e revisado
- **Precisa:** pagar um serviço
- **Oferta:** Traduções do livro
- Implanta: Traduções (espanhol, inglês)

<a id="f30"></a>

## 46 · Distribuído, plataforma e segunda nuvem

O que pesa em vaga pleno e sênior.

**Quando:** 2028

### 46.1 RabbitMQ e depois Kafka entre dois sistemas AM

**Claude com você** · 10 h 00 min

No **Ubuntu** (linha `alanmateus@...$`):

```bash
cd ~/dev/dev-setup && claude "Passo mensageria do roteiro: RabbitMQ e depois Kafka entre dois sistemas AM"
```

- [ ] **Pronto quando:** Evento de um sistema chega no outro sem chamada direta
- Implanta: RabbitMQ · Kafka

### 46.2 Kubernetes local com kind, kubectl, Helm e k9s

**Você** · 10 h 00 min

No **Ubuntu** (linha `alanmateus@...$`):

```bash
mkdir -p ~/.local/bin && curl -Lo ~/.local/bin/kind https://kind.sigs.k8s.io/dl/latest/kind-linux-amd64 && chmod +x ~/.local/bin/kind && sudo snap install kubectl --classic && sudo snap install helm --classic && kind create cluster --name lab && kubectl get nodes
```

- [ ] **Pronto quando:** Um sistema AM rodando no cluster local
- Implanta: Kubernetes local (kind) · kubectl · Helm · k9s

### 46.3 Logs e rastreamento com Loki e Tempo no Grafana

**Claude com você** · 4 h 00 min

No **Ubuntu** (linha `alanmateus@...$`):

```bash
cd ~/dev/dev-setup && claude "Passo loki-tempo do roteiro: Logs e rastreamento com Loki e Tempo no Grafana"
```

- [ ] **Pronto quando:** Uma requisição seguida de ponta a ponta
- Implanta: Loki + Tempo

### 46.4 AWS: Cloud Practitioner e o mesmo sistema rodando lá

**Você** · 20 h 00 min

- **Fora do terminal:** Criar a conta é no site; depois tudo pelo aws e gcloud no terminal.
- [ ] **Pronto quando:** Certificação e post comparando Azure e AWS
- **Precisa:** pagar um serviço
- Implanta: AWS

### 46.5 Google Cloud só o básico, quando um projeto de IA ou dados pedir

**Você** · 5 h 00 min

- **Fora do terminal:** Criar a conta é no site; depois tudo pelo aws e gcloud no terminal.
- [ ] **Pronto quando:** Um serviço usado num projeto real
- Implanta: Google Cloud

### 46.6 App mobile dos sistemas AM com .NET MAUI

**Claude com você** · 20 h 00 min

No **Ubuntu** (linha `alanmateus@...$`):

```bash
cd ~/dev/dev-setup && claude "Passo mobile do roteiro: App mobile dos sistemas AM com .NET MAUI"
```

- [ ] **Pronto quando:** App publicado para teste interno
- Implanta: App mobile (.NET MAUI)

<a id="f31"></a>

## 47 · Infraestrutura própria

Servidor em casa e máquina de IA quando o grupo pedir.

**Quando:** 2028, quando o grupo pedir

### 47.1 Servidor caseiro com backup local e os serviços 24 horas

**Você** · 8 h 00 min

- **Fora do terminal:** Compra e montagem física (ou instalação por janela de VM); depois os verificadores conferem pelo terminal.
- [ ] **Pronto quando:** n8n, banco e painel rodando no servidor; notebook livre
- **Precisa:** comprar algo
- Implanta: Servidor caseiro (NAS + serviços)

### 47.2 Tailscale entre notebook, celular e servidor

**Você** · 1 h 00 min

- **Fora do terminal:** Entrar na conta do Tailscale é pelo navegador; depois: tailscale status.
- [ ] **Pronto quando:** Acesso ao servidor de fora de casa sem abrir porta
- Implanta: Tailscale (VPN)

### 47.3 Workstation com GPU para treinar e gerar voz e vídeo em casa

**Você** · 8 h 00 min

- **Fora do terminal:** Compra e montagem física (ou instalação por janela de VM); depois os verificadores conferem pelo terminal.
- [ ] **Pronto quando:** Fine-tuning de 8B rodando local
- **Precisa:** comprar algo
- Implanta: Workstation com GPU

<a id="f32"></a>

## 48 · Negócios do grupo em Barbacena

Um negócio por vez, cada um só depois que o anterior passa no portão.

**Quando:** Fase A: 12 a 18 meses; B: mais 12 a 18; C: a partir do 3º ou 4º ano

**Começa quando:** Os 5 portões do planejador: negócio anterior se pagando há 3 meses, capital em caixa, alguém de confiança tocando, sistema AM rodando e a sua reserva intacta

### 48.1 Planejador do grupo com os números reais

**Claude com você** · 2 h 00 min

No **Ubuntu** (linha `alanmateus@...$`):

```bash
cd ~/dev/dev-setup && claude "Passo planejador-real do roteiro: Planejador do grupo com os números reais"
```

- [ ] **Pronto quando:** Capital mínimo e portões calculados com os seus dados
- Implanta: Planejador do Grupo

### 48.2 A1 · AMtech Software

**Você** · 40 h 00 min

- **Fora do terminal:** Negócio físico: ponto, alvará, compras e pessoas. O Claude faz os números e os documentos.
- [ ] **Pronto quando:** 3 meses seguidos com lucro e 10 clientes pagantes
- **Precisa:** pagar um serviço
- Implanta: AMtech Software (projetos e SaaS)

### 48.3 A2 · Loja AMtech, peças sob encomenda, ponto de retirada e Maker

**Você** · 80 h 00 min

- **Fora do terminal:** Negócio físico: ponto, alvará, compras e pessoas. O Claude faz os números e os documentos.
- [ ] **Pronto quando:** Loja acima do equilíbrio por 3 meses e técnico que abre e fecha sem você
- **Precisa:** comprar algo, pagar um serviço
- **Oferta:** Assistência técnica · Peças e acessórios sem estoque · Ponto de retirada (Shopee e Mercado Livre) · AMtech Maker (robótica e automação)
- Implanta: Loja AMtech (assistência) · Peças sem estoque (sob encomenda) · Ponto de retirada (Shopee e ML) · AMtech Maker (robótica) · Anatel e Inmetro · Google Perfil da Empresa

### 48.4 B1 · AM Entregas e Mercado Envios Flex

**Você** · 80 h 00 min

- **Fora do terminal:** Negócio físico: ponto, alvará, compras e pessoas. O Claude faz os números e os documentos.
- [ ] **Pronto quando:** 1.000 entregas por mês e 5 contratos fixos
- **Precisa:** comprar algo, pagar um serviço
- **Oferta:** AM Entregas
- Implanta: AM Entregas (moto e carro) · Mercado Envios Flex

### 48.5 B2 · AM Delivery

**Você** · 80 h 00 min

- **Fora do terminal:** Negócio físico: ponto, alvará, compras e pessoas. O Claude faz os números e os documentos.
- [ ] **Pronto quando:** 20 lojistas ativos e 1.500 pedidos por mês
- **Precisa:** pagar um serviço
- **Oferta:** AM Delivery · Licença do AM Delivery para outras cidades
- Implanta: AM Delivery (várias empresas)

### 48.6 C1 · Sushi, delivery primeiro

**Você** · 80 h 00 min

- **Fora do terminal:** Negócio físico: ponto, alvará, compras e pessoas. O Claude faz os números e os documentos.
- [ ] **Pronto quando:** Lucro por 3 meses e sushiman que toca a noite sem você
- **Precisa:** comprar algo, pagar um serviço
- **Oferta:** Sushi (delivery)
- Implanta: Sushi (delivery) · Vigilância sanitária (RDC 216) · iFood (canal de descoberta)

### 48.7 C2 · Padaria com café da manhã e almoço

**Você** · 80 h 00 min

- **Fora do terminal:** Negócio físico: ponto, alvará, compras e pessoas. O Claude faz os números e os documentos.
- [ ] **Pronto quando:** Gerente no comando e CMV dentro da meta por 3 meses
- **Precisa:** comprar algo, pagar um serviço
- **Oferta:** Padaria com café da manhã e almoço
- Implanta: Padaria + café da manhã + almoço

### 48.8 C3 · Cafeteria

**Você** · 40 h 00 min

- **Fora do terminal:** Negócio físico: ponto, alvará, compras e pessoas. O Claude faz os números e os documentos.
- [ ] **Pronto quando:** Cafeteria acima do equilíbrio
- **Precisa:** comprar algo, pagar um serviço
- **Oferta:** Cafeteria
- Implanta: Cafeteria

### 48.9 Serviços presenciais para 2027, se a tarde ficar livre (por parceiros quando der)

**Você** · 30 min

- **Fora do terminal:** Dependem de você presente ou de parceiro técnico; decisão de 2027.
- [ ] **Pronto quando:** Decisão tomada no replanejamento de 2027
- **Oferta:** PC montado e entregue configurado · Redes Wi-Fi e câmeras com monitoramento mensal · Casa inteligente para clientes (Home Assistant) · Instrutor horista (SENAC, SENAI, prefeitura) · Aulas de informática e celular para idosos · Colônia de férias tech (robótica e programação) · Gestão de tráfego pago para o comércio local

### 48.10 Rendas de capital alto: decidir só com o portão aberto

**Você** · 30 min

- **Fora do terminal:** Exigem capital; só quando a renda do núcleo pagar o investimento.
- [ ] **Pronto quando:** Decisão registrada com capital próprio disponível
- **Oferta:** Mercadinho autônomo em condomínio · Máquina de venda de lanches · Aluguel de kits de robótica · Kits e placas de robótica (Tindie e Mercado Livre) · Motos e carros: compra e revenda

<a id="f33"></a>

## 49 · Estudo contínuo

As trilhas de estudo ligadas ao setup, sem copiar conteúdo de ninguém.

**Quando:** Contínuo, desde a semana 2

### 49.1 Pedir o GitHub Education como professor e ligar o Copilot

**Você** · 20 min

No **PowerShell** do Windows (linha `PS C:\>`):

```powershell
Start-Process 'https://education.github.com/discount_requests/application'
```

- [ ] **Pronto quando:** Benefícios aprovados e Copilot ativo no VS Code
- Implanta: GitHub Education · GitHub Copilot

### 49.2 Montar as trilhas: Microsoft Learn, AWS Skill Builder, roadmap.sh e laboratórios do TryHackMe

**Você** · 30 min

- **Fora do terminal:** Cadastro no site ou app do serviço, com documento e confirmação no celular; nenhum deles deixa criar conta por terminal.
- [ ] **Pronto quando:** Uma trilha de cada em andamento, anotada no Obsidian
- Implanta: Microsoft Learn + AWS Skill Builder · roadmap.sh + Akita · TryHackMe / Hack The Box

### 49.3 Organizar as contas de aluno (Alura, Rocketseat, DIO, Udemy)

**Você** · 15 min

- **Fora do terminal:** Cadastro no site ou app do serviço, com documento e confirmação no celular; nenhum deles deixa criar conta por terminal.
- [ ] **Pronto quando:** Acessos no KeePassXC e cursos em andamento listados no Obsidian
- A licença é para assistir e estudar. Para a IA vão só as suas anotações e os seus projetos.
- Implanta: Alura · Rocketseat · DIO · Udemy

### 49.4 Criar os baralhos do Anki (comandos, conceitos, certificações)

**Você** · 20 min

- **Fora do terminal:** Estudo: assistir, praticar e anotar.
- [ ] **Pronto quando:** Revisão do dia feita no notebook e no celular
- Implanta: Anki

### 49.5 Rendas que dependem de formação longa (bug bounty, perícia)

**Você** · 15 min

- **Fora do terminal:** Dependem de certificação e estudo; entram pela trilha de estudo.
- [ ] **Pronto quando:** Portão de formação cumprido
- **Oferta:** Bug bounty e pentest · Perito em informática judicial

### 49.6 Consultoria de investimentos só com a sócia certificada e registrada

**Você** · 15 min

- **Fora do terminal:** Portão regulatório (CVM); fora do terminal.
- [ ] **Pronto quando:** Certificação e registro conferidos
- **Oferta:** Consultoria de investimentos (AM Rendara premium, com sócia certificada)

### 49.7 Estudo vira produto: rodar a esteira depois de cada bloco de estudo

**Você** · 15 min

- **Fora do terminal:** Usa a automação au-esteira, quando construída; a revisão é sua.
- [ ] **Pronto quando:** Aula, exercícios, cartões e roteiro gerados para revisar

### 49.8 Decidir quando começar a graduação em Economia

**Você** · 20 min

- **Fora do terminal:** Decisão de formação; fora do terminal.
- [ ] **Pronto quando:** Decisão com data e custo no Caixa da Casa

### 49.9 Trilha de certificações do mercado financeiro (CNPI → registro de consultor → CGE/CGA → CFP → CFA)

**Você** · 20 min

- **Fora do terminal:** Ordem e motivos em docs/certificacoes.md. CPA e C-PRO só se for trabalhar em banco. Confira o edital do ano antes de pagar.
- [ ] **Pronto quando:** Primeira prova marcada quando a cascata permitir

### 49.10 Rotina diária de inglês; espanhol no B1 e mandarim no B2

**Você** · 10 min

- **Fora do terminal:** Rotina de estudo; os gatilhos de espanhol e mandarim seguem o seu plano de idiomas.
- [ ] **Pronto quando:** 25 a 30 min de inglês por dia na Rotina

### 49.11 AM-OS e AM Linux: trilha de 10 anos de sistemas

**Você** · 15 min

- **Fora do terminal:** Horizonte longo; entra depois do Passo 9 do plano de estudos.
- [ ] **Pronto quando:** Marco do ano definido

### 49.12 Vigiar editais de professor EBTT (IF Sudeste MG, campus Barbacena) e de professor efetivo de MG

**Você** · 20 min

- **Fora do terminal:** A busca semanal de editais (passo au-editais) inclui esses concursos. Decisão sua: 40 h com dedicação exclusiva limita as outras rendas; existem vagas de 20 h.
- [ ] **Pronto quando:** Editais na busca semanal e decisão registrada a cada edital

### 49.13 Encaixar as atividades da Licenciatura em Matemática na Rotina

**Você** · 15 min

- **Fora do terminal:** Rotina do Caixa da Casa (artefato), fora do terminal.
- [ ] **Pronto quando:** Aulas, atividades e provas da faculdade na Rotina do Caixa da Casa

<a id="quando-entra-cada-bloco"></a>

## Quando entra cada bloco

Camada por camada, na mesma ordem do mapa. O número é o passo do roteiro.

### Operação do grupo (esteira, marca, qualidade)

| Bloco | Passo | Quando |
|---|---|---|
| Portfólio de ofertas | 8.7, 30.14, 38.20 | Semanas 3 e 4 · nov/2026; Semanas 8 a 10 · dez/2026 a jan/2027; Fev a dez/2027, uma oferta por vez |
| Esteira de ofertas | 8.7, 30.14 | Semanas 3 e 4 · nov/2026; Semanas 8 a 10 · dez/2026 a jan/2027 |
| Padrão de qualidade | 30.14 | Semanas 8 a 10 · dez/2026 a jan/2027 |
| Marca pessoal Alan Mateus | 27.1, 29.1 | Semana 5 · nov/2026; Semanas 6 e 7 · dez/2026 |
| NPS e avaliações | 30.15 | Semanas 8 a 10 · dez/2026 a jan/2027 |
| CRM único + LGPD | 25.6, 26.6, 30.9 | Dez/2026 a jan/2027; Com a primeira página de venda no ar (jan/2027) e por etapas; Semanas 8 a 10 · dez/2026 a jan/2027 |
| Flywheel de conteúdo | 27.5, 27.6 | Semana 5 · nov/2026 |
| Canal build in public | 39.7 | A partir de fev/2027 |
| Agente atendente (WhatsApp) | 26.5, 38.5, 44.2 | Com a primeira página de venda no ar (jan/2027) e por etapas; Fev a dez/2027, uma oferta por vez; Junto com o primeiro CNPJ |
| Agente orçamentista | 44.3 | Junto com o primeiro CNPJ |
| Agente cobrador | 44.4 | Junto com o primeiro CNPJ |
| Agente pós-venda | 44.5 | Junto com o primeiro CNPJ |
| Agente editor de conteúdo | 27.5, 38.14 | Semana 5 · nov/2026; Fev a dez/2027, uma oferta por vez |
| Analista semanal | 44.1 | Junto com o primeiro CNPJ |
| Organizador fiscal | 44.6 | Junto com o primeiro CNPJ |
| Revisor de oferta | 30.14 | Semanas 8 a 10 · dez/2026 a jan/2027 |
| Agente comprador | 44.7 | Junto com o primeiro CNPJ |
| Diagnóstico do notebook | 0.2 | Antes de tudo · semana 1 (out/2026) |
| Roteiro de implantação | 0.6, 32.4 | Antes de tudo · semana 1 (out/2026); Semana 11 · jan/2027 |
| Instaladores (PowerShell e bash) | 3.1, 4.4 | Semana 1 · out/2026; Semana 2 · nov/2026 |
| Verificadores | 3.9, 4.10, 10.3, 32.4 | Semana 1 · out/2026; Semana 2 · nov/2026; Semana 4 · nov/2026; Semana 11 · jan/2027 |
| Pipeline de conteúdo | 27.4, 27.5, 27.7, 32.2 | Semana 5 · nov/2026; Semana 11 · jan/2027 |
| Acervo (seus documentos) | 8.3, 8.4, 8.5, 38.3 | Semanas 3 e 4 · nov/2026; Fev a dez/2027, uma oferta por vez |
| Agente revisor de qualidade | 20.6, 21.5 | Semana 5 · nov/2026; Semana 6 · nov/2026 a dez/2026 |
| Lucro por ferramenta | 25.3 | Dez/2026 a jan/2027 |
| Prospector com aprovação | 25.6 | Dez/2026 a jan/2027 |

### Público e canais

| Bloco | Passo | Quando |
|---|---|---|
| Meta Business Suite | 29.5 | Semanas 6 e 7 · dez/2026 |
| Instagram | 29.1, 33.6 | Semanas 6 e 7 · dez/2026; Semanas 12 a 15 · jan a fev/2027 |
| YouTube | 29.1, 38.14 | Semanas 6 e 7 · dez/2026; Fev a dez/2027, uma oferta por vez |
| LinkedIn | 29.1, 33.6 | Semanas 6 e 7 · dez/2026; Semanas 12 a 15 · jan a fev/2027 |
| WhatsApp Business | 29.2, 33.6 | Semanas 6 e 7 · dez/2026; Semanas 12 a 15 · jan a fev/2027 |
| Google Perfil da Empresa | 38.9, 48.3 | Fev a dez/2027, uma oferta por vez; Fase A: 12 a 18 meses; B: mais 12 a 18; C: a partir do 3º ou 4º ano |
| Comunidade (Discord ou grupo) | 30.10, 38.15 | Semanas 8 a 10 · dez/2026 a jan/2027; Fev a dez/2027, uma oferta por vez |
| Busca Google (SEO) | 29.12 | Semanas 6 e 7 · dez/2026 |
| Alunos e ex-alunos | 29.10 | Semanas 6 e 7 · dez/2026 |
| Recrutadores | 34.8 | Junto dos Passos 4 a 6 da trilha de estudo (≈ mar a jun/2027): o modelo nasce no Passo 4 (API e login) e ganha testes e qualidade no Passo 6 |
| TikTok | 29.1 | Semanas 6 e 7 · dez/2026 |
| Facebook | 29.1 | Semanas 6 e 7 · dez/2026 |

### Marketing, automação e medição

| Bloco | Passo | Quando |
|---|---|---|
| Meta Ads (Instagram, Facebook) | 39.1 | A partir de fev/2027 |
| Isca grátis + sequência de e-mails | 29.6, 33.5 | Semanas 6 e 7 · dez/2026; Semanas 12 a 15 · jan a fev/2027 |
| MailerLite | 29.6, 33.5, 38.8 | Semanas 6 e 7 · dez/2026; Semanas 12 a 15 · jan a fev/2027; Fev a dez/2027, uma oferta por vez |
| Postiz (agendador) | 10.8 | Semana 4 · nov/2026 |
| Aprovação no celular | 27.3 | Semana 5 · nov/2026 |
| Telegram (avisos) | 18.1, 18.2, 18.3, 18.4, 18.5, 25.5, 27.3 | Semana 5 · nov/2026; Dez/2026 a jan/2027 |
| n8n | 10.1, 10.2, 10.5, 10.7, 12.1, 12.4, 12.6, 12.7, 12.9, 12.10, 12.12, 21.7, 25.5, 38.5 | Semana 4 · nov/2026; Nov/2026 em diante, uma por vez, na ordem de desbloqueio; Semana 6 · nov/2026 a dez/2026; Dez/2026 a jan/2027; Fev a dez/2027, uma oferta por vez |
| Algoritmo de horário | 39.6 | A partir de fev/2027 |
| Tags de conversão (Pixel, Google…) | 29.5, 33.4 | Semanas 6 e 7 · dez/2026; Semanas 12 a 15 · jan a fev/2027 |
| Padrão de UTM | 30.12, 33.4 | Semanas 8 a 10 · dez/2026 a jan/2027; Semanas 12 a 15 · jan a fev/2027 |
| Google e YouTube Ads | 39.2 | A partir de fev/2027 |
| TikTok Ads | 39.2 | A partir de fev/2027 |
| Regras de corte | 30.13 | Semanas 8 a 10 · dez/2026 a jan/2027 |
| Lucro por Venda (calculadora) | 30.13 | Semanas 8 a 10 · dez/2026 a jan/2027 |
| Webhooks de venda | 31.1, 31.2, 32.3, 33.7 | Semana 11 · jan/2027; Semanas 12 a 15 · jan a fev/2027 |
| Banco de métricas (PostgreSQL) | 10.2, 10.7, 31.3 | Semana 4 · nov/2026; Semana 11 · jan/2027 |
| Painel de lucro (Grafana) | 11.6, 12.11, 31.4, 32.3 | Semana 4 · nov/2026; Nov/2026 em diante, uma por vez, na ordem de desbloqueio; Semana 11 · jan/2027 |
| Programa de afiliados | 39.5 | A partir de fev/2027 |
| Prospecção de parceiros | 30.16 | Semanas 8 a 10 · dez/2026 a jan/2027 |
| Dublagem (YouTube + ElevenLabs) | 39.8 | A partir de fev/2027 |
| Spotify Ad Studio | 39.3 | A partir de fev/2027 |
| Kwai Ads | 39.3 | A partir de fev/2027 |
| Pinterest Ads | 39.3 | A partir de fev/2027 |
| LinkedIn Ads | 39.3 | A partir de fev/2027 |
| Mídia nativa (Taboola, Outbrain) | 39.3 | A partir de fev/2027 |
| Influenciadores e newsletters | 39.4 | A partir de fev/2027 |
| PostHog (funil e gravações) | 26.2, 26.3 | Com a primeira página de venda no ar (jan/2027) e por etapas |
| GrowthBook (testes A/B) | 26.3 | Com a primeira página de venda no ar (jan/2027) e por etapas |

### Plataformas de venda e recebimento

| Bloco | Passo | Quando |
|---|---|---|
| Pix Automático + gateway (ex.: Asaas) | 43.4 | Quando a renda pedir |
| Agenda online (Cal.com) | 30.8, 38.18, 38.19 | Semanas 8 a 10 · dez/2026 a jan/2027; Fev a dez/2027, uma oferta por vez |
| CRM simples (planilha) | 30.9 | Semanas 8 a 10 · dez/2026 a jan/2027 |
| Hotmart | 30.5, 33.3, 33.7, 38.3, 38.4 | Semanas 8 a 10 · dez/2026 a jan/2027; Semanas 12 a 15 · jan a fev/2027; Fev a dez/2027, uma oferta por vez |
| Kiwify | 30.5, 33.8 | Semanas 8 a 10 · dez/2026 a jan/2027; Semanas 12 a 15 · jan a fev/2027 |
| Eduzz | 30.6, 33.8 | Semanas 8 a 10 · dez/2026 a jan/2027; Semanas 12 a 15 · jan a fev/2027 |
| Udemy | 30.6, 33.8 | Semanas 8 a 10 · dez/2026 a jan/2027; Semanas 12 a 15 · jan a fev/2027 |
| DIO (parceria) | 30.6 | Semanas 8 a 10 · dez/2026 a jan/2027 |
| YouTube (membros) | 39.9 | A partir de fev/2027 |
| Mercado Pago | 30.7, 38.19 | Semanas 8 a 10 · dez/2026 a jan/2027; Fev a dez/2027, uma oferta por vez |
| Afiliados (Amazon, Hotmart…) | 30.11, 38.1 | Semanas 8 a 10 · dez/2026 a jan/2027; Fev a dez/2027, uma oferta por vez |
| Chatwoot (atendimento) | 26.5 | Com a primeira página de venda no ar (jan/2027) e por etapas |
| Twenty (CRM aberto) | 26.6 | Com a primeira página de venda no ar (jan/2027) e por etapas |

### Pessoa física: impostos e finanças

| Bloco | Passo | Quando |
|---|---|---|
| Registro de marca (INPI) | 30.17 | Semanas 8 a 10 · dez/2026 a jan/2027 |
| Termos, privacidade (LGPD) e contratos | 30.4 | Semanas 8 a 10 · dez/2026 a jan/2027 |
| Certificado digital (e-CNPJ) | 43.2 | Quando a renda pedir |
| API de NFS-e (ex.: Focus NFe) | 43.3 | Quando a renda pedir |
| CNPJ (futuro) | 43.1 | Quando a renda pedir |
| gov.br (prata ou ouro) | 2.7, 30.1 | Semana 1 · out/2026 (o e-mail e as críticas); o resto, 5 contas por semana até dez/2026; Semanas 8 a 10 · dez/2026 a jan/2027 |
| Carnê-leão (Receita Federal) | 30.18, 33.7 | Semanas 8 a 10 · dez/2026 a jan/2027; Semanas 12 a 15 · jan a fev/2027 |
| Declaração anual do IR | 30.19 | Semanas 8 a 10 · dez/2026 a jan/2027 |
| Conta bancária separada (CPF) | 2.7, 30.2 | Semana 1 · out/2026 (o e-mail e as críticas); o resto, 5 contas por semana até dez/2026; Semanas 8 a 10 · dez/2026 a jan/2027 |
| Contador | 30.3 | Semanas 8 a 10 · dez/2026 a jan/2027 |
| Caixa da Casa / AM Rendara | 16.1, 16.2, 16.3, 16.4, 16.5, 16.6, 16.7, 16.8, 20.9, 30.20, 38.4 | Dez/2026; Semana 5 · nov/2026; Semanas 8 a 10 · dez/2026 a jan/2027; Fev a dez/2027, uma oferta por vez |
| Financeiro local | 15.1, 15.2, 15.3, 15.4 | Dez/2026 |
| Documenso (assinatura) | 26.7 | Com a primeira página de venda no ar (jan/2027) e por etapas |
| Invoice Ninja (orçamentos) | 26.7 | Com a primeira página de venda no ar (jan/2027) e por etapas |

### Vitrine web (sites e domínio)

| Bloco | Passo | Quando |
|---|---|---|
| E-mail profissional (enviar e receber) | 29.4 | Semanas 6 e 7 · dez/2026 |
| Domínio (Registro.br) | 29.3 | Semanas 6 e 7 · dez/2026 |
| Site pessoal + blog (Jekyll) | 29.7, 38.1 | Semanas 6 e 7 · dez/2026; Fev a dez/2027, uma oferta por vez |
| Instituto AMS | 29.8, 33.4 | Semanas 6 e 7 · dez/2026; Semanas 12 a 15 · jan a fev/2027 |
| Site Grupo AMtech | 29.9 | Semanas 6 e 7 · dez/2026 |
| Catálogo do HTML | 29.9, 38.2 | Semanas 6 e 7 · dez/2026; Fev a dez/2027, uma oferta por vez |
| Umami (analytics) | 29.11 | Semanas 6 e 7 · dez/2026 |
| Google Search Console | 29.12 | Semanas 6 e 7 · dez/2026 |
| Hostinger (clientes WP) | 22.2, 22.4, 29.13, 38.10 | Semana 6 · nov/2026 a dez/2026; Semanas 6 e 7 · dez/2026; Fev a dez/2027, uma oferta por vez |
| Kit de sites (Hostinger IA) | 13.1, 13.2, 13.3, 13.4 | Semanas 4 e 5 · nov/2026 |
| Avaliador de templates | 13.5 | Semanas 4 e 5 · nov/2026 |

### Produtos (o que você vende)

| Bloco | Passo | Quando |
|---|---|---|
| Mini-curso Lógica de Programação | 30.5, 33.1 | Semanas 8 a 10 · dez/2026 a jan/2027; Semanas 12 a 15 · jan a fev/2027 |
| Formações (TI, Matemática, Finanças) | 39.10 | A partir de fev/2027 |
| Templates e código-fonte | 34.7 | Junto dos Passos 4 a 6 da trilha de estudo (≈ mar a jun/2027): o modelo nasce no Passo 4 (API e login) e ganha testes e qualidade no Passo 6 |
| Livro Lógica e Máquina | 36.2 | Quando o capítulo 1 estiver pronto |
| Aulas particulares | 30.8 | Semanas 8 a 10 · dez/2026 a jan/2027 |
| Sites para pequenas empresas | 29.13, 38.9, 38.10 | Semanas 6 e 7 · dez/2026; Fev a dez/2027, uma oferta por vez |
| Sistemas AM (SaaS) | 42.1 | 2027 |
| Esteira de sites (issue → PR → ar) | 22.3, 22.4, 22.5 | Semana 6 · nov/2026 a dez/2026 |

### Negócios do grupo (Barbacena)

| Bloco | Passo | Quando |
|---|---|---|
| AMtech Software (projetos e SaaS) | 48.2 | Fase A: 12 a 18 meses; B: mais 12 a 18; C: a partir do 3º ou 4º ano |
| Loja AMtech (assistência) | 48.3 | Fase A: 12 a 18 meses; B: mais 12 a 18; C: a partir do 3º ou 4º ano |
| Peças sem estoque (sob encomenda) | 48.3 | Fase A: 12 a 18 meses; B: mais 12 a 18; C: a partir do 3º ou 4º ano |
| Ponto de retirada (Shopee e ML) | 48.3 | Fase A: 12 a 18 meses; B: mais 12 a 18; C: a partir do 3º ou 4º ano |
| AMtech Maker (robótica) | 48.3 | Fase A: 12 a 18 meses; B: mais 12 a 18; C: a partir do 3º ou 4º ano |
| AM Entregas (moto e carro) | 48.4 | Fase A: 12 a 18 meses; B: mais 12 a 18; C: a partir do 3º ou 4º ano |
| Mercado Envios Flex | 48.4 | Fase A: 12 a 18 meses; B: mais 12 a 18; C: a partir do 3º ou 4º ano |
| AM Delivery (várias empresas) | 48.5 | Fase A: 12 a 18 meses; B: mais 12 a 18; C: a partir do 3º ou 4º ano |
| Sushi (delivery) | 48.6 | Fase A: 12 a 18 meses; B: mais 12 a 18; C: a partir do 3º ou 4º ano |
| Cafeteria | 48.8 | Fase A: 12 a 18 meses; B: mais 12 a 18; C: a partir do 3º ou 4º ano |
| Padaria + café da manhã + almoço | 48.7 | Fase A: 12 a 18 meses; B: mais 12 a 18; C: a partir do 3º ou 4º ano |
| 3 CNPJs por frente | 43.1 | Quando a renda pedir |
| Planejador do Grupo | 48.1 | Fase A: 12 a 18 meses; B: mais 12 a 18; C: a partir do 3º ou 4º ano |
| iFood (canal de descoberta) | 48.6 | Fase A: 12 a 18 meses; B: mais 12 a 18; C: a partir do 3º ou 4º ano |
| Vigilância sanitária (RDC 216) | 48.6 | Fase A: 12 a 18 meses; B: mais 12 a 18; C: a partir do 3º ou 4º ano |
| Anatel e Inmetro | 48.3 | Fase A: 12 a 18 meses; B: mais 12 a 18; C: a partir do 3º ou 4º ano |
| Radar de revenda | 11.5 | Semana 4 · nov/2026 |

### Editora AMS Silva (produção de livros)

| Bloco | Passo | Quando |
|---|---|---|
| Selo Editora AMS Silva | 36.7 | Quando o capítulo 1 estiver pronto |
| Repositório do livro | 36.2 | Quando o capítulo 1 estiver pronto |
| Seu modelo de criação | 36.1 | Quando o capítulo 1 estiver pronto |
| Fonte única (Markdown + Pandoc) | 36.2 | Quando o capítulo 1 estiver pronto |
| Exercícios em YAML | 36.2, 38.6, 38.7, 38.13 | Quando o capítulo 1 estiver pronto; Fev a dez/2027, uma oferta por vez |
| Pranchas TikZ e SVG | 4.4 | Semana 2 · nov/2026 |
| Classe LaTeX do livro | 36.2 | Quando o capítulo 1 estiver pronto |
| Pipeline do livro (CI) | 36.2 | Quando o capítulo 1 estiver pronto |
| Revisão automática (LanguageTool, Vale) | 36.2 | Quando o capítulo 1 estiver pronto |
| Agentes da editora | 36.5 | Quando o capítulo 1 estiver pronto |
| Leitores beta e revisão técnica | 36.9 | Quando o capítulo 1 estiver pronto |
| Errata e edições | 36.2 | Quando o capítulo 1 estiver pronto |
| ISBN + código de barras (CBL) | 36.8 | Quando o capítulo 1 estiver pronto |
| Ficha catalográfica | 36.8 | Quando o capítulo 1 estiver pronto |
| Depósito legal | 36.11 | Quando o capítulo 1 estiver pronto |
| Amazon KDP | 36.10 | Quando o capítulo 1 estiver pronto |
| Gráfica sob demanda (Brasil) | 45.1 | Depois do primeiro livro |
| Kit edição especial | 45.2 | Depois do primeiro livro |
| Curso por seção | 45.3 | Depois do primeiro livro |
| Edição do professor | 45.4 | Depois do primeiro livro |
| Traduções (espanhol, inglês) | 45.5 | Depois do primeiro livro |
| Quadro de referências | 36.6 | Quando o capítulo 1 estiver pronto |
| Matriz de editais | 36.6 | Quando o capítulo 1 estiver pronto |
| Projeto do capítulo | 36.1 | Quando o capítulo 1 estiver pronto |
| Mapa de pré-requisitos | 36.1 | Quando o capítulo 1 estiver pronto |
| Seu método (metodo.yaml) | 36.1 | Quando o capítulo 1 estiver pronto |
| Acervos de imagens (APIs) | 36.3 | Quando o capítulo 1 estiver pronto |
| Busca automática de imagens | 36.3 | Quando o capítulo 1 estiver pronto |
| Filtro de licença e fichas | 36.3 | Quando o capítulo 1 estiver pronto |
| Folha de contato (artefato) | 36.3 | Quando o capítulo 1 estiver pronto |
| Créditos e legendas | 36.3 | Quando o capítulo 1 estiver pronto |
| Figuras por código (Matplotlib…) | 36.4 | Quando o capítulo 1 estiver pronto |
| CircuiTikZ | 4.4 | Semana 2 · nov/2026 |
| Geradores de tabelas | 36.4 | Quando o capítulo 1 estiver pronto |
| Manim (animações) | 45.3 | Depois do primeiro livro |
| Texto alternativo | 36.4 | Quando o capítulo 1 estiver pronto |

### Estudo e carreira

| Bloco | Passo | Quando |
|---|---|---|
| Microsoft Learn + AWS Skill Builder | 49.2 | Contínuo, desde a semana 2 |
| TryHackMe / Hack The Box | 49.2 | Contínuo, desde a semana 2 |
| Alura · Rocketseat · DIO · Udemy | 49.3 | Contínuo, desde a semana 2 |
| Anki | 3.2, 38.7, 49.4 | Semana 1 · out/2026; Fev a dez/2027, uma oferta por vez; Contínuo, desde a semana 2 |
| roadmap.sh + Akita | 49.2 | Contínuo, desde a semana 2 |
| GitHub Education | 20.8, 22.1, 49.1 | Semana 5 · nov/2026; Semana 6 · nov/2026 a dez/2026; Contínuo, desde a semana 2 |
| Zoomcamp de dados + cursos de IA | 37.6 | Pendrives, GPU e laboratório a partir da semana 2; Zoomcamp, dbt e Airflow junto do IA2 da Trilha de Dados e IA do vault (depois do Passo 8, ≈ 2028); dataset e treino do 8B junto do IA6 (≈ 2029) |
| GPT do zero (estudo) | 23.1 | 2027, depois do primeiro fine-tuning de 8B |
| Laboratório de redes | 24.5 | Semana 6 · nov/2026 |

### Produção de conteúdo

| Bloco | Passo | Quando |
|---|---|---|
| OBS Studio | 3.2, 28.1, 33.2 | Semana 1 · out/2026; Semana 5 · dez/2026; Semanas 12 a 15 · jan a fev/2027 |
| DaVinci Resolve ou Kdenlive | 3.7, 28.3, 33.2 | Semana 1 · out/2026; Semana 5 · dez/2026; Semanas 12 a 15 · jan a fev/2027 |
| Audacity | 3.2, 28.2 | Semana 1 · out/2026; Semana 5 · dez/2026 |
| Canva · Krita · Inkscape | 3.2, 22.8, 28.4 | Semana 1 · out/2026; Semana 6 · nov/2026 a dez/2026; Semana 5 · dez/2026 |
| Whisper (local) | 4.4, 27.6 | Semana 2 · nov/2026; Semana 5 · nov/2026 |
| Voz clonada (ElevenLabs) | 28.5 | Semana 5 · dez/2026 |
| Fábrica de aulas | 14.1, 14.2, 14.3, 14.4, 14.5, 14.6, 14.7, 14.8, 14.9 | Semanas 5 e 6 · nov/2026 |
| Penpot (design) | 26.8 | Com a primeira página de venda no ar (jan/2027) e por etapas |

### Nuvem, código e entrega

| Bloco | Passo | Quando |
|---|---|---|
| Armazenamento de arquivos (Blob/R2) | 35.4 | Com o Passo 5 da trilha de estudo (≈ abr a jun/2027) para a conta e o deploy do sistema exemplo; o deploy de produção do AM Kaixara é o Passo 10 (≈ 2028) |
| E-mail transacional (Resend, SES…) | 35.5 | Com o Passo 5 da trilha de estudo (≈ abr a jun/2027) para a conta e o deploy do sistema exemplo; o deploy de produção do AM Kaixara é o Passo 10 (≈ 2028) |
| SonarQube Cloud | 34.5 | Junto dos Passos 4 a 6 da trilha de estudo (≈ mar a jun/2027): o modelo nasce no Passo 4 (API e login) e ganha testes e qualidade no Passo 6 |
| Projects · ADRs · MkDocs | 5.5 | Semana 2 · nov/2026 |
| Dependabot + CodeQL | 5.3 | Semana 2 · nov/2026 |
| Google Cloud | 46.5 | 2028 |
| GitHub | 2.7, 5.1, 5.4 | Semana 1 · out/2026 (o e-mail e as críticas); o resto, 5 contas por semana até dez/2026; Semana 2 · nov/2026 |
| GitHub Actions | 5.2, 32.1 | Semana 2 · nov/2026; Semana 11 · jan/2027 |
| GHCR (imagens) | 34.6 | Junto dos Passos 4 a 6 da trilha de estudo (≈ mar a jun/2027): o modelo nasce no Passo 4 (API e login) e ganha testes e qualidade no Passo 6 |
| GitHub Pages | 29.7 | Semanas 6 e 7 · dez/2026 |
| Cloudflare (DNS, Pages, e-mail) | 22.4, 22.6, 22.7, 29.3, 29.8, 31.1, 35.6 | Semana 6 · nov/2026 a dez/2026; Semanas 6 e 7 · dez/2026; Semana 11 · jan/2027; Com o Passo 5 da trilha de estudo (≈ abr a jun/2027) para a conta e o deploy do sistema exemplo; o deploy de produção do AM Kaixara é o Passo 10 (≈ 2028) |
| Vercel | 35.6 | Com o Passo 5 da trilha de estudo (≈ abr a jun/2027) para a conta e o deploy do sistema exemplo; o deploy de produção do AM Kaixara é o Passo 10 (≈ 2028) |
| Azure | 35.2, 35.3, 35.6 | Com o Passo 5 da trilha de estudo (≈ abr a jun/2027) para a conta e o deploy do sistema exemplo; o deploy de produção do AM Kaixara é o Passo 10 (≈ 2028) |
| AWS | 46.4 | 2028 |
| Backblaze B2 (backup) | 7.2 | Semana 3 · nov/2026 |
| GPU por hora (RunPod e afins) | 23.4, 37.9 | 2027, depois do primeiro fine-tuning de 8B; Pendrives, GPU e laboratório a partir da semana 2; Zoomcamp, dbt e Airflow junto do IA2 da Trilha de Dados e IA do vault (depois do Passo 8, ≈ 2028); dataset e treino do 8B junto do IA6 (≈ 2029) |
| Google Drive (seus documentos) | 0.5, 8.1, 21.8 | Antes de tudo · semana 1 (out/2026); Semanas 3 e 4 · nov/2026; Semana 6 · nov/2026 a dez/2026 |
| Repositório padrão | 20.1, 20.2 | Semana 5 · nov/2026 |
| Vigia semanal (GitHub Actions) | 25.1, 25.2 | Dez/2026 a jan/2027 |
| VM sempre ligada (Oracle grátis) | 22.9, 25.1, 25.4, 25.5 | Semana 6 · nov/2026 a dez/2026; Dez/2026 a jan/2027 |
| OpenRouter | 21.15 | Semana 6 · nov/2026 a dez/2026 |

### Aplicação: sistemas AM (Aura)

| Bloco | Passo | Quando |
|---|---|---|
| OpenAPI + Scalar | 34.1 | Junto dos Passos 4 a 6 da trilha de estudo (≈ mar a jun/2027): o modelo nasce no Passo 4 (API e login) e ganha testes e qualidade no Passo 6 |
| PostGIS + MapLibre | 42.3 | 2027 |
| Storybook | 34.1 | Junto dos Passos 4 a 6 da trilha de estudo (≈ mar a jun/2027): o modelo nasce no Passo 4 (API e login) e ganha testes e qualidade no Passo 6 |
| Clean Arch + DDD | 34.1 | Junto dos Passos 4 a 6 da trilha de estudo (≈ mar a jun/2027): o modelo nasce no Passo 4 (API e login) e ganha testes e qualidade no Passo 6 |
| EF Core + Npgsql | 34.1 | Junto dos Passos 4 a 6 da trilha de estudo (≈ mar a jun/2027): o modelo nasce no Passo 4 (API e login) e ganha testes e qualidade no Passo 6 |
| SignalR | 34.1 | Junto dos Passos 4 a 6 da trilha de estudo (≈ mar a jun/2027): o modelo nasce no Passo 4 (API e login) e ganha testes e qualidade no Passo 6 |
| Multi-tenant (RLS) | 34.1 | Junto dos Passos 4 a 6 da trilha de estudo (≈ mar a jun/2027): o modelo nasce no Passo 4 (API e login) e ganha testes e qualidade no Passo 6 |
| Testes: xUnit, Playwright, k6 | 34.1 | Junto dos Passos 4 a 6 da trilha de estudo (≈ mar a jun/2027): o modelo nasce no Passo 4 (API e login) e ganha testes e qualidade no Passo 6 |
| Serviços aura- (10) | 42.4 | 2027 |
| Next.js + Aura Design System | 34.1, 38.17 | Junto dos Passos 4 a 6 da trilha de estudo (≈ mar a jun/2027): o modelo nasce no Passo 4 (API e login) e ganha testes e qualidade no Passo 6; Fev a dez/2027, uma oferta por vez |
| API ASP.NET Core | 34.1, 38.17 | Junto dos Passos 4 a 6 da trilha de estudo (≈ mar a jun/2027): o modelo nasce no Passo 4 (API e login) e ganha testes e qualidade no Passo 6; Fev a dez/2027, uma oferta por vez |
| Keycloak / Entra ID | 34.2 | Junto dos Passos 4 a 6 da trilha de estudo (≈ mar a jun/2027): o modelo nasce no Passo 4 (API e login) e ganha testes e qualidade no Passo 6 |
| IA: RAG + pgvector | 41.1 | Depois do Passo 9 e do IA0 da Trilha de Dados e IA (≈ 2028), junto do IA5 |
| aura-licensing | 42.1 | 2027 |
| aura-status | 35.7 | Com o Passo 5 da trilha de estudo (≈ abr a jun/2027) para a conta e o deploy do sistema exemplo; o deploy de produção do AM Kaixara é o Passo 10 (≈ 2028) |
| AM Kaixara (PDV e cardápio) | 38.12, 42.2 | Fev a dez/2027, uma oferta por vez; 2027 |
| AM Rotara (entregas) | 42.3, 42.5 | 2027 |
| App mobile (.NET MAUI) | 46.6 | 2028 |

### Observabilidade

| Bloco | Passo | Quando |
|---|---|---|
| Sentry (erros) | 34.4 | Junto dos Passos 4 a 6 da trilha de estudo (≈ mar a jun/2027): o modelo nasce no Passo 4 (API e login) e ganha testes e qualidade no Passo 6 |
| Uptime Kuma | 10.6, 25.5 | Semana 4 · nov/2026; Dez/2026 a jan/2027 |
| Seq (logs) | 34.3 | Junto dos Passos 4 a 6 da trilha de estudo (≈ mar a jun/2027): o modelo nasce no Passo 4 (API e login) e ganha testes e qualidade no Passo 6 |
| Loki + Tempo | 46.3 | 2028 |
| OpenTelemetry | 34.3 | Junto dos Passos 4 a 6 da trilha de estudo (≈ mar a jun/2027): o modelo nasce no Passo 4 (API e login) e ganha testes e qualidade no Passo 6 |
| Prometheus | 34.3 | Junto dos Passos 4 a 6 da trilha de estudo (≈ mar a jun/2027): o modelo nasce no Passo 4 (API e login) e ganha testes e qualidade no Passo 6 |
| Grafana | 10.4, 31.4 | Semana 4 · nov/2026; Semana 11 · jan/2027 |
| .NET Aspire | 34.3 | Junto dos Passos 4 a 6 da trilha de estudo (≈ mar a jun/2027): o modelo nasce no Passo 4 (API e login) e ganha testes e qualidade no Passo 6 |

### Containers, Kubernetes e infra como código

| Bloco | Passo | Quando |
|---|---|---|
| Caddy (proxy + HTTPS) | 34.3 | Junto dos Passos 4 a 6 da trilha de estudo (≈ mar a jun/2027): o modelo nasce no Passo 4 (API e login) e ganha testes e qualidade no Passo 6 |
| Mailpit | 34.3 | Junto dos Passos 4 a 6 da trilha de estudo (≈ mar a jun/2027): o modelo nasce no Passo 4 (API e login) e ganha testes e qualidade no Passo 6 |
| Kafka | 46.1 | 2028 |
| kubectl · Helm · k9s | 46.2 | 2028 |
| Azure CLI · AWS CLI | 35.1 | Com o Passo 5 da trilha de estudo (≈ abr a jun/2027) para a conta e o deploy do sistema exemplo; o deploy de produção do AM Kaixara é o Passo 10 (≈ 2028) |
| Datomic local | 42.4 | 2027 |
| Docker + Compose | 4.2, 10.2 | Semana 2 · nov/2026; Semana 4 · nov/2026 |
| PostgreSQL | 10.2, 34.1 | Semana 4 · nov/2026; Junto dos Passos 4 a 6 da trilha de estudo (≈ mar a jun/2027): o modelo nasce no Passo 4 (API e login) e ganha testes e qualidade no Passo 6 |
| Redis | 34.1 | Junto dos Passos 4 a 6 da trilha de estudo (≈ mar a jun/2027): o modelo nasce no Passo 4 (API e login) e ganha testes e qualidade no Passo 6 |
| RabbitMQ | 46.1 | 2028 |
| Kubernetes local (kind) | 46.2 | 2028 |
| Terraform | 35.1, 35.3 | Com o Passo 5 da trilha de estudo (≈ abr a jun/2027) para a conta e o deploy do sistema exemplo; o deploy de produção do AM Kaixara é o Passo 10 (≈ 2028) |

### Claude: recursos, conectores e plugins

| Bloco | Passo | Quando |
|---|---|---|
| Projects + memória | 9.1 | Semana 4 · nov/2026 |
| Artifacts (Docs, Slides, Sheets…) | 9.1 | Semana 4 · nov/2026 |
| Pesquisa aprofundada | 9.1 | Semana 4 · nov/2026 |
| Tarefas agendadas | 9.1, 25.8 | Semana 4 · nov/2026; Dez/2026 a jan/2027 |
| Claude in Chrome + uso do computador | 3.6 | Semana 1 · out/2026 |
| Claude (assinatura e API) | 20.7, 21.9, 22.2, 27.2 | Semana 5 · nov/2026; Semana 6 · nov/2026 a dez/2026 |
| Conector Google (Gmail, Drive…) | 2.3, 9.2 | Semana 1 · out/2026 (o e-mail e as críticas); o resto, 5 contas por semana até dez/2026; Semana 4 · nov/2026 |
| Conectores Canva + Figma | 9.2, 28.4 | Semana 4 · nov/2026; Semana 5 · dez/2026 |
| Conector MailerLite | 9.2, 29.6 | Semana 4 · nov/2026; Semanas 6 e 7 · dez/2026 |
| Vercel · AWS · Microsoft Learn | 9.2 | Semana 4 · nov/2026 |
| Conector Upwork | 9.2 | Semana 4 · nov/2026 |
| Lovable + Supabase | 9.2 | Semana 4 · nov/2026 |
| Notion · monday · GitBook · Stripe | 9.2 | Semana 4 · nov/2026 |
| Plugins: small- business + marketing | 9.3 | Semana 4 · nov/2026 |
| Plugins: engineering + design | 9.3 | Semana 4 · nov/2026 |
| Plugins: finance + Fiscal.ai | 9.3 | Semana 4 · nov/2026 |
| Plugins: Hostinger · Adobe · Cloudinary | 9.3 | Semana 4 · nov/2026 |
| Conector Cloudflare | 9.2, 22.6 | Semana 4 · nov/2026; Semana 6 · nov/2026 a dez/2026 |
| Conector vidIQ | 9.2 | Semana 4 · nov/2026 |

### Assistentes de IA (chat, pesquisa e estudo)

| Bloco | Passo | Quando |
|---|---|---|
| Claude (app) | 9.1 | Semana 4 · nov/2026 |
| ChatGPT | 9.4, 21.8 | Semana 4 · nov/2026; Semana 6 · nov/2026 a dez/2026 |
| Gemini (pago) | 9.4, 21.8 | Semana 4 · nov/2026; Semana 6 · nov/2026 a dez/2026 |
| NotebookLM | 6.7, 21.9 | Semana 2 · nov/2026; Semana 6 · nov/2026 a dez/2026 |
| Grok | 9.4 | Semana 4 · nov/2026 |
| DeepSeek | 9.4 | Semana 4 · nov/2026 |
| Codex (OpenAI) | 9.4 | Semana 4 · nov/2026 |
| Agentes de código do Google | 9.4 | Semana 4 · nov/2026 |
| Perplexity | 9.4 | Semana 4 · nov/2026 |
| GitHub Copilot | 20.8, 22.1, 22.3, 49.1 | Semana 5 · nov/2026; Semana 6 · nov/2026 a dez/2026; Contínuo, desde a semana 2 |

### Dados e treino de IA

| Bloco | Passo | Quando |
|---|---|---|
| Python de dados (Polars, Jupyter) | 37.4 | Pendrives, GPU e laboratório a partir da semana 2; Zoomcamp, dbt e Airflow junto do IA2 da Trilha de Dados e IA do vault (depois do Passo 8, ≈ 2028); dataset e treino do 8B junto do IA6 (≈ 2029) |
| DuckDB + Parquet | 26.4, 37.4 | Com a primeira página de venda no ar (jan/2027) e por etapas; Pendrives, GPU e laboratório a partir da semana 2; Zoomcamp, dbt e Airflow junto do IA2 da Trilha de Dados e IA do vault (depois do Passo 8, ≈ 2028); dataset e treino do 8B junto do IA6 (≈ 2029) |
| dbt Core | 37.7 | Pendrives, GPU e laboratório a partir da semana 2; Zoomcamp, dbt e Airflow junto do IA2 da Trilha de Dados e IA do vault (depois do Passo 8, ≈ 2028); dataset e treino do 8B junto do IA6 (≈ 2029) |
| Airflow (orquestração) | 37.8 | Pendrives, GPU e laboratório a partir da semana 2; Zoomcamp, dbt e Airflow junto do IA2 da Trilha de Dados e IA do vault (depois do Passo 8, ≈ 2028); dataset e treino do 8B junto do IA6 (≈ 2029) |
| Spark (PySpark) | 37.4 | Pendrives, GPU e laboratório a partir da semana 2; Zoomcamp, dbt e Airflow junto do IA2 da Trilha de Dados e IA do vault (depois do Passo 8, ≈ 2028); dataset e treino do 8B junto do IA6 (≈ 2029) |
| Seus datasets (só conteúdo seu) | 37.10 | Pendrives, GPU e laboratório a partir da semana 2; Zoomcamp, dbt e Airflow junto do IA2 da Trilha de Dados e IA do vault (depois do Passo 8, ≈ 2028); dataset e treino do 8B junto do IA6 (≈ 2029) |
| PyTorch + CUDA (WSL2) | 37.3, 37.4 | Pendrives, GPU e laboratório a partir da semana 2; Zoomcamp, dbt e Airflow junto do IA2 da Trilha de Dados e IA do vault (depois do Passo 8, ≈ 2028); dataset e treino do 8B junto do IA6 (≈ 2029) |
| Hugging Face (modelos e Hub) | 37.9 | Pendrives, GPU e laboratório a partir da semana 2; Zoomcamp, dbt e Airflow junto do IA2 da Trilha de Dados e IA do vault (depois do Passo 8, ≈ 2028); dataset e treino do 8B junto do IA6 (≈ 2029) |
| Unsloth (QLoRA) | 37.11 | Pendrives, GPU e laboratório a partir da semana 2; Zoomcamp, dbt e Airflow junto do IA2 da Trilha de Dados e IA do vault (depois do Passo 8, ≈ 2028); dataset e treino do 8B junto do IA6 (≈ 2029) |
| Kaggle · Colab (GPU grátis) | 23.1, 23.3, 37.9, 37.11 | 2027, depois do primeiro fine-tuning de 8B; Pendrives, GPU e laboratório a partir da semana 2; Zoomcamp, dbt e Airflow junto do IA2 da Trilha de Dados e IA do vault (depois do Passo 8, ≈ 2028); dataset e treino do 8B junto do IA6 (≈ 2029) |
| MLflow (experimentos) | 37.4 | Pendrives, GPU e laboratório a partir da semana 2; Zoomcamp, dbt e Airflow junto do IA2 da Trilha de Dados e IA do vault (depois do Passo 8, ≈ 2028); dataset e treino do 8B junto do IA6 (≈ 2029) |
| Avaliação dos modelos | 37.10, 37.12 | Pendrives, GPU e laboratório a partir da semana 2; Zoomcamp, dbt e Airflow junto do IA2 da Trilha de Dados e IA do vault (depois do Passo 8, ≈ 2028); dataset e treino do 8B junto do IA6 (≈ 2029) |
| llama.cpp (GGUF) | 21.3, 37.4, 37.12 | Semana 6 · nov/2026 a dez/2026; Pendrives, GPU e laboratório a partir da semana 2; Zoomcamp, dbt e Airflow junto do IA2 da Trilha de Dados e IA do vault (depois do Passo 8, ≈ 2028); dataset e treino do 8B junto do IA6 (≈ 2029) |
| Paperless-ngx | 19.1, 19.2 | Dez/2026 |
| Grocy | 19.1, 19.3 | Dez/2026 |
| vLLM (GPU alugada) | 23.4, 23.5 | 2027, depois do primeiro fine-tuning de 8B |
| Destilação | 23.3 | 2027, depois do primeiro fine-tuning de 8B |
| Metabase (painéis) | 26.1 | Com a primeira página de venda no ar (jan/2027) e por etapas |
| Análises de cliente (RFM, LTV, churn) | 26.4 | Com a primeira página de venda no ar (jan/2027) e por etapas |

### Agentes de IA e sandbox

| Bloco | Passo | Quando |
|---|---|---|
| Modelos locais: Qwen · Gemma · Llama | 6.4, 21.4, 37.5 | Semana 2 · nov/2026; Semana 6 · nov/2026 a dez/2026; Pendrives, GPU e laboratório a partir da semana 2; Zoomcamp, dbt e Airflow junto do IA2 da Trilha de Dados e IA do vault (depois do Passo 8, ≈ 2028); dataset e treino do 8B junto do IA6 (≈ 2029) |
| Base de conhecimento (RAG) das suas notas | 6.7, 8.6, 25.7 | Semana 2 · nov/2026; Semanas 3 e 4 · nov/2026; Dez/2026 a jan/2027 |
| Claude Code | 6.1, 22.5 | Semana 2 · nov/2026; Semana 6 · nov/2026 a dez/2026 |
| ai-jail | 6.2 | Semana 2 · nov/2026 |
| ai-memory | 6.6, 21.13 | Semana 2 · nov/2026; Semana 6 · nov/2026 a dez/2026 |
| Servidores MCP | 6.5, 21.6 | Semana 2 · nov/2026; Semana 6 · nov/2026 a dez/2026 |
| CLAUDE.md, agentes e skills (seus) | 6.3, 21.10 | Semana 2 · nov/2026; Semana 6 · nov/2026 a dez/2026 |
| Ollama | 6.4, 21.4, 37.5, 37.12 | Semana 2 · nov/2026; Semana 6 · nov/2026 a dez/2026; Pendrives, GPU e laboratório a partir da semana 2; Zoomcamp, dbt e Airflow junto do IA2 da Trilha de Dados e IA do vault (depois do Passo 8, ≈ 2028); dataset e treino do 8B junto do IA6 (≈ 2029) |
| Gateway de modelos (LiteLLM) | 21.1, 21.7, 21.11, 21.15, 22.7, 23.5, 25.5 | Semana 6 · nov/2026 a dez/2026; 2027, depois do primeiro fine-tuning de 8B; Dez/2026 a jan/2027 |
| Evals dos agentes (promptfoo) | 21.2, 21.7, 23.3, 25.7 | Semana 6 · nov/2026 a dez/2026; 2027, depois do primeiro fine-tuning de 8B; Dez/2026 a jan/2027 |
| MCP próprio (seus dados) | 21.6 | Semana 6 · nov/2026 a dez/2026 |
| Claude Agent SDK | 21.5 | Semana 6 · nov/2026 a dez/2026 |
| Cluster de IA na rede | 23.2 | 2027, depois do primeiro fine-tuning de 8B |
| ai-usagebar (Akita) | 21.14 | Semana 6 · nov/2026 a dez/2026 |
| Pacote de contexto + ESTADO.md | 21.12 | Semana 6 · nov/2026 a dez/2026 |
| Strata (MoE grande) | 23.6 | 2027, depois do primeiro fine-tuning de 8B |
| OpenClaw (agente 24 h) | 22.9 | Semana 6 · nov/2026 a dez/2026 |

### Linux (Ubuntu no WSL2, Arch no 2º disco)

| Bloco | Passo | Quando |
|---|---|---|
| Neovim | 40.2 | 2027, conforme cada compra |
| nmap · dig · curl | 4.4 | Semana 2 · nov/2026 |
| Ubuntu (WSL2) | 4.1, 4.5 | Semana 2 · nov/2026 |
| Git + SSH + gh | 4.4, 4.6 | Semana 2 · nov/2026 |
| .NET 10 · Node · Python | 4.4 | Semana 2 · nov/2026 |
| TeX Live | 4.4 | Semana 2 · nov/2026 |
| gitleaks · Trivy | 4.4, 20.2, 20.3 | Semana 2 · nov/2026; Semana 5 · nov/2026 |
| dotfiles | 4.7 | Semana 2 · nov/2026 |
| Arch + Omarchy (2º NVMe) | 40.1 | 2027, conforme cada compra |
| Rotinas agendadas | 17.3, 17.4, 17.5 | Semana 4 · nov/2026 |
| AdGuard Home (DNS) | 24.4 | Semana 6 · nov/2026 |
| WireGuard (na mão) | 24.6 | Semana 6 · nov/2026 |

### Windows 11, apps e máquinas virtuais

| Bloco | Passo | Quando |
|---|---|---|
| Tailscale (VPN) | 23.2, 24.1, 24.2, 25.4, 38.11, 47.2 | 2027, depois do primeiro fine-tuning de 8B; Semana 6 · nov/2026; Dez/2026 a jan/2027; Fev a dez/2027, uma oferta por vez; 2028, quando o grupo pedir |
| .wslconfig + localhost | 3.2 | Semana 1 · out/2026 |
| Terminal · PowerShell · winget | 3.2 | Semana 1 · out/2026 |
| Excalidraw / draw.io | 3.2 | Semana 1 · out/2026 |
| Unity · Cocos | 3.8 | Semana 1 · out/2026 |
| Gerenciador de boot | 40.1 | 2027, conforme cada compra |
| NitroSense + drivers AMD e NVIDIA | 1.3 | Semana 1 · out/2026 |
| 7-Zip | 3.2 | Semana 1 · out/2026 |
| PowerToys | 3.2 | Semana 1 · out/2026 |
| SumatraPDF | 3.2 | Semana 1 · out/2026 |
| ShareX | 3.2 | Semana 1 · out/2026 |
| LibreOffice | 3.2 | Semana 1 · out/2026 |
| Firefox (2º navegador) | 3.2 | Semana 1 · out/2026 |
| Windows 11 Home | 0.3, 0.4, 1.3 | Antes de tudo · semana 1 (out/2026); Semana 1 · out/2026 |
| VS Code | 3.2, 3.5 | Semana 1 · out/2026 |
| Obsidian + Git | 3.2, 4.8, 8.4 | Semana 1 · out/2026; Semana 2 · nov/2026; Semanas 3 e 4 · nov/2026 |
| Syncthing | 2.9, 3.2, 4.9, 24.3 | Semana 1 · out/2026 (o e-mail e as críticas); o resto, 5 contas por semana até dez/2026; Semana 1 · out/2026; Semana 2 · nov/2026; Semana 6 · nov/2026 |
| DBeaver · Bruno | 3.2 | Semana 1 · out/2026 |
| Navegador + Claude in Chrome | 2.5, 2.10, 3.6 | Semana 1 · out/2026 (o e-mail e as críticas); o resto, 5 contas por semana até dez/2026; Semana 1 · out/2026 |
| VirtualBox | 3.2 | Semana 1 · out/2026 |
| Wireshark | 3.2 | Semana 1 · out/2026 |
| VMs: Kali · Arch · Servidores | 40.3 | 2027, conforme cada compra |
| Arduino IDE 2 | 3.2, 38.16 | Semana 1 · out/2026; Fev a dez/2027, uma oferta por vez |
| Rufus (grava pendrives) | 37.1 | Pendrives, GPU e laboratório a partir da semana 2; Zoomcamp, dbt e Airflow junto do IA2 da Trilha de Dados e IA do vault (depois do Passo 8, ≈ 2028); dataset e treino do 8B junto do IA6 (≈ 2029) |
| ActivityWatch | 17.1 | Semana 4 · nov/2026 |

### Segurança e cofre

| Bloco | Passo | Quando |
|---|---|---|
| Commits assinados (chave SSH) | 4.6, 32.1 | Semana 2 · nov/2026; Semana 11 · jan/2027 |
| restic (backup criptografado) | 7.1, 7.4, 10.7 | Semana 3 · nov/2026; Semana 4 · nov/2026 |
| Chave física (YubiKey) | 40.5 | 2027, conforme cada compra |
| TPM + Secure Boot | 3.3 | Semana 1 · out/2026 |
| BitLocker | 3.3 | Semana 1 · out/2026 |
| Defender + Firewall | 3.4 | Semana 1 · out/2026 |
| KeePassXC | 2.1, 2.2, 2.3, 2.4, 2.5, 2.6, 2.7, 2.8, 2.9, 2.10, 2.11, 2.12, 2.13, 2.14, 2.15, 2.16, 18.1 | Semana 1 · out/2026 (o e-mail e as críticas); o resto, 5 contas por semana até dez/2026; Semana 5 · nov/2026 |
| App 2FA (celular) | 1.4, 2.3, 2.7 | Semana 1 · out/2026; Semana 1 · out/2026 (o e-mail e as críticas); o resto, 5 contas por semana até dez/2026 |
| Backup 3-2-1 | 2.11, 7.1, 7.2, 7.3, 8.2 | Semana 1 · out/2026 (o e-mail e as críticas); o resto, 5 contas por semana até dez/2026; Semana 3 · nov/2026; Semanas 3 e 4 · nov/2026 |
| Organizadores | 2.4, 17.2 | Semana 1 · out/2026 (o e-mail e as críticas); o resto, 5 contas por semana até dez/2026; Semana 4 · nov/2026 |
| Segredos do cofre (keepassxc-cli) | 20.4 | Semana 5 · nov/2026 |
| Teste de restauração | 20.5 | Semana 5 · nov/2026 |

### Hardware

| Bloco | Passo | Quando |
|---|---|---|
| Nobreak | 1.2 | Semana 1 · out/2026 |
| Base com cooler | 1.2 | Semana 1 · out/2026 |
| SSD SATA 2,5" | 40.4 | 2027, conforme cada compra |
| Acer Nitro (32 GB, GTX 1650) | 0.2, 1.2 | Antes de tudo · semana 1 (out/2026); Semana 1 · out/2026 |
| 2º NVMe (1–4 TB) | 40.1 | 2027, conforme cada compra |
| 2º monitor | 1.2 | Semana 1 · out/2026 |
| Microfone + câmera | 40.6 | 2027, conforme cada compra |
| Celular | 1.2, 2.9, 4.9 | Semana 1 · out/2026; Semana 1 · out/2026 (o e-mail e as críticas); o resto, 5 contas por semana até dez/2026; Semana 2 · nov/2026 |
| Disco externo | 1.1, 1.2, 2.11, 7.1 | Semana 1 · out/2026; Semana 1 · out/2026 (o e-mail e as críticas); o resto, 5 contas por semana até dez/2026; Semana 3 · nov/2026 |
| Pendrive Kali (persistência) | 37.1 | Pendrives, GPU e laboratório a partir da semana 2; Zoomcamp, dbt e Airflow junto do IA2 da Trilha de Dados e IA do vault (depois do Passo 8, ≈ 2028); dataset e treino do 8B junto do IA6 (≈ 2029) |
| Pendrive Arch (instalação portátil) | 37.2 | Pendrives, GPU e laboratório a partir da semana 2; Zoomcamp, dbt e Airflow junto do IA2 da Trilha de Dados e IA do vault (depois do Passo 8, ≈ 2028); dataset e treino do 8B junto do IA6 (≈ 2029) |
| Arduino · ESP32 · Pi | 1.2, 38.16 | Semana 1 · out/2026; Fev a dez/2027, uma oferta por vez |
| Servidor caseiro (NAS + serviços) | 47.1 | 2028, quando o grupo pedir |
| SSD externo (USB-C 10 Gbps) | 1.2 | Semana 1 · out/2026 |
| Workstation com GPU | 23.6, 47.3 | 2027, depois do primeiro fine-tuning de 8B; 2028, quando o grupo pedir |
| Home Assistant | 19.1, 19.6 | Dez/2026 |
