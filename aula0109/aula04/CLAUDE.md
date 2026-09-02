# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

Repositório de aulas práticas (Benevid). Cada `aulaNN/` é uma atividade independente, com seu próprio venv e sua própria configuração de cliente — não existe build nem dependência compartilhada na raiz.

`AGENTS.md` (raiz) guarda o domínio do diário: as quatro ferramentas, a regra de cálculo e o invariante de que `servidor.py` e o recurso `diario://regras` descrevem as mesmas regras. Leia antes de mexer em `_media` ou `_situacao`.

## Comandos

Tudo roda de dentro de `aula04/`, pelo interpretador do venv (nunca o `python` do sistema):

```bash
.venv/bin/python servidor.py          # sobe o servidor em stdio; fica bloqueado esperando o cliente
```

`@mcp.tool()` devolve a própria função, então dá para exercitar uma ferramenta isolada sem subir o protocolo — é como esta atividade foi validada:

```bash
.venv/bin/python -c "import servidor; print(servidor.resumo_turma())"
.venv/bin/python -c "import servidor; print(servidor.lancar_nota('2024001', 1, 8.5))"   # escreve no CSV
```

Não há pytest, linter ou formatador instalados, nem `requirements.txt`/`pyproject.toml`: as dependências foram instaladas direto no venv. Para acrescentar uma, `.venv/bin/pip install <pacote>`.

## Arquitetura

O estado inteiro vive em `dados/turma.csv`, relido e regravado a cada chamada — não há cache nem trava, a última escrita vence. Os helpers privados (`_ler`, `_gravar`, `_media`, `_situacao`, `_buscar`) são o núcleo; as quatro ferramentas são camadas de formatação em cima deles. Duas convenções que valem para qualquer ferramenta nova:

- o retorno é `str` já formatada para leitura humana (tabela, boletim, histograma), nunca JSON;
- erro de entrada é `ToolError` (`mcp.server.mcpserver.exceptions`), que o SDK converte em resultado com `is_error`; não deixe `ValueError` cru subir.

## SDK: mcp 2.1.1, não FastMCP

O venv tem a linha 2.x do SDK, onde `mcp.server.fastmcp` foi removido — restou um stub que levanta `ModuleNotFoundError`. A classe é `MCPServer`, importada de `mcp.server`. A maior parte dos tutoriais e exemplos de MCP em circulação ainda usa `FastMCP`; não copie de lá sem traduzir. `mcp.run()` sem argumento é stdio; os transportes aceitos são `stdio`, `sse` e `streamable-http`.

## Cliente

O cliente da atividade é o **OpenCode**, não o Claude Code. `aula04/opencode.json` registra o `diario` como MCP local com `cwd` absoluto e hardcoded — se o repositório mudar de lugar, esse caminho quebra.

## Arquivos de agente e de entrega

- `.claude/agents/auditor-agents-md.md` — subagente que audita o `AGENTS.md` contra seis defeitos de configuração e devolve no máximo 15 linhas, sem editar nada.
- `aula04/.claude/skills/relatorio-de-atividade/` — skill que escreve `relatorio.md`. Hoje o arquivo `SKILL.md` está em uma única linha, com o frontmatter YAML colado (`--name:` em vez de `---`), e por isso não carrega.
- `aula04/relatorio.md` — a entrega da atividade; termina com perguntas em aberto para o usuário, que ainda não foram respondidas.
- `aula04/medicao.md` — transcrição bruta de sessão de agente (~1700 linhas), material de medição da disciplina. Não é documentação; não leia inteiro.

O repositório em `aula04/` está inicializado mas **sem nenhum commit** — todos os arquivos aparecem como não rastreados. A skill `relatorio-de-atividade` começa por `git log`/`git diff`, então hoje não encontra histórico algum.
