# 14 - Escreva um algoritmo que calcule e imprima a tabuada do 8 (1 a 10).

class Tabuada:
    def executa_tabuada(self, valor):
        contador = 1
        while contador <= 10:
            conta = valor * contador
            print("{} X {}: {}".format(valor, contador, conta))
            contador += 1

tabuada = Tabuada()
tabuada.executa_tabuada(8)