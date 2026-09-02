#!/usr/bin/env python3
"""Lê um CSV (data,produto,valor) e soma a coluna valor, sem bibliotecas externas."""

import csv
import sys


def somar_valores(caminho):
    total = 0.0
    with open(caminho, "r", encoding="utf-8", newline="") as arquivo:
        leitor = csv.DictReader(arquivo)
        if leitor.fieldnames is None or "valor" not in leitor.fieldnames:
            print("Coluna 'valor' não encontrada no cabeçalho")
            sys.exit(1)

        for numero, linha in enumerate(leitor, start=2):
            try:
                total += float(linha["valor"])
            except (TypeError, ValueError):
                print(f"Valor inválido na linha {numero}, ignorado: '{linha.get('valor')}'")

    return total


def main():
    if len(sys.argv) != 2:
        print("Uso: python soma_csv.py <arquivo.csv>")
        sys.exit(1)

    caminho = sys.argv[1]
    try:
        total = somar_valores(caminho)
    except FileNotFoundError:
        print(f"Arquivo não encontrado: '{caminho}'")
        sys.exit(1)

    print(f"{total:.2f}")


if __name__ == "__main__":
    main()
