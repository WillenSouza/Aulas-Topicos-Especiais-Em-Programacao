import csv
import os
from .aluno import Aluno
from .classificacao import classificar


class Storage:
    @staticmethod
    def salvar(alunos: list[Aluno], caminho: str):
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
