from .aluno import Aluno


def classificar(aluno: Aluno) -> str:
    """Classifica o aluno pela média ponderada: Aprovado (>=7), Exame (>=5) ou Reprovado."""
    media = aluno.media_ponderada()
    if media >= 7:
        return "Aprovado"
    elif media >= 5:
        return "Exame"
    else:
        return "Reprovado"
