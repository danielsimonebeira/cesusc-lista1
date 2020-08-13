# 2 - Escreva um algoritmo que solicita ao usuário para digitar um número inteiro positivo,
# e mostre-o por extenso. Este número deverá variar entre 1 e 5. Se o usuário introduzir
# um número que não pertença a este intervalo, mostre a frase “número inválido”.

class ValidaNumeroPositivo:
    def numero_positivo(self, numero):
        if numero < 1 or numero > 5:
            print("número inválido")
        else:
            for chave, valor in enumerate(['UM', 'DOIS', 'TRES', 'QUATRO', 'CINCO']):
                chave += 1
                if chave == numero:
                    print(' - ',valor)
                    break


valida = ValidaNumeroPositivo()
obter_valor = int(input("Digite o nume de 1 a 5: "))
valida.numero_positivo(obter_valor)

