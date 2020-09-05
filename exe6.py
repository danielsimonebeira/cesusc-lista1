# 6 - Faça um algoritmo que leia um nº inteiro e mostre uma mensagem indicando se
# este número é par ou ímpar, e se é positivo ou negativo

class ValidaNumero:
    def ValidaImparPar(self, numero):
        if (numero % 2) == 0:
            print("O número {} é PAR".format(numero))
        else:
            print("O número {} é IMPAR".format(numero))


numero = int(input("Digite um Numero: "))
valida_numero = ValidaNumero()
valida_numero.ValidaImparPar(numero)



