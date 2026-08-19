from .aluno import Aluno


def classificar(aluno: Aluno) -> str:
    media = aluno.media_ponderada()
    if media >= 7:
        return "Aprovado"
    elif media >= 5:
        return "Exame"
    else:
        return "Reprovado"
