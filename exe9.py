# 9 - faça um método que receba um número X e uma palavra no console e repita x vezes a essa frase.


class Repita:
    def quantidade_palavra(self, numero, palavra):
        contador = 0
        while contador < numero:
            print("[ {} ] - {}".format(contador + 1, palavra))
            contador += 1


quantidade = int(input("Digite a quantidade de repetição: "))
palavra = input("Digite a palavra a ser repetida: ")

repita = Repita()
repita.quantidade_palavra(quantidade, palavra)
