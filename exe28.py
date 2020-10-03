# 28 - Faça um programa que percorre uma lista e exiba na tela o valor mais próximo da média dos valores da lista.
# Exemplo: lista = [2.5, 7.5, 10.0, 4.0] (média = 6.0). Valor mais próximo da média = 7.5

def proximo_da_media(lista):
    """ Busca na lista o valor mais próximo da média.
    Parâmetros:
        lista list: Lista de números a ser verificada.
    Retorno:
        numérico: Valor mais próximo da média.
    """

    media = sum(lista) / len(lista)
    print("Media: ", media)
    diffs = {value: abs(value - media) for value in lista}

    return min(diffs, key=diffs.get)

print("Valor aproximado da media: ", proximo_da_media([2.5, 7.5, 8, 10.0, 4.0]) )