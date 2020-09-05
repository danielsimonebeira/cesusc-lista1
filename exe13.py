# 13 - Escreva um algoritmo que leia as idades de 2 homens e de 2 mulheres
# (considere que as idades dos homens serão sempre diferentes entre si, bem como as das mulheres).
# Calcule e escreva a soma das idades do homem mais velho com a mulher mais nova, e o produto das idades do homem
# mais novo com a mulher mais velha.

class Identifica:
    def homem_velho_mulher_nova(self, homens, mulheres):
        valida_homem_maior_idade = max(homens)
        valida_mulher_menor_idade = min(mulheres)
        soma_idade_homem_velho_mulher_nova = int(valida_mulher_menor_idade) + int(valida_homem_maior_idade)
        print("A soma da idade idade do homem mais velho com a mulher mais nova é {} anos.".format(soma_idade_homem_velho_mulher_nova))

    def homem_novo_mulher_velha(self, quantidade_homem, quantidade_mulher):
        valida_homem_menor_idade = min(quantidade_homem)
        valida_mulher_maior_idade = max(quantidade_mulher)
        produto_idade_homem_novo_mulher_velha = int(valida_mulher_maior_idade) / int(valida_homem_menor_idade)
        print("O produto das idades do homem mais novo com a mulher mais velhas é {0:.2f} anos.".format(produto_idade_homem_novo_mulher_velha))

qtd_homem = []
qtd_mulher = []

for x in range(2):
    x = x + 1
    homem = input("Digite a idade do homen nº {}: ".format(x))
    qtd_homem.append(homem)
    mulher = input("Digite a idade da mulher nº {}: ".format(x))
    qtd_mulher.append(mulher)

identifica = Identifica()
identifica.homem_velho_mulher_nova(qtd_homem, qtd_mulher)
identifica.homem_novo_mulher_velha(qtd_homem, qtd_mulher)

