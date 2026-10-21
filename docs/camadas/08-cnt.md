<!-- Arquivo GERADO por tools/gerar_docs.py a partir de data/. Edite os dados, não este arquivo. -->


# Camada 08 · Containers, Kubernetes e infra como código

[← Arquitetura](../arquitetura.md) · [Índice da documentação](../README.md)

> **Ligação com a camada de baixo:** A CLI docker e o kubectl no Ubuntu falam com a engine do Docker no WSL2.

**13 blocos** · 0 precisam de conta · 6 marcados como futuro

## Mapa de conexões

```mermaid
flowchart LR
  subgraph L_cnt["Containers, Kubernetes e infra como código"]
    n_caddy["Caddy (proxy + HTTPS)"]
    n_mailp["Mailpit"]
    n_kafka["Kafka"]
    n_k8st["kubectl · Helm · k9s"]
    n_clis["Azure CLI · AWS CLI"]
    n_datomic["Datomic local"]
    n_docker["Docker + Compose"]
    n_pg["PostgreSQL"]
    n_redis["Redis"]
    n_rmq["RabbitMQ"]
    n_kind["Kubernetes local (kind)"]
    n_tf["Terraform"]
    n_n8n["n8n"]
  end
  subgraph L_mkt["Marketing, automação e medição"]
    n_aprov["Aprovação no celular"]
    n_hooks["Webhooks de venda"]
    n_horario["Algoritmo de horário"]
    n_metrics["Banco de métricas (PostgreSQL)"]
    n_postiz["Postiz (agendador)"]
  end
  subgraph L_venda["Plataformas de venda e recebimento"]
    n_hotm["Hotmart"]
    n_mailer["MailerLite"]
  end
  subgraph L_nuvem["Nuvem, código e entrega"]
    n_aws["AWS"]
    n_azure["Azure"]
    n_cf["Cloudflare (DNS, Pages, e-mail)"]
    n_gcp["Google Cloud"]
  end
  subgraph L_app["Aplicação: sistemas AM (Aura)"]
    n_ai["IA: RAG + pgvector"]
    n_api["API ASP.NET Core"]
    n_ef["EF Core + Npgsql"]
    n_gis["PostGIS + MapLibre"]
    n_rls["Multi-tenant (RLS)"]
    n_shared["Serviços aura- (10)"]
    n_sig["SignalR"]
  end
  subgraph L_obs["Observabilidade"]
    n_aspire[".NET Aspire"]
  end
  subgraph L_ia["Agentes de IA e sandbox"]
    n_mcp["Servidores MCP"]
    n_mem["ai-memory"]
    n_oll["Ollama (3B–4B)"]
    n_rag["Base de conhecimento (RAG) das suas notas"]
  end
  subgraph L_lin["Linux (Ubuntu no WSL2, Arch no 2º disco)"]
    n_wsl["Ubuntu (WSL2)"]
  end
  subgraph L_win["Windows 11, apps e máquinas virtuais"]
    n_dbv["DBeaver · Bruno"]
  end
  n_caddy -->|"HTTPS"| n_api
  n_mailp -->|"SMTP de teste"| n_api
  n_docker -->|"container"| n_mailp
  n_kafka -->|"eventos"| n_api
  n_k8st -->|"opera"| n_kind
  n_clis -->|"comandos"| n_azure
  n_clis -->|"comandos"| n_aws
  n_datomic -->|"aura-historico"| n_shared
  n_docker -->|"container"| n_pg
  n_docker -->|"container"| n_redis
  n_docker -->|"container"| n_rmq
  n_docker -->|"cluster local"| n_kind
  n_docker -->|"container"| n_n8n
  n_wsl -->|"socket da engine"| n_docker
  n_mem -->|"container"| n_docker
  n_aspire -->|"sobe os serviços"| n_docker
  n_dbv -->|"porta 5432"| n_pg
  n_mcp -->|"leitura do banco de dev"| n_pg
  n_rag -->|"pgvector"| n_pg
  n_ef -->|"Npgsql"| n_pg
  n_rls -->|"políticas"| n_pg
  n_gis -->|"extensão"| n_pg
  n_api -->|"Npgsql"| n_pg
  n_ai -->|"pgvector"| n_pg
  n_sig -->|"backplane"| n_redis
  n_api -->|"cache"| n_redis
  n_api -->|"eventos"| n_rmq
  n_tf -->|"cria recursos"| n_azure
  n_tf -->|"cria recursos"| n_aws
  n_tf -->|"DNS por código"| n_cf
  n_gcp -->|"cria recursos"| n_tf
  n_n8n -->|"novo aluno → e-mail"| n_mailer
  n_n8n -->|"webhook de venda"| n_hotm
  n_n8n -->|"manda o post aprovado"| n_postiz
  n_n8n -->|"grava"| n_metrics
  n_oll -->|"IA local nas automações"| n_n8n
  n_aprov -->|"libera"| n_n8n
  n_horario -->|"escolhe o horário"| n_n8n
  n_hooks -->|"dispara"| n_n8n
  classDef desta fill:#e2ecec,stroke:#0e3a45,color:#13262b
  class n_caddy,n_mailp,n_kafka,n_k8st,n_clis,n_datomic,n_docker,n_pg,n_redis,n_rmq,n_kind,n_tf,n_n8n desta
```

## Blocos

| Bloco | Tipo | O que faz |
|---|---|---|
| [Caddy (proxy + HTTPS)](#caddy) | Local | Fica na frente das APIs e emite o certificado HTTPS sozinho. Usado no servidor e no homelab. |
| [Mailpit](#mailp) | Local | Caixa de e-mail falsa para testar os e-mails dos sistemas sem enviar nada de verdade. |
| [Kafka](#kafka) | Local · futuro | Mensageria padrão em empresa grande. Depois do RabbitMQ. |
| [kubectl · Helm · k9s](#k8st) | Local · futuro | Ferramentas para operar o Kubernetes: comandos, pacotes e painel no terminal. |
| [Azure CLI · AWS CLI](#clis) | Local | Linha de comando das nuvens; usadas pelo Terraform. |
| [Datomic local](#datomic) | Local · futuro | Só quando o aura-historico existir (desvio intencional da stack). |
| [Docker + Compose](#docker) | Local | Engine no WSL2; um compose por sistema. |
| [PostgreSQL](#pg) | Local | Banco de todos os sistemas (com pgvector para IA). |
| [Redis](#redis) | Local | Cache e backplane do SignalR. |
| [RabbitMQ](#rmq) | Local · futuro | Fila de eventos entre sistemas. |
| [Kubernetes local (kind)](#kind) | Local · futuro | Treino de Kubernetes sem pagar nuvem. |
| [Terraform](#tf) | Local | Cria Azure, AWS e Cloudflare por código. |
| [n8n](#n8n) | Local · futuro | Automação: novo aluno → e-mail, post agendado, aviso. |

<a id="caddy"></a>

### Caddy (proxy + HTTPS)

*Local*

Fica na frente das APIs e emite o certificado HTTPS sozinho. Usado no servidor e no homelab.

| Direção | Bloco | Camada | O que passa |
|---|---|---|---|
| → envia para | [API ASP.NET Core](10-app.md#api) | Aplicação: sistemas AM (Aura) | HTTPS |

<a id="mailp"></a>

### Mailpit

*Local*

Caixa de e-mail falsa para testar os e-mails dos sistemas sem enviar nada de verdade.

| Direção | Bloco | Camada | O que passa |
|---|---|---|---|
| → envia para | [API ASP.NET Core](10-app.md#api) | Aplicação: sistemas AM (Aura) | SMTP de teste |
| ← recebe de | [Docker + Compose](08-cnt.md#docker) | Containers, Kubernetes e infra como código | container |

<a id="kafka"></a>

### Kafka

*Local · futuro*

Mensageria padrão em empresa grande. Depois do RabbitMQ.

| Direção | Bloco | Camada | O que passa |
|---|---|---|---|
| → envia para | [API ASP.NET Core](10-app.md#api) | Aplicação: sistemas AM (Aura) | eventos |

<a id="k8st"></a>

### kubectl · Helm · k9s

*Local · futuro*

Ferramentas para operar o Kubernetes: comandos, pacotes e painel no terminal.

| Direção | Bloco | Camada | O que passa |
|---|---|---|---|
| → envia para | [Kubernetes local (kind)](08-cnt.md#kind) | Containers, Kubernetes e infra como código | opera |

<a id="clis"></a>

### Azure CLI · AWS CLI

*Local*

Linha de comando das nuvens; usadas pelo Terraform.

| Direção | Bloco | Camada | O que passa |
|---|---|---|---|
| → envia para | [Azure](11-nuvem.md#azure) | Nuvem, código e entrega | comandos |
| → envia para | [AWS](11-nuvem.md#aws) | Nuvem, código e entrega | comandos |

<a id="datomic"></a>

### Datomic local

*Local · futuro*

Só quando o aura-historico existir (desvio intencional da stack).

| Direção | Bloco | Camada | O que passa |
|---|---|---|---|
| → envia para | [Serviços aura- (10)](10-app.md#shared) | Aplicação: sistemas AM (Aura) | aura-historico |

<a id="docker"></a>

### Docker + Compose

*Local*

Engine no WSL2; um compose por sistema.

| Direção | Bloco | Camada | O que passa |
|---|---|---|---|
| → envia para | [Mailpit](08-cnt.md#mailp) | Containers, Kubernetes e infra como código | container |
| → envia para | [PostgreSQL](08-cnt.md#pg) | Containers, Kubernetes e infra como código | container |
| → envia para | [Redis](08-cnt.md#redis) | Containers, Kubernetes e infra como código | container |
| → envia para | [RabbitMQ](08-cnt.md#rmq) | Containers, Kubernetes e infra como código | container |
| → envia para | [Kubernetes local (kind)](08-cnt.md#kind) | Containers, Kubernetes e infra como código | cluster local |
| → envia para | [n8n](08-cnt.md#n8n) | Containers, Kubernetes e infra como código | container |
| ← recebe de | [Ubuntu (WSL2)](04-lin.md#wsl) | Linux (Ubuntu no WSL2, Arch no 2º disco) | socket da engine |
| ← recebe de | [ai-memory](05-ia.md#mem) | Agentes de IA e sandbox | container |
| ← recebe de | [.NET Aspire](09-obs.md#aspire) | Observabilidade | sobe os serviços |

<a id="pg"></a>

### PostgreSQL

*Local*

Banco de todos os sistemas (com pgvector para IA).

| Direção | Bloco | Camada | O que passa |
|---|---|---|---|
| ← recebe de | [DBeaver · Bruno](03-win.md#dbv) | Windows 11, apps e máquinas virtuais | porta 5432 |
| ← recebe de | [Servidores MCP](05-ia.md#mcp) | Agentes de IA e sandbox | leitura do banco de dev |
| ← recebe de | [Base de conhecimento (RAG) das suas notas](05-ia.md#rag) | Agentes de IA e sandbox | pgvector |
| ← recebe de | [EF Core + Npgsql](10-app.md#ef) | Aplicação: sistemas AM (Aura) | Npgsql |
| ← recebe de | [Multi-tenant (RLS)](10-app.md#rls) | Aplicação: sistemas AM (Aura) | políticas |
| ← recebe de | [PostGIS + MapLibre](10-app.md#gis) | Aplicação: sistemas AM (Aura) | extensão |
| ← recebe de | [Docker + Compose](08-cnt.md#docker) | Containers, Kubernetes e infra como código | container |
| ← recebe de | [API ASP.NET Core](10-app.md#api) | Aplicação: sistemas AM (Aura) | Npgsql |
| ← recebe de | [IA: RAG + pgvector](10-app.md#ai) | Aplicação: sistemas AM (Aura) | pgvector |

<a id="redis"></a>

### Redis

*Local*

Cache e backplane do SignalR.

| Direção | Bloco | Camada | O que passa |
|---|---|---|---|
| ← recebe de | [SignalR](10-app.md#sig) | Aplicação: sistemas AM (Aura) | backplane |
| ← recebe de | [Docker + Compose](08-cnt.md#docker) | Containers, Kubernetes e infra como código | container |
| ← recebe de | [API ASP.NET Core](10-app.md#api) | Aplicação: sistemas AM (Aura) | cache |

<a id="rmq"></a>

### RabbitMQ

*Local · futuro*

Fila de eventos entre sistemas.

| Direção | Bloco | Camada | O que passa |
|---|---|---|---|
| ← recebe de | [Docker + Compose](08-cnt.md#docker) | Containers, Kubernetes e infra como código | container |
| ← recebe de | [API ASP.NET Core](10-app.md#api) | Aplicação: sistemas AM (Aura) | eventos |

<a id="kind"></a>

### Kubernetes local (kind)

*Local · futuro*

Treino de Kubernetes sem pagar nuvem.

| Direção | Bloco | Camada | O que passa |
|---|---|---|---|
| ← recebe de | [kubectl · Helm · k9s](08-cnt.md#k8st) | Containers, Kubernetes e infra como código | opera |
| ← recebe de | [Docker + Compose](08-cnt.md#docker) | Containers, Kubernetes e infra como código | cluster local |

<a id="tf"></a>

### Terraform

*Local*

Cria Azure, AWS e Cloudflare por código.

| Direção | Bloco | Camada | O que passa |
|---|---|---|---|
| → envia para | [Azure](11-nuvem.md#azure) | Nuvem, código e entrega | cria recursos |
| → envia para | [AWS](11-nuvem.md#aws) | Nuvem, código e entrega | cria recursos |
| → envia para | [Cloudflare (DNS, Pages, e-mail)](11-nuvem.md#cf) | Nuvem, código e entrega | DNS por código |
| ← recebe de | [Google Cloud](11-nuvem.md#gcp) | Nuvem, código e entrega | cria recursos |

<a id="n8n"></a>

### n8n

*Local · futuro*

Automação: novo aluno → e-mail, post agendado, aviso.

| Direção | Bloco | Camada | O que passa |
|---|---|---|---|
| → envia para | [MailerLite](17-venda.md#mailer) | Plataformas de venda e recebimento | novo aluno → e-mail |
| → envia para | [Hotmart](17-venda.md#hotm) | Plataformas de venda e recebimento | webhook de venda |
| → envia para | [Postiz (agendador)](18-mkt.md#postiz) | Marketing, automação e medição | manda o post aprovado |
| → envia para | [Banco de métricas (PostgreSQL)](18-mkt.md#metrics) | Marketing, automação e medição | grava |
| ← recebe de | [Ollama (3B–4B)](05-ia.md#oll) | Agentes de IA e sandbox | IA local nas automações |
| ← recebe de | [Docker + Compose](08-cnt.md#docker) | Containers, Kubernetes e infra como código | container |
| ← recebe de | [Aprovação no celular](18-mkt.md#aprov) | Marketing, automação e medição | libera |
| ← recebe de | [Algoritmo de horário](18-mkt.md#horario) | Marketing, automação e medição | escolhe o horário |
| ← recebe de | [Webhooks de venda](18-mkt.md#hooks) | Marketing, automação e medição | dispara |

---

[↑ Camada 09 · Observabilidade](09-obs.md) · [↓ Camada 07 · Claude: recursos, conectores e plugins](07-clc.md)
