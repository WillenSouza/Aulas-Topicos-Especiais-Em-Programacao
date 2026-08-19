from .aluno import Aluno


class LancamentoNotas:
    def __init__(self, aluno: Aluno):
        self.aluno = aluno

    def lançar(self, n1: float, n2: float, n3: float):
        self.aluno.adicionar_nota(n1)
        self.aluno.adicionar_nota(n2)
        self.aluno.adicionar_nota(n3)
