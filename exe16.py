# 16 - Faça um algoritmo que leia os valores de COMPRIMENTO, LARGURA e ALTURA e apresente o valor do volume de
# uma caixa retangular. Utilize para o cálculo a fórmula VOLUME = COMPRIMENTO * LARGURA * ALTURA.


class Volume:
    def calcula(self, comprimento, largura, altura):
        volume = comprimento * largura * altura
        print("Valor do Volume de uma caixa retangular: ", volume)

comprimento = float(input("Digite o comprimento de uma caixa retangular: "))
largura = float(input("Digite a largura de uma caixa retangular: "))
altura = float(input("Digite a altura de uma caixa retangular: "))

volume = Volume()
volume.calcula(comprimento, largura, altura)