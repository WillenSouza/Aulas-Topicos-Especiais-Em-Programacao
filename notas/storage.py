import csv
import os
from .aluno import Aluno
from .classificacao import classificar


class Storage:
    """Persiste e recupera alunos em um arquivo CSV local."""

    @staticmethod
    def salvar(alunos: list[Aluno], caminho: str) -> None:
        """Regrava o arquivo inteiro com o estado atual da lista de alunos.

        Sobrescreve o conteúdo anterior (não é append) — chamar de novo com
        uma lista diferente substitui os dados, não soma. Alunos que ainda
        não têm as 3 notas lançadas são ignorados silenciosamente, pois
        `Aluno.media_ponderada()` exige exatamente 3 notas.
        """
        with open(caminho, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["matricula", "nome", "n1", "n2", "n3", "media", "status"])
            for aluno in alunos:
                if len(aluno.notas) != 3:
                    continue
                media = aluno.media_ponderada()
                status = classificar(aluno)
                writer.writerow([aluno.matricula, aluno.nome, *aluno.notas, media, status])

    @staticmethod
    def carregar(caminho: str) -> list[Aluno]:
        """Lê o CSV e reconstrói a lista de alunos. Retorna [] se o arquivo não existir."""
        alunos = []
        if not os.path.exists(caminho):
            return alunos
        with open(caminho, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                aluno = Aluno(row["matricula"], row["nome"])
                aluno.adicionar_nota(float(row["n1"]))
                aluno.adicionar_nota(float(row["n2"]))
                aluno.adicionar_nota(float(row["n3"]))
                alunos.append(aluno)
        return alunos
