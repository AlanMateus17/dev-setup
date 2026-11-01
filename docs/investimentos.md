<!-- Arquivo GERADO por tools/investimentos/investimentos.py a partir de data/investimentos.json. Não edite à mão. -->

# Investimentos: as suas metodologias, aplicadas por script

[← Índice da documentação](README.md)

> Não é recomendação de investimento. O setup aplica as regras que você escreveu; a decisão de comprar, manter ou vender é sua. Os tickers dos exemplos são inventados.

## Regras

- Portão: só entra dinheiro em ações e nas outras classes do ARCA com o cartão zerado e a reserva de emergência completa (3 → 6 → 12 meses).
- Aporte mensal planejado de R$ 800; meta de renda passiva de R$ 800 por mês.
- ARCA também dentro do pilar de ações: um percentual por metodologia, com limites por empresa e por setor para não concentrar.
- Uma carteira por metodologia (real ou simulada) para comparar o resultado de cada uma contra um índice de referência.
- Rebalancear de preferência com aporte novo: vender só quando a própria regra de venda da metodologia mandar.
- Indicadores vêm de fonte que você confere (demonstrações da empresa na CVM/RI); o script só calcula.
- Recomendar ativos para outras pessoas exige registro na CVM (analista ou consultor). Até lá, tudo aqui é para a sua carteira.

## Metodologias

| Metodologia | Tipo | Situação | Ideia |
|---|---|---|---|
| [Luiz Barsi (carteira previdenciária)](#barsi) | seleção para renda | **já usa** | Comprar empresas de setores perenes que pagam dividendos com constância e reinvestir os dividendos por décadas. |
| [Décio Bazin (preço-teto)](#bazin) | preço | **já usa** | Só comprar abaixo do preço-teto, que garante pelo menos 6% de dividendos sobre o preço pago, em empresas pouco endividadas. |
| [Benjamin Graham (investidor defensivo)](#graham) | preço e segurança | **já usa** | Comprar com margem de segurança abaixo do valor intrínseco, em empresas sólidas e com lucro estável. |
| [Warren Buffett (qualidade a preço justo)](#buffett) | seleção por qualidade | **já usa** | Empresas com vantagem competitiva durável, alta rentabilidade e pouca dívida, mantidas por muito tempo. |
| [Raul Sena (Investidor Sardinha)](#sena) | checklist qualitativo | **já usa** | Usar as perguntas do método do Raul Sena como ele usa e, numa segunda versão, estendidas com as perguntas das outras metodologias. |
| [Fórmula Mágica (Joel Greenblatt)](#formula_magica) | ranking quantitativo | **adicionar** | Ordenar as empresas por retorno sobre o capital (alto é melhor) e por lucro operacional sobre o valor da empresa (barato é melhor) e somar as posições. |
| [Piotroski F-Score](#piotroski) | filtro de saúde financeira | **adicionar** | Nove testes simples de lucro, endividamento e eficiência; nota de 0 a 9. Serve como filtro para as outras metodologias. |
| [Peter Lynch (PEG)](#lynch) | crescimento a preço justo | **avaliar** | Comparar o P/L com o crescimento do lucro: PEG até 1 indica que o preço não está caro para o crescimento. |
| [Modelo de Gordon (preço justo por dividendos)](#gordon) | preço | **avaliar** | Preço justo = próximo dividendo ÷ (retorno exigido − crescimento do dividendo). Complementa o Bazin para pagadoras que crescem. |
| [Índice de referência (benchmark)](#indice) | comparação | **adicionar** | Toda carteira por metodologia é comparada com um ETF de índice comprado no mesmo dia e valor. Se a metodologia perder do índice por 3 anos, você revisa. |

<a id="barsi"></a>
### Luiz Barsi (carteira previdenciária)

Comprar empresas de setores perenes que pagam dividendos com constância e reinvestir os dividendos por décadas.

Critérios que o script confere:
- Setor perene (BESST)
- Pagou dividendos em pelo menos 5 dos últimos anos
- Lucro em pelo menos 5 dos últimos anos
- Dividend yield de pelo menos 6% no preço atual

Perguntas que só você responde:
- A empresa existirá e venderá o mesmo serviço daqui a 20 anos?
- O dividendo vem do lucro recorrente ou de evento único?

**Quando vender:** Só se o fundamento quebrar (lucro e dividendo deixarem de existir de forma recorrente).

Fonte: Literatura pública sobre o método; confira com o material que você estudou.

<a id="bazin"></a>
### Décio Bazin (preço-teto)

Só comprar abaixo do preço-teto, que garante pelo menos 6% de dividendos sobre o preço pago, em empresas pouco endividadas.

Critérios que o script confere:
- Dividend yield médio de 3 a 5 anos de pelo menos 6%
- Dívida bruta / patrimônio líquido até 1
- Preço até o preço-teto (dividendo médio ÷ 6%)

Perguntas que só você responde:
- O dividendo médio inclui algum pagamento extraordinário que distorce a média?

**Quando vender:** Quando o dividend yield sobre o preço atual cair muito abaixo de 6% e houver opção melhor (regra sua).

Fonte: Livro 'Faça Fortuna com Ações, Antes que Seja Tarde', de Décio Bazin.

<a id="graham"></a>
### Benjamin Graham (investidor defensivo)

Comprar com margem de segurança abaixo do valor intrínseco, em empresas sólidas e com lucro estável.

Critérios que o script confere:
- Lucro por ação positivo
- Valor patrimonial por ação positivo
- Liquidez corrente de pelo menos 1,5
- Preço com pelo menos 25% de margem abaixo do valor de Graham (√(22,5 × LPA × VPA))

Perguntas que só você responde:
- O lucro dos últimos 10 anos foi positivo e estável?

**Quando vender:** Quando o preço passar do valor intrínseco (regra sua).

Fonte: Livro 'O Investidor Inteligente', de Benjamin Graham.

<a id="buffett"></a>
### Warren Buffett (qualidade a preço justo)

Empresas com vantagem competitiva durável, alta rentabilidade e pouca dívida, mantidas por muito tempo.

Critérios que o script confere:
- ROE de pelo menos 15%
- Margem líquida de pelo menos 10%
- Dívida líquida / EBITDA até 2

Perguntas que só você responde:
- Qual é a vantagem competitiva (marca, custo, rede, troca difícil)?
- Eu entendo como a empresa ganha dinheiro?
- A gestão aloca bem o capital e trata bem o minoritário?

**Quando vender:** Quando a vantagem competitiva acabar, não por queda de preço.

Fonte: Cartas anuais da Berkshire Hathaway aos acionistas (públicas).

<a id="sena"></a>
### Raul Sena (Investidor Sardinha)

Usar as perguntas do método do Raul Sena como ele usa e, numa segunda versão, estendidas com as perguntas das outras metodologias.

**Quando vender:** Preencha com a regra do método.

Fonte: Material do curso do Raul Sena que você tem. As perguntas não ficam no repositório: o material é pago. Você escreve as SUAS anotações em ~/financas/investimentos.toml.

<a id="formula_magica"></a>
### Fórmula Mágica (Joel Greenblatt)

Ordenar as empresas por retorno sobre o capital (alto é melhor) e por lucro operacional sobre o valor da empresa (barato é melhor) e somar as posições.

Critérios que o script confere:
- Posição no ranking de ROIC
- Posição no ranking de EV/EBIT

Perguntas que só você responde:
- Excluí bancos e seguradoras? (a fórmula não serve para eles)

**Quando vender:** Rebalanceamento anual da carteira pelo ranking.

Fonte: Livro 'O Mercado de Ações ao Seu Alcance', de Joel Greenblatt.

<a id="piotroski"></a>
### Piotroski F-Score

Nove testes simples de lucro, endividamento e eficiência; nota de 0 a 9. Serve como filtro para as outras metodologias.

Critérios que o script confere:
- Nota F-Score de pelo menos 7 (você calcula os 9 testes ou pega de fonte conferida)

**Quando vender:** Quando a nota cair para 3 ou menos (regra sua).

Fonte: Artigo 'Value Investing: The Use of Historical Financial Statement Information', de Joseph Piotroski (2000).

<a id="lynch"></a>
### Peter Lynch (PEG)

Comparar o P/L com o crescimento do lucro: PEG até 1 indica que o preço não está caro para o crescimento.

Critérios que o script confere:
- PEG (P/L ÷ crescimento anual do lucro em %) até 1

Perguntas que só você responde:
- O crescimento usado é sustentável ou foi um ano fora da curva?

**Quando vender:** Quando a história de crescimento mudar.

Fonte: Livro 'O Jeito Peter Lynch de Investir', de Peter Lynch.

<a id="gordon"></a>
### Modelo de Gordon (preço justo por dividendos)

Preço justo = próximo dividendo ÷ (retorno exigido − crescimento do dividendo). Complementa o Bazin para pagadoras que crescem.

Perguntas que só você responde:
- O crescimento usado é menor que o retorno exigido? (senão a fórmula não vale)

**Quando vender:** Quando o preço passar muito do preço justo (regra sua).

Fonte: Modelo de desconto de dividendos (Gordon, 1959), conteúdo das provas C-PRO e CNPI.

<a id="indice"></a>
### Índice de referência (benchmark)

Toda carteira por metodologia é comparada com um ETF de índice comprado no mesmo dia e valor. Se a metodologia perder do índice por 3 anos, você revisa.

**Quando vender:** —

Fonte: Prática de avaliação de desempenho de carteiras (conteúdo CGA/CFA).

## ARCA dentro de ações (ponto de partida; você ajusta em investimentos.toml)

| Grupo de metodologia | % alvo |
|---|---:|
| barsi_bazin | 50% |
| buffett | 20% |
| graham | 15% |
| formula_magica | 15% |

Limites: no máximo 10% da carteira numa empresa e 30% num setor; pelo menos 8 empresas.

## Como usar

```bash
python tools/investimentos/investimentos.py iniciar
python tools/investimentos/investimentos.py avaliar ~/financas/indicadores.csv
python tools/investimentos/investimentos.py aporte ~/financas/carteira.csv 800
python tools/investimentos/investimentos.py comparar ~/financas/carteiras.csv
```

Os modelos de CSV estão em tools/investimentos/modelos (tickers inventados). A política completa fica em ~/financas/politica-investimentos.md.
