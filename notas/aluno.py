class Aluno:
    """Representa um aluno matriculado e as notas lançadas para ele."""

    def __init__(self, matricula: str, nome: str):
        """Cria um aluno sem nenhuma nota lançada ainda."""
        self.matricula = matricula
        self.nome = nome
        self.notas: list[float] = []

    def __repr__(self):
        return f"Aluno(matricula={self.matricula!r}, nome={self.nome!r})"

    def adicionar_nota(self, nota: float) -> None:
        """Lança uma nota para o aluno, na ordem em que é chamada."""
        self.notas.append(nota)

    def media_ponderada(self) -> float:
        """Calcula a média ponderada (pesos 3, 3, 4) das 3 avaliações.

        Levanta ValueError se o aluno ainda não tiver exatamente 3 notas.
        """
        if len(self.notas) != 3:
            raise ValueError("Exatamente 3 notas são necessárias para calcular a média ponderada.")
        n1, n2, n3 = self.notas
        return (n1 * 3 + n2 * 3 + n3 * 4) / 10
