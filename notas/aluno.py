class Aluno:
    def __init__(self, matricula: str, nome: str):
        self.matricula = matricula
        self.nome = nome
        self.notas = []

    def __repr__(self):
        return f"Aluno(matricula={self.matricula!r}, nome={self.nome!r})"

    def adicionar_nota(self, nota: float):
        self.notas.append(nota)

    def media_ponderada(self) -> float:
        if len(self.notas) != 3:
            raise ValueError("Exatamente 3 notas são necessárias para calcular a média ponderada.")
        n1, n2, n3 = self.notas
        return (n1 * 3 + n2 * 3 + n3 * 4) / 10
