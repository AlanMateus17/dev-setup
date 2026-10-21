<!-- Arquivo GERADO por tools/gerar_docs.py a partir de data/. Edite os dados, não este arquivo. -->


# Camada 04 · Linux (Ubuntu no WSL2, Arch no 2º disco)

[← Arquitetura](../arquitetura.md) · [Índice da documentação](../README.md)

> **Ligação com a camada de baixo:** O código fica no ext4 do Linux; o Windows enxerga pela ponte do WSL2.

**10 blocos** · 0 precisam de conta · 2 marcados como futuro

## Mapa de conexões

```mermaid
flowchart LR
  subgraph L_lin["Linux (Ubuntu no WSL2, Arch no 2º disco)"]
    n_nvim["Neovim"]
    n_netw["nmap · dig · curl · Wireshark"]
    n_wsl["Ubuntu (WSL2)"]
    n_git["Git + SSH + gh"]
    n_rt[".NET 10 · Node · Python"]
    n_tex["TeX Live"]
    n_sec["gitleaks · Trivy"]
    n_dot["dotfiles"]
    n_arch["Arch + Omarchy (2º NVMe)"]
    n_syncth["Syncthing"]
  end
  subgraph L_oper["Operação do grupo (esteira, marca, qualidade)"]
    n_overif["Verificadores"]
  end
  subgraph L_prod["Produtos (o que você vende)"]
    n_livro["Livro Lógica e Máquina"]
  end
  subgraph L_editora["Editora AMS Silva (produção de livros)"]
    n_bci["Pipeline do livro (CI)"]
  end
  subgraph L_nuvem["Nuvem, código e entrega"]
    n_gh["GitHub"]
  end
  subgraph L_app["Aplicação: sistemas AM (Aura)"]
    n_status["aura-status"]
  end
  subgraph L_cnt["Containers, Kubernetes e infra como código"]
    n_docker["Docker + Compose"]
  end
  subgraph L_ia["Agentes de IA e sandbox"]
    n_jail["ai-jail"]
  end
  subgraph L_win["Windows 11, apps e máquinas virtuais"]
    n_boot["Gerenciador de boot"]
    n_obsd["Obsidian + Git"]
    n_vms["VMs: Kali · Arch · Servidores"]
    n_vsc["VS Code"]
    n_w11["Windows 11 Home"]
    n_wslcfg[".wslconfig + localhost"]
    n_wterm["Terminal · PowerShell · winget"]
  end
  subgraph L_seg["Segurança e cofre"]
    n_bkp["Backup 3-2-1"]
    n_kee["KeePassXC"]
  end
  subgraph L_hw["Hardware"]
    n_nas["Servidor caseiro (NAS + serviços)"]
    n_nvme["2º NVMe (1–4 TB)"]
  end
  n_nvim -->|"editor"| n_wsl
  n_netw -->|"diagnóstico"| n_vms
  n_wsl -->|"terminal"| n_git
  n_wsl -->|"executa"| n_rt
  n_wsl -->|"socket da engine"| n_docker
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
  n_tex -->|"gera o PDF"| n_livro
  n_tex -->|"compila o PDF"| n_bci
  n_dot -->|"versionado"| n_gh
  n_arch -->|"mesmos dotfiles"| n_dot
  n_nvme -->|"disco próprio"| n_arch
  n_boot -->|"boot"| n_arch
  n_syncth -->|"sincroniza"| n_nas
  n_syncth -->|"vault"| n_obsd
  n_syncth -->|"cofre de senhas"| n_kee
  classDef desta fill:#e2ecec,stroke:#0e3a45,color:#13262b
  class n_nvim,n_netw,n_wsl,n_git,n_rt,n_tex,n_sec,n_dot,n_arch,n_syncth desta
```

## Blocos

| Bloco | Tipo | O que faz |
|---|---|---|
| [Neovim](#nvim) | Local · futuro | Editor de terminal da trilha Arch e Akita. Aprender aos poucos; não substitui o VS Code no começo. |
| [nmap · dig · curl · Wireshark](#netw) | Local | Trilha de redes e diagnóstico de containers. Só contra seus próprios alvos. |
| [Ubuntu (WSL2)](#wsl) | Local | Onde o código vive e roda. |
| [Git + SSH + gh](#git) | Local | Versionamento e acesso ao GitHub. |
| [.NET 10 · Node · Python](#rt) | Local | Runtimes das APIs, do front e dos scripts. |
| [TeX Live](#tex) | Local | Compila o livro e as apostilas. |
| [gitleaks · Trivy](#sec) | Local | Barra senha no commit e acha vulnerabilidades em imagens. |
| [dotfiles](#dot) | Local | Configuração versionada do ambiente. |
| [Arch + Omarchy (2º NVMe)](#arch) | Local · futuro | Linux nativo com boot próprio, sem tocar no Windows. |
| [Syncthing](#syncth) | Local | Sincroniza vault, projetos de vídeo e o cofre do KeePassXC entre as máquinas, sem nuvem no meio. Open source. |

<a id="nvim"></a>

### Neovim

*Local · futuro*

Editor de terminal da trilha Arch e Akita. Aprender aos poucos; não substitui o VS Code no começo.

| Direção | Bloco | Camada | O que passa |
|---|---|---|---|
| → envia para | [Ubuntu (WSL2)](04-lin.md#wsl) | Linux (Ubuntu no WSL2, Arch no 2º disco) | editor |

<a id="netw"></a>

### nmap · dig · curl · Wireshark

*Local*

Trilha de redes e diagnóstico de containers. Só contra seus próprios alvos.

| Direção | Bloco | Camada | O que passa |
|---|---|---|---|
| → envia para | [VMs: Kali · Arch · Servidores](03-win.md#vms) | Windows 11, apps e máquinas virtuais | diagnóstico |

<a id="wsl"></a>

### Ubuntu (WSL2)

*Local*

Onde o código vive e roda.

| Direção | Bloco | Camada | O que passa |
|---|---|---|---|
| → envia para | [Git + SSH + gh](04-lin.md#git) | Linux (Ubuntu no WSL2, Arch no 2º disco) | terminal |
| → envia para | [.NET 10 · Node · Python](04-lin.md#rt) | Linux (Ubuntu no WSL2, Arch no 2º disco) | executa |
| → envia para | [Docker + Compose](08-cnt.md#docker) | Containers, Kubernetes e infra como código | socket da engine |
| ← recebe de | [Backup 3-2-1](02-seg.md#bkp) | Segurança e cofre | copia ~/dev |
| ← recebe de | [Windows 11 Home](03-win.md#w11) | Windows 11, apps e máquinas virtuais | WSL2 |
| ← recebe de | [VS Code](03-win.md#vsc) | Windows 11, apps e máquinas virtuais | Remote – WSL |
| ← recebe de | [ai-jail](05-ia.md#jail) | Agentes de IA e sandbox | só ~/dev/<projeto> |
| ← recebe de | [Neovim](04-lin.md#nvim) | Linux (Ubuntu no WSL2, Arch no 2º disco) | editor |
| ← recebe de | [.wslconfig + localhost](03-win.md#wslcfg) | Windows 11, apps e máquinas virtuais | limite de RAM |
| ← recebe de | [Terminal · PowerShell · winget](03-win.md#wterm) | Windows 11, apps e máquinas virtuais | abre o Ubuntu |
| ← recebe de | [Verificadores](22-oper.md#overif) | Operação do grupo (esteira, marca, qualidade) | confere |

<a id="git"></a>

### Git + SSH + gh

*Local*

Versionamento e acesso ao GitHub.

| Direção | Bloco | Camada | O que passa |
|---|---|---|---|
| → envia para | [GitHub](11-nuvem.md#gh) | Nuvem, código e entrega | push via SSH |
| ← recebe de | [Ubuntu (WSL2)](04-lin.md#wsl) | Linux (Ubuntu no WSL2, Arch no 2º disco) | terminal |
| ← recebe de | [gitleaks · Trivy](04-lin.md#sec) | Linux (Ubuntu no WSL2, Arch no 2º disco) | pre-commit |
| ← recebe de | [aura-status](10-app.md#status) | Aplicação: sistemas AM (Aura) | git status |

<a id="rt"></a>

### .NET 10 · Node · Python

*Local*

Runtimes das APIs, do front e dos scripts.

| Direção | Bloco | Camada | O que passa |
|---|---|---|---|
| ← recebe de | [Ubuntu (WSL2)](04-lin.md#wsl) | Linux (Ubuntu no WSL2, Arch no 2º disco) | executa |

<a id="tex"></a>

### TeX Live

*Local*

Compila o livro e as apostilas.

| Direção | Bloco | Camada | O que passa |
|---|---|---|---|
| → envia para | [Livro Lógica e Máquina](16-prod.md#livro) | Produtos (o que você vende) | gera o PDF |
| → envia para | [Pipeline do livro (CI)](14-editora.md#bci) | Editora AMS Silva (produção de livros) | compila o PDF |

<a id="sec"></a>

### gitleaks · Trivy

*Local*

Barra senha no commit e acha vulnerabilidades em imagens.

| Direção | Bloco | Camada | O que passa |
|---|---|---|---|
| → envia para | [Git + SSH + gh](04-lin.md#git) | Linux (Ubuntu no WSL2, Arch no 2º disco) | pre-commit |

<a id="dot"></a>

### dotfiles

*Local*

Configuração versionada do ambiente.

| Direção | Bloco | Camada | O que passa |
|---|---|---|---|
| → envia para | [GitHub](11-nuvem.md#gh) | Nuvem, código e entrega | versionado |
| ← recebe de | [Arch + Omarchy (2º NVMe)](04-lin.md#arch) | Linux (Ubuntu no WSL2, Arch no 2º disco) | mesmos dotfiles |

<a id="arch"></a>

### Arch + Omarchy (2º NVMe)

*Local · futuro*

Linux nativo com boot próprio, sem tocar no Windows.

| Direção | Bloco | Camada | O que passa |
|---|---|---|---|
| → envia para | [dotfiles](04-lin.md#dot) | Linux (Ubuntu no WSL2, Arch no 2º disco) | mesmos dotfiles |
| ← recebe de | [2º NVMe (1–4 TB)](01-hw.md#nvme) | Hardware | disco próprio |
| ← recebe de | [Gerenciador de boot](03-win.md#boot) | Windows 11, apps e máquinas virtuais | boot |

<a id="syncth"></a>

### Syncthing

*Local*

Sincroniza vault, projetos de vídeo e o cofre do KeePassXC entre as máquinas, sem nuvem no meio. Open source.

| Direção | Bloco | Camada | O que passa |
|---|---|---|---|
| → envia para | [Servidor caseiro (NAS + serviços)](01-hw.md#nas) | Hardware | sincroniza |
| → envia para | [Obsidian + Git](03-win.md#obsd) | Windows 11, apps e máquinas virtuais | vault |
| → envia para | [KeePassXC](02-seg.md#kee) | Segurança e cofre | cofre de senhas |

---

[↑ Camada 05 · Agentes de IA e sandbox](05-ia.md) · [↓ Camada 03 · Windows 11, apps e máquinas virtuais](03-win.md)
