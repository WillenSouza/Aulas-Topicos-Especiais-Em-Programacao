from notas import cli
from notas.aluno import Aluno


def test_listar_turma_imprime_dados_do_aluno(capsys):
    a = Aluno("2024001", "João Silva")
    a.adicionar_nota(7.0)
    a.adicionar_nota(8.0)
    a.adicionar_nota(9.0)

    cli.listar_turma([a])

    saida = capsys.readouterr().out
    assert "João Silva" in saida
    assert "Aprovado" in saida


def test_menu_cadastra_lanca_lista_remove_e_sai(tmp_path, monkeypatch, capsys):
    caminho_csv = tmp_path / "notas.csv"
    monkeypatch.setattr(cli, "ARQUIVO_CSV", str(caminho_csv))

    entradas = iter([
        "1", "2024001", "João Silva",  # cadastrar
        "2", "1", "7", "8", "9",       # lançar avaliações
        "3",                            # listar turma
        "4", "1",                       # remover aluno
        "5",                             # sair
    ])
    monkeypatch.setattr("builtins.input", lambda _: next(entradas))

    try:
        cli.menu()
        assert False, "menu() deve encerrar via sys.exit"
    except SystemExit:
        pass

    saida = capsys.readouterr().out
    assert "João Silva cadastrado" in saida
    assert "Avaliações lançadas" in saida
    assert "João Silva removido" in saida


def test_menu_carrega_alunos_ja_salvos_ao_iniciar(tmp_path, monkeypatch, capsys):
    caminho_csv = tmp_path / "notas.csv"
    monkeypatch.setattr(cli, "ARQUIVO_CSV", str(caminho_csv))

    entradas_sessao_1 = iter(["1", "2024001", "João Silva", "2", "1", "7", "8", "9", "5"])
    monkeypatch.setattr("builtins.input", lambda _: next(entradas_sessao_1))
    try:
        cli.menu()
    except SystemExit:
        pass

    entradas_sessao_2 = iter(["3", "5"])
    monkeypatch.setattr("builtins.input", lambda _: next(entradas_sessao_2))
    try:
        cli.menu()
    except SystemExit:
        pass

    saida = capsys.readouterr().out
    assert "João Silva" in saida
