<!-- Escrito à mão. Plano e ferramenta das fontes de estudo (v2.41). -->

# Fontes de estudo: estudar pelo conteúdo original, sem alucinação

[← Método do Professor](metodo.md)

**O problema:** um aluno não tem como saber se um texto escrito por IA está certo. **A resposta:** o que você estuda é o texto original (documentação oficial, livro, aula), guardado num acervo privado. O guia de estudo só mostra trechos que **o código** encontrou, letra por letra, na fonte. A IA pode sugerir qual trecho explica um termo, mas não consegue inventar um trecho.

## Onde fica cada coisa

| Pasta (fora do Git) | O que tem |
|---|---|
| `~/AMtech/estudo/entrada/` | Onde você joga PDF, EPUB, DOCX, áudio, vídeo ou notas. Não confunda com `~/AMtech/entrada/`, que é do pipeline de conteúdo. |
| `~/AMtech/estudo/fontes/<tipo>/` | Os originais, com o hash no nome |
| `~/AMtech/estudo/corpus/` | Cada fonte em Markdown (transcrição com `[t=mm:ss]`) |
| `~/AMtech/estudo/docs-oficiais/<id>@<versão>/` | Documentações oficiais clonadas por Git, só a pasta da documentação |
| `~/AMtech/estudo/manifesto.jsonl` | De onde veio cada fonte, como foi obtida, licença, versão, commit e hash |

Tudo isso entra no backup restic, que é criptografado. **Nada disso entra em repositório:** `just fontes conferir` roda no `just check` e falha se aparecer arquivo de fonte, livro digital ou PDF fora das pastas de documentos gerados.

## Comandos (Ubuntu, em `~/dev/dev-setup`)

```bash
just fontes docs                          # as documentações cadastradas em data/fontes.json e quais você já baixou
just fontes baixar typescript-handbook    # clona a documentação na versão cadastrada e registra o commit
just fontes entrada --licenca comprado-uso-pessoal   # guarda, registra e converte o que está na entrada
just fontes buscar "union type"           # procura no corpus e nas documentações
just fontes citar ARQUIVO "trecho"        # OK com a linha (e o minuto) ou RECUSADO se o trecho não existir
```

## As 5 camadas e o estado de cada uma

| Camada | O que faz | Estado (21/11/2026) |
|---|---|---|
| 1. Fontes | Originais privados + manifesto | **Pronto** (`entrada`, `manifesto.jsonl`) |
| 2. Conversão | Sem IA que escreve: Docling (PDF/DOCX/PPTX), Pandoc (EPUB/HTML/ODT), WhisperX (áudio e vídeo com o minuto de cada fala); PDF de fora passa antes pelo Dangerzone | **Pronto, se a ferramenta estiver instalada.** Sem ela, o arquivo fica guardado como "pendente" |
| 3. Busca | `rg` no corpus e nas documentações | **Pronto** (`buscar`) |
| 4. Nota com citação | Toda frase do guia com `[fonte linha · t=mm:ss]`; `citar` recusa trecho que não existe | **Conferência pronta** (`citar`). Falta o gerador do guia por termo e por assunto |
| 5. Você | Diagnóstico, blocos, ficha de cabeça, `just professor nota` | **Pronto** (Professor v2.40) |

## O que ainda falta construir

1. **Guia privado no Obsidian** (`~/AMtech/estudo/guia/`): página por assunto e por termo, com os trechos literais conferidos, as suas notas, o "onde você vai usar" (o grafo do MAPA e a busca nos seus repositórios) e os seus erros sobre aquilo.
2. **Modo exercício:** o enunciado + tudo o que é preciso dominar para resolvê-lo + o gabarito oficial depois da tentativa.
3. **Verificador de frases:** cada frase de uma nota é conferida contra o trecho citado por modelos pequenos de inferência (HHEM e MiniCheck), rodando localmente. Medir a qualidade em português antes de confiar.
4. **Validação das suas notas para os livros:** LanguageTool e Vale (ortografia e estilo), links conferidos (lychee), contas no SymPy, código executado, comparação com o corpus para não copiar sem querer, leitores beta.
5. **Completude:** cruzar o MAPA com o CS2023 (ACM/IEEE), o SWEBOK v4, o roadmap.sh, as ementas da faculdade e vagas reais.

## Decisões que são suas

- **Trechos de livro podem ir para IA na nuvem?** A regra atual da Biblioteca diz que não. Com "só local", a seleção de trechos usa o Ollama.
- **Licença de cada fonte:** livro comprado e material da faculdade só para uso pessoal, nunca publicados. Fontes abertas (documentação oficial, OpenStax, Pro Git) respeitam a licença delas: a do Pro Git e a dos livros do OpenStax são não comerciais.
