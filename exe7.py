# 7 - Escreva um algoritmo que leia 10 números informados pelo usuário e, depois,
# informe o menor, número, o maior número, a soma dos números informados e a média
# aritmética dos números informados.

class Algoritmo:
    def maior_menor_numero (self, numero):
        print("O menor número da sequencia de numero é ",min(numero))
        print("O maior número da sequencia é ", max(numero))
        print("A soma de toda sequencia é ", sum(numero))
        media = sum(numero) / 10
        print("A Média é ", sum(numero))

numero = []
contador = 1

while contador < 11:
    alg = int(input("Digite o {}º valor: ".format(contador)))
    numero.append(alg)
    contador += 1

valida_algoritimo = Algoritmo()
valida_algoritimo.maior_menor_numero(numero)