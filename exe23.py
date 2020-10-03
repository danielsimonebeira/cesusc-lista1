# 23 - Crie uma programa que recebe uma lista qualquer e:
# a. retorne o maior elemento
# b. retorne a soma dos elementos
# c. retorne o número de ocorrências do primeiro elemento da lista
# d. retorne a média dos elementos
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

    def valida_elementos(self, elementos, qtd):
        print("Maior elemento: ", max(elementos))
        print("A soma dos elementos: ", sum(elementos))
        primeiro_elemento = elementos[0]
        print("Numéros de ocorrencias do primeiro elemento: ", elementos.count(primeiro_elemento))
        media = sum(elementos) / qtd
        print("A Média dos elementos: ", media)

quantidade = random.randint(1, 50)
elementos = Elementos()
lista = elementos.monta_elementos(quantidade)
elementos.valida_elementos(lista, quantidade)




