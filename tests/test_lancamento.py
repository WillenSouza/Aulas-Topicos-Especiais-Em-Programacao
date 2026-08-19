from notas.aluno import Aluno
from notas.lancamento import LancamentoNotas


def test_lancar_notas():
    a = Aluno("2024001", "João Silva")
    LancamentoNotas(a).lançar(7.0, 8.0, 9.0)
    assert a.notas == [7.0, 8.0, 9.0]


def test_lancar_notas_varias_vezes():
    a = Aluno("2024001", "João Silva")
    LancamentoNotas(a).lançar(5.0, 5.0, 5.0)
    LancamentoNotas(a).lançar(6.0, 6.0, 6.0)
    assert a.notas == [5.0, 5.0, 5.0, 6.0, 6.0, 6.0]
