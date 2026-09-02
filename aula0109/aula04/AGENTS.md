# AGENTS.md

Repositório de aulas práticas (Benevid). Cada `aulaNN/` é uma atividade independente, com seu próprio ambiente e configuração.

## aula04 — servidor MCP do diário

`aula04/servidor.py` expõe o diário de notas de uma turma via MCP. Os dados ficam em `aula04/dados/turma.csv` (colunas: `matricula,nome,n1,n2,n3`), lidos e gravados a cada chamada.

Ferramentas: `listar_alunos`, `boletim(matricula)`, `lancar_nota(matricula, avaliacao, valor)`, `resumo_turma`. Recurso: `diario://regras`.

Regra de cálculo: média ponderada N1=3, N2=3, N3=4. `aprovado` ≥ 7.0 · `exame` ≥ 5.0 · `reprovado` < 5.0 · `incompleto` quando falta alguma nota. Ao mexer no cálculo ou na situação, mantenha `servidor.py` e o recurso `diario://regras` em sincronia — os dois descrevem as mesmas regras.

Rodar: `cd aula04 && .venv/bin/python servidor.py` (registrado como MCP local em `aula04/opencode.json`).
