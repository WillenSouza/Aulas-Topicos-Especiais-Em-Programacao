import pytest
import sys
from unittest.mock import patch
from io import StringIO

sys.path.insert(0, "/home/vitorsauzen/Sistemas de Informação/8º S/Top. Esp. Prog./topicos-especiais-em-programacao/aula03")

from converte import converter, main, celsius_para_fahrenheit, validar_temperatura


class TestConverterValido:
    def test_c_para_f(self):
        assert converter(0, "C", "F") == pytest.approx(32.0)

    def test_f_para_c(self):
        assert converter(32, "F", "C") == pytest.approx(0.0)

    def test_c_para_k(self):
        assert converter(0, "C", "K") == pytest.approx(273.15)

    def test_k_para_c(self):
        assert converter(273.15, "K", "C") == pytest.approx(0.0)

    def test_mesma_unidade(self):
        assert converter(42.5, "C", "C") == pytest.approx(42.5)

    def test_aceita_minusculo_e_espacos(self):
        assert converter(100, " c ", " f ") == pytest.approx(212.0)


class TestConverterErros:
    def test_unidade_origem_invalida(self, capsys):
        assert converter(100, "X", "F") is None
        captured = capsys.readouterr()
        assert "Unidade de origem desconhecida" in captured.out

    def test_unidade_destino_invalida(self, capsys):
        assert converter(100, "C", "Y") is None
        captured = capsys.readouterr()
        assert "Unidade de destino desconhecida" in captured.out

    def test_temperatura_abaixo_zero_absoluto_c(self, capsys):
        assert converter(-300, "C", "F") is None
        captured = capsys.readouterr()
        assert "abaixo do zero absoluto" in captured.out

    def test_temperatura_abaixo_zero_absoluto_f(self, capsys):
        assert converter(-500, "F", "C") is None

    def test_temperatura_abaixo_zero_absoluto_k(self, capsys):
        assert converter(-1, "K", "C") is None

    def test_temperatura_string(self, capsys):
        assert converter("cem", "C", "F") is None
        captured = capsys.readouterr()
        assert "não é um número válido" in captured.out

    def test_temperatura_none(self, capsys):
        assert converter(None, "C", "F") is None
        captured = capsys.readouterr()
        assert "não é um número válido" in captured.out

    def test_temperatura_bool(self, capsys):
        # bool é subclasse de int; deve ser rejeitado
        assert converter(True, "C", "F") is None
        captured = capsys.readouterr()
        assert "não é um número válido" in captured.out

    def test_unidade_vazia(self, capsys):
        assert converter(0, "", "F") is None
        captured = capsys.readouterr()
        assert "vazias" in captured.out

    def test_unidade_none(self, capsys):
        assert converter(0, None, "F") is None
        captured = capsys.readouterr()
        assert "devem ser strings" in captured.out

    def test_de_nao_string(self, capsys):
        assert converter(0, 1, "F") is None
        captured = capsys.readouterr()
        assert "devem ser strings" in captured.out


class TestMainCLI:
    def test_uso_correto(self, monkeypatch, capsys):
        monkeypatch.setattr(sys, "argv", ["converte.py", "100", "C", "F"])
        main()
        captured = capsys.readouterr()
        assert "212.0" in captured.out

    def test_argumentos_insuficientes(self, monkeypatch, capsys):
        monkeypatch.setattr(sys, "argv", ["converte.py", "100"])
        with pytest.raises(SystemExit) as exc_info:
            main()
        assert exc_info.value.code == 1
        captured = capsys.readouterr()
        assert "Uso:" in captured.out

    def test_valor_nao_numerico_cli(self, monkeypatch, capsys):
        monkeypatch.setattr(sys, "argv", ["converte.py", "abc", "C", "F"])
        with pytest.raises(SystemExit) as exc_info:
            main()
        assert exc_info.value.code == 1
        captured = capsys.readouterr()
        assert "não é um número" in captured.out

    def test_unidade_invalida_cli(self, monkeypatch, capsys):
        monkeypatch.setattr(sys, "argv", ["converte.py", "100", "C", "X"])
        monkeypatch.setattr(sys, "argv", ["converte.py", "100", "C", "X"])
        # Como converter retorna None, main não imprime resultado; apenas sai normalmente (sem sys.exit)
        # Vamos apenas verificar que não há erro e não imprime número
        monkeypatch.setattr(sys, "argv", ["converte.py", "100", "C", "X"])
        main()
        captured = capsys.readouterr()
        assert "Unidade de destino desconhecida" in captured.out
        assert "212.0" not in captured.out
