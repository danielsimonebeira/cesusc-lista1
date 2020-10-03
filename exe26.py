# 26 - Faça um programa que receba duas listas e
# retorne True se são iguais ou
# False caso contrário,
# além do número de ocorrências do primeiro elemento da lista.
import random

def gera_lista(numero_lista):
    lista = []
    contador = 1
    quantidade = random.randint(2, 9)
    while contador < quantidade:
        variavel = random.randint(1, 9)
        lista.append(variavel)
        contador += 1
    print("Lista {} gerada: {}".format(numero_lista, lista))
    return lista

def valida_true_false(lista1, lista2):
    resultado = False
    for x in lista1:
        for y in lista2:
            if x == y:
                resultado = True
                return resultado
    return resultado

def numero_ocorrencia(lista1, lista2):
    posicao_lista1 = lista1[0]
    posicao_lista2 = lista2[0]
    uniao_lista = lista1 + lista2
    posicao_uniao_lista = uniao_lista[0]
    print("Número de ocorrências do primeiro elemento da lista1: ", lista1.count(posicao_lista1))
    print("Número de ocorrências do primeiro elemento da lista2: ", lista2.count(posicao_lista2))
    print("Número de ocorrências do primeiro elemento da união das listas: ", uniao_lista.count(posicao_uniao_lista))


lista1 = gera_lista(1)
lista2 = gera_lista(2)

print("\nResultado: ", valida_true_false(lista1, lista2), "\n")
numero_ocorrencia(lista1, lista2)



