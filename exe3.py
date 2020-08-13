# 3 - Crie uma classe calculadora com as quatro operações básicas (soma, subtração,
# multiplicação e divisão). O usuário deve informar dois números e o programa deve
# fazer as quatro operações.

class Calcula:
    def soma(self, primeiro, segundo):
        resultado = primeiro + segundo
        print('A soma do número {} com o {} é igual a {}. '.format(primeiro, segundo, resultado))

    def subtracao(self, primeiro, segundo):
        resultado = primeiro - segundo
        print('A subtracao do número {} com o {} é igual a {}. '.format(primeiro, segundo, resultado))

    def multiplicacao(self, primeiro, segundo):
        resultado = primeiro * segundo
        print('A multiplicação do número {} com o {} é igual a {}. '.format(primeiro, segundo, resultado))

    def divisao(self, primeiro, segundo):
        resultado = primeiro / segundo
        print('A divisão do número {} com o {} é igual a {}. '.format(primeiro, segundo, resultado))


calcula = Calcula()

primeiro_valor = float(input("Digite o 1º numero: "))
segundo_valor = float(input("Digite o 2º numero: "))

calcula.soma(primeiro_valor, segundo_valor)
calcula.subtracao(primeiro_valor, segundo_valor)
calcula.multiplicacao(primeiro_valor, segundo_valor)
calcula.divisao(primeiro_valor, segundo_valor)
