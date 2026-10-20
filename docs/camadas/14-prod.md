<!-- Arquivo GERADO por tools/gerar_docs.py a partir de data/. Edite os dados, não este arquivo. -->


# Camada 14 · Produtos (o que você vende)

[← Arquitetura](../arquitetura.md) · [Índice da documentação](../README.md)

> **Ligação com a camada de baixo:** Cada produto nasce do conteúdo gravado, escrito ou programado.

**7 blocos** · 0 precisam de conta · 2 marcados como futuro

## Mapa de conexões

```mermaid
flowchart LR
  subgraph L_prod["Produtos (o que você vende)"]
    n_curso["Mini-curso Lógica de Programação"]
    n_form["Formações (TI, Matemática, Finanças)"]
    n_tmpl["Templates e código-fonte"]
    n_livro["Livro Lógica e Máquina"]
    n_aulas["Aulas particulares"]
    n_sites["Sites para pequenas empresas"]
    n_saas["Sistemas AM (SaaS)"]
  end
  subgraph L_pub["Público e canais"]
    n_wa["WhatsApp Business"]
  end
  subgraph L_venda["Plataformas de venda e recebimento"]
    n_agenda["Agenda online (Cal.com)"]
    n_comu["Comunidade (Discord ou grupo)"]
    n_crm["CRM simples (planilha)"]
    n_dio["DIO (parceria)"]
    n_eduzz["Eduzz"]
    n_hotm["Hotmart"]
    n_kiwi["Kiwify"]
    n_mp["Mercado Pago"]
    n_udemy["Udemy"]
  end
  subgraph L_emp["Pessoa física: impostos e finanças"]
    n_legal["Termos, privacidade (LGPD) e contratos"]
  end
  subgraph L_web["Vitrine web (sites e domínio)"]
    n_hostg["Hostinger (clientes WP)"]
  end
  subgraph L_cont["Produção de conteúdo"]
    n_edit["DaVinci Resolve ou Kdenlive"]
  end
  subgraph L_nuvem["Nuvem, código e entrega"]
    n_azure["Azure"]
    n_gh["GitHub"]
  end
  subgraph L_app["Aplicação: sistemas AM (Aura)"]
    n_lic["aura-licensing"]
    n_story["Storybook"]
  end
  subgraph L_clc["Claude: recursos, conectores e plugins"]
    n_cupw["Conector Upwork"]
  end
  subgraph L_chat["Assistentes de IA (chat, pesquisa e estudo)"]
    n_nblm["NotebookLM"]
  end
  subgraph L_lin["Linux (Ubuntu no WSL2, Arch no 2º disco)"]
    n_tex["TeX Live"]
  end
  subgraph L_win["Windows 11, apps e máquinas virtuais"]
    n_obsd["Obsidian + Git"]
    n_office["LibreOffice"]
    n_pdf["SumatraPDF"]
    n_sharex["ShareX"]
  end
  n_curso -->|"produto"| n_kiwi
  n_curso -->|"versão para o marketplace"| n_udemy
  n_curso -->|"produto"| n_eduzz
  n_curso -->|"produto cadastrado"| n_hotm
  n_nblm -->|"prepara as aulas"| n_curso
  n_sharex -->|"demonstrações"| n_curso
  n_comu -->|"suporte aos alunos"| n_curso
  n_edit -->|"aulas editadas"| n_curso
  n_obsd -->|"roteiro"| n_curso
  n_form -->|"proposta de parceria"| n_dio
  n_form -->|"produto"| n_hotm
  n_tmpl -->|"download"| n_hotm
  n_tmpl -->|"demo pública"| n_gh
  n_story -->|"demo do template"| n_tmpl
  n_livro -->|"PDF"| n_hotm
  n_tex -->|"gera o PDF"| n_livro
  n_pdf -->|"revisão do PDF"| n_livro
  n_obsd -->|"capítulos"| n_livro
  n_aulas -->|"cobrança"| n_mp
  n_agenda -->|"horários"| n_aulas
  n_wa -->|"agenda"| n_aulas
  n_sites -->|"cobrança"| n_mp
  n_sites -->|"hospedagem do cliente"| n_hostg
  n_office -->|"documentos de clientes"| n_sites
  n_crm -->|"propostas"| n_sites
  n_legal -->|"contrato"| n_sites
  n_cupw -->|"encontra clientes"| n_sites
  n_saas -->|"roda na nuvem"| n_azure
  n_saas -->|"cobrança por módulo"| n_lic
  classDef desta fill:#e2ecec,stroke:#0e3a45,color:#13262b
  class n_curso,n_form,n_tmpl,n_livro,n_aulas,n_sites,n_saas desta
```

## Blocos

| Bloco | Tipo | O que faz |
|---|---|---|
| [Mini-curso Lógica de Programação](#curso) | Local | Primeiro produto de lançamento, para validar antes de construir mais. |
| [Formações (TI, Matemática, Finanças)](#form) | Local · futuro | Cursos completos, depois que o mini-curso vender. |
| [Templates e código-fonte](#tmpl) | Local | Frontends prontos e projetos vendidos como download. |
| [Livro Lógica e Máquina](#livro) | Local | PDF primeiro; impresso depois. |
| [Aulas particulares](#aulas) | Físico | Seus estudos viram aula paga. |
| [Sites para pequenas empresas](#sites) | Local | Freelance em Barbacena: sites e lojas. |
| [Sistemas AM (SaaS)](#saas) | Remoto · futuro | AM Kaixara, AM Rendara e os demais, vendidos por assinatura. |

<a id="curso"></a>

### Mini-curso Lógica de Programação

*Local*

Primeiro produto de lançamento, para validar antes de construir mais.

| Direção | Bloco | Camada | O que passa |
|---|---|---|---|
| → envia para | [Kiwify](17-venda.md#kiwi) | Plataformas de venda e recebimento | produto |
| → envia para | [Udemy](17-venda.md#udemy) | Plataformas de venda e recebimento | versão para o marketplace |
| → envia para | [Eduzz](17-venda.md#eduzz) | Plataformas de venda e recebimento | produto |
| → envia para | [Hotmart](17-venda.md#hotm) | Plataformas de venda e recebimento | produto cadastrado |
| ← recebe de | [NotebookLM](06-chat.md#nblm) | Assistentes de IA (chat, pesquisa e estudo) | prepara as aulas |
| ← recebe de | [ShareX](03-win.md#sharex) | Windows 11, apps e máquinas virtuais | demonstrações |
| ← recebe de | [Comunidade (Discord ou grupo)](17-venda.md#comu) | Plataformas de venda e recebimento | suporte aos alunos |
| ← recebe de | [DaVinci Resolve ou Kdenlive](12-cont.md#edit) | Produção de conteúdo | aulas editadas |
| ← recebe de | [Obsidian + Git](03-win.md#obsd) | Windows 11, apps e máquinas virtuais | roteiro |

<a id="form"></a>

### Formações (TI, Matemática, Finanças)

*Local · futuro*

Cursos completos, depois que o mini-curso vender.

| Direção | Bloco | Camada | O que passa |
|---|---|---|---|
| → envia para | [DIO (parceria)](17-venda.md#dio) | Plataformas de venda e recebimento | proposta de parceria |
| → envia para | [Hotmart](17-venda.md#hotm) | Plataformas de venda e recebimento | produto |

<a id="tmpl"></a>

### Templates e código-fonte

*Local*

Frontends prontos e projetos vendidos como download.

| Direção | Bloco | Camada | O que passa |
|---|---|---|---|
| → envia para | [Hotmart](17-venda.md#hotm) | Plataformas de venda e recebimento | download |
| → envia para | [GitHub](11-nuvem.md#gh) | Nuvem, código e entrega | demo pública |
| ← recebe de | [Storybook](10-app.md#story) | Aplicação: sistemas AM (Aura) | demo do template |

<a id="livro"></a>

### Livro Lógica e Máquina

*Local*

PDF primeiro; impresso depois.

| Direção | Bloco | Camada | O que passa |
|---|---|---|---|
| → envia para | [Hotmart](17-venda.md#hotm) | Plataformas de venda e recebimento | PDF |
| ← recebe de | [TeX Live](04-lin.md#tex) | Linux (Ubuntu no WSL2, Arch no 2º disco) | gera o PDF |
| ← recebe de | [SumatraPDF](03-win.md#pdf) | Windows 11, apps e máquinas virtuais | revisão do PDF |
| ← recebe de | [Obsidian + Git](03-win.md#obsd) | Windows 11, apps e máquinas virtuais | capítulos |

<a id="aulas"></a>

### Aulas particulares

*Físico*

Seus estudos viram aula paga.

| Direção | Bloco | Camada | O que passa |
|---|---|---|---|
| → envia para | [Mercado Pago](17-venda.md#mp) | Plataformas de venda e recebimento | cobrança |
| ← recebe de | [Agenda online (Cal.com)](17-venda.md#agenda) | Plataformas de venda e recebimento | horários |
| ← recebe de | [WhatsApp Business](18-pub.md#wa) | Público e canais | agenda |

<a id="sites"></a>

### Sites para pequenas empresas

*Local*

Freelance em Barbacena: sites e lojas.

| Direção | Bloco | Camada | O que passa |
|---|---|---|---|
| → envia para | [Mercado Pago](17-venda.md#mp) | Plataformas de venda e recebimento | cobrança |
| → envia para | [Hostinger (clientes WP)](15-web.md#hostg) | Vitrine web (sites e domínio) | hospedagem do cliente |
| ← recebe de | [LibreOffice](03-win.md#office) | Windows 11, apps e máquinas virtuais | documentos de clientes |
| ← recebe de | [CRM simples (planilha)](17-venda.md#crm) | Plataformas de venda e recebimento | propostas |
| ← recebe de | [Termos, privacidade (LGPD) e contratos](16-emp.md#legal) | Pessoa física: impostos e finanças | contrato |
| ← recebe de | [Conector Upwork](07-clc.md#cupw) | Claude: recursos, conectores e plugins | encontra clientes |

<a id="saas"></a>

### Sistemas AM (SaaS)

*Remoto · futuro*

AM Kaixara, AM Rendara e os demais, vendidos por assinatura.

| Direção | Bloco | Camada | O que passa |
|---|---|---|---|
| → envia para | [Azure](11-nuvem.md#azure) | Nuvem, código e entrega | roda na nuvem |
| → envia para | [aura-licensing](10-app.md#lic) | Aplicação: sistemas AM (Aura) | cobrança por módulo |

---

[↑ Camada 15 · Vitrine web (sites e domínio)](15-web.md) · [↓ Camada 13 · Estudo e carreira](13-est.md)
