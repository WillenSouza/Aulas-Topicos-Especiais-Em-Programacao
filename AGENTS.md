# AGENTS.md

## Environment

- **API keys**: `.env` contains `OPENAI_BASE_URL`, `OPENAI_API_KEY`, `MODEL`. Do not commit `.env` (it is gitignored).
- **Model config**: `opencode.json` sets the default model via `openrouter/<identificador-do-modelo>`. Update only if changing the model.

## OpenCode setup

- Run OpenCode with: `opencode` (or whatever your shell alias/wrapper is).
- The repo has no build/test/lint commands (no package.json, no Makefile). Any scripts must be defined per-package or added manually.

## Common pitfalls

- Do not attempt to `npm install` or `pip install` unless a package manager config is added to the repo.
- The `.env` file must not be copied or committed — it is listed in `.gitignore`.

## Convenções

- Um módulo por responsabilidade, dentro do pacote `notas/`.
- Nomes de variáveis e mensagens em português.
- Toda função pública tem docstring e teste.

## Comandos

- Testar: `pytest -q`
- Rodar: `python -m notas`

## Nunca

- Não versionar dados de alunos reais.
- Não instalar dependência sem me perguntar antes.
