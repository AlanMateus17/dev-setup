# O método do Professor

Este documento junta duas fontes:

- **A ciência cognitiva**, com as técnicas de aprendizagem que têm mais evidência.
- **O que você já tinha decidido** em conversas anteriores: o `metodo-de-estudo.md` do vault (out/2026), a arquitetura do livro Lógica e Máquina (set/2026), o plano de inglês, a organização para TDAH e a grade 20/80.

Cada linha diz de onde veio e onde aparece no Professor.

## 1. As técnicas (o porquê)

| Técnica | O que é, em uma frase | Origem | Onde está no Professor |
|---|---|---|---|
| Prática de recuperação | Tirar da cabeça fixa mais do que reler | Ciência (Roediger e Karpicke) · seu método, "feche e reconstrua" | Perguntas diagnósticas, perguntas de recuperação, prova sem consulta |
| Repetição espaçada | Rever pouco antes de esquecer, com intervalos crescentes | Ebbinghaus · seu método, item 4: "vale para conceito técnico, não só idioma" | Revisões em 1, 3, 7, 21, 60 e 120 dias; cartões no Anki |
| Intercalação | Alternar assuntos retém mais do que estudar um em bloco | Rohrer e Taylor · seu método, item 1 | `just professor hoje` mistura ofício, setup e finanças no mesmo dia |
| Dificuldade desejável | O que custa na hora (testar-se, espaçar) é o que fica | Bjork · seu método, item 2 | Prova sem consulta; abaixo de 80, a revisão volta para o dia seguinte |
| Exemplos resolvidos com retirada de apoio | Ver resolvido, depois resolver com lacunas, depois sozinho | Ciência (Sweller, carga cognitiva) · padrão do livro (3 a 5 exemplos embutidos) | Exemplo resolvido → Agora você tenta → exercícios |
| Prática deliberada | Treinar o que você ainda não domina, com retorno | Ericsson · seu método, item 5 | A correção lista os pontos fracos e o `hoje` mostra onde praticar |
| Feynman (ensinar) | Explicar sem jargão mostra o buraco | Seu método, item 3 · você é professor | Passo 3 do protocolo, ficha dupla, nível 4 "ensinou" |
| Profundidade calibrada | Decidir antes se o assunto pede "usar" ou "a fundo" | Seu método, item 7 | Campo `profundidade` em cada módulo; a aula se ajusta |
| Velocidade calibrada com dado real | Estimativa é hipótese; o tempo medido corrige | Seu método, item 6 | `just professor fechar ID MINUTOS` guarda o tempo real contra o estimado |
| 20/80 e fundamentos antes de framework | Os 20% do conteúdo que resolvem 80% dos casos vêm primeiro | Sua grade 20/80 (inspirada no Akita) | Regra da aula: o essencial vem primeiro e marcado |
| Motivação antes da definição | A ordem de ensinar não é a ordem de estudar | Seu método, seção C | A aula abre por "Por que isso importa" |

## 2. Os seus formatos (o como)

**Protocolo de fim de bloco** (do seu `metodo-de-estudo.md`). Ao fim de todo bloco: `just professor fechar ID MINUTOS`.

1. Feche o material.
2. Reconstrua de cabeça o que o bloco resolveu e por quê.
3. Ensine em 3 a 5 frases sem jargão.
4. Faça de 1 a 3 cartões de conceito.
5. Anote o tempo real.
6. Só então avance.

**A mesma ideia de 4 jeitos** (o seu loop de 5 etapas, sem a etapa da ficha, que já é o protocolo): a ideia pura → em C# → em TypeScript → no sistema real. Só entra quando faz sentido. Exemplo do seu vault: o "E" lógico vira a tabela-verdade, depois `&&` em C#, depois `&&` em TS, depois o `if (produto.Estoque > 0 && cliente.Ativo)` do AM Kaixara.

**Ficha dupla e registro de entrevista** (produção didática simultânea). O mesmo estudo gera dois materiais:

- **A ficha dupla:** ideia, código, por que importa e conexão com o próximo tópico. Vira material de aula.
- **O registro de entrevista:** contexto, decisão com a alternativa descartada, resultado com número e a pergunta que ele responde. Vira resposta pronta para vaga.

O `fechar` cria o modelo dos dois no Obsidian.

**Exercícios em 4 níveis** (arquitetura do livro Lógica e Máquina):

- **N1, reconhecimento**
- **N2, aplicação direta**
- **N3, aplicação combinada e "encontre o erro"**
- **N4, desafio ou mini-projeto real**

O gabarito é comentado, explicando o porquê de cada resposta.

**Os quadros das suas apostilas:** "Pare e responda", "Erro comum" e "Agora você tenta" aparecem dentro da aula, do mesmo jeito que você usa com os alunos.

**Uma porta só, por causa do TDAH** (da organização do vault): você nunca precisa decidir o que abrir. `just professor hoje` é a porta. Cada bloco tem 25 minutos e um objetivo só.

## 3. O ciclo de um módulo

```
hoje → aula (3 blocos de 25 min) → fechar (protocolo + ficha) → prática no setup → praticei
     → prova sem consulta → corrigir → (≥ 80: nível 3 e revisão espaçada | < 80: revisão amanhã + pontos fracos)
     → ensinar (post, aula, vídeo) → ensinei (nível 4)
```

## 4. O que ficou de fora, de propósito

- **Matemática pura e os exercícios no volume do livro** (até 61 por capítulo). Isso é a obra do livro, não a aula do setup. O Professor usa de 3 a 4 exercícios por nível.
- **Conteúdo de curso pago** (Alura, Rocketseat, Udemy, Finclass). Continua sendo para você assistir, nunca para a IA reproduzir.
- **Vídeos e podcast do Akita como estudo.** O seu plano antigo dizia que eles "não contam como estudo", porque são passivos. A Escola Akita mudou isso: o que conta são as regras e notas que saem deles, não o tempo assistindo.

## 5. Uma divergência para você decidir

O plano do vault (out/2026) mandava **calibrar em 2 h por dia e tratar as 4 h como bônus**. O plano do eixo (nov/2026) foi montado com 4 h por dia. O Professor funciona com os dois. Se a semana real fechar perto das 2 h, o critério de cada trimestre precisa ser revisto em vez de virar dívida de atraso.
