# AGENTS.md — Aula 03 TOP. ESP. PROG.

Repositório: série de exercícios documentando interações de codificação com agentes de IA em português. Não é uma biblioteca/aplicação.

## Estrutura
- Os exercícios ficam em diretórios autocontidos: `ex1/`, `ex2/`, `ex3/`, `ex5/`, `ex6/`.
- `ex4` não possui diretório de código; suas observações estão registradas no `observacoes.md` da raiz.
- Sem pacote raiz, sem `requirements.txt`, sem CI.
- Principais arquivos de código por exercício:
  - `ex1/conversor_temp.py`, `ex1/converte.py`
  - `ex2/soma_csv.py`
  - `ex3/normalizar_nome.py`
  - `ex5/media_ponderada.py`
  - `ex6/converte.py`, `ex6/conversor_temp.py`
- Os entregáveis incluem tanto `.py` quanto notas de observação `.md` (`observacoes.md`, `ex*.md`). Não os apague.

## Testes (apenas ex6)
- `pytest ex6/tests/test_converte.py` (21 casos: `TestConverterValido` / `TestConverterErros`).
- Os testes podem conter inserções de `sys.path` específicas do ambiente; execute a partir da raiz do repositório ou defina `PYTHONPATH=.` para evitar falhas de importação. Adapte o caminho ao workspace atual se necessário.
- Nenhum outro exercício possui testes automatizados.

## Fluxo de trabalho / convenções
- Python 3. Arquivos e comentários em português conforme convenção do curso.
- `ex3`: deve tratar partículas minúsculas (`de`, `da`, `dos`, `e`, etc.) — `.title()` está incorreto.
- `ex6`: `converter()` retorna `None` + imprime erro; não levanta exceção. `main()` recebe `sys.argv`; a validação aplica `.strip().upper()` nas unidades.
- Se o usuário solicitar criação de testes para um novo exercício, siga os padrões estabelecidos em `ex6/tests/test_converte.py` (monkeypatch/`capsys`, contrato `return None + print`).

## Armadilhas a evitar pelo agente
- Não sobrescreva `ex*.md` / `observacoes.md`; eles registram o comportamento do agente para avaliação.
- Ao corrigir `ex6`, preserve o padrão `return None + print` (sem exceções, conforme notas).
- Se solicitado um único teste, direcione para `ex6/tests/test_converte.py`; outros exercícios não possuem infraestrutura de testes.
- Antes de referenciar qualquer diretório de exercício, verifique se ele existe no estado atual do workspace.

## Observações do exercício 7
Fechamento: O /init gerou o defeito Blind Reference (principal), que corrigi assim: substituí as referências a diretórios inexistentes (ex4/, ex7/) por uma listagem explícita dos diretórios realmente presentes no repositório, adicionei nota explicativa sobre o ex4 observacional, removi a instrução fantasma sobre ex7/tests/test_converte.py, e adicionei uma cláusula de verificação dinâmica para prevenir referências cegas futuras. Simultaneamente, corrigi a Init Fossilization (caminho absoluto hardcoded) e a Conflicting Instructions (duplicação contraditória ex6/ex7). 