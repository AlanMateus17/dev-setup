<!-- Arquivo GERADO por tools/senhas/senhas.py (ecossistema.json + infra/**/*.env.example + data/senhas.json). Não edite à mão. -->

# Senhas do setup: o que guardar e como cada uma é preenchida

263 itens: 227 contas em sites, 20 segredos que o setup gera, 5 chaves de provedores, 4 chaves e tokens, 6 anotações e 1 que fica só na memória. Nenhuma senha aparece aqui.

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
| Avenue (corretora nos EUA) | conta | achada no seu e-mail |
| B3 Investidor (Área do Investidor) | conta |  |
| Bancos (uma entrada por banco) | conta | Senha do app, do internet banking e a eletrônica, cada uma no seu campo. |
| Binance | conta | achada no seu e-mail |
| Bity (cripto) | conta | achada no seu e-mail |
| Blockchain.com (carteira) | conta | achada no seu e-mail |
| Caixa (login Caixa) | conta | achada no seu e-mail |
| Certificado digital (e-CNPJ) | conta |  |
| Corretora de investimentos | conta | Inclui a assinatura eletrônica. |
| Firefly III (reserva) | conta |  |
| Ghostfolio (painel do patrimônio) | conta |  |
| Grão | conta | achada no seu e-mail |
| Honda Serviços Financeiros | conta | achada no seu e-mail |
| Itaú | conta | achada no seu e-mail |
| Link (pagamentos da Stripe) | conta | achada no seu e-mail |
| Mercado Pago | conta | Pix e cartão para serviços e aulas. |
| Nubank | conta | achada no seu e-mail |
| PayPal | conta | achada no seu e-mail |
| PicPay | conta | achada no seu e-mail |
| Rico | conta | achada no seu e-mail |
| Tesouro Direto | conta |  |
| TradingView | conta | achada no seu e-mail |
| XP Investimentos | conta | achada no seu e-mail |

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
| Prodemge (acesso do Estado de MG) | conta | achada no seu e-mail |
| SEE-MG (portal e e-mail institucional) | conta |  |

## 04 Grupo AMtech Digital

| Item | Tipo | Observação |
|---|---|---|
| All in One SEO | conta | achada no seu e-mail |
| Artlist | conta | achada no seu e-mail |
| Astra / Brainstorm Force | conta | achada no seu e-mail |
| Atlassian (Jira e Confluence) | conta | achada no seu e-mail |
| beehiiv | conta | achada no seu e-mail |
| Behance (Adobe) | conta | achada no seu e-mail |
| BookStack (manuais dos clientes) | conta |  |
| Brevo | conta | achada no seu e-mail |
| Cal.com e Discord | conta | Agenda com pagamento para as aulas e a comunidade dos alunos. |
| Calendly | conta | achada no seu e-mail |
| Canva | conta | Grátis para começar; Krita e Inkscape cobrem o resto. |
| Cloudflare | conta | DNS, HTTPS, Pages para os sites comerciais e redirecionamento de e-mail. Plano grátis. |
| Creately | conta | achada no seu e-mail |
| Design.com | conta | achada no seu e-mail |
| Dovetail | conta | achada no seu e-mail |
| E-mail profissional (enviar e receber) | conta |  |
| E-mail transacional (Resend, SES…) | conta |  |
| Elementor | conta | achada no seu e-mail |
| ERPNext (negócios físicos) | conta |  |
| Figma | conta | achada no seu e-mail |
| Formbricks (NPS e pesquisas) | conta |  |
| Gerenciador de Negócios da Meta | conta | Pixel, API de Conversões e conta de anúncios; uma conta só. |
| GetQR | conta | achada no seu e-mail |
| GitBook | conta | achada no seu e-mail |
| Google Ads | conta | Pesquisa e YouTube; tag do Google no site. |
| Hostinger | conta | Você já tem; útil para sites WordPress de clientes. |
| KineMaster | conta | achada no seu e-mail |
| Lumin PDF | conta | achada no seu e-mail |
| Mercado Envios Flex | conta |  |
| Napkin AI | conta | achada no seu e-mail |
| Notion | conta | achada no seu e-mail |
| Nuvemshop | conta | achada no seu e-mail |
| Pinterest Ads | conta | Confira se a conta aceita o Brasil. |
| Plane (projetos de cliente) | conta |  |
| Plausible (reserva do Umami) | conta |  |
| PostHog (funil e gravações) | conta |  |
| Registro.br | conta | Domínio .com.br no CNPJ (ou CPF até abrir a empresa). |
| Resend | conta | achada no seu e-mail |
| Taboola ou Outbrain | conta | Mídia nativa, para artigos do blog. |
| Umami | conta | Visitas dos sites sem cookies invasivos: Umami Cloud grátis ou rodando no seu servidor. |
| Vecteezy | conta | achada no seu e-mail |
| vidIQ | conta | achada no seu e-mail |
| WhatsApp Business | conta | Número separado do pessoal, se possível. |
| Wondershare (Filmora) | conta | achada no seu e-mail |
| Wordfence | conta | achada no seu e-mail |
| WordPress.com | conta | achada no seu e-mail |
| WPForms | conta | achada no seu e-mail |
| WPS Office | conta | achada no seu e-mail |
| Zoom | conta | achada no seu e-mail |

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
| Stripe | conta | achada no seu e-mail |
| Udemy | conta | Conta de instrutor, PayPal ou Payoneer e o formulário fiscal dos EUA. |

## 06 Código e nuvem

| Item | Tipo | Observação |
|---|---|---|
| AWS | conta | Quando chegar a etapa 2 de nuvem. Ative alerta de custo no primeiro dia. |
| Azure | conta |  |
| Backblaze | conta | Backup fora de casa; ative alerta de custo. |
| bore (túnel TCP próprio) | conta |  |
| Cloud Clusters | conta | achada no seu e-mail |
| CodePen | conta | achada no seu e-mail |
| Coolify (apps de cliente em VPS) | conta |  |
| Cursor | conta | achada no seu e-mail |
| Disqus | conta | achada no seu e-mail |
| Docker Hub | conta | Opcional; o GHCR já resolve. |
| Dokploy (reserva do Coolify) | conta |  |
| Forgejo (espelho dos repositórios) | conta |  |
| GDG (Google Developer Groups) | conta | achada no seu e-mail |
| GitHub | conta | Código, portfólio, Actions, Pages. Grátis. |
| GitKraken | conta | achada no seu e-mail |
| GitLab | conta | achada no seu e-mail |
| GlitchTip (erros dos sistemas) | conta |  |
| GPU por hora (RunPod e afins) | conta |  |
| Headscale (rede própria) | conta |  |
| HomeByMe (3D) | conta | achada no seu e-mail |
| OpenRouter | conta |  |
| Plunk (e-mail próprio no SES) | conta |  |
| Prisma | conta | achada no seu e-mail |
| QuickNode (nó de blockchain) | conta | achada no seu e-mail |
| Sentry (erros) | conta |  |
| SigNoz (logs, traces e métricas) | conta |  |
| SonarQube Cloud | conta |  |
| Speckle (modelos na web) | conta |  |
| Supabase | conta | achada no seu e-mail |
| Tabnine | conta | achada no seu e-mail |
| Tailscale | conta | Rede privada entre as máquinas; plano grátis. |
| Unity | conta | achada no seu e-mail |
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
| Google AI Studio | conta | achada no seu e-mail |
| Grok (xAI) | conta | Grátis com limite. |
| Hugging Face (modelos e Hub) | conta |  |
| NotebookLM | conta |  |
| OpenAI (ChatGPT) | conta | achada no seu e-mail |
| Perplexity | conta | Grátis. |
| TurboScribe | conta | achada no seu e-mail |
| Hugging Face (token só de leitura) | chave |  |

## 08 Redes

| Item | Tipo | Observação |
|---|---|---|
| Comunidade (Discord ou grupo) | conta |  |
| Facebook | conta |  |
| Globo (conta Globo) | conta | achada no seu e-mail |
| Instagram (conta profissional) | conta | Canal principal de venda. |
| Kwai Ads | conta | Depois de Meta e TikTok. |
| LinkedIn Campaign Manager | conta | Só para B2B. |
| Telegram | conta | Bot de avisos: peça pronta para aprovar e serviço fora do ar. |
| TikTok e Facebook | conta | Perfis da marca, separados dos pessoais. |
| X (Twitter) | conta | achada no seu e-mail |
| YouTube | conta |  |
| WhatsApp pessoal (PIN da verificação em duas etapas) | anotacao |  |

## 09 Estudo

| Item | Tipo | Observação |
|---|---|---|
| 42 São Paulo (intra e processo seletivo) | conta |  |
| Academia.edu | conta | achada no seu e-mail |
| Acervo Lins (livros do VHSlins) | conta | achada no seu e-mail |
| ADS · Estácio (matrícula de 2023: diploma e histórico) | conta | Guarde mesmo formado: diploma, histórico e o e-mail @alunos.estacio.br. |
| Alfa Concursos | conta | achada no seu e-mail |
| ANBIMA Edu (certificações) | conta | achada no seu e-mail |
| Anki | conta |  |
| AnkiWeb | conta | achada no seu e-mail |
| BugHunt · HackerOne (bug bounty) | conta |  |
| CodeChef | conta | achada no seu e-mail |
| Coursera | conta | achada no seu e-mail |
| Curso em Vídeo | conta | achada no seu e-mail |
| DataCamp | conta | achada no seu e-mail |
| DevBase | conta | achada no seu e-mail |
| Duolingo ou plataforma de idiomas | conta |  |
| Finclass | conta |  |
| GeeksforGeeks | conta | achada no seu e-mail |
| Guru99 | conta | achada no seu e-mail |
| Hashtag Treinamentos | conta | achada no seu e-mail |
| Hot Reload | conta | achada no seu e-mail |
| Kaggle · Colab (GPU grátis) | conta |  |
| LabEx | conta | achada no seu e-mail |
| Licenciatura em Matemática · Estácio (matrícula de 2025) | conta | Portal do aluno e e-mail @alunos.estacio.br desta matrícula. |
| PortSwigger Web Security Academy | conta |  |
| Reverso | conta | achada no seu e-mail |
| roadmap.sh | conta | achada no seu e-mail |
| Rocketseat | conta |  |
| Scribd | conta | achada no seu e-mail |
| TryHackMe / Hack The Box | conta |  |

## 10 Compras e assinaturas

| Item | Tipo | Observação |
|---|---|---|
| Acer (registro do notebook) | conta | achada no seu e-mail |
| AliExpress | conta | achada no seu e-mail |
| AppBarber | conta | achada no seu e-mail |
| Authy (2FA) | conta | achada no seu e-mail |
| Autodesk educacional (Revit, Civil 3D) | conta |  |
| Cemig (energia) | conta | achada no seu e-mail |
| Claro (Minha Claro) | conta | achada no seu e-mail |
| Compras (Mercado Livre, Shopee, Amazon) | conta |  |
| Decolar | conta | achada no seu e-mail |
| Disney+ | conta | achada no seu e-mail |
| Epic Games | conta | achada no seu e-mail |
| Espaço Laser | conta | achada no seu e-mail |
| Estadão | conta | achada no seu e-mail |
| iFood | conta | achada no seu e-mail |
| Max (HBO) | conta | achada no seu e-mail |
| MG Conecta (internet de casa) | conta | achada no seu e-mail |
| Motorola | conta | achada no seu e-mail |
| My Honda | conta | achada no seu e-mail |
| Operadora do celular | conta |  |
| Ponto de retirada (Shopee e ML) | conta |  |
| Prime Video | conta | achada no seu e-mail |
| Rappi | conta | achada no seu e-mail |
| Rockstar Games | conta | achada no seu e-mail |
| Spotify Ad Studio | conta | Áudio e podcast, para marca. |
| Strava | conta | achada no seu e-mail |
| Streaming e assinaturas pessoais | conta |  |
| Ticket (benefícios) | conta | achada no seu e-mail |
| TotalPass | conta | achada no seu e-mail |
| Uber | conta | achada no seu e-mail |
| Waze | conta | achada no seu e-mail |

## 12 Carreira e vagas

| Item | Tipo | Observação |
|---|---|---|
| 99Freelas | conta | achada no seu e-mail |
| BNE (Banco Nacional de Empregos) | conta | achada no seu e-mail |
| Contrata Net | conta | achada no seu e-mail |
| Empregare | conta | achada no seu e-mail |
| Freelancer.com | conta | achada no seu e-mail |
| InfoJobs | conta | achada no seu e-mail |
| Superprof (perfil de professor) | conta | achada no seu e-mail |
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

## Achados no e-mail para você conferir

Remetentes de cadastro ou cobrança que podem ser só loja, newsletter ou golpe. O que for conta sua vai para `do_email` em `data/senhas.json`; o resto, apague a conta ou ignore.

- 365customerservice.com (cuidado: parece golpe imitando a Microsoft)
- bubbleapps.io (Agende Online)
- joinrs.com
- gpsvc.app.br
- zeorouteplanner.com
- compraevolta.com.br
- instacart.com
- leiloespublico.com.br (leilões de MG)
- programacnhpopular.com (cuidado: parece golpe)
- meiaentradadigital.com.br
- aprimoramente.com
- ferpadesign.com.br
- fireapparel.com.br
- oggibikes.com.br
- domecanico.com.br
- stranger.com.br
- fozoco.com
- wpbeginner.com
- luminpdf.com
