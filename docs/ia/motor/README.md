# Motor de decisão e custo mínimo de IA

[← Arquitetura de IA](../README.md) · Decisão registrada no [ADR 0014](../../adr/0014-motor-de-decisao-e-custo-minimo.md)

Planejado na conversa de 11/11/2026. O objetivo: o Alan continua escrevendo do jeito dele, e o setup decide sozinho **quem** faz cada pedido (ferramenta pronta, código, automação, IA local, IA online ou o próprio Alan), gastando o mínimo e com a mesma régua de qualidade em programação, sistemas, empreendedorismo e finanças.

Regra-mãe: **a IA propõe, o código decide e verifica.**

## Arquivos de contexto

| # | Arquivo | O que guarda |
|---|---|---|
| 1 | [01-modelos-e-api.md](01-modelos-e-api.md) | Fable 5.2 e os outros modelos, chat x API, técnicas de economia de tokens |
| 2 | [02-perfil-senior-e-formulario.md](02-perfil-senior-e-formulario.md) | Os 7 erros recorrentes, as 10 regras, o formulário de pedido, o que é automático e o que é manual, plano de 30 dias |
| 3 | [03-escada-e-roteador.md](03-escada-e-roteador.md) | A escada de 5 degraus, o que é determinístico, o roteador local, o papel de cada ferramenta |
| 4 | [04-regra-de-tres.md](04-regra-de-tres.md) | Tarefa repetida 3 vezes vira cache, template ou script |
| 5 | [05-qualidade-e-seguranca.md](05-qualidade-e-seguranca.md) | As 6 peças anti-erro, as 7 lacunas de sênior e as técnicas para cada uma |
| 6 | [06-engenharia-reversa-e-ferramentas.md](06-engenharia-reversa-e-ferramentas.md) | Dissecação em 4 níveis, construir x usar, as 3 camadas, Hugging Face |
| 7 | [07-nuvem-barata.md](07-nuvem-barata.md) | O que vai para a nuvem, fase 0 grátis e fase 1 paga |

Documento complementar (Claude Docs): [Plano de Perfil Sênior](https://claude.ai/artifact/NH2Y9FNG9L7FvWkZcn9cVi). Skill proposta no chat: `arquiteto-de-prompt` (confirmar se foi salva).

## Ordem de construção (versão 0.1)

1. **Escada** (estender o `just triagem` atual, sem criar ferramenta nova).
2. **Catálogo único de capacidades** (evoluir `data/recursos.json`).
3. **Registro de cada decisão e custo** (no Núcleo AMtech).
4. Em seguida: preenchimento automático do formulário pelo modelo local, regra de três, guardas de segurança no CI, nuvem.

## Pendências (decisão do Alan)

- [x] **Calendário (decidido em 11/11/2026):** nada fica congelado. O motor e as frentes novas entram agora; a execução segue a ordem do roteiro e o limite de 3 frentes "agora".
- [ ] Confirmar se a skill `arquiteto-de-prompt` foi salva e se deve rodar em toda tarefa.
- [ ] Escolher a linguagem do roteador (Python, como o resto de `tools/`, é o padrão).
