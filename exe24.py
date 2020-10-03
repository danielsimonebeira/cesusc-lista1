# 24 - Receba duas listas e exiba a união destas listas e a intercalação destas listas, isto é,
# 1º da 1ª lista, 1º da 2ª lista, 2º da 1ª lista, 2º da 2ª lista.
import random

class Elementos:
    def monta_elementos(self, qtd):
        lista = []
        contador = 1
        while contador < qtd:
            variavel = random.randint(1, 50)
            lista.append(variavel)
            contador += 1
        print("Lista gerada: ", lista)
        return lista

    def uniao(self, *arg):
        return list(set([j for i in arg for j in i]))

    def intercalacao(self, l1, l2, l3):
        intercala = []
        for a, b, c in zip(l1, l2, l3):
            intercala.append(a)
            intercala.append(b)
            intercala.append(c)
        return intercala


quantidade = random.randint(1, 9)
elementos = Elementos()

lista1 = elementos.monta_elementos(quantidade)
lista2 = elementos.monta_elementos(quantidade)
lista3 = elementos.monta_elementos(quantidade)

resultado_uniao = elementos.uniao(lista1, lista2, lista3)
print("\nUnião da lista1, lista2 e lista2: ", resultado_uniao)

resultado_intercala = elementos.intercalacao(lista1, lista2, lista3)
print("\nIntercalação da lista1, lista2 e lista2: ", resultado_intercala)


