<!-- Arquivo GERADO por tools/gerar_docs.py a partir de data/. Edite os dados, não este arquivo. -->


# Camada 12 · Produção de conteúdo

[← Arquitetura](../arquitetura.md) · [Índice da documentação](../README.md)

> **Ligação com a camada de baixo:** Gravação e edição rodam no notebook; os arquivos finais sobem para as plataformas.

**6 blocos** · 2 precisam de conta · 0 marcados como futuro

## Mapa de conexões

```mermaid
flowchart LR
  subgraph L_cont["Produção de conteúdo"]
    n_obss["OBS Studio"]
    n_edit["DaVinci Resolve ou Kdenlive"]
    n_aud["Audacity"]
    n_img["Canva · Krita · Inkscape"]
    n_whis["Whisper (local)"]
    n_voz["Voz clonada (ElevenLabs)"]
  end
  subgraph L_pub["Público e canais"]
    n_ig["Instagram"]
    n_yt["YouTube"]
  end
  subgraph L_mkt["Marketing, automação e medição"]
    n_dub["Dublagem (YouTube + ElevenLabs)"]
  end
  subgraph L_web["Vitrine web (sites e domínio)"]
    n_inst["Instituto AMS"]
  end
  subgraph L_prod["Produtos (o que você vende)"]
    n_curso["Mini-curso Lógica de Programação"]
  end
  subgraph L_clc["Claude: recursos, conectores e plugins"]
    n_ccan["Conectores Canva + Figma"]
    n_phst["Plugins: Hostinger · Adobe · Cloudinary"]
  end
  subgraph L_chat["Assistentes de IA (chat, pesquisa e estudo)"]
    n_gpt["ChatGPT"]
  end
  subgraph L_win["Windows 11, apps e máquinas virtuais"]
    n_obsd["Obsidian + Git"]
  end
  subgraph L_hw["Hardware"]
    n_mic["Microfone + câmera"]
  end
  n_obss -->|"gravação"| n_edit
  n_obss -->|"áudio"| n_whis
  n_mic -->|"áudio e vídeo USB"| n_obss
  n_edit -->|"vídeo final"| n_yt
  n_edit -->|"aulas editadas"| n_curso
  n_phst -->|"imagem e vídeo"| n_edit
  n_aud -->|"áudio limpo"| n_edit
  n_voz -->|"narração"| n_edit
  n_img -->|"posts"| n_ig
  n_img -->|"capas"| n_inst
  n_gpt -->|"gera imagens"| n_img
  n_ccan -->|"posts e capas"| n_img
  n_whis -->|"transcrição"| n_obsd
  n_voz -->|"sua voz em outros idiomas"| n_dub
  classDef desta fill:#e2ecec,stroke:#0e3a45,color:#13262b
  class n_obss,n_edit,n_aud,n_img,n_whis,n_voz desta
```

## Blocos

| Bloco | Tipo | O que faz |
|---|---|---|
| [OBS Studio](#obss) | Local | Grava tela, câmera e áudio das aulas e vídeos. |
| [DaVinci Resolve ou Kdenlive](#edit) | Local | Edição de vídeo. Os dois têm versão grátis. |
| [Audacity](#aud) | Local | Limpa ruído e ajusta o áudio. |
| [Canva · Krita · Inkscape](#img) | Local · precisa de conta | Capas, posts e thumbnails. Canva precisa de conta; Krita e Inkscape são open source. |
| [Whisper (local)](#whis) | Local | Transcreve as aulas para legenda, artigo e capítulo. |
| [Voz clonada (ElevenLabs)](#voz) | Remoto · precisa de conta | Clonagem profissional da sua própria voz (plano Creator em diante, uso comercial nos planos pagos). Treino com 30 minutos ou mais de áudio limpo. Avise o público que a voz é gerada por IA. |

<a id="obss"></a>

### OBS Studio

*Local*

Grava tela, câmera e áudio das aulas e vídeos.

| Direção | Bloco | Camada | O que passa |
|---|---|---|---|
| → envia para | [DaVinci Resolve ou Kdenlive](12-cont.md#edit) | Produção de conteúdo | gravação |
| → envia para | [Whisper (local)](12-cont.md#whis) | Produção de conteúdo | áudio |
| ← recebe de | [Microfone + câmera](01-hw.md#mic) | Hardware | áudio e vídeo USB |

<a id="edit"></a>

### DaVinci Resolve ou Kdenlive

*Local*

Edição de vídeo. Os dois têm versão grátis.

| Direção | Bloco | Camada | O que passa |
|---|---|---|---|
| → envia para | [YouTube](19-pub.md#yt) | Público e canais | vídeo final |
| → envia para | [Mini-curso Lógica de Programação](14-prod.md#curso) | Produtos (o que você vende) | aulas editadas |
| ← recebe de | [Plugins: Hostinger · Adobe · Cloudinary](07-clc.md#phst) | Claude: recursos, conectores e plugins | imagem e vídeo |
| ← recebe de | [OBS Studio](12-cont.md#obss) | Produção de conteúdo | gravação |
| ← recebe de | [Audacity](12-cont.md#aud) | Produção de conteúdo | áudio limpo |
| ← recebe de | [Voz clonada (ElevenLabs)](12-cont.md#voz) | Produção de conteúdo | narração |

<a id="aud"></a>

### Audacity

*Local*

Limpa ruído e ajusta o áudio.

| Direção | Bloco | Camada | O que passa |
|---|---|---|---|
| → envia para | [DaVinci Resolve ou Kdenlive](12-cont.md#edit) | Produção de conteúdo | áudio limpo |

<a id="img"></a>

### Canva · Krita · Inkscape

*Local · precisa de conta*

Capas, posts e thumbnails. Canva precisa de conta; Krita e Inkscape são open source.

| Direção | Bloco | Camada | O que passa |
|---|---|---|---|
| → envia para | [Instagram](19-pub.md#ig) | Público e canais | posts |
| → envia para | [Instituto AMS](15-web.md#inst) | Vitrine web (sites e domínio) | capas |
| ← recebe de | [ChatGPT](06-chat.md#gpt) | Assistentes de IA (chat, pesquisa e estudo) | gera imagens |
| ← recebe de | [Conectores Canva + Figma](07-clc.md#ccan) | Claude: recursos, conectores e plugins | posts e capas |

<a id="whis"></a>

### Whisper (local)

*Local*

Transcreve as aulas para legenda, artigo e capítulo.

| Direção | Bloco | Camada | O que passa |
|---|---|---|---|
| → envia para | [Obsidian + Git](03-win.md#obsd) | Windows 11, apps e máquinas virtuais | transcrição |
| ← recebe de | [OBS Studio](12-cont.md#obss) | Produção de conteúdo | áudio |

<a id="voz"></a>

### Voz clonada (ElevenLabs)

*Remoto · precisa de conta*

Clonagem profissional da sua própria voz (plano Creator em diante, uso comercial nos planos pagos). Treino com 30 minutos ou mais de áudio limpo. Avise o público que a voz é gerada por IA.

| Direção | Bloco | Camada | O que passa |
|---|---|---|---|
| → envia para | [DaVinci Resolve ou Kdenlive](12-cont.md#edit) | Produção de conteúdo | narração |
| → envia para | [Dublagem (YouTube + ElevenLabs)](18-mkt.md#dub) | Marketing, automação e medição | sua voz em outros idiomas |

---

[↑ Camada 13 · Estudo e carreira](13-est.md) · [↓ Camada 11 · Nuvem, código e entrega](11-nuvem.md)
