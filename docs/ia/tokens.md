# Economia de tokens: produzir mais, gastar menos

[← Arquitetura de IA](README.md)

Token é o que o Claude cobra: cada palavra que entra (o que você manda) e que sai (o que ele responde) conta. Produzir mais gastando menos não é escrever menos; é **fazer o Claude trabalhar só no que é difícil** e deixar o resto com o seu computador, que é de graça.

## As cinco regras

1. **Peça um script, não o resultado.** O erro que mais gasta token é pedir ao Claude para "desenhar" ou "listar tudo". Peça o programa que faz isso. Um script de 40 linhas custa pouco token e gera a planta, as 500 linhas da tabela ou as 50 questões de graça, no seu PC, quantas vezes você quiser.
2. **Uma conversa por tarefa.** Conversa longa reenvia todo o histórico a cada mensagem: a quinta pergunta paga pelas quatro anteriores. Comece nova com o pacote de contexto (`contexto.py --inicio`), que é curto.
3. **A IA certa para cada tarefa.** O Claude é o caro. Rascunho, resumo, transcrição e tradução vão para o modelo local (Ollama) ou grátis. Pergunte ao roteador: `tools/ia/tokens.py rota "sua tarefa"`.
4. **Busca nas suas notas (RAG), não colar.** Em vez de colar um documento inteiro toda vez, o setup busca só o trecho que importa. Menos entra, menos custa.
5. **Deixe o resultado pronto antes de pedir revisão.** Mande o Claude revisar o que já está quase pronto (gasta pouco), não construir do zero numa conversa de ida e volta (gasta muito).

## Exemplo: a planta baixa de uma casa

**Jeito caro (não faça):** "Claude, desenhe a planta baixa da minha casa com sala, dois quartos, cozinha e banheiro, com todas as medidas." Ele responde com páginas de texto ou SVG, você pede ajuste, ele redesenha tudo de novo. Cada rodada paga o desenho inteiro.

**Jeito do setup (barato e melhor):**

1. Você fala (ou escreve): *"Jarvis, casa térrea, 7 por 10 metros: sala, 2 quartos, cozinha e banheiro."*
2. O Claude Code escreve **um script de FreeCAD ou Bonsai** com as paredes, portas e janelas como parâmetros (largura, altura, posição). Isso é pouco token.
3. O script roda no seu PC e gera o modelo em IFC. Zero token.
4. O `ifc_resumo.py` confere pavimentos, cômodos e áreas. Zero token.
5. Você diz *"o quarto 2 está pequeno, aumenta meio metro"*. O Claude muda **um número** no script, não a planta inteira. Quase zero token.

A planta fica melhor porque é paramétrica: muda um número e o desenho inteiro se ajusta, com as medidas certas. E "o mais perfeito possível" vem de rodar o script e conferir, não de o Claude acertar tudo de primeira no escuro.

> Lembre: uma planta para **construir** precisa de engenheiro ou arquiteto registrado (CREA/CAU). O que o setup faz é o estudo e o modelo; quem assina é o profissional.

## Qual parte o setup toma conta sozinho

| Você faz | O setup faz |
|---|---|
| Fala ou escreve o que quer | Ouve (Whisper local) e entende |
| — | Escolhe a IA certa pela regra do roteador |
| — | Roda os scripts, gera os arquivos, confere com os verificadores |
| Confirma o que muda algo (publicar, comprar, apagar) | Faz o resto e registra |
| Revisa o resultado na tela | Mostra pronto para aprovar |

O que **não** dá para largar 100% na mão do setup: a aprovação final. Um assistente que faz tudo sem conferir também faz besteira sem conferir. O setup foi montado para você só aprovar, não para você não olhar.

## Ferramentas

```bash
python3 ~/dev/dev-setup/tools/ia/tokens.py rota "revisar a arquitetura do AM Kaixara"   # qual IA usar
python3 ~/dev/dev-setup/tools/ia/tokens.py tamanho aula.md                               # estima os tokens
python3 ~/dev/dev-setup/tools/ia/cabe.py 32                                              # cabe um modelo local?
```

O teto de gasto real fica no gateway LiteLLM (`infra/ia`) e no ai-usagebar; a tabela de rotas por tarefa está em [recursos.md](../recursos.md) e em [custos.md](../custos.md). A regra nº 1 — pedir o script, não o resultado — vale para todo agente do setup e está nas regras da IA.
