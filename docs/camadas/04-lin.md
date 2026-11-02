<!-- Arquivo GERADO por tools/gerar_docs.py a partir de data/. Edite os dados, não este arquivo. -->


# Camada 04 · Linux (Ubuntu no WSL2, Arch no 2º disco)

[← Arquitetura](../arquitetura.md) · [Índice da documentação](../README.md)

> **Ligação com a camada de baixo:** O código fica no ext4 do Linux; o Windows enxerga pela ponte do WSL2.

**13 blocos** · 0 precisam de conta · 3 marcados como futuro

## Mapa de conexões

```mermaid
flowchart LR
  subgraph L_lin["Linux (Ubuntu no WSL2, Arch no 2º disco)"]
    n_nvim["Neovim"]
    n_netw["nmap · dig · curl"]
    n_wsl["Ubuntu (WSL2)"]
    n_git["Git + SSH + gh"]
    n_rt[".NET 10 · Node · Python"]
    n_tex["TeX Live"]
    n_sec["gitleaks · Trivy"]
    n_dot["dotfiles"]
    n_arch["Arch + Omarchy (2º NVMe)"]
    n_rotinas["Rotinas agendadas"]
    n_adguard["AdGuard Home (DNS)"]
    n_wireguard["WireGuard (na mão)"]
    n_ros2["ROS 2 + ponte MQTT"]
  end
  subgraph L_oper["Operação do grupo (esteira, marca, qualidade)"]
    n_overif["Verificadores"]
  end
  subgraph L_mkt["Marketing, automação e medição"]
    n_tg["Telegram (avisos)"]
  end
  subgraph L_editora["Editora AMS Silva (produção de livros)"]
    n_bci["Pipeline do livro (CI)"]
  end
  subgraph L_nuvem["Nuvem, código e entrega"]
    n_gh["GitHub"]
    n_repopadrao["Repositório padrão"]
  end
  subgraph L_app["Aplicação: sistemas AM (Aura)"]
    n_api["API ASP.NET Core"]
    n_status["aura-status"]
  end
  subgraph L_cnt["Containers, Kubernetes e infra como código"]
    n_docker["Docker + Compose"]
    n_mqtt["Mosquitto (MQTT)"]
  end
  subgraph L_dados["Dados e treino de IA"]
    n_pyds["Python de dados (Polars, Jupyter)"]
    n_torch["PyTorch + CUDA (WSL2)"]
  end
  subgraph L_ia["Agentes de IA e sandbox"]
    n_cc["Claude Code"]
    n_jail["ai-jail"]
  end
  subgraph L_win["Windows 11, apps e máquinas virtuais"]
    n_boot["Gerenciador de boot"]
    n_tail["Tailscale (VPN)"]
    n_vms["VMs: Kali · Arch · Servidores"]
    n_vsc["VS Code"]
    n_w11["Windows 11 Home"]
    n_wslcfg[".wslconfig + localhost"]
    n_wterm["Terminal · PowerShell · winget"]
  end
  subgraph L_seg["Segurança e cofre"]
    n_bkp["Backup 3-2-1"]
  end
  subgraph L_hw["Hardware"]
    n_nvme["2º NVMe (1–4 TB)"]
    n_parch["Pendrive Arch (instalação portátil)"]
    n_rob["Arduino · ESP32 · Pi"]
  end
  n_nvim -->|"editor"| n_wsl
  n_netw -->|"diagnóstico"| n_vms
  n_wsl -->|"terminal"| n_git
  n_wsl -->|"executa"| n_rt
  n_wsl -->|"socket da engine"| n_docker
  n_wsl -->|"CUDA no WSL2"| n_torch
  n_bkp -->|"copia ~/dev"| n_wsl
  n_w11 -->|"WSL2"| n_wsl
  n_vsc -->|"Remote – WSL"| n_wsl
  n_jail -->|"só ~/dev/#lt;projeto#gt;"| n_wsl
  n_wslcfg -->|"limite de RAM"| n_wsl
  n_wterm -->|"abre o Ubuntu"| n_wsl
  n_overif -->|"confere"| n_wsl
  n_git -->|"push via SSH"| n_gh
  n_sec -->|"pre-commit"| n_git
  n_status -->|"git status"| n_git
  n_cc -->|"commit com sua revisão"| n_git
  n_rt -->|"compila e roda"| n_api
  n_rt -->|"Python + uv"| n_pyds
  n_tex -->|"compila o PDF"| n_bci
  n_repopadrao -->|"inclui"| n_sec
  n_dot -->|"versionado"| n_gh
  n_dot -->|"mesmos dotfiles"| n_parch
  n_arch -->|"mesmos dotfiles"| n_dot
  n_nvme -->|"disco próprio"| n_arch
  n_boot -->|"boot"| n_arch
  n_parch -->|"treino antes do 2º NVMe"| n_arch
  n_rotinas -->|"resumo da manhã"| n_tg
  n_adguard -->|"DNS da rede"| n_tail
  n_wireguard -->|"base de"| n_tail
  n_ros2 -->|"ponte"| n_mqtt
  n_rob -->|"Raspberry Pi"| n_ros2
  classDef desta fill:#e2ecec,stroke:#0e3a45,color:#13262b
  class n_nvim,n_netw,n_wsl,n_git,n_rt,n_tex,n_sec,n_dot,n_arch,n_rotinas,n_adguard,n_wireguard,n_ros2 desta
```

## Blocos

| Bloco | Tipo | O que faz | Quando entra |
|---|---|---|---|
| [Neovim](#nvim) | Local · futuro | Editor de terminal da trilha Arch e Akita. Aprender aos poucos; não substitui o VS Code no começo. | passo 40.2 · 2027, conforme cada compra |
| [nmap · dig · curl](#netw) | Local | Diagnóstico de rede no Ubuntu: portas, DNS e requisições HTTP. Instalados pelo bootstrap.sh. | passo 4.4 · Semana 2 · nov/2026 |
| [Ubuntu (WSL2)](#wsl) | Local | Onde o código vive e roda. | passo 4.1 · Semana 2 · nov/2026; passo 4.5 · Semana 2 · nov/2026 |
| [Git + SSH + gh](#git) | Local | Versionamento e acesso ao GitHub. | passo 4.4 · Semana 2 · nov/2026; passo 4.6 · Semana 2 · nov/2026 |
| [.NET 10 · Node · Python](#rt) | Local | Runtimes das APIs, do front e dos scripts. | passo 4.4 · Semana 2 · nov/2026 |
| [TeX Live](#tex) | Local | Compila o livro e as apostilas. | passo 4.4 · Semana 2 · nov/2026 |
| [gitleaks · Trivy](#sec) | Local | Barra senha no commit e acha vulnerabilidades em imagens. | passo 4.4 · Semana 2 · nov/2026; passo 20.2 · Semana 5 · nov/2026; passo 20.3 · Semana 5 · nov/2026 |
| [dotfiles](#dot) | Local | Configuração versionada do ambiente. | passo 4.7 · Semana 2 · nov/2026 |
| [Arch + Omarchy (2º NVMe)](#arch) | Local · futuro | Linux nativo com boot próprio, sem tocar no Windows. Antes dele, o Arch portátil em pendrive ou SSD USB. | passo 40.1 · 2027, conforme cada compra |
| [Rotinas agendadas](#rotinas) | Local | Resumo da manhã no Telegram e manutenção semanal, pelo cron do Ubuntu. | passo 17.3 · Semana 4 · nov/2026; passo 17.4 · Semana 4 · nov/2026; passo 17.5 · Semana 4 · nov/2026 |
| [AdGuard Home (DNS)](#adguard) | Local | DNS da casa com bloqueio de anúncios e rastreadores, também pelo Tailscale. | passo 24.4 · Semana 6 · nov/2026 |
| [WireGuard (na mão)](#wireguard) | Local | Túnel montado à mão entre duas máquinas, para entender o que o Tailscale faz. | passo 24.6 · Semana 6 · nov/2026 |
| [ROS 2 + ponte MQTT](#ros2) | Local · futuro | Robôs no Raspberry Pi com ROS 2; o mqtt_client leva os tópicos para o MQTT e o Home Assistant manda e recebe comandos. | passo 51.10 · Voz no PC e política em dez/2026; servidor da casa e cada aparelho conforme a compra (2027); orquestrador depois da Operação 24 horas |

<a id="nvim"></a>

### Neovim

*Local · futuro*

Editor de terminal da trilha Arch e Akita. Aprender aos poucos; não substitui o VS Code no começo.

**Quando entra:** passo 40.2 · 2027, conforme cada compra ([roteiro](../implantacao/roteiro.md))

| Direção | Bloco | Camada | O que passa |
|---|---|---|---|
| → envia para | [Ubuntu (WSL2)](04-lin.md#wsl) | Linux (Ubuntu no WSL2, Arch no 2º disco) | editor |

<a id="netw"></a>

### nmap · dig · curl

*Local*

Diagnóstico de rede no Ubuntu: portas, DNS e requisições HTTP. Instalados pelo bootstrap.sh.

**Quando entra:** passo 4.4 · Semana 2 · nov/2026 ([roteiro](../implantacao/roteiro.md))

| Direção | Bloco | Camada | O que passa |
|---|---|---|---|
| → envia para | [VMs: Kali · Arch · Servidores](03-win.md#vms) | Windows 11, apps e máquinas virtuais | diagnóstico |

<a id="wsl"></a>

### Ubuntu (WSL2)

*Local*

Onde o código vive e roda.

**Quando entra:** passo 4.1 · Semana 2 · nov/2026; passo 4.5 · Semana 2 · nov/2026 ([roteiro](../implantacao/roteiro.md))

| Direção | Bloco | Camada | O que passa |
|---|---|---|---|
| → envia para | [Git + SSH + gh](04-lin.md#git) | Linux (Ubuntu no WSL2, Arch no 2º disco) | terminal |
| → envia para | [.NET 10 · Node · Python](04-lin.md#rt) | Linux (Ubuntu no WSL2, Arch no 2º disco) | executa |
| → envia para | [Docker + Compose](09-cnt.md#docker) | Containers, Kubernetes e infra como código | socket da engine |
| → envia para | [PyTorch + CUDA (WSL2)](06-dados.md#torch) | Dados e treino de IA | CUDA no WSL2 |
| ← recebe de | [Backup 3-2-1](02-seg.md#bkp) | Segurança e cofre | copia ~/dev |
| ← recebe de | [Windows 11 Home](03-win.md#w11) | Windows 11, apps e máquinas virtuais | WSL2 |
| ← recebe de | [VS Code](03-win.md#vsc) | Windows 11, apps e máquinas virtuais | Remote – WSL |
| ← recebe de | [ai-jail](05-ia.md#jail) | Agentes de IA e sandbox | só ~/dev/<projeto> |
| ← recebe de | [Neovim](04-lin.md#nvim) | Linux (Ubuntu no WSL2, Arch no 2º disco) | editor |
| ← recebe de | [.wslconfig + localhost](03-win.md#wslcfg) | Windows 11, apps e máquinas virtuais | limite de RAM |
| ← recebe de | [Terminal · PowerShell · winget](03-win.md#wterm) | Windows 11, apps e máquinas virtuais | abre o Ubuntu |
| ← recebe de | [Verificadores](23-oper.md#overif) | Operação do grupo (esteira, marca, qualidade) | confere |

<a id="git"></a>

### Git + SSH + gh

*Local*

Versionamento e acesso ao GitHub.

**Quando entra:** passo 4.4 · Semana 2 · nov/2026; passo 4.6 · Semana 2 · nov/2026 ([roteiro](../implantacao/roteiro.md))

| Direção | Bloco | Camada | O que passa |
|---|---|---|---|
| → envia para | [GitHub](12-nuvem.md#gh) | Nuvem, código e entrega | push via SSH |
| ← recebe de | [Ubuntu (WSL2)](04-lin.md#wsl) | Linux (Ubuntu no WSL2, Arch no 2º disco) | terminal |
| ← recebe de | [gitleaks · Trivy](04-lin.md#sec) | Linux (Ubuntu no WSL2, Arch no 2º disco) | pre-commit |
| ← recebe de | [aura-status](11-app.md#status) | Aplicação: sistemas AM (Aura) | git status |
| ← recebe de | [Claude Code](05-ia.md#cc) | Agentes de IA e sandbox | commit com sua revisão |

<a id="rt"></a>

### .NET 10 · Node · Python

*Local*

Runtimes das APIs, do front e dos scripts.

**Quando entra:** passo 4.4 · Semana 2 · nov/2026 ([roteiro](../implantacao/roteiro.md))

| Direção | Bloco | Camada | O que passa |
|---|---|---|---|
| → envia para | [API ASP.NET Core](11-app.md#api) | Aplicação: sistemas AM (Aura) | compila e roda |
| → envia para | [Python de dados (Polars, Jupyter)](06-dados.md#pyds) | Dados e treino de IA | Python + uv |
| ← recebe de | [Ubuntu (WSL2)](04-lin.md#wsl) | Linux (Ubuntu no WSL2, Arch no 2º disco) | executa |

<a id="tex"></a>

### TeX Live

*Local*

Compila o livro e as apostilas.

**Quando entra:** passo 4.4 · Semana 2 · nov/2026 ([roteiro](../implantacao/roteiro.md))

| Direção | Bloco | Camada | O que passa |
|---|---|---|---|
| → envia para | [Pipeline do livro (CI)](15-editora.md#bci) | Editora AMS Silva (produção de livros) | compila o PDF |

<a id="sec"></a>

### gitleaks · Trivy

*Local*

Barra senha no commit e acha vulnerabilidades em imagens.

**Quando entra:** passo 4.4 · Semana 2 · nov/2026; passo 20.2 · Semana 5 · nov/2026; passo 20.3 · Semana 5 · nov/2026 ([roteiro](../implantacao/roteiro.md))

| Direção | Bloco | Camada | O que passa |
|---|---|---|---|
| → envia para | [Git + SSH + gh](04-lin.md#git) | Linux (Ubuntu no WSL2, Arch no 2º disco) | pre-commit |
| ← recebe de | [Repositório padrão](12-nuvem.md#repopadrao) | Nuvem, código e entrega | inclui |

<a id="dot"></a>

### dotfiles

*Local*

Configuração versionada do ambiente.

**Quando entra:** passo 4.7 · Semana 2 · nov/2026 ([roteiro](../implantacao/roteiro.md))

| Direção | Bloco | Camada | O que passa |
|---|---|---|---|
| → envia para | [GitHub](12-nuvem.md#gh) | Nuvem, código e entrega | versionado |
| → envia para | [Pendrive Arch (instalação portátil)](01-hw.md#parch) | Hardware | mesmos dotfiles |
| ← recebe de | [Arch + Omarchy (2º NVMe)](04-lin.md#arch) | Linux (Ubuntu no WSL2, Arch no 2º disco) | mesmos dotfiles |

<a id="arch"></a>

### Arch + Omarchy (2º NVMe)

*Local · futuro*

Linux nativo com boot próprio, sem tocar no Windows. Antes dele, o Arch portátil em pendrive ou SSD USB.

**Quando entra:** passo 40.1 · 2027, conforme cada compra ([roteiro](../implantacao/roteiro.md))

| Direção | Bloco | Camada | O que passa |
|---|---|---|---|
| → envia para | [dotfiles](04-lin.md#dot) | Linux (Ubuntu no WSL2, Arch no 2º disco) | mesmos dotfiles |
| ← recebe de | [2º NVMe (1–4 TB)](01-hw.md#nvme) | Hardware | disco próprio |
| ← recebe de | [Gerenciador de boot](03-win.md#boot) | Windows 11, apps e máquinas virtuais | boot |
| ← recebe de | [Pendrive Arch (instalação portátil)](01-hw.md#parch) | Hardware | treino antes do 2º NVMe |

<a id="rotinas"></a>

### Rotinas agendadas

*Local*

Resumo da manhã no Telegram e manutenção semanal, pelo cron do Ubuntu.

**Quando entra:** passo 17.3 · Semana 4 · nov/2026; passo 17.4 · Semana 4 · nov/2026; passo 17.5 · Semana 4 · nov/2026 ([roteiro](../implantacao/roteiro.md))

| Direção | Bloco | Camada | O que passa |
|---|---|---|---|
| → envia para | [Telegram (avisos)](21-mkt.md#tg) | Marketing, automação e medição | resumo da manhã |

<a id="adguard"></a>

### AdGuard Home (DNS)

*Local*

DNS da casa com bloqueio de anúncios e rastreadores, também pelo Tailscale.

**Quando entra:** passo 24.4 · Semana 6 · nov/2026 ([roteiro](../implantacao/roteiro.md))

| Direção | Bloco | Camada | O que passa |
|---|---|---|---|
| → envia para | [Tailscale (VPN)](03-win.md#tail) | Windows 11, apps e máquinas virtuais | DNS da rede |

<a id="wireguard"></a>

### WireGuard (na mão)

*Local*

Túnel montado à mão entre duas máquinas, para entender o que o Tailscale faz.

**Quando entra:** passo 24.6 · Semana 6 · nov/2026 ([roteiro](../implantacao/roteiro.md))

| Direção | Bloco | Camada | O que passa |
|---|---|---|---|
| → envia para | [Tailscale (VPN)](03-win.md#tail) | Windows 11, apps e máquinas virtuais | base de |

<a id="ros2"></a>

### ROS 2 + ponte MQTT

*Local · futuro*

Robôs no Raspberry Pi com ROS 2; o mqtt_client leva os tópicos para o MQTT e o Home Assistant manda e recebe comandos.

**Quando entra:** passo 51.10 · Voz no PC e política em dez/2026; servidor da casa e cada aparelho conforme a compra (2027); orquestrador depois da Operação 24 horas ([roteiro](../implantacao/roteiro.md))

| Direção | Bloco | Camada | O que passa |
|---|---|---|---|
| → envia para | [Mosquitto (MQTT)](09-cnt.md#mqtt) | Containers, Kubernetes e infra como código | ponte |
| ← recebe de | [Arduino · ESP32 · Pi](01-hw.md#rob) | Hardware | Raspberry Pi |

---

[↑ Camada 05 · Agentes de IA e sandbox](05-ia.md) · [↓ Camada 03 · Windows 11, apps e máquinas virtuais](03-win.md)
