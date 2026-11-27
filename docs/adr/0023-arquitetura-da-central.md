# 0023 · Arquitetura da Central: uma API, allowlist única e nenhum argumento no texto do bash

- **Status:** aceita (v1 construída em 27/11/2026, versão 2.61.0)
- **Data:** 2026-11-27
- **Rever em:** 2027-01-20, junto com a ADR 0022

## Contexto

A emenda da [ADR 0022](0022-decisoes-de-25-11-2026.md) decidiu criar a Central para usar 100% do setup, com login, CSRF, allowlist,
confirmação e auditoria desde a v1, e usuários, permissões e `organizacao_id` no banco desde a v1. A varredura de 27/11 achou:

1. **Injeção pelo `justfile`.** 40 das 68 receitas colavam o argumento no texto do bash (`"{{texto}}"`). Passar argumentos "como lista"
   ao `just` não protege: o `just` cola o valor no texto antes de chamar o bash. Testado com o `just` 1.59:
   `just pedir 'x"; touch ARQUIVO; echo "'` criava o arquivo. O `set positional-arguments` já estava ligado; só 8 receitas usavam `"$@"`.
2. **Allowlists diferentes** (código do bot, plano da Central, nenhuma no terminal) iriam divergir.
3. A tabela `auditoria` do núcleo não tem migrações nem proteção contra alteração.

## Decisões

1. **Nenhum argumento no texto do bash.** As 40 receitas usam `"$1"`, `"$2"`, `"$@"` (e `${1:+--empresa "$1"}` no lugar do `if` do just).
   `tools/central/allowlist.py --check` (no `just check` e no CI) falha se qualquer receita voltar a usar `{{…}}` no corpo.
   O `aprovar` confere que o PR é um número antes do `gh`.
2. **`data/central.json` é a allowlist única**, com as 70 receitas e cinco níveis:
   - `automatico`: roda direto;
   - `avisa`: roda e avisa no Telegram;
   - `pede-ok`: só com aprovação, 30 min, uso único;
   - `so-terminal`: aparece, mas roda só no terminal;
   - `proibido`: não aparece.

   Cada argumento tem um padrão (regex inteira) ou é texto livre com limite, que vai como **um** argumento. Também há subcomandos e opções permitidos, e subcomandos ou opções que sobem o nível (ex.: `validar --restaurar` pede aprovação). O check falha com receita não classificada.
3. **A Central (`tools/central/`) é a única que executa** pela tela:
   - FastAPI, HTML gerado no servidor e JavaScript só de arquivo (a CSP proíbe script inline);
   - sem HTMX, para ter zero dependência de front;
   - só `127.0.0.1:8700`.

   O executor chama `just --justfile … <receita> <args>` com `shell=False`, ambiente mínimo (sem token do Telegram, chaves de API ou `GH_TOKEN`), tempo limite e saída ao vivo por SSE. O `pedir` chama `fila.adicionar()` direto, sem passar pelo bash.
4. **Banco:** tabelas `central_*` dentro do `nucleo.db`, que já está no backup, com migrações numeradas (`central_migracoes`):
   - organizações, papéis (`dono`, `leitor`, `bot`), usuários com `organizacao_id`, sessões, execuções e aprovações;
   - `central_auditoria` com corrente de hash, conferida por `central.py verificar` e na tela Auditoria.

   A tabela `auditoria` antiga do núcleo continua como está (o `nucleo.py` a usa); juntar as duas fica para quando o bot virar cliente da API.
5. **Login:**
   - senha com scrypt (biblioteca padrão), mínimo 12 caracteres, bloqueio de 15 min depois de 5 erros;
   - sessão de 12 h ociosa e 7 dias no máximo; trocar a senha derruba as sessões;
   - cookie `HttpOnly` + `SameSite=Strict`, CSRF em todo `POST`;
   - Host e Origin conferidos;
   - `Referrer-Policy: same-origin` (com `no-referrer` o Chrome manda `Origin: null` e o próprio login falhava, achado no teste com navegador).
6. **Aprovação:** um `UPDATE … WHERE estado = 'pendente' AND expira >= agora` garante uso único. A allowlist é conferida de novo na hora de aprovar. `aprovar N` (merge) exige digitar o número do PR.

## Consequências

- Uma regra de segurança vale para a tela e para o terminal: o terminal também não tem mais injeção por argumento.
- O bot do Telegram ainda chama scripts direto. Torná-lo cliente da API, com botões ✅, é a fase seguinte (C4 do plano).
- Celular: `tailscale serve` no Windows apontando para `127.0.0.1:8700` e o nome da máquina em `AMTECH_CENTRAL_HOSTS`. Fica para depois de usar a v1 no notebook.
- Receitas com formulário próprio por fazer (`diag`, `erro`, `atrito`, `motor-custo`) ficam como `so-terminal` até terem campos.

## Alternativas descartadas

- **Allowlist só no código da Central:** o bot e a Central divergiriam, e o `just check` não teria como conferir.
- **OliveTin ou Homepage:** descartados na ADR 0022.
- **Agente separado com shell (estilo OpenClaw):** seria outra porta para o computador, sem allowlist.
- **Repositório novo para a Central:** seria mais uma fonte da verdade (avaliação, §1).
