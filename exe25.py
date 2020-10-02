# 25 - Faça uma função que receba uma lista e exiba os elementos da última metade na frente dos elementos da primeira metade
import random


def apresenta_lista_invertida():
    lista = []
    contador = 1
    quantidade = random.randint(2, 9)
    while contador < quantidade:
        variavel = random.randint(1, 50)
        lista.append(variavel)
        contador += 1

    print("Lista gerada: ", lista)
    lista.reverse()
    print(" Lista invertida ", lista)


apresenta_lista_invertida()