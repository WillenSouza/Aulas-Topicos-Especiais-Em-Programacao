from notas.aluno import Aluno


def test_criar_aluno():
    a = Aluno("2024001", "João Silva")
    assert a.matricula == "2024001"
    assert a.nome == "João Silva"
    assert a.notas == []


def test_adicionar_nota():
    a = Aluno("2024001", "João Silva")
    a.adicionar_nota(7.5)
    a.adicionar_nota(8.0)
    a.adicionar_nota(6.5)
    assert a.notas == [7.5, 8.0, 6.5]


def test_media_ponderada():
    a = Aluno("2024001", "João Silva")
    a.adicionar_nota(7.0)
    a.adicionar_nota(7.0)
    a.adicionar_nota(7.0)
    media = a.media_ponderada()
    assert media == 7.0


def test_media_ponderada_pesos():
    a = Aluno("2024001", "João Silva")
    a.adicionar_nota(10.0)
    a.adicionar_nota(10.0)
    a.adicionar_nota(0.0)
    media = a.media_ponderada()
    assert media == 6.0


def test_media_ponderada_exigir_3_notas():
    a = Aluno("2024001", "João Silva")
    try:
        a.media_ponderada()
        assert False, "Deve levantar ValueError"
    except ValueError:
        pass
