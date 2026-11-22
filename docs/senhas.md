<!-- Arquivo GERADO por tools/senhas/senhas.py (ecossistema.json + infra/**/*.env.example + data/senhas.json). Não edite à mão. -->

# Senhas do setup: o que guardar e como cada uma é preenchida

150 itens: 114 contas em sites, 20 segredos que o setup gera, 5 chaves de provedores, 4 chaves e tokens, 6 anotações e 1 que fica só na memória. Nenhuma senha aparece aqui.

Para ver o que já está no cofre e o que falta: `just senhas`. Para pegar uma senha: `just senha NOME`.

| Como preencher | Quando usar |
|---|---|
| conta | extensão KeePassXC-Browser: preenche no login e oferece salvar a senha nova |
| gerar | o setup gera (just senhas-criar) e entrega ao serviço (just senhas-rodar) |
| externa | pegue no site do provedor e guarde no cofre; o terminal usa com just senhas-rodar |
| chave | guarde no cofre; o comando que usa lê do cofre sozinho |
| ssh | KeePassXC como agente SSH (passo kp-ssh) |
| anotacao | entrada no cofre com o texto em Notas |
| memoria | fora do cofre, de propósito |

## 00 Essenciais (e-mail e contas-mãe)

| Item | Tipo | Observação |
|---|---|---|
| Microsoft (Azure) | conta | Conta de estudo com alerta de orçamento. Use e-mail da empresa. |
| Celular (conta Google ou Apple e PIN) | anotacao | PIN e conta do aparelho. |
| Chave de recuperação do BitLocker | anotacao | Sem ela, um problema no Windows pode trancar o disco para sempre. |
| Códigos de backup do 2FA (Google, GitHub, Microsoft) | anotacao | Uma entrada por conta, com os códigos no campo Notas. |
| Senha mestra do cofre (KeePassXC) | memoria | Só na sua cabeça e numa folha guardada em casa. Nunca dentro do próprio cofre. |
| Windows do notebook (PIN e conta Microsoft) | anotacao | O Windows Hello usa este PIN. |

## 01 Bancos e dinheiro

| Item | Tipo | Observação |
|---|---|---|
| Akaunting (contabilidade CNPJ) | conta |  |
| API de NFS-e (ex.: Focus NFe) | conta |  |
| B3 Investidor (Área do Investidor) | conta |  |
| Bancos (uma entrada por banco) | conta | Senha do app, do internet banking e a eletrônica, cada uma no seu campo. |
| Certificado digital (e-CNPJ) | conta |  |
| Corretora de investimentos | conta | Inclui a assinatura eletrônica. |
| Firefly III (reserva) | conta |  |
| Ghostfolio (painel do patrimônio) | conta |  |
| Mercado Pago | conta | Pix e cartão para serviços e aulas. |
| Tesouro Direto | conta |  |

## 02 Governo

| Item | Tipo | Observação |
|---|---|---|
| CNH Digital / Detran-MG | conta |  |
| Conta bancária separada | conta | Banco digital sem mensalidade, só para as vendas. |
| gov.br (prata ou ouro) | conta | Acesso ao carnê-leão online e ao IR. |
| INEP · Página do Participante (ENEM 2027) | conta | Entra pelo gov.br; a inscrição pede o login. |
| INPI | conta | Registro da marca Editora AMS Silva. |
| Meu INSS | conta | Entra pelo gov.br. |

## 03 Escola (só os seus acessos)

| Item | Tipo | Observação |
|---|---|---|
| DED+ (diário escolar) | conta | Só o seu acesso de professor; nada de dados de aluno no cofre. |
| Google Classroom da escola | conta |  |
| SEE-MG (portal e e-mail institucional) | conta |  |

## 04 Grupo AMtech Digital

| Item | Tipo | Observação |
|---|---|---|
| BookStack (manuais dos clientes) | conta |  |
| Cal.com e Discord | conta | Agenda com pagamento para as aulas e a comunidade dos alunos. |
| Canva | conta | Grátis para começar; Krita e Inkscape cobrem o resto. |
| Cloudflare | conta | DNS, HTTPS, Pages para os sites comerciais e redirecionamento de e-mail. Plano grátis. |
| E-mail profissional (enviar e receber) | conta |  |
| E-mail transacional (Resend, SES…) | conta |  |
| ERPNext (negócios físicos) | conta |  |
| Formbricks (NPS e pesquisas) | conta |  |
| Gerenciador de Negócios da Meta | conta | Pixel, API de Conversões e conta de anúncios; uma conta só. |
| Google Ads | conta | Pesquisa e YouTube; tag do Google no site. |
| Hostinger | conta | Você já tem; útil para sites WordPress de clientes. |
| Mercado Envios Flex | conta |  |
| Pinterest Ads | conta | Confira se a conta aceita o Brasil. |
| Plane (projetos de cliente) | conta |  |
| Plausible (reserva do Umami) | conta |  |
| PostHog (funil e gravações) | conta |  |
| Registro.br | conta | Domínio .com.br no CNPJ (ou CPF até abrir a empresa). |
| Taboola ou Outbrain | conta | Mídia nativa, para artigos do blog. |
| Umami | conta | Visitas dos sites sem cookies invasivos: Umami Cloud grátis ou rodando no seu servidor. |
| WhatsApp Business | conta | Número separado do pessoal, se possível. |

## 05 Instituto e Editora

| Item | Tipo | Observação |
|---|---|---|
| Acervos de imagens (APIs) | conta |  |
| Afiliados (Amazon, Hotmart…) | conta |  |
| Alura · Rocketseat · DIO · Udemy | conta |  |
| Amazon KDP | conta | Ebook e impressão sob demanda; dados fiscais para receber do exterior. |
| CBL (plataforma de ISBN) | conta | ISBN e código de barras; confira se aceita CPF. |
| DIO | conta | Perfil ativo com artigos e projetos para buscar a parceria. |
| Eduzz | conta |  |
| HeyForm (qualifica o orçamento) | conta |  |
| Hotmart, Kiwify e Eduzz | conta | Todas aceitam CPF. Compare as taxas atuais; lance o mini-curso em uma por vez. |
| ISBN + código de barras (CBL) | conta |  |
| Kiwify | conta |  |
| MailerLite | conta | Newsletter; plano grátis já decidido. |
| Pix Automático + gateway (ex.: Asaas) | conta |  |
| Polar (venda internacional) | conta |  |
| Udemy | conta | Conta de instrutor, PayPal ou Payoneer e o formulário fiscal dos EUA. |

## 06 Código e nuvem

| Item | Tipo | Observação |
|---|---|---|
| AWS | conta | Quando chegar a etapa 2 de nuvem. Ative alerta de custo no primeiro dia. |
| Azure | conta |  |
| Backblaze | conta | Backup fora de casa; ative alerta de custo. |
| bore (túnel TCP próprio) | conta |  |
| Coolify (apps de cliente em VPS) | conta |  |
| Docker Hub | conta | Opcional; o GHCR já resolve. |
| Dokploy (reserva do Coolify) | conta |  |
| Forgejo (espelho dos repositórios) | conta |  |
| GitHub | conta | Código, portfólio, Actions, Pages. Grátis. |
| GlitchTip (erros dos sistemas) | conta |  |
| GPU por hora (RunPod e afins) | conta |  |
| Headscale (rede própria) | conta |  |
| OpenRouter | conta |  |
| Plunk (e-mail próprio no SES) | conta |  |
| Sentry (erros) | conta |  |
| SigNoz (logs, traces e métricas) | conta |  |
| SonarQube Cloud | conta |  |
| Speckle (modelos na web) | conta |  |
| Tailscale | conta | Rede privada entre as máquinas; plano grátis. |
| Vercel | conta | Frontends de estudo e portfólio. Confira os termos antes de usar para venda. |
| VM sempre ligada (Oracle grátis) | conta |  |
| Chave SSH do GitHub (login e assinatura) | ssh | O KeePassXC entrega a chave ao agente SSH quando o cofre abre. |

## 07 IA

| Item | Tipo | Observação |
|---|---|---|
| ChatGPT (OpenAI) | conta | Plano grátis. |
| Claude (Anthropic) | conta | Assinatura que você já tem; API à parte para os sistemas. |
| Claude · segunda conta (a do Claude Code) | conta | A conta que faz a instalação do setup. |
| Codex (OpenAI) | conta |  |
| DeepSeek | conta | Grátis; nunca envie dados sensíveis. |
| ElevenLabs | conta | Plano Creator para clonar a própria voz; 2FA obrigatório. |
| Gemini (pago) | conta |  |
| Grok (xAI) | conta | Grátis com limite. |
| Hugging Face (modelos e Hub) | conta |  |
| NotebookLM | conta |  |
| Perplexity | conta | Grátis. |
| Hugging Face (token só de leitura) | chave |  |

## 08 Redes

| Item | Tipo | Observação |
|---|---|---|
| Comunidade (Discord ou grupo) | conta |  |
| Facebook | conta |  |
| Instagram (conta profissional) | conta | Canal principal de venda. |
| Kwai Ads | conta | Depois de Meta e TikTok. |
| LinkedIn Campaign Manager | conta | Só para B2B. |
| Telegram | conta | Bot de avisos: peça pronta para aprovar e serviço fora do ar. |
| TikTok e Facebook | conta | Perfis da marca, separados dos pessoais. |
| YouTube | conta |  |
| WhatsApp pessoal (PIN da verificação em duas etapas) | anotacao |  |

## 09 Estudo

| Item | Tipo | Observação |
|---|---|---|
| 42 São Paulo (intra e processo seletivo) | conta |  |
| Anki | conta |  |
| BugHunt · HackerOne (bug bounty) | conta |  |
| Duolingo ou plataforma de idiomas | conta |  |
| Faculdade de ADS (portal: diploma e histórico) | conta | Guarde mesmo formado: diploma e histórico. |
| Finclass | conta |  |
| Kaggle · Colab (GPU grátis) | conta |  |
| Licenciatura em Matemática (portal do aluno) | conta | Troque o nome pela faculdade quando guardar. |
| PortSwigger Web Security Academy | conta |  |
| Rocketseat | conta |  |
| TryHackMe / Hack The Box | conta |  |

## 10 Compras e assinaturas

| Item | Tipo | Observação |
|---|---|---|
| Autodesk educacional (Revit, Civil 3D) | conta |  |
| Compras (Mercado Livre, Shopee, Amazon) | conta |  |
| Operadora do celular | conta |  |
| Ponto de retirada (Shopee e ML) | conta |  |
| Spotify Ad Studio | conta | Áudio e podcast, para marca. |
| Streaming e assinaturas pessoais | conta |  |

## 12 Carreira e vagas

| Item | Tipo | Observação |
|---|---|---|
| Vagas (LinkedIn Jobs, Gupy e afins) | conta |  |

## 20 Setup técnico

| Item | Tipo | Observação |
|---|---|---|
| Wi-Fi de casa e roteador (admin) | conta | O roteador sai do usuário e senha de fábrica. |
| automacao · GRAFANA_DB_SENHA | gerar | `20 Setup técnico/automacao/GRAFANA_DB_SENHA` |
| automacao · GRAFANA_SENHA | gerar | `20 Setup técnico/automacao/GRAFANA_SENHA` |
| automacao · METRICAS_SENHA | gerar | `20 Setup técnico/automacao/METRICAS_SENHA` |
| automacao · N8N_CHAVE | gerar | `20 Setup técnico/automacao/N8N_CHAVE` |
| Bot do Telegram (token do @BotFather) | chave | Usado pelo amtech-bot da fila de pedidos. |
| casa · PAPERLESS_SECRET | gerar | `20 Setup técnico/casa/PAPERLESS_SECRET` |
| Chave do age (arquivos cifrados) | anotacao |  |
| ia · ANTHROPIC_API_KEY | externa | `20 Setup técnico/ia/ANTHROPIC_API_KEY` |
| ia · CLOUDFLARE_API_KEY | externa | `20 Setup técnico/ia/CLOUDFLARE_API_KEY` |
| ia · DEEPSEEK_API_KEY | externa | `20 Setup técnico/ia/DEEPSEEK_API_KEY` |
| ia · GEMINI_API_KEY | externa | `20 Setup técnico/ia/GEMINI_API_KEY` |
| ia · LITELLM_MASTER_KEY | gerar | `20 Setup técnico/ia/LITELLM_MASTER_KEY` |
| ia · OPENROUTER_API_KEY | externa | `20 Setup técnico/ia/OPENROUTER_API_KEY` |
| jarvis · FRIGATE_RTSP_SENHA | gerar | `20 Setup técnico/jarvis/FRIGATE_RTSP_SENHA` |
| Senha da sala limpa (gocryptfs) | gerar | Pedida pelo just lab-abrir. |
| Senha do backup (restic) | gerar | Perder esta senha é perder o backup inteiro. |
| soberania · AKAUNTING_ADMIN_SENHA | gerar | `20 Setup técnico/soberania/AKAUNTING_ADMIN_SENHA` |
| soberania · AKAUNTING_DB_SENHA | gerar | `20 Setup técnico/soberania/AKAUNTING_DB_SENHA` |
| soberania · BOOKSTACK_APP_KEY | gerar | `20 Setup técnico/soberania/BOOKSTACK_APP_KEY` |
| soberania · BOOKSTACK_DB_SENHA | gerar | `20 Setup técnico/soberania/BOOKSTACK_DB_SENHA` |
| soberania · FIREFLY_APP_KEY | gerar | `20 Setup técnico/soberania/FIREFLY_APP_KEY` |
| soberania · FIREFLY_DB_SENHA | gerar | `20 Setup técnico/soberania/FIREFLY_DB_SENHA` |
| soberania · GHOSTFOLIO_DB_SENHA | gerar | `20 Setup técnico/soberania/GHOSTFOLIO_DB_SENHA` |
| soberania · GHOSTFOLIO_REDIS_SENHA | gerar | `20 Setup técnico/soberania/GHOSTFOLIO_REDIS_SENHA` |
| soberania · GLITCHTIP_CHAVE | gerar | `20 Setup técnico/soberania/GLITCHTIP_CHAVE` |
| soberania · GLITCHTIP_DB_SENHA | gerar | `20 Setup técnico/soberania/GLITCHTIP_DB_SENHA` |
| soberania · SOFTSERVE_CHAVE_ADMIN | gerar | `20 Setup técnico/soberania/SOFTSERVE_CHAVE_ADMIN` |

## GitHub

| Item | Tipo | Observação |
|---|---|---|
| GitHub · chave gh-admin (visibilidade dos repositórios) | chave | Fine-grained, Administration: Read and write, 90 dias. Usada por just repos-visibilidade. |
