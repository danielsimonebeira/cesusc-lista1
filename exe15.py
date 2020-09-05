# 15 - Ler 10 valores (considere que não serão lidos valores iguais) e escrever o maior deles.

class Adiciona_valoraes:
    def guarda_valores(self):
        lista = []
        contador = 1
        while contador < 11:
            valor = int(input("Digite o {}º valor: ".format(contador)))
            lista.append(valor)
            contador += 1
        return lista


adiciona = Adiciona_valoraes()
obter_lista = adiciona.guarda_valores()
valor_maximo = max(obter_lista)
print("\nO maior valor é ", valor_maximo)