# CLI de Notas

Um sistema de linha de comando para gerenciamento de notas de alunos em uma disciplina.

## Funcionalidades

- Cadastrar alunos (matrícula e nome)
- Lançar 3 avaliações por aluno
- Calcular média ponderada (pesos 3, 3, 4)
- Classificar alunos: Média >= 7 → Aprovado, Média >= 5 → Exame, Média < 5 → Reprovado
- Listar turma em tabela
- Persistência em CSV local

## Estrutura do projeto

```
notas/
  __init__.py   - exports das classes
  aluno.py      - classe Aluno (matrícula, nome, notas)
  lancamento.py - lançamento de 3 notas por aluno
  classificao.py - classificação (Aprovado/Exame/Reprovado)
  storage.py    - leitura/escrita CSV
  cli.py        - interface de menu
tests/          - testes pytest
__main__.py     - entrada para python -m notas
```

## Uso completo

### Via linha de comando

```bash
python3 -m notas
```

Menu interativo:
1. **Cadastrar aluno** - digite matrícula e nome
2. **Lançar avaliações** - selecione um aluno e digite as 3 notas
3. **Listar turma** - vê a tabela com matrícula, notas, média e status
4. **Sair** - encerra o programa

### Via código Python

```python
from notas.aluno import Aluno
from notas.lancamento import LancamentoNotas
from notas.classificacao import classificar
from notas.storage import Storage

# Criar aluno
a = Aluno("2024001", "João Silva")

# Lançar notas
LancamentoNotas(a).lançar(7.0, 8.0, 9.0)

# Calcula média ponderada
media = a.media_ponderada()  # 8.0

# Classificar
status = classificar(a)  # "Aprovado"

# Persistir em CSV
Storage.salvar([a], "notas.csv")

# Carregar de CSV
alunos = Storage.carregar("notas.csv")
```

## Testes

```bash
pytest -q  # 13 testes passando
```
