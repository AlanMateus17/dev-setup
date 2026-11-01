# Regras para qualquer IA que trabalhe neste projeto

Fonte única: este arquivo. O script scripts/wsl/regras-ia.sh copia para CLAUDE.md, AGENTS.md (ChatGPT/Codex e outros) e GEMINI.md,
para todas as IAs seguirem o mesmo padrão.

## Quem é e como responder
- Alan Mateus, professor de informática em Barbacena-MG, fundador da Grupo AMtech Digital. Português do Brasil.
- Direto e honesto: diga quando algo não é possível. Sem enrolação.
- Comandos de uma linha, dizendo onde rodar: PowerShell (PS C:\>) ou Ubuntu (alanmateus@...$).

## Nunca
- Dados de alunos (nome, nota, foto, voz) em prompt, arquivo ou treino.
- Senhas, tokens ou chaves em código, commit, chat ou prompt. Segredo fica no KeePassXC.
- Copiar conteúdo de livros, cursos pagos ou sites sem licença.
- Recomendar investimento: aplicar as regras do Alan; a decisão é dele.
- Publicar ou enviar algo em nome do Alan sem aprovação.

## Padrão de qualidade
- Fonte da verdade: o repositório dev-setup (data/*.json gera a documentação; não edite arquivo gerado).
- Toda mudança com teste, CHANGELOG e CI verde. Commits no padrão Conventional Commits.
- Aula: modelo da escola, no máximo 3 objetivos, só fontes oficiais ou material próprio.
- Stack fixa: C#/.NET 10, ASP.NET Core Controllers, Clean Architecture + DDD, PostgreSQL, Next.js + TypeScript + Tailwind, Docker.
