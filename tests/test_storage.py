import os
import tempfile
from notas.aluno import Aluno
from notas.storage import Storage


def test_salvar_e_carregar():
    tmp = tempfile.NamedTemporaryFile(mode="w", suffix=".csv", delete=False, encoding="utf-8")
    tmp.close()
    try:
        a1 = Aluno("2024001", "João Silva")
        a1.adicionar_nota(7.0)
        a1.adicionar_nota(8.0)
        a1.adicionar_nota(9.0)
        a2 = Aluno("2024002", "Maria Silva")
        a2.adicionar_nota(5.0)
        a2.adicionar_nota(6.0)
        a2.adicionar_nota(4.0)

        Storage.salvar([a1, a2], tmp.name)
        alunos = Storage.carregar(tmp.name)

        assert len(alunos) == 2
        assert alunos[0].nome == "João Silva"
        assert alunos[0].notas == [7.0, 8.0, 9.0]
        assert alunos[1].nome == "Maria Silva"
        assert alunos[1].notas == [5.0, 6.0, 4.0]
    finally:
        os.unlink(tmp.name)
