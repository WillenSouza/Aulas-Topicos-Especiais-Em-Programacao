def media_ponderada(notas, pesos):
    if len(notas) != len(pesos):
        raise ValueError("Listas de tamanhos diferentes")
    soma_pesos = sum(pesos)
    if soma_pesos == 0:
        raise ValueError("Soma de pesos igual a zero")
    return sum(n * p for n, p in zip(notas, pesos)) / soma_pesos
