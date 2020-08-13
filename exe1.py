# 1- Escreva uma classe que contém um método que calcule se a pessoa é maior de 18
# anos ou não. Receba os dados pela console e chame este método.

class ValidaPessoa:
    def idade_maior(self, idade):
        if idade > 18:
            print('A idade {} é maior de 18 anos. '.format(idade))
        else:
            print('A idade {} é menor de 18 anos. '.format(idade))


verifica_idade = ValidaPessoa()
obter_idade = int(input("Digite a idade: "))
verifica_idade.idade_maior(obter_idade)

