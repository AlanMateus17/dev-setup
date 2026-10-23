<!-- Arquivo GERADO por tools/gerar_docs.py a partir de data/. Edite os dados, não este arquivo. -->


# Camada 19 · Plataformas de venda e recebimento

[← Arquitetura](../arquitetura.md) · [Índice da documentação](../README.md)

> **Ligação com a camada de baixo:** Cada venda é lançada no carnê-leão e o dinheiro cai na sua conta separada.

**11 blocos** · 10 precisam de conta · 2 marcados como futuro

## Mapa de conexões

```mermaid
flowchart LR
  subgraph L_venda["Plataformas de venda e recebimento"]
    n_pixa["Pix Automático + gateway (ex.: Asaas)"]
    n_agenda["Agenda online (Cal.com)"]
    n_crm["CRM simples (planilha)"]
    n_hotm["Hotmart"]
    n_kiwi["Kiwify"]
    n_eduzz["Eduzz"]
    n_udemy["Udemy"]
    n_dio["DIO (parceria)"]
    n_ytm["YouTube (membros)"]
    n_mp["Mercado Pago"]
    n_afil["Afiliados (Amazon, Hotmart…)"]
  end
  subgraph L_oper["Operação do grupo (esteira, marca, qualidade)"]
    n_ocob["Agente cobrador"]
    n_ocrm["CRM único + LGPD"]
  end
  subgraph L_pub["Público e canais"]
    n_comu["Comunidade (Discord ou grupo)"]
    n_yt["YouTube"]
  end
  subgraph L_mkt["Marketing, automação e medição"]
    n_afprog["Programa de afiliados"]
    n_hooks["Webhooks de venda"]
    n_mailer["MailerLite"]
  end
  subgraph L_emp["Pessoa física: impostos e finanças"]
    n_banco["Conta bancária separada (CPF)"]
    n_nfse["Carnê-leão (Receita Federal)"]
  end
  subgraph L_web["Vitrine web (sites e domínio)"]
    n_inst["Instituto AMS"]
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
  subgraph L_editora["Editora AMS Silva (produção de livros)"]
    n_bcurso["Curso por seção"]
    n_prof["Edição do professor"]
  end
  subgraph L_app["Aplicação: sistemas AM (Aura)"]
    n_lic["aura-licensing"]
  end
  subgraph L_clc["Claude: recursos, conectores e plugins"]
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
  n_ocob -->|"Pix"| n_pixa
  n_agenda -->|"horários"| n_aulas
  n_agenda -->|"pagamento"| n_mp
  n_crm -->|"propostas"| n_sites
  n_crm -->|"vira"| n_ocrm
  n_hotm -->|"lança no carnê-leão"| n_nfse
  n_hotm -->|"saque"| n_banco
  n_hotm -->|"venda e reembolso"| n_hooks
  n_hotm -->|"convite na compra"| n_comu
  n_kee -->|"senhas"| n_hotm
  n_nav -->|"painel web"| n_hotm
  n_pbiz -->|"funil e lançamento"| n_hotm
  n_curso -->|"produto cadastrado"| n_hotm
  n_form -->|"produto"| n_hotm
  n_tmpl -->|"download"| n_hotm
  n_livro -->|"PDF"| n_hotm
  n_inst -->|"botão comprar"| n_hotm
  n_mailer -->|"lançamento"| n_hotm
  n_afprog -->|"afiliados cadastrados"| n_hotm
  n_bcurso -->|"venda"| n_hotm
  n_prof -->|"licença para escolas"| n_hotm
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
  n_ocob -->|"cobrança"| n_mp
  n_afil -->|"comissões no carnê-leão"| n_nfse
  n_site -->|"links no blog"| n_afil
  n_yt -->|"links na descrição"| n_afil
  classDef desta fill:#e2ecec,stroke:#0e3a45,color:#13262b
  class n_pixa,n_agenda,n_crm,n_hotm,n_kiwi,n_eduzz,n_udemy,n_dio,n_ytm,n_mp,n_afil desta
```

## Blocos

| Bloco | Tipo | O que faz |
|---|---|---|
| [Pix Automático + gateway (ex.: Asaas)](#pixa) | Remoto · precisa de conta · futuro | Cobrança recorrente dos sistemas AM por Pix, sem cartão. Lançado pelo Banco Central em 2025. Entra quando o primeiro SaaS tiver cliente. |
| [Agenda online (Cal.com)](#agenda) | Remoto · precisa de conta | Aluno particular escolhe horário sozinho e já paga. Open source, com plano grátis. |
| [CRM simples (planilha)](#crm) | Local | Lista de alunos, clientes e propostas. Uma planilha resolve até dezenas de clientes. |
| [Hotmart](#hotm) | Remoto · precisa de conta | Checkout, área de membros e afiliados para cursos e PDFs. Aceita vender no CPF. Melhor quando você mesmo leva o público. |
| [Kiwify](#kiwi) | Remoto · precisa de conta | Mesma função da Hotmart, com painel mais simples. Aceita vender no CPF. |
| [Eduzz](#eduzz) | Remoto · precisa de conta | Outra plataforma brasileira de infoprodutos, com programa de afiliados próprio. |
| [Udemy](#udemy) | Remoto · precisa de conta | Marketplace mundial: ela traz alunos que você não alcançaria. Ganha bem menos por venda orgânica do que pelo seu cupom. Recebe por PayPal ou Payoneer e pede um formulário fiscal dos EUA. |
| [DIO (parceria)](#dio) | Remoto · precisa de conta | Não é marketplace aberto como a Udemy. Os experts trabalham em parceria com a DIO; o caminho é publicar artigos e projetos lá e se candidatar ou ser convidado. |
| [YouTube (membros)](#ytm) | Remoto · precisa de conta · futuro | Assinatura mensal do canal, quando houver público. |
| [Mercado Pago](#mp) | Remoto · precisa de conta | Pix e cartão para aulas particulares e serviços de sites. |
| [Afiliados (Amazon, Hotmart…)](#afil) | Remoto · precisa de conta | Links de produtos de terceiros no blog e nos vídeos. |

<a id="pixa"></a>

### Pix Automático + gateway (ex.: Asaas)

*Remoto · precisa de conta · futuro*

Cobrança recorrente dos sistemas AM por Pix, sem cartão. Lançado pelo Banco Central em 2025. Entra quando o primeiro SaaS tiver cliente.

| Direção | Bloco | Camada | O que passa |
|---|---|---|---|
| → envia para | [aura-licensing](10-app.md#lic) | Aplicação: sistemas AM (Aura) | cobrança recorrente |
| → envia para | [Conta bancária separada (CPF)](18-emp.md#banco) | Pessoa física: impostos e finanças | recebimento |
| ← recebe de | [Agente cobrador](22-oper.md#ocob) | Operação do grupo (esteira, marca, qualidade) | Pix |

<a id="agenda"></a>

### Agenda online (Cal.com)

*Remoto · precisa de conta*

Aluno particular escolhe horário sozinho e já paga. Open source, com plano grátis.

| Direção | Bloco | Camada | O que passa |
|---|---|---|---|
| → envia para | [Aulas particulares](16-prod.md#aulas) | Produtos (o que você vende) | horários |
| → envia para | [Mercado Pago](19-venda.md#mp) | Plataformas de venda e recebimento | pagamento |

<a id="crm"></a>

### CRM simples (planilha)

*Local*

Lista de alunos, clientes e propostas. Uma planilha resolve até dezenas de clientes.

| Direção | Bloco | Camada | O que passa |
|---|---|---|---|
| → envia para | [Sites para pequenas empresas](16-prod.md#sites) | Produtos (o que você vende) | propostas |
| → envia para | [CRM único + LGPD](22-oper.md#ocrm) | Operação do grupo (esteira, marca, qualidade) | vira |

<a id="hotm"></a>

### Hotmart

*Remoto · precisa de conta*

Checkout, área de membros e afiliados para cursos e PDFs. Aceita vender no CPF. Melhor quando você mesmo leva o público.

| Direção | Bloco | Camada | O que passa |
|---|---|---|---|
| → envia para | [Carnê-leão (Receita Federal)](18-emp.md#nfse) | Pessoa física: impostos e finanças | lança no carnê-leão |
| → envia para | [Conta bancária separada (CPF)](18-emp.md#banco) | Pessoa física: impostos e finanças | saque |
| → envia para | [Webhooks de venda](20-mkt.md#hooks) | Marketing, automação e medição | venda e reembolso |
| → envia para | [Comunidade (Discord ou grupo)](21-pub.md#comu) | Público e canais | convite na compra |
| ← recebe de | [KeePassXC](02-seg.md#kee) | Segurança e cofre | senhas |
| ← recebe de | [Navegador + Claude in Chrome](03-win.md#nav) | Windows 11, apps e máquinas virtuais | painel web |
| ← recebe de | [Plugins: small- business + marketing](07-clc.md#pbiz) | Claude: recursos, conectores e plugins | funil e lançamento |
| ← recebe de | [Mini-curso Lógica de Programação](16-prod.md#curso) | Produtos (o que você vende) | produto cadastrado |
| ← recebe de | [Formações (TI, Matemática, Finanças)](16-prod.md#form) | Produtos (o que você vende) | produto |
| ← recebe de | [Templates e código-fonte](16-prod.md#tmpl) | Produtos (o que você vende) | download |
| ← recebe de | [Livro Lógica e Máquina](16-prod.md#livro) | Produtos (o que você vende) | PDF |
| ← recebe de | [Instituto AMS](17-web.md#inst) | Vitrine web (sites e domínio) | botão comprar |
| ← recebe de | [MailerLite](20-mkt.md#mailer) | Marketing, automação e medição | lançamento |
| ← recebe de | [Programa de afiliados](20-mkt.md#afprog) | Marketing, automação e medição | afiliados cadastrados |
| ← recebe de | [Curso por seção](14-editora.md#bcurso) | Editora AMS Silva (produção de livros) | venda |
| ← recebe de | [Edição do professor](14-editora.md#prof) | Editora AMS Silva (produção de livros) | licença para escolas |

<a id="kiwi"></a>

### Kiwify

*Remoto · precisa de conta*

Mesma função da Hotmart, com painel mais simples. Aceita vender no CPF.

| Direção | Bloco | Camada | O que passa |
|---|---|---|---|
| → envia para | [Carnê-leão (Receita Federal)](18-emp.md#nfse) | Pessoa física: impostos e finanças | lança no carnê-leão |
| → envia para | [Conta bancária separada (CPF)](18-emp.md#banco) | Pessoa física: impostos e finanças | saque |
| → envia para | [Webhooks de venda](20-mkt.md#hooks) | Marketing, automação e medição | venda e reembolso |
| ← recebe de | [Mini-curso Lógica de Programação](16-prod.md#curso) | Produtos (o que você vende) | produto |
| ← recebe de | [Instituto AMS](17-web.md#inst) | Vitrine web (sites e domínio) | botão comprar |

<a id="eduzz"></a>

### Eduzz

*Remoto · precisa de conta*

Outra plataforma brasileira de infoprodutos, com programa de afiliados próprio.

| Direção | Bloco | Camada | O que passa |
|---|---|---|---|
| → envia para | [Carnê-leão (Receita Federal)](18-emp.md#nfse) | Pessoa física: impostos e finanças | lança no carnê-leão |
| → envia para | [Conta bancária separada (CPF)](18-emp.md#banco) | Pessoa física: impostos e finanças | saque |
| → envia para | [Webhooks de venda](20-mkt.md#hooks) | Marketing, automação e medição | venda e reembolso |
| ← recebe de | [Mini-curso Lógica de Programação](16-prod.md#curso) | Produtos (o que você vende) | produto |

<a id="udemy"></a>

### Udemy

*Remoto · precisa de conta*

Marketplace mundial: ela traz alunos que você não alcançaria. Ganha bem menos por venda orgânica do que pelo seu cupom. Recebe por PayPal ou Payoneer e pede um formulário fiscal dos EUA.

| Direção | Bloco | Camada | O que passa |
|---|---|---|---|
| → envia para | [Carnê-leão (Receita Federal)](18-emp.md#nfse) | Pessoa física: impostos e finanças | carnê-leão (exterior) |
| → envia para | [Conta bancária separada (CPF)](18-emp.md#banco) | Pessoa física: impostos e finanças | PayPal ou Payoneer |
| ← recebe de | [Mini-curso Lógica de Programação](16-prod.md#curso) | Produtos (o que você vende) | versão para o marketplace |

<a id="dio"></a>

### DIO (parceria)

*Remoto · precisa de conta*

Não é marketplace aberto como a Udemy. Os experts trabalham em parceria com a DIO; o caminho é publicar artigos e projetos lá e se candidatar ou ser convidado.

| Direção | Bloco | Camada | O que passa |
|---|---|---|---|
| ← recebe de | [Formações (TI, Matemática, Finanças)](16-prod.md#form) | Produtos (o que você vende) | proposta de parceria |
| ← recebe de | [Obsidian + Git](03-win.md#obsd) | Windows 11, apps e máquinas virtuais | artigos e projetos |

<a id="ytm"></a>

### YouTube (membros)

*Remoto · precisa de conta · futuro*

Assinatura mensal do canal, quando houver público.

| Direção | Bloco | Camada | O que passa |
|---|---|---|---|
| ← recebe de | [YouTube](21-pub.md#yt) | Público e canais | membros |

<a id="mp"></a>

### Mercado Pago

*Remoto · precisa de conta*

Pix e cartão para aulas particulares e serviços de sites.

| Direção | Bloco | Camada | O que passa |
|---|---|---|---|
| → envia para | [Carnê-leão (Receita Federal)](18-emp.md#nfse) | Pessoa física: impostos e finanças | lança no carnê-leão |
| → envia para | [Conta bancária separada (CPF)](18-emp.md#banco) | Pessoa física: impostos e finanças | saque |
| ← recebe de | [Agenda online (Cal.com)](19-venda.md#agenda) | Plataformas de venda e recebimento | pagamento |
| ← recebe de | [Aulas particulares](16-prod.md#aulas) | Produtos (o que você vende) | cobrança |
| ← recebe de | [Sites para pequenas empresas](16-prod.md#sites) | Produtos (o que você vende) | cobrança |
| ← recebe de | [Agente cobrador](22-oper.md#ocob) | Operação do grupo (esteira, marca, qualidade) | cobrança |

<a id="afil"></a>

### Afiliados (Amazon, Hotmart…)

*Remoto · precisa de conta*

Links de produtos de terceiros no blog e nos vídeos.

| Direção | Bloco | Camada | O que passa |
|---|---|---|---|
| → envia para | [Carnê-leão (Receita Federal)](18-emp.md#nfse) | Pessoa física: impostos e finanças | comissões no carnê-leão |
| ← recebe de | [Site pessoal + blog (Jekyll)](17-web.md#site) | Vitrine web (sites e domínio) | links no blog |
| ← recebe de | [YouTube](21-pub.md#yt) | Público e canais | links na descrição |

---

[↑ Camada 20 · Marketing, automação e medição](20-mkt.md) · [↓ Camada 18 · Pessoa física: impostos e finanças](18-emp.md)
