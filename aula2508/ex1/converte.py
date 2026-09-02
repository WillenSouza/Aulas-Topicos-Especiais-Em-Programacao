#!/usr/bin/env python3
"""Conversor de temperatura entre Celsius, Fahrenheit e Kelvin via linha de comando."""

import sys


def celsius_para_fahrenheit(c):
    return (c * 9 / 5) + 32


def celsius_para_kelvin(c):
    return c + 273.15


def fahrenheit_para_celsius(f):
    return (f - 32) * 5 / 9


def fahrenheit_para_kelvin(f):
    return (f - 32) * 5 / 9 + 273.15


def kelvin_para_celsius(k):
    return k - 273.15


def kelvin_para_fahrenheit(k):
    return (k - 273.15) * 9 / 5 + 32


def validar_temperatura(temperatura, unidade):
    """Valida se a temperatura é físicamente possível."""
    if unidade == "C" and temperatura < -273.15:
        return False
    if unidade == "F" and temperatura < -459.67:
        return False
    if unidade == "K" and temperatura < 0:
        return False
    return True


def converter(temperatura, de, para):
    """Converte temperatura entre unidades. Retorna o valor convertido ou None em caso de erro."""
    unidades_validas = {"C", "F", "K"}

    if de not in unidades_validas:
        print(f"Unidade de origem desconhecida: '{de}'")
        print("Unidades válidas: C, F, K")
        return None

    if para not in unidades_validas:
        print(f"Unidade de destino desconhecida: '{para}'")
        print("Unidades válidas: C, F, K")
        return None

    if not validar_temperatura(temperatura, de):
        print(f"Temperatura abaixo do zero absoluto para unidade '{de}'")
        return None

    if de == para:
        return temperatura

    if de == "C":
        if para == "F":
            return celsius_para_fahrenheit(temperatura)
        if para == "K":
            return celsius_para_kelvin(temperatura)

    if de == "F":
        if para == "C":
            return fahrenheit_para_celsius(temperatura)
        if para == "K":
            return fahrenheit_para_kelvin(temperatura)

    if de == "K":
        if para == "C":
            return kelvin_para_celsius(temperatura)
        if para == "F":
            return kelvin_para_fahrenheit(temperatura)


def main():
    if len(sys.argv) != 4:
        print("Uso: python converte.py <temperatura> <de> <para>")
        print("Exemplo: python converte.py 100 C F")
        print("Unidades válidas: C, F, K")
        sys.exit(1)

    try:
        temperatura = float(sys.argv[1])
    except ValueError:
        print(f"Valor inválido: '{sys.argv[1]}' não é um número")
        sys.exit(1)

    de = sys.argv[2].upper()
    para = sys.argv[3].upper()

    resultado = converter(temperatura, de, para)
    if resultado is not None:
        print(f"{resultado:.1f}")


if __name__ == "__main__":
    main()