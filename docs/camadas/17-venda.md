<!-- Arquivo GERADO por tools/gerar_docs.py a partir de data/. Edite os dados, não este arquivo. -->


# Camada 17 · Plataformas de venda e recebimento

[← Arquitetura](../arquitetura.md) · [Índice da documentação](../README.md)

> **Ligação com a camada de baixo:** Cada venda é lançada no carnê-leão e o dinheiro cai na sua conta separada.

**14 blocos** · 13 precisam de conta · 3 marcados como futuro

## Mapa de conexões

```mermaid
flowchart LR
  subgraph L_venda["Plataformas de venda e recebimento"]
    n_pixa["Pix Automático + gateway (ex.: Asaas)"]
    n_agenda["Agenda online (Cal.com)"]
    n_comu["Comunidade (Discord ou grupo)"]
    n_ads["Anúncios (Meta Ads)"]
    n_crm["CRM simples (planilha)"]
    n_hotm["Hotmart"]
    n_kiwi["Kiwify"]
    n_eduzz["Eduzz"]
    n_udemy["Udemy"]
    n_dio["DIO (parceria)"]
    n_ytm["YouTube (membros)"]
    n_mp["Mercado Pago"]
    n_mailer["MailerLite"]
    n_afil["Afiliados (Amazon, Hotmart…)"]
  end
  subgraph L_pub["Público e canais"]
    n_ig["Instagram"]
    n_yt["YouTube"]
  end
  subgraph L_mkt["Marketing, automação e medição"]
    n_afprog["Programa de afiliados"]
    n_hooks["Webhooks de venda"]
    n_isca["Isca grátis + sequência de e-mails"]
    n_metrics["Banco de métricas (PostgreSQL)"]
    n_pixel["Pixel + API de Conversões"]
    n_regras["Regras de corte"]
    n_utm["Padrão de UTM"]
  end
  subgraph L_emp["Pessoa física: impostos e finanças"]
    n_banco["Conta bancária separada (CPF)"]
    n_nfse["Carnê-leão (Receita Federal)"]
  end
  subgraph L_web["Vitrine web (sites e domínio)"]
    n_inst["Instituto AMS"]
    n_mail["E-mail profissional (enviar e receber)"]
    n_site["Site pessoal + blog (Jekyll)"]
  end
  subgraph L_prod["Produtos (o que você vende)"]
    n_aulas["Aulas particulares"]
    n_curso["Mini-curso Lógica de Programação"]
    n_form["Formações (TI, Matemática, Finanças)"]
    n_livro["Livro Lógica e Máquina"]
    n_sites["Sites para pequenas empresas"]
    n_tmpl["Templates e código-fonte"]
  end
  subgraph L_app["Aplicação: sistemas AM (Aura)"]
    n_lic["aura-licensing"]
  end
  subgraph L_cnt["Containers, Kubernetes e infra como código"]
    n_n8n["n8n"]
  end
  subgraph L_clc["Claude: recursos, conectores e plugins"]
    n_cml["Conector MailerLite"]
    n_pbiz["Plugins: small- business + marketing"]
  end
  subgraph L_win["Windows 11, apps e máquinas virtuais"]
    n_nav["Navegador + Claude in Chrome"]
    n_obsd["Obsidian + Git"]
  end
  subgraph L_seg["Segurança e cofre"]
    n_kee["KeePassXC"]
  end
  n_pixa -->|"cobrança recorrente"| n_lic
  n_pixa -->|"recebimento"| n_banco
  n_agenda -->|"horários"| n_aulas
  n_agenda -->|"pagamento"| n_mp
  n_comu -->|"suporte aos alunos"| n_curso
  n_ads -->|"alcance pago"| n_ig
  n_ads -->|"gasto por campanha"| n_metrics
  n_pixel -->|"otimiza para venda"| n_ads
  n_utm -->|"marca os links"| n_ads
  n_regras -->|"pausa ou escala"| n_ads
  n_crm -->|"propostas"| n_sites
  n_hotm -->|"lança no carnê-leão"| n_nfse
  n_hotm -->|"saque"| n_banco
  n_hotm -->|"venda e reembolso"| n_hooks
  n_kee -->|"senhas"| n_hotm
  n_nav -->|"painel web"| n_hotm
  n_pbiz -->|"funil e lançamento"| n_hotm
  n_n8n -->|"webhook de venda"| n_hotm
  n_curso -->|"produto cadastrado"| n_hotm
  n_form -->|"produto"| n_hotm
  n_tmpl -->|"download"| n_hotm
  n_livro -->|"PDF"| n_hotm
  n_inst -->|"botão comprar"| n_hotm
  n_mailer -->|"lançamento"| n_hotm
  n_afprog -->|"afiliados cadastrados"| n_hotm
  n_kiwi -->|"lança no carnê-leão"| n_nfse
  n_kiwi -->|"saque"| n_banco
  n_kiwi -->|"venda e reembolso"| n_hooks
  n_curso -->|"produto"| n_kiwi
  n_inst -->|"botão comprar"| n_kiwi
  n_eduzz -->|"lança no carnê-leão"| n_nfse
  n_eduzz -->|"saque"| n_banco
  n_eduzz -->|"venda e reembolso"| n_hooks
  n_curso -->|"produto"| n_eduzz
  n_udemy -->|"carnê-leão (exterior)"| n_nfse
  n_udemy -->|"PayPal ou Payoneer"| n_banco
  n_curso -->|"versão para o marketplace"| n_udemy
  n_form -->|"proposta de parceria"| n_dio
  n_obsd -->|"artigos e projetos"| n_dio
  n_yt -->|"membros"| n_ytm
  n_mp -->|"lança no carnê-leão"| n_nfse
  n_mp -->|"saque"| n_banco
  n_aulas -->|"cobrança"| n_mp
  n_sites -->|"cobrança"| n_mp
  n_mailer -->|"leva à página de venda"| n_inst
  n_mail -->|"remetente"| n_mailer
  n_cml -->|"campanhas"| n_mailer
  n_n8n -->|"novo aluno → e-mail"| n_mailer
  n_site -->|"formulário da newsletter"| n_mailer
  n_isca -->|"sequência"| n_mailer
  n_site -->|"links no blog"| n_afil
  classDef desta fill:#e2ecec,stroke:#0e3a45,color:#13262b
  class n_pixa,n_agenda,n_comu,n_ads,n_crm,n_hotm,n_kiwi,n_eduzz,n_udemy,n_dio,n_ytm,n_mp,n_mailer,n_afil desta
```

## Blocos

| Bloco | Tipo | O que faz |
|---|---|---|
| [Pix Automático + gateway (ex.: Asaas)](#pixa) | Remoto · precisa de conta · futuro | Cobrança recorrente dos sistemas AM por Pix, sem cartão. Lançado pelo Banco Central em 2025. Entra quando o primeiro SaaS tiver cliente. |
| [Agenda online (Cal.com)](#agenda) | Remoto · precisa de conta | Aluno particular escolhe horário sozinho e já paga. Open source, com plano grátis. |
| [Comunidade (Discord ou grupo)](#comu) | Remoto · precisa de conta | Alunos do curso juntos: tira-dúvidas, retenção e indicação. |
| [Anúncios (Meta Ads)](#ads) | Remoto · precisa de conta · futuro | Só depois que o produto vender organicamente; antes disso é dinheiro jogado fora. |
| [CRM simples (planilha)](#crm) | Local | Lista de alunos, clientes e propostas. Uma planilha resolve até dezenas de clientes. |
| [Hotmart](#hotm) | Remoto · precisa de conta | Checkout, área de membros e afiliados para cursos e PDFs. Aceita vender no CPF. Melhor quando você mesmo leva o público. |
| [Kiwify](#kiwi) | Remoto · precisa de conta | Mesma função da Hotmart, com painel mais simples. Aceita vender no CPF. |
| [Eduzz](#eduzz) | Remoto · precisa de conta | Outra plataforma brasileira de infoprodutos, com programa de afiliados próprio. |
| [Udemy](#udemy) | Remoto · precisa de conta | Marketplace mundial: ela traz alunos que você não alcançaria. Ganha bem menos por venda orgânica do que pelo seu cupom. Recebe por PayPal ou Payoneer e pede um formulário fiscal dos EUA. |
| [DIO (parceria)](#dio) | Remoto · precisa de conta | Não é marketplace aberto como a Udemy. Os experts trabalham em parceria com a DIO; o caminho é publicar artigos e projetos lá e se candidatar ou ser convidado. |
| [YouTube (membros)](#ytm) | Remoto · precisa de conta · futuro | Assinatura mensal do canal, quando houver público. |
| [Mercado Pago](#mp) | Remoto · precisa de conta | Pix e cartão para aulas particulares e serviços de sites. |
| [MailerLite](#mailer) | Remoto · precisa de conta | Newsletter do blog com grupos por tema e funil de lançamento. Você já escolheu o plano grátis. |
| [Afiliados (Amazon, Hotmart…)](#afil) | Remoto · precisa de conta | Links de produtos de terceiros no blog e nos vídeos. |

<a id="pixa"></a>

### Pix Automático + gateway (ex.: Asaas)

*Remoto · precisa de conta · futuro*

Cobrança recorrente dos sistemas AM por Pix, sem cartão. Lançado pelo Banco Central em 2025. Entra quando o primeiro SaaS tiver cliente.

| Direção | Bloco | Camada | O que passa |
|---|---|---|---|
| → envia para | [aura-licensing](10-app.md#lic) | Aplicação: sistemas AM (Aura) | cobrança recorrente |
| → envia para | [Conta bancária separada (CPF)](16-emp.md#banco) | Pessoa física: impostos e finanças | recebimento |

<a id="agenda"></a>

### Agenda online (Cal.com)

*Remoto · precisa de conta*

Aluno particular escolhe horário sozinho e já paga. Open source, com plano grátis.

| Direção | Bloco | Camada | O que passa |
|---|---|---|---|
| → envia para | [Aulas particulares](14-prod.md#aulas) | Produtos (o que você vende) | horários |
| → envia para | [Mercado Pago](17-venda.md#mp) | Plataformas de venda e recebimento | pagamento |

<a id="comu"></a>

### Comunidade (Discord ou grupo)

*Remoto · precisa de conta*

Alunos do curso juntos: tira-dúvidas, retenção e indicação.

| Direção | Bloco | Camada | O que passa |
|---|---|---|---|
| → envia para | [Mini-curso Lógica de Programação](14-prod.md#curso) | Produtos (o que você vende) | suporte aos alunos |

<a id="ads"></a>

### Anúncios (Meta Ads)

*Remoto · precisa de conta · futuro*

Só depois que o produto vender organicamente; antes disso é dinheiro jogado fora.

| Direção | Bloco | Camada | O que passa |
|---|---|---|---|
| → envia para | [Instagram](19-pub.md#ig) | Público e canais | alcance pago |
| → envia para | [Banco de métricas (PostgreSQL)](18-mkt.md#metrics) | Marketing, automação e medição | gasto por campanha |
| ← recebe de | [Pixel + API de Conversões](18-mkt.md#pixel) | Marketing, automação e medição | otimiza para venda |
| ← recebe de | [Padrão de UTM](18-mkt.md#utm) | Marketing, automação e medição | marca os links |
| ← recebe de | [Regras de corte](18-mkt.md#regras) | Marketing, automação e medição | pausa ou escala |

<a id="crm"></a>

### CRM simples (planilha)

*Local*

Lista de alunos, clientes e propostas. Uma planilha resolve até dezenas de clientes.

| Direção | Bloco | Camada | O que passa |
|---|---|---|---|
| → envia para | [Sites para pequenas empresas](14-prod.md#sites) | Produtos (o que você vende) | propostas |

<a id="hotm"></a>

### Hotmart

*Remoto · precisa de conta*

Checkout, área de membros e afiliados para cursos e PDFs. Aceita vender no CPF. Melhor quando você mesmo leva o público.

| Direção | Bloco | Camada | O que passa |
|---|---|---|---|
| → envia para | [Carnê-leão (Receita Federal)](16-emp.md#nfse) | Pessoa física: impostos e finanças | lança no carnê-leão |
| → envia para | [Conta bancária separada (CPF)](16-emp.md#banco) | Pessoa física: impostos e finanças | saque |
| → envia para | [Webhooks de venda](18-mkt.md#hooks) | Marketing, automação e medição | venda e reembolso |
| ← recebe de | [KeePassXC](02-seg.md#kee) | Segurança e cofre | senhas |
| ← recebe de | [Navegador + Claude in Chrome](03-win.md#nav) | Windows 11, apps e máquinas virtuais | painel web |
| ← recebe de | [Plugins: small- business + marketing](07-clc.md#pbiz) | Claude: recursos, conectores e plugins | funil e lançamento |
| ← recebe de | [n8n](08-cnt.md#n8n) | Containers, Kubernetes e infra como código | webhook de venda |
| ← recebe de | [Mini-curso Lógica de Programação](14-prod.md#curso) | Produtos (o que você vende) | produto cadastrado |
| ← recebe de | [Formações (TI, Matemática, Finanças)](14-prod.md#form) | Produtos (o que você vende) | produto |
| ← recebe de | [Templates e código-fonte](14-prod.md#tmpl) | Produtos (o que você vende) | download |
| ← recebe de | [Livro Lógica e Máquina](14-prod.md#livro) | Produtos (o que você vende) | PDF |
| ← recebe de | [Instituto AMS](15-web.md#inst) | Vitrine web (sites e domínio) | botão comprar |
| ← recebe de | [MailerLite](17-venda.md#mailer) | Plataformas de venda e recebimento | lançamento |
| ← recebe de | [Programa de afiliados](18-mkt.md#afprog) | Marketing, automação e medição | afiliados cadastrados |

<a id="kiwi"></a>

### Kiwify

*Remoto · precisa de conta*

Mesma função da Hotmart, com painel mais simples. Aceita vender no CPF.

| Direção | Bloco | Camada | O que passa |
|---|---|---|---|
| → envia para | [Carnê-leão (Receita Federal)](16-emp.md#nfse) | Pessoa física: impostos e finanças | lança no carnê-leão |
| → envia para | [Conta bancária separada (CPF)](16-emp.md#banco) | Pessoa física: impostos e finanças | saque |
| → envia para | [Webhooks de venda](18-mkt.md#hooks) | Marketing, automação e medição | venda e reembolso |
| ← recebe de | [Mini-curso Lógica de Programação](14-prod.md#curso) | Produtos (o que você vende) | produto |
| ← recebe de | [Instituto AMS](15-web.md#inst) | Vitrine web (sites e domínio) | botão comprar |

<a id="eduzz"></a>

### Eduzz

*Remoto · precisa de conta*

Outra plataforma brasileira de infoprodutos, com programa de afiliados próprio.

| Direção | Bloco | Camada | O que passa |
|---|---|---|---|
| → envia para | [Carnê-leão (Receita Federal)](16-emp.md#nfse) | Pessoa física: impostos e finanças | lança no carnê-leão |
| → envia para | [Conta bancária separada (CPF)](16-emp.md#banco) | Pessoa física: impostos e finanças | saque |
| → envia para | [Webhooks de venda](18-mkt.md#hooks) | Marketing, automação e medição | venda e reembolso |
| ← recebe de | [Mini-curso Lógica de Programação](14-prod.md#curso) | Produtos (o que você vende) | produto |

<a id="udemy"></a>

### Udemy

*Remoto · precisa de conta*

Marketplace mundial: ela traz alunos que você não alcançaria. Ganha bem menos por venda orgânica do que pelo seu cupom. Recebe por PayPal ou Payoneer e pede um formulário fiscal dos EUA.

| Direção | Bloco | Camada | O que passa |
|---|---|---|---|
| → envia para | [Carnê-leão (Receita Federal)](16-emp.md#nfse) | Pessoa física: impostos e finanças | carnê-leão (exterior) |
| → envia para | [Conta bancária separada (CPF)](16-emp.md#banco) | Pessoa física: impostos e finanças | PayPal ou Payoneer |
| ← recebe de | [Mini-curso Lógica de Programação](14-prod.md#curso) | Produtos (o que você vende) | versão para o marketplace |

<a id="dio"></a>

### DIO (parceria)

*Remoto · precisa de conta*

Não é marketplace aberto como a Udemy. Os experts trabalham em parceria com a DIO; o caminho é publicar artigos e projetos lá e se candidatar ou ser convidado.

| Direção | Bloco | Camada | O que passa |
|---|---|---|---|
| ← recebe de | [Formações (TI, Matemática, Finanças)](14-prod.md#form) | Produtos (o que você vende) | proposta de parceria |
| ← recebe de | [Obsidian + Git](03-win.md#obsd) | Windows 11, apps e máquinas virtuais | artigos e projetos |

<a id="ytm"></a>

### YouTube (membros)

*Remoto · precisa de conta · futuro*

Assinatura mensal do canal, quando houver público.

| Direção | Bloco | Camada | O que passa |
|---|---|---|---|
| ← recebe de | [YouTube](19-pub.md#yt) | Público e canais | membros |

<a id="mp"></a>

### Mercado Pago

*Remoto · precisa de conta*

Pix e cartão para aulas particulares e serviços de sites.

| Direção | Bloco | Camada | O que passa |
|---|---|---|---|
| → envia para | [Carnê-leão (Receita Federal)](16-emp.md#nfse) | Pessoa física: impostos e finanças | lança no carnê-leão |
| → envia para | [Conta bancária separada (CPF)](16-emp.md#banco) | Pessoa física: impostos e finanças | saque |
| ← recebe de | [Agenda online (Cal.com)](17-venda.md#agenda) | Plataformas de venda e recebimento | pagamento |
| ← recebe de | [Aulas particulares](14-prod.md#aulas) | Produtos (o que você vende) | cobrança |
| ← recebe de | [Sites para pequenas empresas](14-prod.md#sites) | Produtos (o que você vende) | cobrança |

<a id="mailer"></a>

### MailerLite

*Remoto · precisa de conta*

Newsletter do blog com grupos por tema e funil de lançamento. Você já escolheu o plano grátis.

| Direção | Bloco | Camada | O que passa |
|---|---|---|---|
| → envia para | [Instituto AMS](15-web.md#inst) | Vitrine web (sites e domínio) | leva à página de venda |
| → envia para | [Hotmart](17-venda.md#hotm) | Plataformas de venda e recebimento | lançamento |
| ← recebe de | [E-mail profissional (enviar e receber)](15-web.md#mail) | Vitrine web (sites e domínio) | remetente |
| ← recebe de | [Conector MailerLite](07-clc.md#cml) | Claude: recursos, conectores e plugins | campanhas |
| ← recebe de | [n8n](08-cnt.md#n8n) | Containers, Kubernetes e infra como código | novo aluno → e-mail |
| ← recebe de | [Site pessoal + blog (Jekyll)](15-web.md#site) | Vitrine web (sites e domínio) | formulário da newsletter |
| ← recebe de | [Isca grátis + sequência de e-mails](18-mkt.md#isca) | Marketing, automação e medição | sequência |

<a id="afil"></a>

### Afiliados (Amazon, Hotmart…)

*Remoto · precisa de conta*

Links de produtos de terceiros no blog e nos vídeos.

| Direção | Bloco | Camada | O que passa |
|---|---|---|---|
| ← recebe de | [Site pessoal + blog (Jekyll)](15-web.md#site) | Vitrine web (sites e domínio) | links no blog |

---

[↑ Camada 18 · Marketing, automação e medição](18-mkt.md) · [↓ Camada 16 · Pessoa física: impostos e finanças](16-emp.md)
