from .aluno import Aluno


class LancamentoNotas:
    """Lança as 3 avaliações de um aluno, na ordem N1, N2, N3."""

    def __init__(self, aluno: Aluno):
        self.aluno = aluno

    def lançar(self, n1: float, n2: float, n3: float) -> None:
        """Lança as 3 notas do aluno associado a este lançamento."""
        self.aluno.adicionar_nota(n1)
        self.aluno.adicionar_nota(n2)
        self.aluno.adicionar_nota(n3)
