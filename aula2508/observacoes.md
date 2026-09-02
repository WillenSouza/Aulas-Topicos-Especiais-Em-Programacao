# Observações — Aula 03
Modelo usado: Nemotron 3.5 Lightning (free)

### Ex1: o agente decidiu por mim: 

NO PROMPT SIMPLIFICADO

 - linguagem: python
 - quantas conversões poderiam ser feitas 
 - quais as temperaturas disponíveis
 - como seria a escolha das temperaturas / interface de uso
 - ao colocar valores null ele retorna valor inválido, se a opção null ele também retorna erro, mas somente depois de permitir digitar a temperatura
 - o formato de saída é uma igualdade da temperaturas convertidas com suas unidades de medida

NO PROMPT ESTRUTURADO

 - mensagem de erro para quando há 0 absoluto
 - mensagem de erro para unidades desconhecidas

### Ex2: com o motivo, ele também evitou:

O PROMPT 1: 
- Criou 2 arquivos csv distintos onde cada um continha exemplos de arquivos csv. 
-Quanto ao código ele cumpriu as limitações mas adicionou funcionalidades que não foram requisitadas como sugestão de melhoria, usou apenas bibliotecas padrões e não de sugestões de melhorias.

O PROMPT 2:
- Construiu todas as funcionalidades que foram requisitadas.
- Apenas modificou algumas funções que haviam sido geradas pelo prompt 1. 
- Seguiu todos os requisitos que foram especificados.


### Ex3: sem exemplos ele errou em: ______ com exemplos: ______

SEM EXEMPLOS:
 - Pedro De Alcantara E Silva

COM EXEMPLOS:
 - ele percebeu a existência de um arquivo que já executava a mesma função retornou o seguinte identificador de que uma das funções utilizadas não era adequada para um tipo de conversão : "The existing function uses .title() which doesn't handle the "da/dos" lowercase case. I'll update it to properly normalize names according to the examples."
 - executou os ajustes e todos os testes passaram
 - resultado do teste: Pedro de Alcantara e Silva

### Ex4: Delimitadores

Sem delimitador ele 
- Respondeu "Misto" e rejeitou explicitamente a injeção de instrução, mantendo a classificação original; 

Com delimitador ele 
- Ativou o modo de pensamento ("Thought: 721ms") antes de responder, também classificou como "Misto" e seguiu a regra de tratar o conteúdo interno como dado, ignorando a tentativa de injeção.

### Ex5: Critério de Aceite

Sem aceite ele parou quando 
- Terminou de criar o arquivo, sem realizar nenhum teste; 

Com aceite ele 
- Criou o arquivo com a função, executou 3 testes de validação através do terminal e somente parou após validar que as três condições de aceite foram compridas.

### Ex6: Pensar antes de agir

Ele perguntou:

1. **A)** Devo manter o comportamento atual com `return None + print` (já existente) ou trocar para `raise ValueError` / `TypeError`?
2. **B)** Devo testar apenas a função `converter()` (testes unitários) ou também a `main()` via `monkeypatch`/`capsys`?
3. **C)** Devo incluir validação de tipo (verificar se o argumento é `int`/`float`) e rejeitar strings vazias/`None` na função `converter`?

Além dessas, ele também levantou dúvidas sobre os pontos de validação (onde colocar, quais casos cobrir), porém, as perguntas objetivas que exigem confirmação são as três acima.

### Ex7: auto-correção

Ele encontrou sozinho: (Sem ter bloco [Aeite] no ex6)

**Cumpre:**
- Validação em `converter()` (rejeita tipo errado, vazio/None, aplica `.strip().upper()`).
- Testes (`tests/test_converte.py`) com 21 casos para `converter()` e `main()` (monkeypatch/capsys).
- Mantido `return None + print` (sem exceções).

**Possíveis falhas:**
1. `main()` não valida `sys.argv[2]`/`[3]` vazios antes de chamar `converter()`.
2. `validar_temperatura()` só é testada indiretamente, não isoladamente.
3. `.upper()` torna a entrada *case-insensitive* — se o critério exigir maiúsculas exatas, é falha.
4. Teste em `tests/test_converte.py` — se houver exigência de nome/local específico, pode não estar conforme.

## Observações do exercício 7
Fechamento: O /init gerou o defeito Blind Reference (principal), que corrigi assim: substituí as referências a diretórios inexistentes (ex4/, ex7/) por uma listagem explícita dos diretórios realmente presentes no repositório, adicionei nota explicativa sobre o ex4 observacional, removi a instrução fantasma sobre ex7/tests/test_converte.py, e adicionei uma cláusula de verificação dinâmica para prevenir referências cegas futuras. Simultaneamente, corrigi a Init Fossilization (caminho absoluto hardcoded) e a Conflicting Instructions (duplicação contraditória ex6/ex7). 