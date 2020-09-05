# 8 - faça um método que mostre 10 vezes na tela a palatra python (for i in range(10))


class MostraPalavra:
    def apresenta_tela(self, palavra):
        for i in range(10):
            conta = i + 1
            print('[ {} ] - {}'.format(conta, palavra))

palavra = MostraPalavra()
palavra.apresenta_tela('Python')