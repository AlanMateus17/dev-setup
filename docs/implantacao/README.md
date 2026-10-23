# Implantação

[← Índice da documentação](../README.md)

Como sair do planejamento para o setup funcionando: scripts que instalam, scripts que conferem e um roteiro com o critério de pronto de cada passo. Quando a última fase passar, alimentar o sistema é só colocar arquivos numa pasta.

- [Roteiro de implantação](roteiro.md): 18 fases e 129 passos, na ordem, com o que cada passo implanta (gerado)
- [`acompanhamento.html`](acompanhamento.html): a mesma lista para marcar o progresso no navegador (gerado)

## Tudo o que está no setup está no roteiro

Cada passo diz quais blocos do [mapa do setup](../mapa.html) ele implanta. Os 303 blocos têm lugar:

| Onde | Blocos | O que significa |
|---|---:|---|
| Num passo do roteiro | 214 | Você instala, configura ou cria seguindo o passo |
| Peça a construir | 9 | Ainda não existe como código: as peças do pipeline de imagens e os agentes da editora, que começam com o capítulo 1 |
| Não se instala | 3 | Públicos (alunos, recrutadores) e os conectores que você decidiu não usar |
| Para depois | 77 | Marcados como futuro no mapa: os 9 negócios físicos, CNPJ, anúncios pagos, AWS, Kubernetes, YubiKey e afins |

O CI confere isso a cada envio: se alguém acrescentar um bloco ao mapa e esquecer o roteiro, o teste falha e diz qual bloco ficou de fora. A lista completa está no fim do [roteiro](roteiro.md#cobertura) e do acompanhamento.

Os 9 negócios ficam em "para depois" de propósito: cada um tem o próprio plano de abertura em [Negócios](../negocios/README.md), com o mínimo para abrir e o momento certo. O roteiro deixa pronta a base que todos usam.

## O que fica funcionando no fim do núcleo

```mermaid
flowchart LR
  subgraph W["Windows"]
    P["Programas<br/>instalar.ps1"]
    V1["verificar.ps1"]
  end
  subgraph L["Ubuntu no WSL2"]
    B["Ferramentas, Git assinado,<br/>Claude Code, ai-jail<br/>bootstrap.sh"]
    E["~/AMtech/entrada"] --> PC["processar.py<br/>a cada 15 min"]
    PC --> F["~/AMtech/fila<br/>peças para aprovar"]
    V2["verificar.sh"]
  end
  subgraph D["Docker"]
    N["n8n"] --> M[("Métricas<br/>PostgreSQL")]
    M --> G["Grafana<br/>painel de lucro"]
    K["Uptime Kuma"]
  end
  PC -->|"aviso"| T["Telegram"]
  H["Hotmart · Kiwify"] -->|"webhook pelo túnel"| N
  F -->|"você aprova e agenda"| R["Redes"]
```

## O que acontece quando você alimenta o sistema

| Você coloca | Onde | O sistema faz |
|---|---|---|
| Uma aula gravada | `~/AMtech/entrada/aulas` | Transcreve no notebook, gera 3 cortes com início e fim, carrossel, newsletter, questão de concurso e legendas; avisa no Telegram |
| Um capítulo ou trecho do livro | `~/AMtech/entrada/capitulos` | Artigo de blog, cards de conceito, newsletter e roteiro de vídeo curto |
| Anotações de um reparo | `~/AMtech/entrada/reparos` | Post do Google Perfil, dica para Reels e pergunta frequente do site |
| Uma decisão da semana | `~/AMtech/entrada/decisoes` | Roteiro do vídeo de build in public, post no LinkedIn e newsletter |
| Uma ideia solta | `~/AMtech/entrada/ideias` | Ângulos de conteúdo, rascunho de post e a linha para o portfólio de ofertas |
| Uma venda | (chega sozinha) | Webhook da plataforma → n8n → tabela de vendas → painel de lucro por produto e campanha |

Tudo segue o seu [guia de marca](../../config/marca.md). Arquivo que dá erro três vezes vai para `entrada/_com-erro` com o motivo, sem travar a fila.

## Como você sabe que está funcionando

Três verificadores, todos somente leitura, que terminam dizendo "pronto" ou listando exatamente o que falta:

| Verificador | Onde roda | Confere |
|---|---|---|
| `scripts/windows/verificar.ps1` | PowerShell | Programas, WSL2, .wslconfig, Docker, Ollama e, como Administrador, Secure Boot, TPM e criptografia |
| `scripts/wsl/verificar.sh` | Ubuntu | Ferramentas e versões (inclusive nmap, dig, Azure CLI, Terraform, Vercel CLI e Wrangler como opcionais), Git com commits assinados, login no GitHub, pastas |
| `scripts/wsl/verificar.sh --servicos` | Ubuntu | n8n, banco de métricas, Grafana, Uptime Kuma, Postiz e o pipeline de conteúdo |

## O que eu testei e o que não consegui testar

Testado aqui, num Ubuntu 24.04 igual ao do WSL:

- `bootstrap.sh` rodado de verdade duas vezes: instalou .NET 10, fnm, gitleaks, trivy e ai-jail, configurou Git e criou as pastas; na segunda vez não refez nada.
- `verificar.sh`, inclusive a saída em JSON.
- O banco de métricas com dados de exemplo: lucro, CPA, venda repetida que não duplica, e o usuário do Grafana que só lê.
- O pipeline de conteúdo com 10 testes automáticos (transcrição, fila, quarentena, nomes repetidos) e uma rodada simulada.
- O `compose.yaml` validado pelo Docker Compose; os scripts passaram no ShellCheck e no PSScriptAnalyzer.
- Os scripts do Windows rodaram no PowerShell 7 com `winget`, `wsl` e `code` simulados.
- `nuvem.sh` rodado de verdade duas vezes: instalou Azure CLI 2.91, Vercel CLI e Wrangler; na segunda vez não refez nada.

Não deu para testar aqui:

- O Windows de verdade (winget, WSL, criptografia). Por isso todo script do Windows tem o modo que só mostra o que faria, e o verificador confere depois.
- Baixar as imagens Docker e subir a stack (o ambiente daqui bloqueia os registros de imagens). O primeiro `docker compose up -d` no seu notebook é o teste.
- O instalador do Node pelo fnm e o do Claude Code, que dependem de sites bloqueados aqui.
- O Terraform, que vem do repositório da HashiCorp, também bloqueado aqui. O `nuvem.sh` avisa com ERRO se falhar no seu notebook.
- Os nomes das extensões do VS Code no Marketplace (bloqueado aqui). Se algum mudou, o script mostra ERRO só naquela extensão e segue.
- A chamada real à API do Claude e ao Telegram, que precisam das suas chaves.

## O que nenhum script faz por você

- Criar contas, senhas, 2FA e aprovar pagamentos.
- Aprovar as peças antes de publicar. O pipeline deixa tudo pronto na fila; publicar sem revisão é exatamente o risco que o setup evita.
- Publicar no TikTok pela API sem a auditoria do app (só sai como privado).
- Conectar os webhooks de venda: o n8n precisa de um endereço público (túnel), e o fluxo é montado com você na fase 12.

## Custos novos

| Item | Custo |
|---|---|
| API do Claude para o pipeline | Por uso, separado da assinatura; defina um limite mensal no console da Anthropic |
| Backblaze B2 (cópia fora de casa) | Cerca de US$ 6,95 por TB por mês, ou o armazenamento do plano Google que você já tem |
| Domínio .com.br | Anuidade do Registro.br |
| Azure, Resend, Sentry, SonarQube Cloud | Começam no plano grátis; ligue o alerta de orçamento da Azure antes de criar qualquer recurso |
| ElevenLabs (voz clonada) | Plano pago, só se decidir usar |
| ISBN e ficha catalográfica | Por livro, na CBL, quando o primeiro livro estiver pronto |
| Todo o resto (n8n, Grafana, PostgreSQL, Uptime Kuma, Postiz, ai-jail, restic) | Grátis, rodando no seu notebook |

## Ritmo sugerido

São cerca de 67 horas no total: 46 no núcleo (fases 0 a 13) e 21 na expansão (14 a 17). No bloco de construção da sua semana (quinta e sexta de manhã, umas 5 horas):

| Semana | Fases |
|---|---|
| 1 | 0 Preparar, 1 Windows |
| 2 | 2 Linux, 3 GitHub, 4 Agentes |
| 3 | 5 Backup, 6 Claude e assistentes, 7 Automação |
| 4 | 8 Pipeline de conteúdo, 9 Estúdio |
| 5 e 6 | 10 Contas, canais e sites |
| 7 a 9 | 11 Vendas e finanças no CPF |
| 10 | 12 Vendas medidas, 13 Teste do núcleo |
| Depois | 14 Sistemas AM e 15 Nuvem quando o primeiro sistema entrar na esteira; 16 Editora quando o capítulo 1 e o seu modelo estiverem prontos; 17 Estudo, contínuo |

O pipeline de conteúdo já funciona no fim da semana 4. Daí em diante, cada aula que você gravar já vira peças, enquanto as contas e as vendas vão sendo montadas.
