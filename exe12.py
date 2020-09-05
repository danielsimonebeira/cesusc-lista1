# 12 - Ler dois valores (considere que não serão lidos valores iguais) e escrever o maior deles.

class Valida_maior:
    def numero_maior(self, valor_a, valor_b):
        if valor_a > valor_b:
            print("O valor %s é maior"%(valor_a))
        else:
            print("O valor %s é maior"%(valor_b))

valor_a = int(input("Digite o valor A: "))
valor_b = int(input("Digite o valor B: "))
if valor_a == valor_b:
    print("Os valores são iguais. Programa finalizado.")
else:
    valida = Valida_maior()
    valida.numero_maior(valor_a, valor_b)