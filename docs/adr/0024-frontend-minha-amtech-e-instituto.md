# 0024 · Frontend: Minha AMtech (painel do dono) e Instituto AMS (portal do aluno), com o Aura como fonte única

- **Status:** proposta (27/11/2026, para o Alan decidir)
- **Data:** 2026-11-27
- **Rever em:** depois da fase A2 (ver `docs/central/frontend.md`, seção 8)

## Contexto

A Central v1 (ADR 0023) funciona, mas foi desenhada como ferramenta de desenvolvedor: receitas, níveis, auditoria. O Alan quer usá-la
como usuário final, para delegar, estudar, ensinar e acompanhar as rendas, e quer que os alunos estudem por ela.

Três fatos do repositório pesam aqui:

1. **A Central executa comandos no notebook.** Ela não pode ter caminho vindo de alunos, que no EMTI são menores.
2. **O catálogo já separa o produto de ensino.** A Plataforma do Instituto (`ed-instituto`) e o AM Mentor (`ed-ammentor`) fazem parte da suíte AM Escola (`data/softwares.json`).
3. **Já existe um design system, o Aura.** Ele está em `04-documentos-transversais/rnf-transversais-design-tema.md`, no vault. A RNFT-D03 diz que painel administrativo usa sempre a paleta Aura e que só superfície pública usa a cor da marca. A RNFT-D06 proíbe cor fora do arquivo de tokens.

## Decisões

1. **Duas superfícies.**
   - **Minha AMtech:** a Central, com uma nova casca de usuário final, local e com paleta Aura fixa.
   - **Instituto AMS:** portal do aluno, outro repositório, na internet, com a cor da marca do Instituto.

   O Instituto nunca chama a Central. Conteúdo vai da Central para o Instituto só por PR em rascunho com o seu ok.
2. **Fonte única dos tokens:** `data/aura.json` gera `tools/central/static/aura.css` e o tema do Instituto. Um `--check` no `just check` barra cor fora dos tokens.
3. **Linguagem de usuário na Minha AMtech:**
   - 6 destinos no notebook (Início, Delegar, Estudar, Ensinar, Rendas, Sistemas) e os 5 primeiros na barra do celular;
   - a caixa "Para você decidir";
   - as telas da v1 atrás de "Modo técnico".
4. **Mesma stack da ADR 0023 na Minha AMtech** (sem build). O Instituto segue a ADR 0017 e começa pelo modelo Astro que já existe.
5. **Devagar:** uma fase por PR e por versão, com 2 semanas de uso real entre as fases da Minha AMtech.

## Consequências

- O que já foi construído na 2.61.0 (allowlist, aprovações, auditoria, pedido em português, telas de dados) vira o motor das telas novas. Nada é reescrito.
- O Instituto só começa depois das decisões da fase I0: escola, responsáveis, hospedagem e primeiro público.
- Os painéis HTML gerados que a Minha AMtech cobrir são aposentados, um por vez.

## Alternativas descartadas

- **Alunos entrando na Central:** abriria caminho até um computador que executa comandos.
- **Um design novo:** contrariaria a RNFT-D01 e a RNFT-D06. O Aura já existe e tem os valores exatos.
- **Next.js na Minha AMtech agora:** seria uma segunda base de código para uma ferramenta de um usuário. A ADR 0023 manteve sem build.
