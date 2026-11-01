# Repositório padrão AMtech

Copiado por `scripts/wsl/padronizar-repo.sh` (só cria o que falta, nunca sobrescreve).

- `.pre-commit-config.yaml`: higiene, segredos (gitleaks) e mensagem de commit no padrão Conventional Commits.
- `.github/workflows/qualidade.yml`: gitleaks, Trivy, Semgrep e testes em todo push.
- `.github/pull_request_template.md`: a Definition of Done.
- `docs/adr/`: decisões de arquitetura.
- `.editorconfig` e `CHANGELOG.md`.
