<!-- Arquivo GERADO por tools/gerar_docs.py a partir de data/. Edite os dados, não este arquivo. -->


# Camada 13 · Estudo e carreira

[← Arquitetura](../arquitetura.md) · [Índice da documentação](../README.md)

> **Ligação com a camada de baixo:** O que você estuda vira produto, aula, post e linha no currículo.

**6 blocos** · 5 precisam de conta · 0 marcados como futuro

## Mapa de conexões

```mermaid
flowchart LR
  subgraph L_est["Estudo e carreira"]
    n_learn["Microsoft Learn + AWS Skill Builder"]
    n_thm["TryHackMe / Hack The Box"]
    n_plat["Alura · Rocketseat · DIO · Udemy"]
    n_anki["Anki"]
    n_road["roadmap.sh + Akita"]
    n_ghed["GitHub Education"]
  end
  subgraph L_editora["Editora AMS Silva (produção de livros)"]
    n_exyaml["Exercícios em YAML"]
  end
  subgraph L_nuvem["Nuvem, código e entrega"]
    n_aws["AWS"]
    n_azure["Azure"]
  end
  subgraph L_chat["Assistentes de IA (chat, pesquisa e estudo)"]
    n_copi["GitHub Copilot"]
  end
  subgraph L_win["Windows 11, apps e máquinas virtuais"]
    n_obsd["Obsidian + Git"]
    n_vms["VMs: Kali · Arch · Servidores"]
  end
  n_learn -->|"certificação"| n_azure
  n_learn -->|"Skill Builder"| n_aws
  n_thm -->|"prática"| n_vms
  n_thm -->|"writeups"| n_obsd
  n_plat -->|"suas anotações"| n_obsd
  n_obsd -->|"notas viram cartões"| n_anki
  n_exyaml -->|"baralhos"| n_anki
  n_road -->|"roteiro"| n_obsd
  n_ghed -->|"Copilot Pro"| n_copi
  classDef desta fill:#e2ecec,stroke:#0e3a45,color:#13262b
  class n_learn,n_thm,n_plat,n_anki,n_road,n_ghed desta
```

## Blocos

| Bloco | Tipo | O que faz |
|---|---|---|
| [Microsoft Learn + AWS Skill Builder](#learn) | Remoto · precisa de conta | Trilhas oficiais e gratuitas para AZ-900, AZ-204 e AWS. |
| [TryHackMe / Hack The Box](#thm) | Remoto · precisa de conta | Laboratórios guiados de segurança para Security+, eJPT e OSCP. |
| [Alura · Rocketseat · DIO · Udemy](#plat) | Remoto · precisa de conta | Contas de aluno. A licença é para você assistir e estudar; baixar, copiar ou extrair as aulas para alimentar IA não é permitido. O que vai para a IA são as suas anotações e os seus projetos. |
| [Anki](#anki) | Local · precisa de conta | Repetição espaçada para comandos, conceitos, certificações e concurso. Open source. A conta grátis do AnkiWeb sincroniza notebook e celular. |
| [roadmap.sh + Akita](#road) | Remoto | Roteiros de estudo e referência da trilha Linux. |
| [GitHub Education](#ghed) | Remoto · precisa de conta | Pacote para professores: Copilot Pro e outros benefícios. Peça a verificação. |

<a id="learn"></a>

### Microsoft Learn + AWS Skill Builder

*Remoto · precisa de conta*

Trilhas oficiais e gratuitas para AZ-900, AZ-204 e AWS.

| Direção | Bloco | Camada | O que passa |
|---|---|---|---|
| → envia para | [Azure](11-nuvem.md#azure) | Nuvem, código e entrega | certificação |
| → envia para | [AWS](11-nuvem.md#aws) | Nuvem, código e entrega | Skill Builder |

<a id="thm"></a>

### TryHackMe / Hack The Box

*Remoto · precisa de conta*

Laboratórios guiados de segurança para Security+, eJPT e OSCP.

| Direção | Bloco | Camada | O que passa |
|---|---|---|---|
| → envia para | [VMs: Kali · Arch · Servidores](03-win.md#vms) | Windows 11, apps e máquinas virtuais | prática |
| → envia para | [Obsidian + Git](03-win.md#obsd) | Windows 11, apps e máquinas virtuais | writeups |

<a id="plat"></a>

### Alura · Rocketseat · DIO · Udemy

*Remoto · precisa de conta*

Contas de aluno. A licença é para você assistir e estudar; baixar, copiar ou extrair as aulas para alimentar IA não é permitido. O que vai para a IA são as suas anotações e os seus projetos.

| Direção | Bloco | Camada | O que passa |
|---|---|---|---|
| → envia para | [Obsidian + Git](03-win.md#obsd) | Windows 11, apps e máquinas virtuais | suas anotações |

<a id="anki"></a>

### Anki

*Local · precisa de conta*

Repetição espaçada para comandos, conceitos, certificações e concurso. Open source. A conta grátis do AnkiWeb sincroniza notebook e celular.

| Direção | Bloco | Camada | O que passa |
|---|---|---|---|
| ← recebe de | [Obsidian + Git](03-win.md#obsd) | Windows 11, apps e máquinas virtuais | notas viram cartões |
| ← recebe de | [Exercícios em YAML](14-editora.md#exyaml) | Editora AMS Silva (produção de livros) | baralhos |

<a id="road"></a>

### roadmap.sh + Akita

*Remoto*

Roteiros de estudo e referência da trilha Linux.

| Direção | Bloco | Camada | O que passa |
|---|---|---|---|
| → envia para | [Obsidian + Git](03-win.md#obsd) | Windows 11, apps e máquinas virtuais | roteiro |

<a id="ghed"></a>

### GitHub Education

*Remoto · precisa de conta*

Pacote para professores: Copilot Pro e outros benefícios. Peça a verificação.

| Direção | Bloco | Camada | O que passa |
|---|---|---|---|
| → envia para | [GitHub Copilot](06-chat.md#copi) | Assistentes de IA (chat, pesquisa e estudo) | Copilot Pro |

---

[↑ Camada 14 · Editora AMS Silva (produção de livros)](14-editora.md) · [↓ Camada 12 · Produção de conteúdo](12-cont.md)
