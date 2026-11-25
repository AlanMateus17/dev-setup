# Estação única AM5: plano de hardware

[← Camada 01 · Hardware](../camadas/01-hw.md) · [Índice da documentação](../README.md)

Plano de 19/11/2026 (original no Google Drive: *Plano de Infraestrutura e Hardware – Estação Única AM5*), trazido para o repositório em 25/11/2026. É o detalhamento do bloco **Workstation com GPU** (`ws`) da camada 01.

> **Quando compra:** nada daqui muda a ordem de compras. A estação é hardware caro: só entra com sobra, pela cascata do [plano de financiamento](../operacao/08-financiar-o-setup.md), e a GPU só depois do portão. Até lá valem Kaggle, Colab e GPU por hora ([custos](../custos.md): comprar só quando o aluguel passar do valor da parcela por 6 meses seguidos). Preços de 19/11/2026: confira de novo antes de comprar.

## 1. O que a estação faz

Um único computador, modular, que junta tudo o que hoje fica espalhado entre o notebook e a nuvem:

- **Desenvolvimento:** o monorepo dos sistemas do grupo (AM Gestão e as suítes seguintes), builds, compiladores e IDEs.
- **Serviços 24/7 em Docker:** PostgreSQL, Redis, Forgejo, LiteLLM, BookStack, Firefly III, Actual Budget e Headscale (ver [soberania](../../infra/soberania/LEIA.md)).
- **IA local:** Ollama rodando direto, agentes de código e cofres cifrados com gocryptfs.
- **Bancada:** robótica e eletrônica (Arduino, ESP32) e a produção de material de aula (LaTeX).

### Por que AM5, e não dois processadores nem Threadripper

1. **Memória sem NUMA:** um soquete só, sem a latência entre processadores de um servidor dual.
2. **Consumo:** o Ryzen 9 9950X aguenta 24/7 numa tomada de 127 V de casa.
3. **Velocidade por núcleo:** até 5,7 GHz, compila e responde mais rápido que processador de servidor da mesma geração.
4. **Dinheiro onde importa:** sobra para memória de vídeo, DDR5 e NVMe.
5. **Cresce para o lado:** um segundo nó AM5 igual, ligado pelo Headscale e balanceado pelo LiteLLM, sem ponto único de falha.

### Limites da placa-mãe (X870E)

- Até 192 GB (ou 256 GB) de DDR5 em 4 slots.
- 2 slots PCIe 5.0 em x8/x8 (duas GPUs).
- 4 a 5 NVMe direto na CPU e no chipset (20 a 40 TB).
- Rede de 2,5 Gbps e 5 Gbps na placa.

## 2. Lista de compras completa

### Gabinete

| Item | Peça | Faixa de preço (R$) |
|---|---|---|
| Processador | AMD Ryzen 9 9950X (16 núcleos / 32 threads, até 5,7 GHz) | 3.100 – 4.360 |
| Placa-mãe | MSI MPG X870E Carbon WiFi (ATX, 4× DDR5, 4× M.2, 2× PCIe 5.0, LAN 5G + 2,5G) | 2.540 – 3.720 |
| Memória | Kingston FURY Beast 64 GB (2×32 GB) DDR5-6000, 2 slots livres | 4.935 – 10.895 |
| Placa de vídeo | NVIDIA RTX 5060 Ti 16 GB GDDR7 (IA local) | 5.000 – 5.460 |
| SSD do sistema | NVMe 1 TB PCIe 4.0 (ex.: Kingston NV3), só o Linux | 990 – 1.270 |
| SSD de dados | NVMe 4 TB PCIe 4.0 (ex.: Adata Legend 900 PRO): Docker, Postgres, IA | 3.140 – 3.815 |
| HD de backup | SATA 8 TB NAS (ex.: WD Red Plus): snapshots locais | 3.200 – 3.650 |
| Refrigeração | Water cooler Arctic Liquid Freezer III 360 mm | 900 – 930 |
| Fonte | 1000 W 80 Plus Gold, modular (ATX 3.0 / PCIe 5.0) | 800 – 1.050 |
| Gabinete | Lian Li Lancool 216 (mesh, fluxo para 2 GPUs) | 750 – 1.490 |
| **Subtotal** | | **25.355 – 36.640** |

### Periféricos, energia e bancada

| Item | Peça | Faixa de preço (R$) |
|---|---|---|
| Monitores | 2× 27" QHD IPS (ex.: Dell Alienware AW2725DM) | 2.125 – 2.730 |
| Suporte | Articulado duplo com pistão a gás (ex.: NB H180) | 330 – 350 |
| Hubs USB | 2× USB 3.0 de 7 portas com fonte e chave por porta (ex.: Ugreen CM481) | 550 – 650 |
| Nobreak | Intelbras SNB 1500 VA senoidal puro 127 V, com USB | 3.400 |
| Filtro de linha | iClamper Energia 5 tomadas | 75 – 100 |
| Microfone | USB de mesa com mute físico (ex.: Saramonic USB) | 290 – 300 |
| Webcam | Full HD com tampa de privacidade (ex.: Logitech C920s) | 435 – 460 |
| Cabos | Cat6 + calha sob a mesa | 100 |
| **Subtotal** | | **7.305 – 8.090** |

**Total: R$ 32.660 a R$ 44.730.**

O nobreak, o 2º monitor, o microfone e a câmera já são blocos da camada 01 para o notebook: comprados para ele, servem depois na estação, sem comprar de novo.

## 3. Entrada enxuta (R$ 24.000 a R$ 26.000)

Mantém a CPU e a placa-mãe de topo (o teto de expansão) e corta o resto para depois:

1. **32 GB de RAM** no começo, no lugar de 64 GB: libera R$ 2.500 a R$ 6.000; os slots ficam livres.
2. **Sem o HD de 8 TB:** backup e volumes do Docker numa partição separada do NVMe de 4 TB até lá. Economia: cerca de R$ 3.200.
3. **Um monitor só:** o segundo (logs e agentes) vem no ciclo seguinte. Economia: R$ 1.100 a R$ 1.360.

## 4. Upgrades sem trocar a base

```text
[1: Armazenamento] ──► [2: Memória] ──► [3: Duas GPUs] ──► [4: Cluster AM5]
 +2× NVMe 4 TB          +64/128 GB DDR5   +1 GPU 16/24 GB    +1 nó AM5 igual
 +4× HD SATA            128 a 192 GB      Ollama / vLLM      Headscale + LiteLLM
```

1. **Armazenamento:** os 2 slots M.2 que sobram com 4 TB cada; HDs nas 4 portas SATA.
2. **Memória:** mais 2×32 GB (128 GB) ou kits de alta densidade até 192 GB.
3. **Segunda GPU** (16 ou 24 GB) no 2º PCIe 5.0, somando memória de vídeo no Ollama/vLLM para modelos maiores.
4. **Segundo nó AM5** pela rede Headscale/Tailscale, com o LiteLLM distribuindo e cobrindo falhas.

## 5. Configuração e cuidados 24/7

**Sistema:** Linux direto no NVMe de 1 TB (Debian stable ou Ubuntu LTS). Windows só em VM KVM/QEMU quando precisar. Vale só para a estação: no notebook continua o [ADR 0001](../adr/0001-wsl2-em-vez-de-dual-boot.md) (WSL2). Se a estação for comprada, registre um ADR novo.

**Energia:** USB do nobreak no Linux com o **NUT** (Network UPS Tools), que desliga os containers e o sistema com calma numa queda longa.

**Backup 3-2-1:** restic (ou borg) com snapshots diários do Postgres, do Forgejo, do vault do Obsidian e das chaves do gocryptfs para o HD local; cópia cifrada fora de casa no Backblaze B2 ou Cloudflare R2 (o mesmo [`backup.sh`](../../scripts/wsl/backup.sh) do notebook).

**Bancada isolada:** Arduino, automação e relés **só** no hub USB 2, com fonte própria e chave por porta, para proteger as portas da placa-mãe de surto e descarga eletrostática.

## O que falta preencher

- [ ] Peças que você já tem e que entram na estação (marque aqui o que já comprou).
- [ ] Preço conferido na semana da compra (Kabum, Pichau, Terabyte, Mercado Livre).
- [ ] Marco de renda da cascata que libera a entrada enxuta.
