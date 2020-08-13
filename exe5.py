# 5 - Ler um valor e escrever se é positivo ou negativo (considere o valor zero como
# positivo)

class Valida:
    def positivo_negativo(self, valor):
        if valor >= 0:
            print('Valor digitado {} é POSITIVO'.format(valor))
        else:
            print('Valor digitado {} é NEGATIVO'.format(valor))

valida = Valida()
valor = int(input("Digite um número: "))
valida.positivo_negativo(valor)