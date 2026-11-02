# Changelog

Formato baseado em [Keep a Changelog](https://keepachangelog.com/pt-BR/1.1.0/).

## [2.9.0] - 2026-11-02

### Adicionado
- tools/git/taguear.py: cria as tags de versão a partir do CHANGELOG, achando o commit de cada versão, de uma vez (com --criar --push); avisa se o histórico estiver incompleto. Com testes.
- docs/boas-praticas.md: git e versões (Conventional Commits, SemVer, tags, main protegida), segredos e segurança, qualidade, documentação, backup e licenças — para todo repositório.
- Passo el-tags na fase Padrão de elite (taguear todas as versões).

## [2.8.0] - 2026-11-02

### Adicionado
- Plano de financiamento do setup (docs/operacao/08-financiar-o-setup.md): a renda de TI (mini-curso, sites, avaliação de IA) começa sem nenhuma compra; cada marco de renda libera uma compra pela cascata; o hardware caro (servidor da casa, SO-101, Reachy, GPU) é desejo e entra por último, cada peça ligada à renda que a paga.

## [2.7.1] - 2026-11-02

### Alterado
- docs/ia/tokens.md: a regra "peça o gerador, não o resultado" aplicada a tudo (aula, site, questões, orçamento, documentos, dados), seção "preciso dar todas as informações?" (não: a IA assume padrões e você corrige) e a economia por voz, escrito ou arquivo.
- Regras da IA: a IA assume padrões sensatos, marca o que assumiu e reúsa preferências e regras do repositório em vez de perguntar de novo.

## [2.7.0] - 2026-11-02

### Adicionado
- Laboratório de alvo isolado (infra/lab-alvo + scripts/wsl/lab-alvo.sh e scripts/windows/lab-alvo.ps1): o software estudado roda numa rede sem internet, com atacante, prova do isolamento e foto para desfazer o ataque; ciclo engenharia reversa → pentest → relatório em docs/seguranca. Bloco, fluxo e 3 passos novos.
- Orçamento do setup (tools/custos/orcamento.py): soma só desenvolvimento e protótipos (item de venda fica de fora), por etapa e por tipo, único vs. recorrente, com faixa min–máx; modelo em orcamento.example.toml. Com testes.
- Economia de tokens (docs/ia/tokens.md e tools/ia/tokens.py): a regra "peça o script, não o resultado", o roteador de IA por tarefa e a estimativa de tokens; exemplo da planta baixa. Regra adicionada às regras da IA.

## [2.6.0] - 2026-11-02

### Adicionado
- Construção civil, arquitetura e engenharia civil pela TI (docs/construcao): BIM aberto (Bonsai 0.8.5 com IfcOpenShell e ifcopenshell-mcp, FreeCAD 1.1), Autodesk educacional para professor (só estudo e ensino), QGIS, análise e energia (FreeCAD FEM, PyNite, EnergyPlus), Speckle, SINAPI; trilha de conceitos em 8 blocos, normas que importam (sem PDF pirata) e o que pode alimentar a IA.
- infra/templates/regras-ia/construcao.md: regras para a IA em engenharia (quem assina, memória de cálculo, norma com número e ano, SINAPI com mês e UF, LGPD, formatos abertos).
- tools/construcao/ifc_resumo.py: resumo de qualquer IFC (esquema, pavimentos, elementos e quantidades), sem dependências, com 7 testes.
- 9 blocos, fluxo "do modelo BIM à estimativa da obra", fase 53 (13 passos) e as ofertas Automação BIM para escritórios e AM Obra.

### Corrigido
- Pacote de contexto (contexto.py): as regras da seção "Nunca" saíam como se fossem permitidas; agora saem com "NUNCA:" na frente, com teste.
- Regras da IA ganharam as travas de segurança (escopo.py) e da casa (política do Jarvis).
- ESTADO.md de 02/11 compactado em 5 linhas, como manda a regra.
- Artefatos de Acompanhamento, Portfólio, Mapa e Ecossistema republicados com os dados atuais (o progresso marcado continua salvo).

## [2.5.1] - 2026-11-02

### Alterado
- Catálogo do Hugging Face com foco em TI (primeiro), casa inteligente e agropecuária; TI ganhou o Qwen2.5-Coder 1.5B para autocompletar offline.
- Agropecuária no lugar do modelo de doença de folha: pecuária (contagem de gado por câmera, bebedouro, cocho e balança), lavoura e horta (irrigação por umidade e previsão de chuva, LoRa, datasets de erva daninha) e o negócio AMtech Campo.

### Adicionado
- Bloco Kit de campo; oferta Automação e monitoramento para sítios e produtores (AMtech Campo, 2027); fase 52 com 16 passos.

### Removido
- Passo hf-agro (modelo de doença de folha para o projeto da escola).

## [2.5.0] - 2026-11-02

### Adicionado
- Catálogo do Hugging Face (docs/ia/hugging-face.md): voz (Whisper large-v3-turbo e ajustes para português, Kokoro, Piper, openWakeWord), câmeras (Qwen3-VL 2B local, SmolVLM2, detectores do Frigate), robótica (LeRobot, SmolVLA, ACT), documentos (Docling e Granite-Docling), RAG (bge-m3), modelos em português (Tucano2), filtro de injeção (Prompt Guard 2) e agentes (smolagents, Spaces com MCP), cada um com onde roda na GTX 1650 e o cuidado de licença.
- Compras em ordem do que destravam: servidor da casa, par SO-101, Reachy Mini, LeKiwi, câmeras e, só depois do portão, GPU de 12 GB.
- tools/ia/cabe.py --hf DONO/MODELO: lê o número de parâmetros na API do Hugging Face e avisa quando o treino pede bfloat16.
- Blocos SO-101, Reachy Mini, LeRobot e Docling; fase 52 (Hugging Face e IA física, 12 passos), do token de leitura ao modelo de doença de folha do projeto agro.

## [2.4.0] - 2026-11-02

### Adicionado
- Jarvis por comando de voz (docs/jarvis): voz local, casa (energia, água, câmeras, portas, janelas, eletrodomésticos), robótica e PC, com a pesquisa do que existe (Home Assistant Assist e Wyoming, MCP do Home Assistant, Claude Code /voice, Frigate, AI-on-the-edge-device, ESPHome, ROS 2 com mqtt_client, Pipecat).
- tools/jarvis/politica.py: níveis livre, voz, celular e proibido por ação, com mínimos fixos no código (destrancar, abrir janela, porta e portão, desligar geladeira, desarmar alarme, desligar câmera), limite de 25 entidades expostas e geração das automações que religam a geladeira; modelo em politica.example.toml.
- tools/jarvis/falar.py: hook Stop do Claude Code que fala a última resposta pelo Piper local, sem nunca travar o agente.
- infra/jarvis: Whisper na GPU, Piper pt_BR, openWakeWord ("hey jarvis") e Mosquitto; perfis zigbee (Zigbee2MQTT) e cameras (Frigate).
- ADR 0004: a casa roda num servidor próprio com Home Assistant OS; o notebook empresta a GPU para a voz.
- 14 blocos, 23 conexões e o fluxo "um comando de voz até a tomada"; fase 51 refeita com 13 passos, da voz no PC à primeira contribuição open source.

### Alterado
- Fechadura entra no Jarvis: trancar livre, destrancar só com o toque no celular (antes ficava totalmente fora).

## [2.3.0] - 2026-11-02

### Adicionado
- Frente de segurança (docs/seguranca): engenharia reversa com IA (Ghidra, GhidraMCP, ILSpy, trilha de exercícios e a aula "do C ao assembly e de volta"), AppSec nos sistemas AM (camadas do STRIDE ao ZAP, o erro de autorização que nenhum scanner acha, repositórios de referência para comparar arquitetura), empresa de pentest (serviço completo do termo assinado ao reteste, red team no horizonte, construir ou usar pronto, lei e contrato) e o Jarvis (orquestrador com lista branca, voz local e aprovação).
- tools/seguranca: guarda de escopo (escopo.py: bloqueia teste sem termo assinado, fora da janela ou fora dos alvos, e registra cada comando), calculadora CVSS 3.1 pela especificação do FIRST (cvss.py) e gerador de relatório de pentest que recusa achado fora do escopo (relatorio.py), com 20 testes.
- Modelos em infra/templates/seguranca: termo de autorização, escopo, achados, modelagem de ameaças com checklist ASVS, ZAP passivo no CI e o crackme da aula em C e C#.
- Laboratório de ataque local (infra/lab-seguranca: Juice Shop e WebGoat em 127.0.0.1) e scripts/wsl/ferramentas-re.sh.
- 15 blocos, 28 conexões e 2 fluxos (pentest e engenharia reversa); fases 50 (engenharia reversa, AppSec e pentest, 16 passos) e 51 (Jarvis, 5 passos).
- Ofertas novas: laudo de segurança dos sites que você mantém, curso de segurança e engenharia reversa para devs e pentest completo (AMtech Segurança); bug bounty ganhou passo próprio.
- Certificações de segurança: eJPT → BSCP → OSCP → OSWE e OSEP.

## [2.2.2] - 2026-11-01

### Corrigido
- Esteira de sites: o workflow qualidade agora roda o Lighthouse (desempenho 80+, acessibilidade e SEO 90+), como a documentação já prometia; relatório guardado nos artefatos da execução.

## [2.2.1] - 2026-11-01

### Corrigido
- Passos repetidos do GitHub Education (ct-copilot, como estudante, e github-education) unificados em ag-ghed, como professor.
- Passo ia-rotas aponta para a tabela de rotas de docs/recursos.md.
- CONTINUAR.md atualizado com a versão 2.x: números, guias novos, decisões (roteador, esteira, investimentos, certificações), ferramentas, tabela das 50 fases e pendências novas.

## [2.2.0] - 2026-11-01

### Alterado
- Investimentos nas quatro classes do ARCA, com todas as metodologias ao mesmo tempo: Ações (9: Barsi, Bazin, Graham, Buffett, Sena, Fórmula Mágica, Piotroski, Lynch, Gordon), FIIs (7: desconto P/VP, Bazin, Barsi, prêmio sobre a NTN-B, qualidade, crédito de FII de papel, Sena), renda fixa (4: liquidez com garantia, IPCA+, escada, segurança do emissor) e Internacional (7: Bogle, aristocratas, Buffett, Graham e Bazin lá fora, REITs, Sena).
- Cada ativo recebe o resultado de cada metodologia que se aplica e um consenso (forte, médio, fraco); metodologia que não se aplica ao tipo de ativo não conta.
- Aporte em dois níveis (ARCA por classe → metodologia dentro da classe), com mínimo por compra para não virar migalha, limites por ativo e setor, aviso de FGC acima de R$ 250 mil por instituição e escada com menos de 3 degraus.
- Renda fixa compara título isento com tributado pela tabela regressiva; regras de imposto em vigor (MP 1303 caducou em 08/10/2025; Lei 14.754 no exterior; Lei 15.270 nos dividendos altos) documentadas.
- Comparação por classe contra o índice e alocações gerais para simular (Graham defensivo, Portfólio permanente, Bogle).

## [2.1.0] - 2026-11-01

### Adicionado
- Investimentos (data/investimentos.json → docs/investimentos.md, tools/investimentos): as suas metodologias (ARCA, Barsi, Bazin, Graham, Buffett, Sena) e as novas para testar (Fórmula Mágica, Piotroski, Peter Lynch, Gordon, índice de referência). O script avalia quem passa em cada metodologia (com preço-teto de Bazin e valor de Graham), divide o aporte pelo ARCA dentro de ações com limites por empresa e setor, respeita o portão (cartão zerado e reserva completa) e compara cada carteira com o índice. Dados em ~/financas, fora do GitHub; modelos com tickers inventados.
- Certificações (data/certificacoes.json → docs/certificacoes.md, tools/carreira): mercado financeiro (CNPI → registro de consultor na CVM → CGE/CGA → CFP → CFA; CPA e C-PRO só para banco), nuvem e IA, e segurança, com o que cada uma habilita, requisito, custo e fonte.
- Fase f-investimentos com 9 passos (inv-iniciar a inv-cnpi).

### Alterado
- AZ-204 trocado pelo AI-200 em toda a documentação (o AZ-204 deixou de ser agendável em 31/07/2026).
- Passo est-certificacoes com a ordem nova; CPA-10, CPA-20 e CEA substituídas por CPA, C-PRO R e C-PRO I (ANBIMA, jan/2026).

## [2.0.0] - 2026-11-01

### Alterado (mudança de modelo)
- O setup deixa de depender de um agente só: toda tarefa tem ferramenta primária, reserva e portão humano (docs/recursos.md). Nenhuma tarefa depende dos créditos de uma ferramenta.
- Custos: Copilot pelo GitHub Education como professor (Pro com agente na nuvem), não como estudante; agentes de código do Google cortados (Gemini CLI saiu do ar para contas pessoais em 18/06/2026).

### Adicionado
- Auditoria de recursos das ferramentas com conta (data/recursos.json → docs/recursos.md, tools/recursos): Copilot, Claude (rotinas), Codex, Google, Hostinger (MCP, deploy por push, créditos de IA), OpenClaw, Cloudflare (Workers AI), Lovable, v0, Mercado Pago (MCP), Hotmart e Canva, com fonte e decisão por recurso.
- Esteira de sites (infra/templates/esteira-site): ficha como issue, agente abre o PR, CI de HTML, links e acessibilidade, revisão pela rotina do Claude, prévia, aprovação e deploy na Hostinger.
- Blocos OpenClaw (isolado, futuro) e Esteira de sites; fase f-agentes com 9 passos (ag-ghed, ag-hostinger-mcp, ag-esteira, ag-deploy, ag-rotina-pr, ag-cf-mcp, ag-gateway-cf, ag-canva-edu, ag-openclaw).
- Modelo "gratis-cf" (Workers AI) no gateway.

## [1.31.0] - 2026-11-01

### Adicionado
- Passos que faltavam: revisão de fim de ano das turmas (fa-revisao-ano), apostilas de robótica a partir da Aula 41 (fa-robotica), publicação dos posts do setup (ct-posts-setup), editais de professor EBTT e efetivo de MG (est-ebtt) e Licenciatura na Rotina (est-licenciatura).
- CONTINUAR.md reescrito: contexto completo (regras, onde está tudo, o que já foi feito, decisões, ferramentas com comandos, todas as fases, pendências e como pedir ajuda).

## [1.30.0] - 2026-11-01

### Adicionado
- Verificador de documentos (tools/documentos/verificar.py): perfil ABNT (A4, margens, fonte, espaçamento, recuo, numeração, sumário, referências) com correção automática da formatação, e perfil escola (campos vazios, dados de aluno, máximo de objetivos).
- Rendas "Verificador e formatador ABNT automático" (próxima, 7ª) e "Conferência automática de documentos para escolas" (fila), com softwares e passos fa-conferir e fa-abnt.

### Removido
- Dependência dos congelados (harumakis) na máquina de venda: o plano de congelados saiu, por decisão do Alan.

## [1.29.0] - 2026-11-01

### Adicionado
- CONTINUAR.md: contexto completo para começar qualquer conversa nova (regras, onde está tudo, decisões, pendências, como pedir ajuda); `tools/sessao/contexto.py --inicio` junta o CONTINUAR.md com o estado atual. Link no README.

## [1.28.0] - 2026-11-01

### Adicionado
- Dados e crescimento: fase com Metabase (infra/dados), PostHog (funil e gravações), GrowthBook (testes A/B), análises de cliente (RFM, LTV, churn, previsão), Chatwoot (atendimento numa caixa só), Twenty (CRM aberto), Documenso (assinatura), Invoice Ninja (orçamentos e cobrança) e Penpot (design). 9 blocos novos.
- Outras ferramentas de IA por categoria em docs/custos.md: o que acrescentam, como geram renda, decisão e quando entram.

## [1.27.0] - 2026-11-01

### Adicionado
- Conversas curtas: pacote de contexto por passo ou resumo (tools/sessao/contexto.py, poucas centenas de tokens), ESTADO.md como memória de 5 linhas por sessão e o protocolo em docs/operacao/sessoes-curtas.md.
- Ferramentas do Akita: ai-memory 2.0 (passo de atualização), ai-usagebar (limite das IAs no terminal) e Strata (MoE de 125B em casa, quando houver GPU de 12 GB+).
- Avaliação das outras IAs em docs/custos.md: DeepSeek (usar barato, nada sensível), Perplexity e OpenRouter (grátis), Z.AI GLM (testar como reserva de código), Codex (só se vier no plano), Grok (cortar). Rotas e gateway com os modelos "barato" e "reserva".

## [1.26.0] - 2026-11-01

### Adicionado
- Lucro e prejuízo por ferramenta e por renda (tools/roi/roi.py): atribuição proporcional ao custo, retorno por hora contra a hora mínima, alerta de prejuízo há 2 meses; dados em ~/financas/roi.toml.
- Vigia semanal no GitHub Actions (.github/workflows/vigia.yml): sites dos clientes de data/vigia.json e segredos no histórico, sem depender do notebook ligado.
- Operação 24 horas (docs/operacao/24-horas.md) e fase no roteiro: VM grátis da Oracle (limite reduzido em jun/2026), migração de n8n, bot, Kuma e gateway, prospector com aprovação, evals mensais e no máximo 2 tarefas agendadas do Claude. 4 blocos novos.

## [1.25.0] - 2026-11-01

### Alterado
- Custos: ChatGPT passa de "cortar" para "testar grátis" (ChatGPT Go pelo Nubank) e Gemini de "cortar" para "trocar" (Google AI Plus no lugar do Google One). Claude Max entra como "adiar".

### Adicionado
- Rotas por tarefa (qual IA para cada trabalho) e práticas para o limite do Claude durar, em docs/custos.md.
- Regras únicas para todas as IAs (infra/templates/regras-ia + scripts/wsl/regras-ia.sh → CLAUDE.md, AGENTS.md, GEMINI.md).
- Modelo "gratis" (cota grátis do Gemini) no gateway LiteLLM; passos ia-segunda, ia-rotas, ia-regras e ia-gemini-api.

## [1.24.0] - 2026-11-01

### Adicionado
- Auditoria de custos (data/custos.json → docs/custos.md): regra de construir, pegar aberto ou pagar; 45 itens com decisão (cortar, trocar, adiar, limitar, manter grátis, manter) e alternativa; modelos abertos por tarefa com licença. Passos para aplicar os cortes, pedir o GitHub Education e revisar a cada 3 meses.

### Corrigido
- Blocos repetidos criados na versão anterior: Syncthing (já existia) e gitleaks/Trivy (já existiam como "gitleaks · Trivy"). Passos e conexões apontam para os blocos originais.

## [1.23.0] - 2026-11-01

### Adicionado
- Padrão de elite: repositório padrão (pre-commit com gitleaks e Conventional Commits, CI com gitleaks, Trivy, Semgrep e testes, Definition of Done, ADRs) aplicado por scripts/wsl/padronizar-repo.sh sem sobrescrever nada; segredos direto do KeePassXC (scripts/wsl/segredos.sh); teste mensal de restauração do backup (scripts/wsl/teste-restauracao.sh).
- IA com qualidade medida: gateway LiteLLM (infra/ia) com nomes estáveis (local, rapido, forte, gpu-alugada), fallback e teto de gasto; evals com promptfoo; passos do agente revisor de qualidade, do MCP próprio e dos agentes do n8n pelo gateway.
- Modelos grandes sem computador maior: docs/ia/README.md (quantização, MoE, cluster na rede, QLoRA, GPU por hora com vLLM, destilação, API) e a calculadora tools/ia/cabe.py.
- Rede própria: docs/rede/README.md, Tailscale agora, Syncthing, AdGuard Home (infra/rede), laboratório de redes e WireGuard à mão.
- Quatro fases novas no roteiro e 18 blocos novos no ecossistema.

## [1.22.0] - 2026-11-01

### Adicionado
- Kit de sites com IA da Hostinger: 3 pacotes, ficha do cliente, 26 prompts por tipo de negócio, checklist de entrega, relatório mensal (tools/kitsites/gerar.py → docs/operacao/kit-sites.md), conferência automática do site com laudo (tools/kitsites/conferir.py) e modelo de contrato para revisão de advogado.
- Avaliador de templates (tools/avaliador/avaliar.py): útil, adaptar ou descartar, tecnologia, licença, módulos e tipos de negócio, sem rodar código de terceiros; recusa .zip com caminhos suspeitos.
- Radar de revenda (tools/radar/radar.py): lucro por hora contra a hora mínima, sinais de golpe, preço baixo demais e checklist por categoria; referências de preço em ~/.config/amtech/radar.toml, fora do repositório.
- Organizadores: Downloads por tipo, simulando antes e sem apagar (tools/organizar/downloads.py); exportação de senhas pronta para o KeePassXC, sem mostrar senhas (tools/organizar/senhas_csv.py).
- Bot do Telegram (tools/remoto/bot.py): só o seu chat, só comandos fixos (/status, /resumo, /radar), configuração com permissão 600.
- Financeiro local (tools/financeiro/financeiro.py): importa extratos Nubank ou CSV sem duplicar, resume o mês e aplica a cascata; modelos de regras, caixas e Política de Investimentos; dados em ~/financas.
- Fábrica de aulas: preenche modelos .docx da escola com campos {{assim}} (tools/fabrica/preencher.py) e monta o planejamento semanal com no máximo 3 objetivos (tools/fabrica/plano_semanal.py); recusa dados de aluno. Esqueleto do repositório privado "aulas" em infra/templates/repo-aulas.
- Rotinas: resumo da manhã, manutenção semanal (simula por padrão) e agendamento no cron (scripts/wsl/resumo-manha.sh, manutencao-semanal.sh, agendar.sh).
- Casa e vida: Home Assistant, Paperless-ngx e Grocy em infra/casa/compose.yaml.
- Roteiro: fases Kit de sites, Escola, Departamento financeiro, Rotina automatizada, Comandos remotos e Casa e vida; passos de KeePassXC (organizar a exportação, agente SSH, Auto-Type, segundo fator) e de estudo (esteira, Economia, certificações, idiomas, AM-OS). 10 blocos novos no ecossistema.

## [1.21.0] - 2026-11-01

### Adicionado
- Catálogo de softwares (data/softwares.json → docs/operacao/softwares.md): 62 softwares vendáveis (26 sites por tipo de negócio, 14 sistemas AM, 11 micro-SaaS, 5 de educação, 6 produtos) e 7 sites e ferramentas seus, montados com 20 módulos reaproveitáveis na ordem de construção. Cada software liga a uma oferta do portfólio; o CI recusa módulo ou oferta inexistente e módulo sem uso.

## [1.20.0] - 2026-11-01

### Adicionado
- Mapa de automações do arsenal: 20 automações compartilhadas (checkout, funil, esteira estudo → produto, Fábrica, publicação com aprovação, mídia, CRM, recorrência, manutenção de sites, atendimento, CI, estoque, radar, editais, conciliação, agenda, horas, cascata, painel, Telegram), cada oferta ligada às que usa e a ordem de construção pelo que cada uma destrava.
- Nível de cada oferta: o setup faz tudo menos criar e aprovar (85%+), faz a maior parte (50–84%) ou depende da sua hora.
- Fase "Automações do arsenal" no roteiro, com um passo por automação a construir. O CI recusa automação inexistente, passiva sem automação e automação a construir sem passo.

## [1.19.0] - 2026-11-01

### Adicionado
- Marca AMtech Economia (finanças e empreendedorismo) com 7 ofertas: plano de negócios e viabilidade, BPO financeiro, captação de crédito e editais, mentoria financeira sem recomendar ativos, modelos financeiros para empresas, calculadoras online e consultoria de investimentos (só com sócia certificada). O catálogo chega a 100 ofertas.

## [1.18.0] - 2026-11-01

### Adicionado
- Arsenal de rendas no portfólio: 93 ofertas (46 novas), cada uma com perfil (passiva, ativa que vale a pena, ativa), % automático, veredito (agora, próxima, manter, fila, 2027, decidir, descartar) e o motivo.
- Nota de facilidade (sinergia + demanda + (6 − esforço) + (6 − capital)) e ranking da mais fácil para a mais difícil.
- Regras validadas no CI: hora mínima de R$ 45, teto de 7 horas extras por semana, no máximo 3 rendas em "agora" e ordem única para as próximas.
- Marcas: AMtech Educação, Software, Digital, Campo (presencial por parceiros), Mídia e Patrimônio.
- Radar de revenda (bloco novo): lê alertas de busca salvos, compara com o preço de referência e só avisa o que passa da hora mínima; nunca compra nem fala com vendedor.
- Fase "Arsenal de rendas" no roteiro (nov/2026) e passos para a fila, os serviços de 2027, as rendas de capital alto e as de formação longa.

## [1.17.0] - 2026-10-31

### Adicionado
- Cada comando do roteiro e do acompanhamento diz onde rodar: no PowerShell do Windows (linha PS C:\>), no Ubuntu (linha alanmateus@...$) ou no navegador.

## [1.16.3] - 2026-10-30

### Corrigido
- "fnm: command not found" ao abrir o Ubuntu: a linha do fnm no .bashrc agora põe ~/.local/bin no PATH antes, e o bootstrap carrega o fnm antes de checar o Node (parava de reinstalar o Node a cada rodada).
- bootstrap.sh instala bind9-dnsutils (o pacote dnsutils não existe mais no Ubuntu 26.04).

## [1.16.2] - 2026-10-30

### Corrigido
- extensoes-vscode.ps1 parava na primeira extensão: o aviso do Node que o code.cmd escreve no stderr virava erro no Windows PowerShell 5.1. Agora chama o code pelo cmd.
- Passo da criptografia explica o caso "Proteção Desativada, nenhum protetor": disco criptografado esperando a chave.

## [1.16.1] - 2026-10-30

### Mudado
- O setup aceita o Ubuntu que já existe no WSL, 24.04 ou mais novo (o seu é o 26.04): passo, bootstrap, cofre do Obsidian e integração do Docker usam o nome da sua distro, e o repositório da HashiCorp cai para o do 24.04 quando o da sua versão ainda não existe.

## [1.16.0] - 2026-10-30

### Adicionado
- Comando de terminal em mais 96 passos (agora 131 de 253): extrair e pôr a pasta no lugar, contar os documentos, backup inicial com robocopy, Windows Update pelo PSWindowsUpdate, cofre criado com keepassxc-cli, cópia do cofre conferida, criptografia e chave de recuperação, Defender e Firewall, dotfiles, Dependabot e CodeQL pelo gh, projeto do GitHub, modelo do Ollama, teste de restauração, túnel da Cloudflare, teste de commit assinado, verificadores juntos, Kubernetes local, e `claude "Passo ..."` em todo passo feito pelo Claude.
- Campo **Fora do terminal**: os passos sem comando dizem por quê (site do serviço, celular, órgão público, hardware, conteúdo ou decisão sua). O CI falha se um passo ficar sem comando e sem motivo.

## [1.15.1] - 2026-10-24

### Corrigido
- Os comandos do Windows usavam `.\scripts\windows\...` e falhavam quando o PowerShell de Administrador abria em System32. Agora apontam para `$HOME\dev-setup\scripts\windows\...`, e o primeiro passo deixa a pasta em `C:\Users\SEU_USUARIO\dev-setup`. O passo de copiar para o WSL usa essa mesma pasta.

## [1.15.0] - 2026-10-24

### Adicionado
- Fase "Senhas: recuperar, trocar e guardar" logo depois de Preparar (12 passos): cofre do KeePassXC com senha mestra de 6 palavras, kit de emergência em papel, o e-mail principal primeiro, importação das senhas do Chrome, Edge e Google com o CSV apagado na hora, relatório de senhas fracas, repetidas e vazadas, troca das contas críticas com verificação em duas etapas, recuperação das esquecidas, cofre no celular, preenchimento no navegador, backup e revisão a cada 3 meses. O passo do KeePassXC sai da fase Windows e abre essa fase.

## [1.14.1] - 2026-10-23

### Corrigido
- O diagnóstico agora roda com `RODAR-DIAGNOSTICO.cmd` na raiz (botão direito > Executar como administrador): ele entra sozinho na própria pasta, confere que `scripts\windows\diagnostico.ps1` está ali e não percorre nenhuma outra pasta. As instruções anteriores rodavam `Unblock-File` a partir da pasta onde o PowerShell abria (System32 ou a pasta do usuário).
- O plano B do passo (comando para colar) só aceita o arquivo dentro de `scripts\windows` e não usa `Unblock-File`: com `-ExecutionPolicy Bypass` ele não é necessário.

## [1.14.0] - 2026-10-23

### Adicionado
- Etapa 0 "Diagnóstico: o que você já tem" antes de tudo: `scripts/windows/diagnostico.ps1` (somente leitura) lê hardware, segurança, programas, WSL, Docker, Ollama e extensões, compara com o setup e diz em que passo do roteiro cada pendência se resolve; mais a lista das contas que você já tem e a contagem dos documentos. Roda no CI.
- Fase "Primeira venda: o mini-curso no ar" (8 passos, da gravação à primeira venda com acesso, suporte, painel e carnê-leão) e fase "Mais ofertas, uma por vez" (20 ofertas na ordem da pontuação).
- Cada uma das 47 ofertas do portfólio ligada ao passo em que entra à venda; o portfólio mostra "Quando entra"; o CI falha se uma oferta ficar sem passo.
- Passo que põe o banco de métricas e os fluxos do n8n no backup diário (eles ficavam em volumes do Docker, fora do restic).
- Bloco Diagnóstico do notebook e o fluxo "Do notebook à primeira venda".

## [1.13.0] - 2026-10-23

### Mudado
- Todo o planejamento entra no passo a passo: os 87 blocos que estavam como "para depois", "peça a construir" ou "não se instala" ganharam passo, e cada uma das 30 fases tem **quando** (semana e mês) e, quando depende de resultado, o **gatilho**. Fases novas: marketing pago, Linux nativo, IA nos sistemas AM, sistemas AM à venda, CNPJ, agentes do grupo, editora depois do primeiro livro, plataforma e segunda nuvem, infraestrutura própria e os 9 negócios pelos portões.
- O roteiro e o acompanhamento terminam com "Quando entra cada bloco", camada por camada; o diagrama, o mapa e os documentos de cada camada mostram o passo e a data de cada bloco.
- O CI falha se um bloco, mesmo futuro, não tiver passo, ou se uma fase não tiver data.
- "Fora do setup" vira "Decisões": dual boot, Kali, mobile e o treino do 8B entram por outro caminho, com passo; ficam de fora só OpenClaw (segurança) e o que você mesmo rejeitou.
- O diagrama volta a ter a seção de auditoria e a opção "Ver todas as conexões".

### Adicionado
- Bloco App mobile (.NET MAUI), em 2028.

## [1.12.0] - 2026-10-23

### Adicionado
- `tools/acervo/acervo.py`: lê todos os seus documentos sem alterar a origem, acha cópias, separa os pessoais, marca material de terceiros e da escola e dados de alunos, converte o resto para Markdown no Obsidian e escreve o relatório de produtos candidatos. Regras em `regras.py`, 9 testes no CI e teste de verdade com .docx, .pptx e .pdf.
- `scripts/wsl/vault.sh`: cofre do Obsidian em `~/dev/notas` com pastas de estudo, aulas, acervo, produtos e conteúdo, e modelos de nota.
- Fase "Acervo: tudo o que você já tem" no roteiro (7 passos), blocos Google Drive e Acervo e o fluxo "Do documento antigo à venda".
- Campo `precisa` nos passos (compra, pagamento, conteúdo) e o filtro "Só o que dá para fazer hoje" no acompanhamento: 135 dos 148 passos só precisam do notebook e de contas grátis.

## [1.11.0] - 2026-10-23

### Adicionado
- Camada nova "Dados e treino de IA" com 13 blocos: Python de dados, DuckDB, dbt, Airflow, PySpark, PyTorch com CUDA no WSL2, Hugging Face, Unsloth, Kaggle e Colab, MLflow, avaliação, GGUF e os seus datasets (só conteúdo seu). Fluxos "Treinar uma IA sua" e "Dados de venda viram decisão".
- Pendrives de Kali (persistência criptografada) e de Arch (instalação portátil), Rufus no winget e o cuidado com Secure Boot e BitLocker no mapa.
- `scripts/wsl/lab-ia.sh`: laboratório de dados e de IA em `~/dev/lab-ia` (opção `--so-dados`); `verificar.sh` confere a GPU e o laboratório.
- Fase "Dados, IA e pendrives" no roteiro (12 passos, do pendrive ao seu modelo no Ollama) e duas etapas novas na ordem de estudo: engenharia de dados e IA profunda.

### Mudado
- "LLM 8B na GPU / fine-tuning" e "Engenharia de dados" saem de "cortado". Fica cortado só treinar um 8B na GTX 1650 (pede 6 GB de VRAM, a placa tem 4): o 8B roda no notebook dividido entre GPU e RAM, e o treino vai para a nuvem.
- Os botões de fluxo do diagrama saem dos dados, não do HTML.

## [1.10.0] - 2026-10-23

### Corrigido
- Diagrama do ecossistema: as 529 linhas apareciam todas juntas, atravessando o desenho; no celular os blocos ficavam cortados e o painel do bloco aparecia lá embaixo da página. Agora os blocos se reorganizam na largura da tela, as linhas aparecem só para o bloco ou o fluxo escolhido (com seta) e o painel fica fixo na tela.
- Os 13 fluxos tinham 37 passos sem conexão entre si, então o destaque mostrava blocos soltos. Todos refeitos sobre conexões reais.
- Conexões com o sentido trocado (Sentry, Seq, Mailpit, Kafka, Terraform → Google Cloud, Obsidian → Anki, livro → isca, flywheel → pipeline) e conexões erradas ou duplicadas (n8n → Hotmart, Obsidian → livro, TeX → livro, Arduino nos dois sentidos, 7-Zip → backup, edição do professor → sites).
- Blocos na camada errada: n8n e MailerLite (marketing), comunidade e Google Perfil da Empresa (público), Syncthing (Windows), assinatura e API do Claude (Claude).
- Mapa do setup: células vazias cinza no fim de cada camada, cartões de mercado com o texto empurrado para baixo e a lista de cortes desalinhada.
- Roteiro: a página de vendas do Instituto AMS ia para o Vercel, cujo plano grátis não permite uso comercial; agora vai para a Cloudflare Pages, como o mapa já indicava.
- Contas: a lista agora sai dos próprios blocos marcados com conta; Umami e Anki passam a pedir conta; Cloudflare e vidIQ saem de "sugeridos" (já estão conectados).

### Adicionado
- Blocos Wireshark e Telegram (avisos); 38 conexões que faltavam (pipeline → API do Claude e Telegram, túnel da Cloudflare → n8n, MCP → banco de métricas, Uptime Kuma → n8n e Telegram, entre outras).
- `gerar_docs.py` falha com bloco sem conexão, conexão nos dois sentidos, conexão sem rótulo e fluxo com passo sem conexão; `tools/test_gerar_docs.py` no CI.

## [1.9.0] - 2026-10-23

### Corrigido
- O roteiro de implantação cobria só parte do setup (cerca de 176 dos 303 blocos). Agora cada passo diz quais blocos implanta e todos os 303 têm lugar: 214 em passos, 9 peças a construir, 3 que não se instalam e 77 para depois.
- Blocos n8n, banco de métricas, painel de lucro, webhooks de venda e aprovação no celular deixam de ser "futuro": a implantação já os coloca no ar.

### Adicionado
- Roteiro com 18 fases e 129 passos: hardware, Defender, Claude in Chrome, extensões do VS Code, dotfiles, Obsidian Git, Syncthing, ADRs, MCP, ai-memory, RAG, recursos do Claude, conectores e plugins, outros assistentes, estúdio de conteúdo, WhatsApp Business, sites, Umami, Hostinger, vendas e finanças no CPF (gov.br, banco, contador, LGPD, plataformas, Mercado Pago, agenda, CRM, comunidade, afiliados, UTM, ofertas, avaliações, prospecção, INPI, carnê-leão, IRPF, Caixa da Casa), base dos sistemas AM, nuvem e deploy, editora e estudo.
- `tools/implantacao/gerar.py` falha se um bloco do setup ficar fora do roteiro, se um passo citar bloco que não existe ou se um bloco estiver em dois lugares; roteiro e acompanhamento mostram o que cada passo implanta e a cobertura completa. 5 testes novos.
- `scripts/wsl/nuvem.sh`: Azure CLI, Terraform, Vercel CLI e Wrangler.
- `scripts/windows/extensoes-vscode.ps1` com `vscode-extensoes.txt` e `.vscode/extensions.json`.
- Wireshark no winget (o Unity Hub só pelo passo de decisão); nmap e dnsutils no `bootstrap.sh`; `verificar.sh` confere as ferramentas novas como opcionais.

## [1.8.0] - 2026-10-21

### Adicionado
- Implantação: `data/implantacao.json` com 11 fases e 58 passos, gerando `docs/implantacao/roteiro.md` e `acompanhamento.html`.
- `scripts/windows/instalar.ps1` e `verificar.ps1` (winget com IDs conferidos, WSL2, .wslconfig, segurança).
- `scripts/wsl/bootstrap.sh`, `verificar.sh` e `ativar-pipeline.sh` (ferramentas, .NET 10, Node, uv, gitleaks, trivy, Claude Code, ai-jail, Git assinado, pastas, timer).
- `infra/automacao/`: Docker Compose com n8n, banco de métricas (esquema, views de lucro e de melhor horário, usuário só de leitura), Grafana e Uptime Kuma; `infra/postiz/README.md`.
- `tools/conteudo/processar.py`: pipeline de conteúdo com transcrição local, guia de marca, fila de aprovação e aviso no Telegram, com 10 testes.
- `config/marca.md`: guia de marca para preencher.
- CI: job novo com ShellCheck, PSScriptAnalyzer e validação do Docker Compose.

## [1.7.1] - 2026-10-21

### Corrigido
- `docs/mapa.html` estava escrito à mão e mostrava 10 camadas e 5 fluxos antigos. Agora é gerado de `tools/mapa.template.html` com `data/ecossistema.json` e `data/mapa.json`: as 22 camadas, os 299 blocos com conexões e os 13 fluxos, conferido no CI.
- Receita do ponto de retirada corrigida de R$ 1.150 para R$ 1.140, como dá o motor financeiro.
- Os dados embutidos no planejador e no portfólio escapam `</` para não quebrar a página.

### Adicionado
- `tools/negocios/test_coerencia.py`: confere se os números escritos nos documentos batem com o motor financeiro e com o portfólio.

## [1.7.0] - 2026-10-21

### Adicionado
- `docs/operacao/`: esteira de ofertas, marca e presença, flywheel de conteúdo, automação e escala, padrão de qualidade, clientes e dados, ordem de execução.
- `data/portfolio.json` com 47 ofertas (14 fontes de renda novas) e `tools/portfolio/portfolio.py`, que valida, pontua e gera `docs/operacao/portfolio.md` e `portfolio.html`, com testes no CI.
- Camada "Operação do grupo", 18 blocos (incluindo os agentes do grupo) e o fluxo "Do trabalho ao conteúdo".

## [1.6.0] - 2026-10-21

### Adicionado
- `docs/negocios/`: os nove negócios do grupo em Barbacena (software, loja, peças, Maker, ponto de retirada, entregas e Flex, delivery, sushi, cafeteria, padaria), estrutura de CNPJs, ordem com portões, cardápios e desperdício, mínimo legal e sistemas.
- `data/negocios.json` e `tools/negocios/financas.py`: motor financeiro com Simples por anexo, ponto de equilíbrio, rampa, retorno e capital mínimo, com testes no CI.
- `docs/negocios/numeros.md` e `docs/negocios/planejador.html` (planejador interativo), gerados e conferidos no CI.
- Camada "Negócios do grupo", 18 blocos, 34 conexões e o fluxo "Abrir o próximo negócio".

## [1.5.0] - 2026-10-21

### Adicionado
- `docs/editora/10-imagens-e-figuras.md`: acervos, regras de licença, busca automática e figuras geradas por código.
- `docs/editora/11-automacao-e-metodo.md`: o método de criação dentro do pipeline e o que é automático.
- `tools/editora/tabela_verdade.py` com testes, rodando no CI.
- 11 blocos e o fluxo "Ilustrar um capítulo".

## [1.4.0] - 2026-10-21

### Adicionado
- `docs/editora/09-nivel-e-concursos.md`: caminho único, livro autocontido, matemática e física da TI, concursos PF, PRF e Forças Armadas, critério de domínio.
- Blocos Matriz de editais, Projeto do capítulo e Mapa de pré-requisitos.
- Critérios 11 a 13 na avaliação do livro; itens novos no checklist de rigor.

## [1.3.0] - 2026-10-21

### Adicionado
- Camada "Editora AMS Silva (produção de livros)" com 22 blocos: selo, repositório do livro, modelo de criação, fonte única, exercícios em YAML, pranchas TikZ, classe LaTeX, pipeline do livro, revisão automática, agentes, leitores beta, errata, ISBN, ficha catalográfica, depósito legal, KDP, gráfica sob demanda, kit, curso, edição do professor, traduções e quadro de referências.
- Fluxo "Produzir um capítulo do livro".
- Plano da editora em `docs/editora/` (8 documentos).

## [1.2.0] - 2026-10-20

### Adicionado
- `docs/marketing/11-canais-de-anuncio.md`: todos os canais de anúncio com o limite de custo de cada um.
- `docs/infra/`: vários computadores, SSD externo, NAS local e armazenamento em nuvem.
- Blocos de Spotify, Kwai, Pinterest, LinkedIn, mídia nativa e influenciadores; SSD externo, workstation, Syncthing, Backblaze B2 e GPU por hora.

### Alterado
- Servidor caseiro detalhado (NAS + serviços 24 h).

## [1.1.0] - 2026-10-20

### Adicionado
- Camada 18 "Marketing, automação e medição" (Postiz, aprovação no celular, algoritmo de horário, Pixel + CAPI, UTM, regras de corte, webhooks, banco de métricas, painel de lucro, afiliados, prospecção, dublagem).
- TikTok e Facebook na camada de público; voz clonada com ElevenLabs.
- Fluxos "Publicar automaticamente no melhor horário" e "Medir o lucro de uma campanha".
- Plano de marketing, vendas e automação em `docs/marketing/` (10 documentos).

### Alterado
- O gerador remove páginas de camada que deixaram de existir.
- Diagramas Mermaid sem cliques (o GitHub não os abre); a navegação fica nas tabelas.

## [1.0.0] - 2026-10-20

### Adicionado
- Fonte única de dados em `data/` (18 camadas, blocos, conexões, fluxos, contas, auditoria e plano de estudo).
- Gerador `tools/gerar_docs.py` com validação dos dados.
- Uma página por camada em `docs/camadas/`, com diagrama Mermaid e tabela de conexões de cada bloco.
- Arquitetura, fluxos de ponta a ponta, contas, auditoria, sistemas operacionais, nuvem, mercado, roteiro, peças autorais e cortes.
- Diagrama interativo `docs/index.html`, gerado a partir dos mesmos dados.
- ADRs 0001 a 0003.
- Script de inventário somente leitura do Windows.
- Workflow do GitHub Actions que valida os dados e confere os arquivos gerados.
