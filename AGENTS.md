# AGENTS.md

## Projeto

CLI de notas para uma disciplina: cadastra alunos, lança 3 avaliações por aluno,
calcula média ponderada (pesos 3, 3, 4) e classifica em Aprovado/Exame/Reprovado.
Persistência em CSV local — sem banco de dados, sem rede, sem serviço externo.

## Stack

- Python 3.12+
- `pytest` para testes (única dependência — nada de terceiros no código de produção)
- Biblioteca padrão do Python para tudo o mais (`csv`, `os`, `sys`)

## Estrutura do projeto

Um módulo por responsabilidade, dentro do pacote `notas/`:

- `aluno.py` — entidade `Aluno` (dados + cálculo de média ponderada)
- `lancamento.py` — lançamento das 3 notas de um aluno
- `classificacao.py` — regra de classificação (Aprovado/Exame/Reprovado)
- `storage.py` — persistência em CSV (salvar/carregar)
- `cli.py` — menu interativo, orquestra os módulos acima
- `__main__.py` — ponto de entrada (`python3 -m notas`)

Testes em `tests/`, um arquivo por módulo, espelhando essa mesma divisão.

## Convenções

- Um módulo por responsabilidade — não junte lógica de domínio, persistência e
  interface no mesmo arquivo.
- Nomes de variáveis, mensagens ao usuário e commits em português.
- Toda função pública tem docstring e teste correspondente em `tests/`.
- Use type hints nas assinaturas públicas (como já é feito em `aluno.py`,
  `storage.py`, `lancamento.py`).

## Comandos

- Testar: `pytest -q`
- Rodar: `python3 -m notas` (o comando `python` sem sufixo não existe neste
  ambiente a menos que `python-is-python3` esteja instalado — use `python3`)

## Arquitetura — invariantes que não são óbvios só lendo o código

Estes pontos já causaram bugs reais neste projeto. Releia antes de mexer em
`storage.py` ou no fluxo de `menu()`:

- `Storage.salvar` **sobrescreve o arquivo inteiro** a cada chamada (modo
  `"w"`, não `"a"`). Ele é chamado a cada cadastro, lançamento de notas e
  remoção — nunca volte para modo append, isso reintroduz duplicação de linhas.
- `Storage.salvar` **ignora silenciosamente** (não lança erro) alunos que ainda
  não têm as 3 notas lançadas — eles só entram no CSV depois de completos.
  Isso é proposital: `Aluno.media_ponderada()` lança `ValueError` se
  `len(notas) != 3`, então sempre confira essa condição antes de calcular
  média ou status para um aluno.
- `menu()` chama `Storage.carregar` **no início da sessão** para repopular a
  lista de alunos a partir do CSV existente. Sem isso, cada execução começa do
  zero e o próximo save apaga o que já estava salvo. Qualquer mudança na
  inicialização do menu precisa preservar esse carregamento.

## Ambiente

- `.env` contém `OPENAI_BASE_URL`, `OPENAI_API_KEY` e `MODEL` — nunca deve ser
  commitado (já está no `.gitignore`).
- `opencode.json` define o modelo padrão via OpenRouter
  (`openrouter/<identificador-do-modelo>`). Atualize só se for trocar de modelo.

## Antes de considerar uma tarefa concluída

- Rodar `pytest -q` e confirmar que passa.
- Rodar `python3 -m notas` manualmente pelo menos uma vez, cobrindo o fluxo
  que foi alterado, para validar o comportamento interativo (os testes não
  cobrem o menu em si).
- Conferir `git status`/`git diff` antes de commitar — nada de `.env` ou
  `notas.csv` staged.

## Nunca

- Não versionar dados de alunos reais (nem em `notas.csv`, que está no
  `.gitignore`).
- Não commitar o `.env`.
- Não instalar dependência nova sem perguntar antes.
- Não trocar `Storage.salvar` de volta para modo append sem entender por que
  foi mudado (ver seção "Arquitetura" acima).
