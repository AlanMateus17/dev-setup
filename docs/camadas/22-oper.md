<!-- Arquivo GERADO por tools/gerar_docs.py a partir de data/. Edite os dados, não este arquivo. -->


# Camada 22 · Operação do grupo (esteira, marca, qualidade)

[← Arquitetura](../arquitetura.md) · [Índice da documentação](../README.md)

> **Ligação com a camada de baixo:** Toda oferta passa pela esteira e pelo padrão de qualidade antes de chegar ao público; cada venda e cada trabalho voltam como dado e conteúdo.

**22 blocos** · 2 precisam de conta · 9 marcados como futuro

## Mapa de conexões

```mermaid
flowchart LR
  subgraph L_oper["Operação do grupo (esteira, marca, qualidade)"]
    n_ocatal["Portfólio de ofertas"]
    n_oesteira["Esteira de ofertas"]
    n_oqual["Padrão de qualidade"]
    n_omarca["Marca pessoal Alan Mateus"]
    n_ogbp["Google Perfil da Empresa"]
    n_oaval["NPS e avaliações"]
    n_ocrm["CRM único + LGPD"]
    n_ofly["Flywheel de conteúdo"]
    n_obuild["Canal build in public"]
    n_oatend["Agente atendente (WhatsApp)"]
    n_oorc["Agente orçamentista"]
    n_ocob["Agente cobrador"]
    n_opos["Agente pós-venda"]
    n_oedit["Agente editor de conteúdo"]
    n_oanal["Analista semanal"]
    n_ofisc["Organizador fiscal"]
    n_orevo["Revisor de oferta"]
    n_ocomp["Agente comprador"]
    n_oimpl["Roteiro de implantação"]
    n_oinst["Instaladores (PowerShell e bash)"]
    n_overif["Verificadores"]
    n_opipe["Pipeline de conteúdo"]
  end
  subgraph L_pub["Público e canais"]
    n_ig["Instagram"]
    n_li["LinkedIn"]
    n_wa["WhatsApp Business"]
    n_yt["YouTube"]
  end
  subgraph L_mkt["Marketing, automação e medição"]
    n_aprov["Aprovação no celular"]
  end
  subgraph L_venda["Plataformas de venda e recebimento"]
    n_crm["CRM simples (planilha)"]
    n_mailer["MailerLite"]
    n_mp["Mercado Pago"]
    n_pixa["Pix Automático + gateway (ex.: Asaas)"]
  end
  subgraph L_emp["Pessoa física: impostos e finanças"]
    n_conta["Contador"]
    n_nfse["Carnê-leão (Receita Federal)"]
  end
  subgraph L_prod["Produtos (o que você vende)"]
    n_curso["Mini-curso Lógica de Programação"]
    n_livro["Livro Lógica e Máquina"]
    n_sites["Sites para pequenas empresas"]
  end
  subgraph L_neg["Negócios do grupo (Barbacena)"]
    n_nloja["Loja AMtech (assistência)"]
    n_npad["Padaria + café da manhã + almoço"]
    n_nplan["Planejador do Grupo"]
    n_nsoft["AMtech Software (projetos e SaaS)"]
    n_nsushi["Sushi (delivery)"]
  end
  subgraph L_cont["Produção de conteúdo"]
    n_voz["Voz clonada (ElevenLabs)"]
    n_whis["Whisper (local)"]
  end
  subgraph L_app["Aplicação: sistemas AM (Aura)"]
    n_nkaix["AM Kaixara (PDV e cardápio)"]
  end
  subgraph L_obs["Observabilidade"]
    n_graf["Grafana"]
  end
  subgraph L_cnt["Containers, Kubernetes e infra como código"]
    n_docker["Docker + Compose"]
    n_n8n["n8n"]
  end
  subgraph L_lin["Linux (Ubuntu no WSL2, Arch no 2º disco)"]
    n_wsl["Ubuntu (WSL2)"]
  end
  subgraph L_win["Windows 11, apps e máquinas virtuais"]
    n_w11["Windows 11 Home"]
  end
  n_ocatal -->|"fila por pontuação"| n_oesteira
  n_ocatal -->|"negócios físicos"| n_nplan
  n_oesteira -->|"portão de lançamento"| n_oqual
  n_oesteira -->|"lança"| n_curso
  n_oesteira -->|"lança"| n_livro
  n_oesteira -->|"lança"| n_nsoft
  n_orevo -->|"confere"| n_oqual
  n_oaval -->|"melhoria"| n_oqual
  n_omarca -->|"perfil"| n_ig
  n_omarca -->|"canal"| n_yt
  n_omarca -->|"carreira e B2B"| n_li
  n_omarca -->|"rosto"| n_obuild
  n_ogbp -->|"presença local"| n_nloja
  n_ogbp -->|"presença local"| n_nsushi
  n_ogbp -->|"presença local"| n_npad
  n_opos -->|"pede avaliação"| n_ogbp
  n_opos -->|"NPS"| n_oaval
  n_ocrm -->|"etiquetas"| n_mailer
  n_opos -->|"próximo passo"| n_ocrm
  n_crm -->|"vira"| n_ocrm
  n_ofly -->|"trabalho capturado"| n_oedit
  n_ofly -->|"decisões reais"| n_obuild
  n_opipe -->|"alimentado por"| n_ofly
  n_obuild -->|"vídeo semanal"| n_yt
  n_oatend -->|"responde"| n_wa
  n_n8n -->|"roda"| n_oatend
  n_oorc -->|"propostas"| n_sites
  n_ocob -->|"Pix"| n_pixa
  n_ocob -->|"cobrança"| n_mp
  n_n8n -->|"roda"| n_ocob
  n_n8n -->|"roda"| n_opos
  n_oedit -->|"fila de aprovação"| n_aprov
  n_oedit -->|"narração"| n_voz
  n_whis -->|"transcrição"| n_oedit
  n_opipe -->|"executa"| n_oedit
  n_oanal -->|"lê o painel"| n_graf
  n_ofisc -->|"carnê-leão"| n_nfse
  n_ofisc -->|"entrega ao contador"| n_conta
  n_ocomp -->|"estoque mínimo"| n_nkaix
  n_oimpl -->|"passos com script"| n_oinst
  n_oinst -->|"depois confere"| n_overif
  n_oinst -->|"instala"| n_opipe
  n_overif -->|"confere"| n_wsl
  n_overif -->|"confere"| n_docker
  n_overif -->|"confere"| n_w11
  n_overif -->|"confere"| n_n8n
  n_overif -->|"confere"| n_graf
  n_whis -->|"transcreve"| n_opipe
  classDef desta fill:#e2ecec,stroke:#0e3a45,color:#13262b
  class n_ocatal,n_oesteira,n_oqual,n_omarca,n_ogbp,n_oaval,n_ocrm,n_ofly,n_obuild,n_oatend,n_oorc,n_ocob,n_opos,n_oedit,n_oanal,n_ofisc,n_orevo,n_ocomp,n_oimpl,n_oinst,n_overif,n_opipe desta
```

## Blocos

| Bloco | Tipo | O que faz |
|---|---|---|
| [Portfólio de ofertas](#ocatal) | Local | data/portfolio.json: todas as ofertas do grupo com estágio, notas, pontuação e próximo passo. Gera docs/operacao/portfolio.md e o portfólio interativo. |
| [Esteira de ofertas](#oesteira) | Local | Ideia, validação, construção, lançamento e escala, com portões objetivos. Uma oferta em construção e uma em validação por vez. |
| [Padrão de qualidade](#oqual) | Local | Checklist de 'pronto' por tipo de oferta: infoproduto, livro, software, serviço, negócio físico e conteúdo. |
| [Marca pessoal Alan Mateus](#omarca) | Remoto | O guarda-chuva de confiança do grupo: Instituto AMS, Editora AMS Silva, AMtech e os negócios locais apontam para você. |
| [Google Perfil da Empresa](#ogbp) | Remoto · precisa de conta · futuro | O canal local mais importante: loja, assistência e restaurantes. Post semanal, fotos, horários e resposta a avaliações em 24 h. |
| [NPS e avaliações](#oaval) | Remoto | Uma pergunta depois de cada compra ou serviço e pedido de avaliação no Google. Reclamação vira issue da oferta. |
| [CRM único + LGPD](#ocrm) | Local | Uma ficha por cliente com ofertas compradas, origem e consentimento. Começa em planilha e MailerLite; vira tabela no PostgreSQL do grupo. |
| [Flywheel de conteúdo](#ofly) | Local | Cada aula, capítulo, projeto, reparo ou prato vira várias peças: cortes, carrossel, artigo, newsletter, questão, template. |
| [Canal build in public](#obuild) | Remoto · precisa de conta · futuro | Vídeo semanal com rosto mostrando decisões reais do grupo: números, setup, aulas. Gera confiança para todas as ofertas. |
| [Agente atendente (WhatsApp)](#oatend) | Local · futuro | Responde perguntas frequentes, mostra catálogo e horários e agenda. Passa para você o que não souber. Nunca promete preço fora da tabela. |
| [Agente orçamentista](#oorc) | Local · futuro | Monta propostas a partir dos pacotes e do histórico, para você aprovar. |
| [Agente cobrador](#ocob) | Local · futuro | Lembra vencimentos e envia o Pix; avisa você nos atrasos. Não faz estorno nem acordo sozinho. |
| [Agente pós-venda](#opos) | Local · futuro | Pergunta a nota, pede avaliação e oferece o próximo passo da jornada do cliente. |
| [Agente editor de conteúdo](#oedit) | Local | Transforma transcrições em cortes, títulos, legendas, carrosséis, posts do Google e newsletter, seguindo o guia de estilo da marca. |
| [Analista semanal](#oanal) | Local · futuro | Lê o painel toda segunda e manda 3 fatos e 1 sugestão de decisão. Só leitura. |
| [Organizador fiscal](#ofisc) | Local · futuro | Junta notas, extratos e vendas do mês para o contador e para o carnê-leão. |
| [Revisor de oferta](#orevo) | Local | Confere cada lançamento contra o padrão de qualidade antes de ir ao ar. |
| [Agente comprador](#ocomp) | Local · futuro | Sugere a lista de compras dos negócios de comida pelo estoque mínimo e pela previsão de produção. |
| [Roteiro de implantação](#oimpl) | Local | data/implantacao.json: fases e passos com critério de pronto, cada passo ligado aos blocos que implanta. Gera docs/implantacao/roteiro.md e a página de acompanhamento; o CI falha se um bloco do setup ficar de fora. |
| [Instaladores (PowerShell e bash)](#oinst) | Local | instalar.ps1 (winget, WSL2, .wslconfig) e bootstrap.sh (ferramentas, linguagens, Claude Code, ai-jail, Git assinado). Seguros para rodar de novo. |
| [Verificadores](#overif) | Local | verificar.ps1 e verificar.sh: somente leitura, dizem 'pronto' ou listam o que falta. Também conferem os serviços da automação. |
| [Pipeline de conteúdo](#opipe) | Local | tools/conteudo/processar.py com timer de 15 min: entrada → transcrição → peças pelo guia de marca → fila de aprovação → aviso no Telegram. |

<a id="ocatal"></a>

### Portfólio de ofertas

*Local*

data/portfolio.json: todas as ofertas do grupo com estágio, notas, pontuação e próximo passo. Gera docs/operacao/portfolio.md e o portfólio interativo.

| Direção | Bloco | Camada | O que passa |
|---|---|---|---|
| → envia para | [Esteira de ofertas](22-oper.md#oesteira) | Operação do grupo (esteira, marca, qualidade) | fila por pontuação |
| → envia para | [Planejador do Grupo](15-neg.md#nplan) | Negócios do grupo (Barbacena) | negócios físicos |

<a id="oesteira"></a>

### Esteira de ofertas

*Local*

Ideia, validação, construção, lançamento e escala, com portões objetivos. Uma oferta em construção e uma em validação por vez.

| Direção | Bloco | Camada | O que passa |
|---|---|---|---|
| → envia para | [Padrão de qualidade](22-oper.md#oqual) | Operação do grupo (esteira, marca, qualidade) | portão de lançamento |
| → envia para | [Mini-curso Lógica de Programação](16-prod.md#curso) | Produtos (o que você vende) | lança |
| → envia para | [Livro Lógica e Máquina](16-prod.md#livro) | Produtos (o que você vende) | lança |
| → envia para | [AMtech Software (projetos e SaaS)](15-neg.md#nsoft) | Negócios do grupo (Barbacena) | lança |
| ← recebe de | [Portfólio de ofertas](22-oper.md#ocatal) | Operação do grupo (esteira, marca, qualidade) | fila por pontuação |

<a id="oqual"></a>

### Padrão de qualidade

*Local*

Checklist de 'pronto' por tipo de oferta: infoproduto, livro, software, serviço, negócio físico e conteúdo.

| Direção | Bloco | Camada | O que passa |
|---|---|---|---|
| ← recebe de | [Esteira de ofertas](22-oper.md#oesteira) | Operação do grupo (esteira, marca, qualidade) | portão de lançamento |
| ← recebe de | [Revisor de oferta](22-oper.md#orevo) | Operação do grupo (esteira, marca, qualidade) | confere |
| ← recebe de | [NPS e avaliações](22-oper.md#oaval) | Operação do grupo (esteira, marca, qualidade) | melhoria |

<a id="omarca"></a>

### Marca pessoal Alan Mateus

*Remoto*

O guarda-chuva de confiança do grupo: Instituto AMS, Editora AMS Silva, AMtech e os negócios locais apontam para você.

| Direção | Bloco | Camada | O que passa |
|---|---|---|---|
| → envia para | [Instagram](21-pub.md#ig) | Público e canais | perfil |
| → envia para | [YouTube](21-pub.md#yt) | Público e canais | canal |
| → envia para | [LinkedIn](21-pub.md#li) | Público e canais | carreira e B2B |
| → envia para | [Canal build in public](22-oper.md#obuild) | Operação do grupo (esteira, marca, qualidade) | rosto |

<a id="ogbp"></a>

### Google Perfil da Empresa

*Remoto · precisa de conta · futuro*

O canal local mais importante: loja, assistência e restaurantes. Post semanal, fotos, horários e resposta a avaliações em 24 h.

| Direção | Bloco | Camada | O que passa |
|---|---|---|---|
| → envia para | [Loja AMtech (assistência)](15-neg.md#nloja) | Negócios do grupo (Barbacena) | presença local |
| → envia para | [Sushi (delivery)](15-neg.md#nsushi) | Negócios do grupo (Barbacena) | presença local |
| → envia para | [Padaria + café da manhã + almoço](15-neg.md#npad) | Negócios do grupo (Barbacena) | presença local |
| ← recebe de | [Agente pós-venda](22-oper.md#opos) | Operação do grupo (esteira, marca, qualidade) | pede avaliação |

<a id="oaval"></a>

### NPS e avaliações

*Remoto*

Uma pergunta depois de cada compra ou serviço e pedido de avaliação no Google. Reclamação vira issue da oferta.

| Direção | Bloco | Camada | O que passa |
|---|---|---|---|
| → envia para | [Padrão de qualidade](22-oper.md#oqual) | Operação do grupo (esteira, marca, qualidade) | melhoria |
| ← recebe de | [Agente pós-venda](22-oper.md#opos) | Operação do grupo (esteira, marca, qualidade) | NPS |

<a id="ocrm"></a>

### CRM único + LGPD

*Local*

Uma ficha por cliente com ofertas compradas, origem e consentimento. Começa em planilha e MailerLite; vira tabela no PostgreSQL do grupo.

| Direção | Bloco | Camada | O que passa |
|---|---|---|---|
| → envia para | [MailerLite](19-venda.md#mailer) | Plataformas de venda e recebimento | etiquetas |
| ← recebe de | [Agente pós-venda](22-oper.md#opos) | Operação do grupo (esteira, marca, qualidade) | próximo passo |
| ← recebe de | [CRM simples (planilha)](19-venda.md#crm) | Plataformas de venda e recebimento | vira |

<a id="ofly"></a>

### Flywheel de conteúdo

*Local*

Cada aula, capítulo, projeto, reparo ou prato vira várias peças: cortes, carrossel, artigo, newsletter, questão, template.

| Direção | Bloco | Camada | O que passa |
|---|---|---|---|
| → envia para | [Agente editor de conteúdo](22-oper.md#oedit) | Operação do grupo (esteira, marca, qualidade) | trabalho capturado |
| → envia para | [Canal build in public](22-oper.md#obuild) | Operação do grupo (esteira, marca, qualidade) | decisões reais |
| ← recebe de | [Pipeline de conteúdo](22-oper.md#opipe) | Operação do grupo (esteira, marca, qualidade) | alimentado por |

<a id="obuild"></a>

### Canal build in public

*Remoto · precisa de conta · futuro*

Vídeo semanal com rosto mostrando decisões reais do grupo: números, setup, aulas. Gera confiança para todas as ofertas.

| Direção | Bloco | Camada | O que passa |
|---|---|---|---|
| → envia para | [YouTube](21-pub.md#yt) | Público e canais | vídeo semanal |
| ← recebe de | [Flywheel de conteúdo](22-oper.md#ofly) | Operação do grupo (esteira, marca, qualidade) | decisões reais |
| ← recebe de | [Marca pessoal Alan Mateus](22-oper.md#omarca) | Operação do grupo (esteira, marca, qualidade) | rosto |

<a id="oatend"></a>

### Agente atendente (WhatsApp)

*Local · futuro*

Responde perguntas frequentes, mostra catálogo e horários e agenda. Passa para você o que não souber. Nunca promete preço fora da tabela.

| Direção | Bloco | Camada | O que passa |
|---|---|---|---|
| → envia para | [WhatsApp Business](21-pub.md#wa) | Público e canais | responde |
| ← recebe de | [n8n](08-cnt.md#n8n) | Containers, Kubernetes e infra como código | roda |

<a id="oorc"></a>

### Agente orçamentista

*Local · futuro*

Monta propostas a partir dos pacotes e do histórico, para você aprovar.

| Direção | Bloco | Camada | O que passa |
|---|---|---|---|
| → envia para | [Sites para pequenas empresas](16-prod.md#sites) | Produtos (o que você vende) | propostas |

<a id="ocob"></a>

### Agente cobrador

*Local · futuro*

Lembra vencimentos e envia o Pix; avisa você nos atrasos. Não faz estorno nem acordo sozinho.

| Direção | Bloco | Camada | O que passa |
|---|---|---|---|
| → envia para | [Pix Automático + gateway (ex.: Asaas)](19-venda.md#pixa) | Plataformas de venda e recebimento | Pix |
| → envia para | [Mercado Pago](19-venda.md#mp) | Plataformas de venda e recebimento | cobrança |
| ← recebe de | [n8n](08-cnt.md#n8n) | Containers, Kubernetes e infra como código | roda |

<a id="opos"></a>

### Agente pós-venda

*Local · futuro*

Pergunta a nota, pede avaliação e oferece o próximo passo da jornada do cliente.

| Direção | Bloco | Camada | O que passa |
|---|---|---|---|
| → envia para | [Google Perfil da Empresa](22-oper.md#ogbp) | Operação do grupo (esteira, marca, qualidade) | pede avaliação |
| → envia para | [NPS e avaliações](22-oper.md#oaval) | Operação do grupo (esteira, marca, qualidade) | NPS |
| → envia para | [CRM único + LGPD](22-oper.md#ocrm) | Operação do grupo (esteira, marca, qualidade) | próximo passo |
| ← recebe de | [n8n](08-cnt.md#n8n) | Containers, Kubernetes e infra como código | roda |

<a id="oedit"></a>

### Agente editor de conteúdo

*Local*

Transforma transcrições em cortes, títulos, legendas, carrosséis, posts do Google e newsletter, seguindo o guia de estilo da marca.

| Direção | Bloco | Camada | O que passa |
|---|---|---|---|
| → envia para | [Aprovação no celular](20-mkt.md#aprov) | Marketing, automação e medição | fila de aprovação |
| → envia para | [Voz clonada (ElevenLabs)](12-cont.md#voz) | Produção de conteúdo | narração |
| ← recebe de | [Flywheel de conteúdo](22-oper.md#ofly) | Operação do grupo (esteira, marca, qualidade) | trabalho capturado |
| ← recebe de | [Whisper (local)](12-cont.md#whis) | Produção de conteúdo | transcrição |
| ← recebe de | [Pipeline de conteúdo](22-oper.md#opipe) | Operação do grupo (esteira, marca, qualidade) | executa |

<a id="oanal"></a>

### Analista semanal

*Local · futuro*

Lê o painel toda segunda e manda 3 fatos e 1 sugestão de decisão. Só leitura.

| Direção | Bloco | Camada | O que passa |
|---|---|---|---|
| → envia para | [Grafana](09-obs.md#graf) | Observabilidade | lê o painel |

<a id="ofisc"></a>

### Organizador fiscal

*Local · futuro*

Junta notas, extratos e vendas do mês para o contador e para o carnê-leão.

| Direção | Bloco | Camada | O que passa |
|---|---|---|---|
| → envia para | [Carnê-leão (Receita Federal)](18-emp.md#nfse) | Pessoa física: impostos e finanças | carnê-leão |
| → envia para | [Contador](18-emp.md#conta) | Pessoa física: impostos e finanças | entrega ao contador |

<a id="orevo"></a>

### Revisor de oferta

*Local*

Confere cada lançamento contra o padrão de qualidade antes de ir ao ar.

| Direção | Bloco | Camada | O que passa |
|---|---|---|---|
| → envia para | [Padrão de qualidade](22-oper.md#oqual) | Operação do grupo (esteira, marca, qualidade) | confere |

<a id="ocomp"></a>

### Agente comprador

*Local · futuro*

Sugere a lista de compras dos negócios de comida pelo estoque mínimo e pela previsão de produção.

| Direção | Bloco | Camada | O que passa |
|---|---|---|---|
| → envia para | [AM Kaixara (PDV e cardápio)](10-app.md#nkaix) | Aplicação: sistemas AM (Aura) | estoque mínimo |

<a id="oimpl"></a>

### Roteiro de implantação

*Local*

data/implantacao.json: fases e passos com critério de pronto, cada passo ligado aos blocos que implanta. Gera docs/implantacao/roteiro.md e a página de acompanhamento; o CI falha se um bloco do setup ficar de fora.

| Direção | Bloco | Camada | O que passa |
|---|---|---|---|
| → envia para | [Instaladores (PowerShell e bash)](22-oper.md#oinst) | Operação do grupo (esteira, marca, qualidade) | passos com script |

<a id="oinst"></a>

### Instaladores (PowerShell e bash)

*Local*

instalar.ps1 (winget, WSL2, .wslconfig) e bootstrap.sh (ferramentas, linguagens, Claude Code, ai-jail, Git assinado). Seguros para rodar de novo.

| Direção | Bloco | Camada | O que passa |
|---|---|---|---|
| → envia para | [Verificadores](22-oper.md#overif) | Operação do grupo (esteira, marca, qualidade) | depois confere |
| → envia para | [Pipeline de conteúdo](22-oper.md#opipe) | Operação do grupo (esteira, marca, qualidade) | instala |
| ← recebe de | [Roteiro de implantação](22-oper.md#oimpl) | Operação do grupo (esteira, marca, qualidade) | passos com script |

<a id="overif"></a>

### Verificadores

*Local*

verificar.ps1 e verificar.sh: somente leitura, dizem 'pronto' ou listam o que falta. Também conferem os serviços da automação.

| Direção | Bloco | Camada | O que passa |
|---|---|---|---|
| → envia para | [Ubuntu (WSL2)](04-lin.md#wsl) | Linux (Ubuntu no WSL2, Arch no 2º disco) | confere |
| → envia para | [Docker + Compose](08-cnt.md#docker) | Containers, Kubernetes e infra como código | confere |
| → envia para | [Windows 11 Home](03-win.md#w11) | Windows 11, apps e máquinas virtuais | confere |
| → envia para | [n8n](08-cnt.md#n8n) | Containers, Kubernetes e infra como código | confere |
| → envia para | [Grafana](09-obs.md#graf) | Observabilidade | confere |
| ← recebe de | [Instaladores (PowerShell e bash)](22-oper.md#oinst) | Operação do grupo (esteira, marca, qualidade) | depois confere |

<a id="opipe"></a>

### Pipeline de conteúdo

*Local*

tools/conteudo/processar.py com timer de 15 min: entrada → transcrição → peças pelo guia de marca → fila de aprovação → aviso no Telegram.

| Direção | Bloco | Camada | O que passa |
|---|---|---|---|
| → envia para | [Agente editor de conteúdo](22-oper.md#oedit) | Operação do grupo (esteira, marca, qualidade) | executa |
| → envia para | [Flywheel de conteúdo](22-oper.md#ofly) | Operação do grupo (esteira, marca, qualidade) | alimentado por |
| ← recebe de | [Whisper (local)](12-cont.md#whis) | Produção de conteúdo | transcreve |
| ← recebe de | [Instaladores (PowerShell e bash)](22-oper.md#oinst) | Operação do grupo (esteira, marca, qualidade) | instala |

---

[↓ Camada 21 · Público e canais](21-pub.md)
