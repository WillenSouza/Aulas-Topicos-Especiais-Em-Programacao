---
name: relatorio-de-atividade
description: Escreve o relatório técnico de uma atividade prática da disciplina em `relatorio.md`, reconstruindo o que aconteceu a partir dos commits do repositório e usando o formato exigido pela avaliação (o que foi pedido, o que foi feito, o que falhou, como foi resolvido, ferramentas de IA). Use sempre que eu pedir relatório, relatório da atividade, documentação da atividade, "documenta o que eu fiz", "escreve o md da entrega", ou quando eu disser que vou fechar, finalizar ou subir a entrega — mesmo que eu não use a palavra "relatório".
---

# Relatório de atividade

Este relatório é avaliado como prestação de contas, não como texto de divulgação. O que vale
nele é ser verdadeiro e curto: cada afirmação precisa ter origem em uma evidência que eu possa
apontar, e o professor precisa conseguir ler tudo de uma vez. Por isso o trabalho começa lendo
o histórico do repositório, e não escrevendo.

## Passo 1 — Levantar as evidências antes de escrever

Rode, na raiz do repositório da atividade:

```bash
git log --oneline --reverse        # a linha do tempo da atividade, em ordem cronológica
```

Leia as mensagens em ordem: elas são a narrativa do que foi tentado. Marque especialmente os
commits com "fix", "corrige", "ajusta", "volta", "tenta de novo" — eles quase sempre apontam
para uma falha que precisa aparecer nas seções "O que falhou" e "Como foi resolvido".

Depois, meça o tamanho do que mudou contra o primeiro commit da atividade:

```bash
git rev-list --max-parents=0 HEAD  # primeiro commit do repositório
git diff --stat <primeiro-commit> HEAD
```

Se o repositório já existia antes desta atividade, o primeiro commit do repositório **não** é o
primeiro commit da atividade. Nesse caso, pergunte qual é o commit inicial em vez de adotar o
mais antigo por conveniência.

Quando a mensagem de um commit sugerir um erro mas não disser qual, abra o commit:

```bash
git show <commit>
```

**As únicas fontes válidas** são: o histórico do git, a saída de comandos e ferramentas desta
conversa, e o que eu afirmar diretamente. Nada mais. Se não houver repositório git, ou se o
histórico for um único commit do tipo "primeira versão", diga isso na hora e peça o material
que falta — não reconstrua a atividade por dedução.

## Passo 2 — Escrever `relatorio.md`

Use exatamente estas seções, nesta ordem, com estes títulos:

```markdown
# Relatório — <nome da atividade>

## O que foi pedido

## O que foi feito

## O que falhou

## Como foi resolvido

## Ferramentas de IA
```

**O que foi pedido** — o enunciado em duas frases. Se eu não colei o enunciado, procure por
`README`, `enunciado` ou equivalente no repositório. Se não achar, deixe a lacuna marcada
(veja abaixo) em vez de inferir o enunciado a partir do código.

**O que foi feito** — o que existe e funciona no final. É o estado atual, não a história das
tentativas: arquivos que existem, comandos que rodam, o que o programa faz quando executado.
Números só se vierem do `git diff --stat`.

**O que falhou** — cada erro que apareceu no caminho, com **a mensagem exata**, entre acentos
graves ou em bloco de código. Mensagem parafraseada não serve como evidência. Se o histórico e
a conversa não mostram nenhuma falha, escreva que não houve falhas durante a atividade — isso
é uma resposta legítima e melhor do que uma falha inventada para preencher a seção.

**Como foi resolvido** — o que corrigiu cada falha, na mesma ordem em que as falhas aparecem
na seção anterior, uma correção por falha. Se alguma falha não foi resolvida, diga que segue
aberta em vez de escrever uma solução plausível.

**Ferramentas de IA** — para cada ferramenta usada: qual agente, qual modelo e em que etapa da
atividade. Uma linha por ferramenta:

```markdown
- <agente> (<modelo>) — <etapa em que foi usado>
```

"Usei IA para ajudar" não atende ao que a avaliação pede. Se eu não souber o modelo exato de
alguma ferramenta, marque a lacuna e pergunte no final.

### Lacunas

Quando uma informação necessária não estiver nas evidências, escreva `[falta: <o quê>]` no
lugar dela e transforme isso em pergunta no Passo 3. Uma lacuna marcada é honesta; uma lacuna
preenchida com suposição contamina o relatório inteiro, porque o leitor perde a referência de
onde ele é confiável.

## Passo 3 — Fechar perguntando

Termine a resposta no chat (não dentro do `relatorio.md`) listando as lacunas como perguntas
curtas e específicas, uma por linha. Perguntas específicas se respondem em um minuto;
"faltou algo?" não se responde.

Exemplo de fechamento:

```
Ficaram três lacunas no relatório:
- Qual foi a mensagem exata do erro do commit "corrige import"?
- O enunciado pedia validação de entrada, ou isso foi decisão sua?
- Qual modelo do Copilot você usou na etapa de testes?
```

Não ofereça preencher essas lacunas por conta própria.

## Regras que não se negociam

- **Nunca inventar um erro que não aconteceu.** Vale também para soluções, métricas e etapas.
- **Máximo de uma página** — cerca de 500 palavras. Relatório longo não é lido. Ao cortar,
  corte adjetivos, contexto e introduções; nunca corte fatos ou mensagens de erro.
- **Português do Brasil, primeira pessoa do singular** — "implementei", "percebi que". Nunca
  "foi implementado", "implementou-se" ou "nós".
- **Sem seções extras.** As cinco seções são o que a avaliação exige; acrescentar
  "conclusão" ou "próximos passos" gasta a página em algo que não é pedido.

## Conferência final

Antes de entregar, verifique:

- As cinco seções estão presentes e na ordem exigida.
- Cada falha tem mensagem exata e uma correção correspondente na mesma ordem.
- Cada ferramenta de IA tem agente, modelo e etapa.
- Todo número no texto veio do `git diff --stat` ou de mim.
- Cabe em uma página.
- Está em primeira pessoa do singular, em pt-BR.
- As lacunas `[falta: ...]` viraram perguntas no chat.

## Exemplo de par falha/solução

**A partir do histórico:**
`git log` mostra `feat: conecta ao banco` seguido de `fix: corrige string de conexão`, e a
conversa contém a saída `psycopg2.OperationalError: could not translate host name "db" to address`.

**No relatório:**

```markdown
## O que falhou
Na primeira tentativa de subir a aplicação, a conexão com o banco quebrou com
`psycopg2.OperationalError: could not translate host name "db" to address`.

## Como foi resolvido
Troquei o host `db` por `localhost` na string de conexão, já que o banco estava rodando fora
do Docker.
```