# 4 - Faça um programa que receba um valor que é o valor pago, um segundo valor que
# é o preço do produto e retorne o troco a ser dado.

class Caixa:
    def dar_troco(self, valor, produto):
        if valor > produto:
            troco = valor - produto
            print('O troco é de R$ {}'.format(troco))
        elif valor == produto:
            print('Não é necessario dar troco.')
        else:
            cobrar = produto - valor
            print("Valor é inferior ao preço do produto. Falta R$ {} para completar".format(cobrar))

caixa = Caixa()
pagar = float(input('Valor recebido: '))
preco_produto = float(input('Preço do produto: '))
caixa.dar_troco(pagar, preco_produto)
