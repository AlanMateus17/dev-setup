<!-- Arquivo GERADO por tools/gerar_docs.py a partir de data/. Edite os dados, não este arquivo. -->


# Camada 18 · Marketing, automação e medição

[← Arquitetura](../arquitetura.md) · [Índice da documentação](../README.md)

> **Ligação com a camada de baixo:** O que é publicado e anunciado aqui leva às plataformas de venda; cada venda volta como dado para o banco de métricas.

**16 blocos** · 3 precisam de conta · 10 marcados como futuro

## Mapa de conexões

```mermaid
flowchart LR
  subgraph L_mkt["Marketing, automação e medição"]
    n_isca["Isca grátis + sequência de e-mails"]
    n_postiz["Postiz (agendador)"]
    n_aprov["Aprovação no celular"]
    n_horario["Algoritmo de horário"]
    n_pixel["Pixel + API de Conversões"]
    n_utm["Padrão de UTM"]
    n_gads["Google e YouTube Ads"]
    n_ttads["TikTok Ads"]
    n_regras["Regras de corte"]
    n_calc["Lucro por Venda (calculadora)"]
    n_hooks["Webhooks de venda"]
    n_metrics["Banco de métricas (PostgreSQL)"]
    n_painel["Painel de lucro (Grafana)"]
    n_afprog["Programa de afiliados"]
    n_prosp["Prospecção de parceiros"]
    n_dub["Dublagem (YouTube + ElevenLabs)"]
  end
  subgraph L_pub["Público e canais"]
    n_facebook["Facebook"]
    n_ig["Instagram"]
    n_li["LinkedIn"]
    n_tiktok["TikTok"]
    n_yt["YouTube"]
  end
  subgraph L_venda["Plataformas de venda e recebimento"]
    n_ads["Anúncios (Meta Ads)"]
    n_eduzz["Eduzz"]
    n_hotm["Hotmart"]
    n_kiwi["Kiwify"]
    n_mailer["MailerLite"]
  end
  subgraph L_emp["Pessoa física: impostos e finanças"]
    n_nfse["Carnê-leão (Receita Federal)"]
  end
  subgraph L_web["Vitrine web (sites e domínio)"]
    n_inst["Instituto AMS"]
  end
  subgraph L_cont["Produção de conteúdo"]
    n_voz["Voz clonada (ElevenLabs)"]
  end
  subgraph L_cnt["Containers, Kubernetes e infra como código"]
    n_n8n["n8n"]
  end
  subgraph L_clc["Claude: recursos, conectores e plugins"]
    n_cvid["Conector vidIQ"]
    n_pbiz["Plugins: small- business + marketing"]
  end
  n_isca -->|"sequência"| n_mailer
  n_inst -->|"captura o e-mail"| n_isca
  n_postiz -->|"publica"| n_yt
  n_postiz -->|"publica"| n_ig
  n_postiz -->|"publica"| n_tiktok
  n_postiz -->|"publica"| n_facebook
  n_postiz -->|"publica"| n_li
  n_n8n -->|"manda o post aprovado"| n_postiz
  n_utm -->|"marca os links"| n_postiz
  n_aprov -->|"libera"| n_n8n
  n_horario -->|"escolhe o horário"| n_n8n
  n_metrics -->|"desempenho por horário"| n_horario
  n_pixel -->|"eventos de compra"| n_inst
  n_pixel -->|"otimiza para venda"| n_ads
  n_utm -->|"marca os links"| n_ads
  n_gads -->|"gasto"| n_metrics
  n_regras -->|"pausa ou escala"| n_gads
  n_ttads -->|"gasto"| n_metrics
  n_regras -->|"pausa ou escala"| n_ttads
  n_regras -->|"pausa ou escala"| n_ads
  n_calc -->|"CPA e ROAS de empate"| n_regras
  n_painel -->|"dispara alertas"| n_regras
  n_calc -->|"comissão máxima"| n_afprog
  n_hooks -->|"dispara"| n_n8n
  n_hotm -->|"venda e reembolso"| n_hooks
  n_kiwi -->|"venda e reembolso"| n_hooks
  n_eduzz -->|"venda e reembolso"| n_hooks
  n_metrics -->|"consultas"| n_painel
  n_metrics -->|"base do carnê-leão"| n_nfse
  n_n8n -->|"grava"| n_metrics
  n_ads -->|"gasto por campanha"| n_metrics
  n_afprog -->|"afiliados cadastrados"| n_hotm
  n_prosp -->|"novos afiliados"| n_afprog
  n_cvid -->|"canais semelhantes"| n_prosp
  n_pbiz -->|"rascunho de propostas"| n_prosp
  n_dub -->|"faixas de áudio"| n_yt
  n_voz -->|"sua voz em outros idiomas"| n_dub
  classDef desta fill:#e2ecec,stroke:#0e3a45,color:#13262b
  class n_isca,n_postiz,n_aprov,n_horario,n_pixel,n_utm,n_gads,n_ttads,n_regras,n_calc,n_hooks,n_metrics,n_painel,n_afprog,n_prosp,n_dub desta
```

## Blocos

| Bloco | Tipo | O que faz |
|---|---|---|
| [Isca grátis + sequência de e-mails](#isca) | Local | Aula ou PDF grátis que captura o e-mail e abre uma sequência de 5 a 7 e-mails até o mini-curso. |
| [Postiz (agendador)](#postiz) | Local · futuro | Agendador open source (AGPL-3.0) que publica em mais de 28 redes. Roda no seu Docker com PostgreSQL e Redis; integra com o n8n. |
| [Aprovação no celular](#aprov) | Local · futuro | Nenhum post sai sem o seu ok (Telegram ou e-mail). Protege o canal de erro da IA. |
| [Algoritmo de horário](#horario) | Local · futuro | Calcula o desempenho por rede, dia e hora com os seus dados; 80% dos posts nas melhores faixas, 20% testando faixas novas. |
| [Pixel + API de Conversões](#pixel) | Remoto · precisa de conta | Pixel e CAPI da Meta juntos, com deduplicação por event_id. Sem isso o anúncio não aprende quem compra. |
| [Padrão de UTM](#utm) | Local | Todo link marcado com fonte, meio, campanha e criativo, para ligar cada venda ao anúncio ou post que a trouxe. |
| [Google e YouTube Ads](#gads) | Remoto · precisa de conta · futuro | Para vídeos longos que já convertem e buscas com intenção de compra. |
| [TikTok Ads](#ttads) | Remoto · precisa de conta · futuro | Depois que os cortes orgânicos mostrarem tração. |
| [Regras de corte](#regras) | Local | Pausa criativo ou conjunto quando o CPA passa do de empate; sobe 15% do orçamento quando fica abaixo do CPA da margem. |
| [Lucro por Venda (calculadora)](#calc) | Remoto | Artefato com taxas das plataformas, imposto, CPA e ROAS de empate, simulador e o lucro real de cada campanha. |
| [Webhooks de venda](#hooks) | Remoto · futuro | Hotmart, Kiwify e Eduzz avisam cada venda e reembolso; o n8n grava no banco. |
| [Banco de métricas (PostgreSQL)](#metrics) | Local · futuro | Tabelas de produtos, vendas, gastos, ferramentas e impostos. |
| [Painel de lucro (Grafana)](#painel) | Local · futuro | Lucro por produto, canal, campanha e país, atualizado sozinho. |
| [Programa de afiliados](#afprog) | Remoto · futuro | Comissão definida pela calculadora, aberta depois de 20 vendas próprias. |
| [Prospecção de parceiros](#prosp) | Local | Busca e qualificação de parceiros com IA; mensagem revisada e enviada por você. |
| [Dublagem (YouTube + ElevenLabs)](#dub) | Remoto · futuro | Dublagem automática do YouTube para vídeos; ElevenLabs para cursos fora do YouTube. Espanhol primeiro. |

<a id="isca"></a>

### Isca grátis + sequência de e-mails

*Local*

Aula ou PDF grátis que captura o e-mail e abre uma sequência de 5 a 7 e-mails até o mini-curso.

| Direção | Bloco | Camada | O que passa |
|---|---|---|---|
| → envia para | [MailerLite](17-venda.md#mailer) | Plataformas de venda e recebimento | sequência |
| ← recebe de | [Instituto AMS](15-web.md#inst) | Vitrine web (sites e domínio) | captura o e-mail |

<a id="postiz"></a>

### Postiz (agendador)

*Local · futuro*

Agendador open source (AGPL-3.0) que publica em mais de 28 redes. Roda no seu Docker com PostgreSQL e Redis; integra com o n8n.

| Direção | Bloco | Camada | O que passa |
|---|---|---|---|
| → envia para | [YouTube](19-pub.md#yt) | Público e canais | publica |
| → envia para | [Instagram](19-pub.md#ig) | Público e canais | publica |
| → envia para | [TikTok](19-pub.md#tiktok) | Público e canais | publica |
| → envia para | [Facebook](19-pub.md#facebook) | Público e canais | publica |
| → envia para | [LinkedIn](19-pub.md#li) | Público e canais | publica |
| ← recebe de | [n8n](08-cnt.md#n8n) | Containers, Kubernetes e infra como código | manda o post aprovado |
| ← recebe de | [Padrão de UTM](18-mkt.md#utm) | Marketing, automação e medição | marca os links |

<a id="aprov"></a>

### Aprovação no celular

*Local · futuro*

Nenhum post sai sem o seu ok (Telegram ou e-mail). Protege o canal de erro da IA.

| Direção | Bloco | Camada | O que passa |
|---|---|---|---|
| → envia para | [n8n](08-cnt.md#n8n) | Containers, Kubernetes e infra como código | libera |

<a id="horario"></a>

### Algoritmo de horário

*Local · futuro*

Calcula o desempenho por rede, dia e hora com os seus dados; 80% dos posts nas melhores faixas, 20% testando faixas novas.

| Direção | Bloco | Camada | O que passa |
|---|---|---|---|
| → envia para | [n8n](08-cnt.md#n8n) | Containers, Kubernetes e infra como código | escolhe o horário |
| ← recebe de | [Banco de métricas (PostgreSQL)](18-mkt.md#metrics) | Marketing, automação e medição | desempenho por horário |

<a id="pixel"></a>

### Pixel + API de Conversões

*Remoto · precisa de conta*

Pixel e CAPI da Meta juntos, com deduplicação por event_id. Sem isso o anúncio não aprende quem compra.

| Direção | Bloco | Camada | O que passa |
|---|---|---|---|
| → envia para | [Instituto AMS](15-web.md#inst) | Vitrine web (sites e domínio) | eventos de compra |
| → envia para | [Anúncios (Meta Ads)](17-venda.md#ads) | Plataformas de venda e recebimento | otimiza para venda |

<a id="utm"></a>

### Padrão de UTM

*Local*

Todo link marcado com fonte, meio, campanha e criativo, para ligar cada venda ao anúncio ou post que a trouxe.

| Direção | Bloco | Camada | O que passa |
|---|---|---|---|
| → envia para | [Anúncios (Meta Ads)](17-venda.md#ads) | Plataformas de venda e recebimento | marca os links |
| → envia para | [Postiz (agendador)](18-mkt.md#postiz) | Marketing, automação e medição | marca os links |

<a id="gads"></a>

### Google e YouTube Ads

*Remoto · precisa de conta · futuro*

Para vídeos longos que já convertem e buscas com intenção de compra.

| Direção | Bloco | Camada | O que passa |
|---|---|---|---|
| → envia para | [Banco de métricas (PostgreSQL)](18-mkt.md#metrics) | Marketing, automação e medição | gasto |
| ← recebe de | [Regras de corte](18-mkt.md#regras) | Marketing, automação e medição | pausa ou escala |

<a id="ttads"></a>

### TikTok Ads

*Remoto · precisa de conta · futuro*

Depois que os cortes orgânicos mostrarem tração.

| Direção | Bloco | Camada | O que passa |
|---|---|---|---|
| → envia para | [Banco de métricas (PostgreSQL)](18-mkt.md#metrics) | Marketing, automação e medição | gasto |
| ← recebe de | [Regras de corte](18-mkt.md#regras) | Marketing, automação e medição | pausa ou escala |

<a id="regras"></a>

### Regras de corte

*Local*

Pausa criativo ou conjunto quando o CPA passa do de empate; sobe 15% do orçamento quando fica abaixo do CPA da margem.

| Direção | Bloco | Camada | O que passa |
|---|---|---|---|
| → envia para | [Anúncios (Meta Ads)](17-venda.md#ads) | Plataformas de venda e recebimento | pausa ou escala |
| → envia para | [Google e YouTube Ads](18-mkt.md#gads) | Marketing, automação e medição | pausa ou escala |
| → envia para | [TikTok Ads](18-mkt.md#ttads) | Marketing, automação e medição | pausa ou escala |
| ← recebe de | [Lucro por Venda (calculadora)](18-mkt.md#calc) | Marketing, automação e medição | CPA e ROAS de empate |
| ← recebe de | [Painel de lucro (Grafana)](18-mkt.md#painel) | Marketing, automação e medição | dispara alertas |

<a id="calc"></a>

### Lucro por Venda (calculadora)

*Remoto*

Artefato com taxas das plataformas, imposto, CPA e ROAS de empate, simulador e o lucro real de cada campanha.

| Direção | Bloco | Camada | O que passa |
|---|---|---|---|
| → envia para | [Regras de corte](18-mkt.md#regras) | Marketing, automação e medição | CPA e ROAS de empate |
| → envia para | [Programa de afiliados](18-mkt.md#afprog) | Marketing, automação e medição | comissão máxima |

<a id="hooks"></a>

### Webhooks de venda

*Remoto · futuro*

Hotmart, Kiwify e Eduzz avisam cada venda e reembolso; o n8n grava no banco.

| Direção | Bloco | Camada | O que passa |
|---|---|---|---|
| → envia para | [n8n](08-cnt.md#n8n) | Containers, Kubernetes e infra como código | dispara |
| ← recebe de | [Hotmart](17-venda.md#hotm) | Plataformas de venda e recebimento | venda e reembolso |
| ← recebe de | [Kiwify](17-venda.md#kiwi) | Plataformas de venda e recebimento | venda e reembolso |
| ← recebe de | [Eduzz](17-venda.md#eduzz) | Plataformas de venda e recebimento | venda e reembolso |

<a id="metrics"></a>

### Banco de métricas (PostgreSQL)

*Local · futuro*

Tabelas de produtos, vendas, gastos, ferramentas e impostos.

| Direção | Bloco | Camada | O que passa |
|---|---|---|---|
| → envia para | [Painel de lucro (Grafana)](18-mkt.md#painel) | Marketing, automação e medição | consultas |
| → envia para | [Algoritmo de horário](18-mkt.md#horario) | Marketing, automação e medição | desempenho por horário |
| → envia para | [Carnê-leão (Receita Federal)](16-emp.md#nfse) | Pessoa física: impostos e finanças | base do carnê-leão |
| ← recebe de | [n8n](08-cnt.md#n8n) | Containers, Kubernetes e infra como código | grava |
| ← recebe de | [Anúncios (Meta Ads)](17-venda.md#ads) | Plataformas de venda e recebimento | gasto por campanha |
| ← recebe de | [Google e YouTube Ads](18-mkt.md#gads) | Marketing, automação e medição | gasto |
| ← recebe de | [TikTok Ads](18-mkt.md#ttads) | Marketing, automação e medição | gasto |

<a id="painel"></a>

### Painel de lucro (Grafana)

*Local · futuro*

Lucro por produto, canal, campanha e país, atualizado sozinho.

| Direção | Bloco | Camada | O que passa |
|---|---|---|---|
| → envia para | [Regras de corte](18-mkt.md#regras) | Marketing, automação e medição | dispara alertas |
| ← recebe de | [Banco de métricas (PostgreSQL)](18-mkt.md#metrics) | Marketing, automação e medição | consultas |

<a id="afprog"></a>

### Programa de afiliados

*Remoto · futuro*

Comissão definida pela calculadora, aberta depois de 20 vendas próprias.

| Direção | Bloco | Camada | O que passa |
|---|---|---|---|
| → envia para | [Hotmart](17-venda.md#hotm) | Plataformas de venda e recebimento | afiliados cadastrados |
| ← recebe de | [Prospecção de parceiros](18-mkt.md#prosp) | Marketing, automação e medição | novos afiliados |
| ← recebe de | [Lucro por Venda (calculadora)](18-mkt.md#calc) | Marketing, automação e medição | comissão máxima |

<a id="prosp"></a>

### Prospecção de parceiros

*Local*

Busca e qualificação de parceiros com IA; mensagem revisada e enviada por você.

| Direção | Bloco | Camada | O que passa |
|---|---|---|---|
| → envia para | [Programa de afiliados](18-mkt.md#afprog) | Marketing, automação e medição | novos afiliados |
| ← recebe de | [Conector vidIQ](07-clc.md#cvid) | Claude: recursos, conectores e plugins | canais semelhantes |
| ← recebe de | [Plugins: small- business + marketing](07-clc.md#pbiz) | Claude: recursos, conectores e plugins | rascunho de propostas |

<a id="dub"></a>

### Dublagem (YouTube + ElevenLabs)

*Remoto · futuro*

Dublagem automática do YouTube para vídeos; ElevenLabs para cursos fora do YouTube. Espanhol primeiro.

| Direção | Bloco | Camada | O que passa |
|---|---|---|---|
| → envia para | [YouTube](19-pub.md#yt) | Público e canais | faixas de áudio |
| ← recebe de | [Voz clonada (ElevenLabs)](12-cont.md#voz) | Produção de conteúdo | sua voz em outros idiomas |

---

[↑ Camada 19 · Público e canais](19-pub.md) · [↓ Camada 17 · Plataformas de venda e recebimento](17-venda.md)
