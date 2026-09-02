def media_ponderada(valores, pesos):
    """Calcula a média ponderada de valores com pesos."""
    if len(valores) != len(pesos):
        raise ValueError("Valores e pesos devem ter o mesmo tamanho")
    soma_pesos = sum(pesos)
    if soma_pesos == 0:
        raise ValueError("Soma dos pesos não pode ser zero")
    return sum(v * p for v, p in zip(valores, pesos)) / soma_pesos


if __name__ == "__main__":
    notas = [8, 7, 9]
    pesos = [2, 3, 1]
    print(media_ponderada(notas, pesos))  # 7.5
