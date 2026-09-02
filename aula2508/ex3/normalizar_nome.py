def normalizar_nome(nome):
    if not nome:
        return ""
    nome = nome.strip()
    nome = " ".join(nome.split())
    palavras = nome.lower().split()
    pequenas = {"da", "dos", "de", "do", "das", "e"}
    resultado = []
    for i, palavra in enumerate(palavras):
        if i == 0:
            resultado.append(palavra.capitalize())
        elif palavra in pequenas:
            resultado.append(palavra)
        else:
            resultado.append(palavra.capitalize())
    return " ".join(resultado)