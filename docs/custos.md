<!-- Arquivo GERADO por tools/custos/custos.py a partir de data/custos.json. Não edite à mão. -->

# Custos: o que construir, o que pegar aberto e o que pagar

[← Índice da documentação](README.md)

Regra geral: **pague só pelo que custa menos que as suas horas ou exige confiança e legalidade.** O resto você constrói (se diferencia você) ou pega aberto (se é infraestrutura comum). Revisão a cada 3 meses (passo do roteiro).

## A regra

**Construir você mesmo**

- O que diferencia você e vira produto: sistemas AM, Fábrica de aulas, kit de sites, radar, agentes do grupo, MCP próprio
- Cola entre ferramentas: scripts, verificadores, geradores (pouco código, muito ganho)

**Pegar código aberto e hospedar**

- Infraestrutura que todo mundo precisa e ninguém paga por ela: n8n, Postiz, Cal.com, Umami, Uptime Kuma, Grafana, Paperless, Home Assistant, LiteLLM, Ollama, llama.cpp, Whisper, Listmonk, GlitchTip, Keycloak
- Modelos abertos com licença Apache 2.0 ou MIT para o que vira produto
- n8n: a licença permite uso interno e nos seus fluxos; não permite revender o próprio n8n como serviço

**Pagar**

- Só quando custa menos que as suas horas ou quando exige confiança/legalidade: Claude (uma IA só), domínio, Hostinger já pago, taxas por venda, contador e certificado quando houver CNPJ
- Toda assinatura passa pela auditoria trimestral e pela cascata

## Item por item

| Decisão | Item | Hoje | Alternativa | Por quê |
|---|---|---|---|---|
| **testar grátis** | ChatGPT pago | mensal | ChatGPT Go grátis pelo Nubank (1 mês; 3 meses no Nubank+; 1 ano no Ultravioleta), depois R$ 39,99 se for usado toda semana | Segunda IA para imagens, voz e quando o limite do Claude acabar. Plus (R$ 99,90) só se o Go não bastar. |
| **cortar** | Codex (OpenAI) | mensal | Claude Code | Ferramenta repetida. |
| **cortar** | Grok | mensal | Plano grátis | Sem uso que o Claude não cubra. |
| **cortar uma** | Alura · Rocketseat · Udemy | mensal | Ficar com uma plataforma na renovação + Microsoft Learn, roadmap.sh e documentação oficial (grátis) | Regra já decidida: nenhum curso novo até o cartão zerar. |
| **trocar** | Gemini pago | mensal | Google AI Plus (R$ 24,99, com 200 GB) no lugar do Google One atual, se o seu plano for de até 200 GB | Quase sem custo extra: troca o armazenamento que você já paga por armazenamento + Gemini Pro + NotebookLM com mais uso. Melhor IA para rascunhar aulas a partir das fontes. |
| **trocar** | SonarQube Cloud | grátis só para público | Semgrep CE no CI (já no repositório padrão) | Repositório privado no Sonar é pago; o Semgrep cobre de graça. |
| **trocar para comercial** | Vercel | grátis (Hobby) | Cloudflare Pages ou GitHub Pages (grátis e permitem uso comercial) ou o Hostinger que você já paga | O plano Hobby da Vercel é para uso pessoal, não comercial: site de cliente ou de venda não pode ficar nele. |
| **adiar** | API de NFS-e | mensal | Emissor nacional da NFS-e (gov, grátis) enquanto for MEI | API só quando o volume de notas pedir. |
| **adiar** | Anúncios pagos | por uso | Conteúdo orgânico + SEO + indicação | Só depois de uma oferta vender sem anúncio; regras de corte já no setup. |
| **adiar** | Backblaze B2 | por TB | Disco externo + Google Drive que você já paga (restic via rclone) | Uma nuvem de backup só; use a que já está paga. |
| **adiar** | Certificado digital e-CNPJ | anual | — | Só quando houver CNPJ. |
| **adiar** | Chave física (YubiKey) | compra | App 2FA no celular + códigos de recuperação no cofre | Bom, mas não urgente. |
| **adiar** | Claude Max (5x) | US$ 100 por mês | Pro + Google AI Plus + ChatGPT Go grátis + modelos locais + Gemini API grátis no gateway | É a solução direta para o limite, mas custa caro hoje. Entra quando uma renda passar no portão e o limite ainda travar o trabalho. |
| **adiar** | Conector Upwork | créditos por proposta | — | Só com inglês B1. |
| **adiar** | Dublagem (ElevenLabs) | mensal | Dublagem automática do YouTube, quando disponível no canal | Só depois de um curso vender em português. |
| **adiar** | Influenciadores e newsletters | por uso | Parcerias por permuta | Só com oferta validada. |
| **adiar** | Servidor caseiro | compra | Um PC usado barato ou o notebook antigo como servidor | Servidor não precisa de máquina nova. |
| **adiar** | Voz clonada (ElevenLabs) | mensal | OpenVoice V2 (MIT) ou Piper (vozes prontas) locais | Pagar só no mês em que um curso pago estiver sendo gravado; testar antes o aberto. |
| **adiar** | Workstation com GPU | compra | Kaggle, Colab, GPU por hora, cluster na rede | Comprar só quando o aluguel passar do valor da parcela por 6 meses seguidos. |
| **adiar** | YouTube membros | por venda | — | Depende de canal monetizado. |
| **adiar** | vLLM em GPU alugada | por hora | Ollama local e gateway | Só quando um modelo seu tiver uso real. |
| **limitar** | Claude por API (agentes) | por uso | Modelos locais pelo gateway para tarefas simples | Teto mensal no LiteLLM; 'local' por padrão, 'rapido' só quando o eval mostrar que o local não basta. |
| **limitar** | GPU por hora | por hora | Kaggle e Colab grátis primeiro | Alugar só para o que não cabe no grátis, com teto e desligando ao terminar. |
| **usar grátis** | Agentes de código do Google | mensal | Cota grátis | Só para comparar; nada pago. |
| **usar grátis** | DeepSeek | por uso | Chat grátis; modelos abertos no Ollama | Pesos abertos rodam local quando couberem. |
| **usar grátis** | Gemini API (cota grátis do AI Studio) | grátis (cota) | — | Rascunhos em lote pelo gateway sem gastar o Claude. Na cota grátis o Google pode usar os dados para melhorar produtos: nada sensível, nada de aluno. |
| **usar grátis** | GitHub Copilot | mensal | GitHub Education (estudante) | Estudante verificado recebe o Copilot sem pagar; você está na Licenciatura. |
| **manter grátis** | Anki | grátis no PC | AnkiDroid (grátis) no celular | O app pago é só o de iPhone. |
| **manter grátis** | Cal.com | grátis | Auto-hospedar se precisar de mais | O plano individual grátis basta. |
| **manter grátis** | Canva | grátis | Krita e Inkscape | Pro só se um cliente pagar por isso. |
| **manter grátis** | DaVinci Resolve | grátis | Kdenlive | A versão grátis basta. |
| **manter grátis** | MailerLite | grátis (limite) | Listmonk auto-hospedado + envio barato (SES/Resend) | O plano grátis encolheu em 2025: confira o limite. Passou dele, Listmonk custa centavos. |
| **manter grátis** | Sentry | grátis (cota) | GlitchTip auto-hospedado se passar da cota | A cota grátis basta no começo. |
| **manter grátis** | Tailscale | grátis (pessoal) | Headscale auto-hospedado se um dia precisar | O plano pessoal grátis cobre todos os seus aparelhos. |
| **usar o que já paga** | E-mail profissional | incluso | E-mail do plano Hostinger; Cloudflare Email Routing para encaminhar | Não contratar Google Workspace agora. |
| **manter** | ActivityWatch | grátis | — | Código aberto. |
| **manter** | Claude (assinatura) | mensal | — | A ferramenta que mais devolve hora sua: código, setup, conteúdo. A única IA paga. |
| **manter** | Domínio (Registro.br) | anual | — | Barato e necessário. |
| **manter** | Gateway Pix (Asaas) | por venda | Mercado Pago, que você já usa | Sem mensalidade; paga só quando vende. |
| **manter** | Google One | mensal | — | Já pago; vira o destino do backup criptografado. |
| **manter** | Hostinger | anual | — | Já pago; hospeda os sites dos clientes e o e-mail profissional sem custo extra. |
| **manter** | Hotmart / Kiwify | por venda | — | Sem mensalidade. |
| **manter** | Postiz | grátis (auto-hospedado) | Agendador nativo das redes | Código aberto no seu PC. |
| **manter** | Umami | grátis | — | Auto-hospedado ou plano grátis. |
| **manter** | Zoomcamp e cursos de IA | grátis | — | Os Zoomcamps são gratuitos. |
| **manter** | restic | grátis | — | Código aberto. |
| **regra** | Hardware novo em geral | compra | Comprar só o que um passo do roteiro bloqueia | Cada compra entra pelo Caixa da Casa e pela cascata. |

| Decisão | Itens |
|---|---:|
| testar grátis | 1 |
| cortar | 2 |
| cortar uma | 1 |
| trocar | 2 |
| trocar para comercial | 1 |
| adiar | 14 |
| limitar | 2 |
| usar grátis | 4 |
| manter grátis | 7 |
| usar o que já paga | 1 |
| manter | 11 |
| regra | 1 |

## Modelos abertos para cada tarefa

Para o que vira produto, prefira licença Apache 2.0 ou MIT e confira a licença do tamanho exato que baixar.

| Tarefa | Modelo | Licença | Onde roda |
|---|---|---|---|
| Chat e agentes locais | Qwen (maioria dos tamanhos), Mistral 7B, Phi | Apache 2.0 / MIT (confira cada tamanho) | Ollama no notebook (até ~14B com offload) |
| Código local | Qwen Coder | Apache 2.0 (confira o tamanho) | Ollama |
| Busca nas suas notas (embeddings para RAG) | bge-m3, nomic-embed-text | MIT / Apache 2.0 | Ollama, até em CPU |
| Transcrição de aulas e vídeos | Whisper (faster-whisper) | MIT | GPU 4 GB ou CPU |
| Voz | Piper (vozes prontas) · OpenVoice V2 (clonar a SUA voz) | MIT | CPU |
| OCR de documentos | Tesseract (dentro do Paperless) | Apache 2.0 | CPU |
| Imagens | FLUX.1 schnell | Apache 2.0 | GPU alugada ou Colab (pesado para 4 GB) |
| Modelos grandes para estudo | Llama, Gemma | Licenças próprias com restrições: leia antes de usar em produto | Quantizados ou alugados |

## Qual IA para cada tarefa

| Tarefa | IA | Por quê |
|---|---|---|
| Planejar o setup, arquitetura, revisão de código e do que vai para cliente | Claude (Pro) | Melhor raciocínio longo e coerência com o repositório |
| Código no setup e nos sistemas | Claude Code; Gemini como segunda opinião | Lê e muda o repositório com testes |
| Rascunho de aulas e documentos a partir das ementas e fontes oficiais | NotebookLM / Gemini (AI Plus) | Responde preso às fontes que você carrega; economiza o limite do Claude |
| Revisar a aula pronta contra as suas regras | Claude | Uma revisão curta gasta pouco limite |
| Pesquisa com fontes | Perplexity (grátis) ou Gemini; Claude para fechar a decisão | Busca barata, decisão no Claude |
| Imagens, capas e voz de conversa | ChatGPT Go | Ponto forte dele |
| Transcrever, resumir e rascunhar em volume | Modelos locais (Ollama) ou Gemini API grátis pelo gateway | Sem custo e sem gastar limite |
| Tudo que tem dado sensível (aluno, finanças, senha) | Nenhuma IA na nuvem; modelo local ou à mão | Segurança acima de conveniência |

## Fazer o limite do Claude durar

- Uma conversa por tarefa: conversa longa relê tudo a cada mensagem e consome o limite muito mais rápido.
- Projects com os arquivos fixos (regras, ementas, setup) em vez de colar tudo de novo.
- Modelo mais leve do Claude para tarefas simples; o mais forte só para planejar e revisar.
- Rascunho na IA mais barata, revisão final no Claude.
- Peça o resultado em arquivo ou no repositório, não em textos longos repetidos no chat.

Coerência entre IAs: as mesmas regras em CLAUDE.md, AGENTS.md e GEMINI.md (scripts/wsl/regras-ia.sh).

Assinaturas pessoais (streaming, apps) ficam fora do repositório: confira no Caixa da Casa.
