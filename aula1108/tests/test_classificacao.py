from notas.aluno import Aluno
from notas.classificacao import classificar


def test_aprovado():
    a = Aluno("2024001", "João Silva")
    a.adicionar_nota(8.0)
    a.adicionar_nota(8.0)
    a.adicionar_nota(8.0)
    assert classificar(a) == "Aprovado"


def test_exame():
    a = Aluno("2024001", "João Silva")
    a.adicionar_nota(5.0)
    a.adicionar_nota(5.0)
    a.adicionar_nota(7.0)
    assert classificar(a) == "Exame"


def test_reprovado():
    a = Aluno("2024001", "João Silva")
    a.adicionar_nota(3.0)
    a.adicionar_nota(4.0)
    a.adicionar_nota(5.0)
    assert classificar(a) == "Reprovado"


def test_borda_exame_7():
    a = Aluno("2024001", "João Silva")
    a.adicionar_nota(7.0)
    a.adicionar_nota(7.0)
    a.adicionar_nota(7.0)
    assert classificar(a) == "Aprovado"


def test_borda_exame_5():
    a = Aluno("2024001", "João Silva")
    a.adicionar_nota(5.0)
    a.adicionar_nota(5.0)
    a.adicionar_nota(5.0)
    assert classificar(a) == "Exame"
