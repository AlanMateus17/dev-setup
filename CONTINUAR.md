# CONTINUAR: contexto para começar qualquer conversa nova

Cole este arquivo (ou a saída de `python3 tools/sessao/contexto.py --inicio`) na primeira mensagem de uma conversa nova com o Claude ou outra IA. Atualize-o quando uma decisão grande mudar; as decisões do dia a dia vão para o ESTADO.md.

## Quem sou e como trabalhar comigo
- Alan Mateus, professor de informática (EMTI) em Barbacena-MG, também trabalho num restaurante, fundador da Grupo AMtech Digital. Tenho TDAH.
- Seja direto e honesto: diga quando algo não é possível.
- Comandos de uma linha, sempre dizendo onde rodar: PowerShell (PS C:\>) ou Ubuntu (alanmateus@...$). Eu já errei muito rodando comando no terminal errado.
- Senhas são digitadas à mão no terminal, nunca coladas. Nunca peça nem leia minhas senhas. Segredos ficam só no KeePassXC.
- Nada de dado de aluno em IA. Nada publicado ou enviado em meu nome sem aprovação. Não é assessoria financeira.
- Uma conversa = uma tarefa. No fim, me dê 5 linhas para o ESTADO.md.

## O setup (fonte da verdade)
- Repositório privado github.com/AlanMateus17/dev-setup (branch main, CI verde). No PC: ~/dev/dev-setup no Ubuntu (WSL) e C:\Users\alanmateus\dev-setup no Windows.
- Dados em data/*.json geram a documentação (não editar arquivo gerado). Números atuais: `python3 tools/sessao/contexto.py --resumo`.
- Acompanhamento (artefato com o progresso marcado): https://claude.ai/artifact/CJ27fg9sycvhqZ2s9GSbjd
- Portfólio (100 rendas com veredito): https://claude.ai/artifact/Mbj1yj6LRmUnf3SJLrTfaB
- Mapa: https://claude.ai/artifact/BTUyCQfojw6cngvR5W5oAB · Ecossistema: https://claude.ai/artifact/4Ze2J4Y1oKgAkjuQmbAAG1
- Pacote de contexto de um passo: `python3 ~/dev/dev-setup/tools/sessao/contexto.py --passo ID | clip.exe` (ou `--resumo`).

## Já feito no meu notebook
Fases 0, 3, 4 e 5 (diagnóstico, Windows, Linux/WSL com Docker e gh, GitHub e CI), backup inicial, Windows Update, 2FA do GitHub, KeePassXC instalado com os cofres copiados para o pendrive.

## Decisões principais
- Arsenal: 100 fontes de renda. Só 3 em "agora": mini-curso, sites com manutenção mensal, avaliação de IA. Próximas: AM Mentor, aulas em turma, revenda de notebooks, Fábrica para professores, Setup profissional, plano de negócios.
- Regras: hora mínima R$ 45 (a confirmar), teto de 7 h extras por semana (quinta 13h–16h30 negócio, sábado 9h30–12h30 produção), portão de 3 meses se pagando, corte abaixo da hora mínima por 2 meses.
- Marcas: AMtech Educação, Software, Digital, Campo (presencial por parceiros), Mídia, Economia, Patrimônio.
- IAs: Claude Pro principal; Google AI Plus no lugar do Google One; ChatGPT Go grátis pelo Nubank; DeepSeek/OpenRouter/Gemini API grátis só para rascunho sem dado sensível; Grok cortado; Claude Max só quando uma renda passar no portão.
- Custos: construir o que diferencia, código aberto para infraestrutura, pagar só o que vale mais que minhas horas (docs/custos.md).
- Ferramentas prontas no repositório: kit de sites (Hostinger IA, 26 prompts, conferir.py, contrato modelo), avaliador de templates, radar de revenda, organizadores (Downloads, CSV de senhas para o KeePassXC), bot do Telegram, financeiro local (~/financas), Fábrica de aulas (preencher .docx da escola), rotinas (resumo da manhã, manutenção), repositório padrão (pre-commit, gitleaks, Trivy, Semgrep), segredos via keepassxc-cli, teste de restauração, gateway LiteLLM com evals, calculadora de modelos (cabe.py), lucro por ferramenta (roi.py), vigia semanal no GitHub Actions.

## Pendências minhas (confira o ESTADO.md para a versão mais nova)
1. Senhas: passo kp-organizar e 2.4 (exportar do Chrome, importar no KeePassXC, apagar o CSV, copiar o cofre para o pendrive).
2. ActivityWatch (winget) e cadastro na avaliação de IA (passo ar-ia).
3. Confirmar R$ 45 e 7 h.
4. Templates do Rei dos Sites: comprei? onde estão? (o avaliador está pronto; repositório só privado).
5. Modelos .docx da escola e uma ementa para a Fábrica.
6. Hardware da mesa (passo 1.2).

## Próximo passo
Parar de adicionar áreas e executar até a primeira venda. Começar pelo passo kp-organizar (senhas).

## Como pedir ajuda numa conversa nova
1. Cole este arquivo e o pacote do passo: `python3 ~/dev/dev-setup/tools/sessao/contexto.py --passo ID | clip.exe`.
2. Peça ao Claude para abrir o repositório AlanMateus17/dev-setup (GitHub conectado) e marcar o passo no acompanhamento quando terminar.
3. Toda mudança no setup: editar data/*.json ou a ferramenta, rodar os geradores e testes, CHANGELOG, commit e push; o CI tem de ficar verde.
