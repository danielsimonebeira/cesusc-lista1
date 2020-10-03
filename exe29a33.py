# 29 - Qual a diferença de lista e dicionário?
# 30 - Crie um dict com 5 nomes e idades, crie um segundo dict duplicando os itens.
# 31 - Crie um dict com 5 nomes e profissões e remova o ultimo elemento
# 32 - Lançar nota final para 3 alunos, deve ser possível adicionar, atualizar e deletar.
# Apresente o resultado somente a nota de cada aluno ao final das operações.
# 33 - Incremente o exercício anterior para receber 3 notas para cada aluno,
# onde deve ser possível efetuar as operações de adicionar, atualizar e deletar e mostre a média.
# (se possível você pode aproveitar exercícios anteriores)

# Atividade 29
print(150 * '-', "\nAtividade 29")
print("Qual a diferença de lista e dicionário? "
      "\nResposta: Listas = Lista é uma coleção de valores indexada, em que cada valor é identificado por um índice. "
      "\nO primeiro item na lista está no índice 0, o segundo no índice 1 e assim por diante"
      "\nDicionario = Estrutura de dados que implementa mapeamentos entre uma chave (key) e algum conteúdo (value), A chave funciona como um índice para acessar o conteúdo",
      '\n' + 150 * '-')

# Atividade 30
print("Atividade 30")
dicionario_nome_idade = {
    "Daniel": 30,
    "Thai": 32,
    "Renato": 35,
    "Maria": 21,
    "Aline": 45
}
dicionario_nome_idade_duplicado = {}
copia = dicionario_nome_idade.copy()
dicionario_nome_idade_duplicado = copia

print("Dicionario 1 ", dicionario_nome_idade)
print("Dicionario 2 ", dicionario_nome_idade_duplicado)
print(150 * "-")

# Atividade 31
print("Atividade 31")
dicionario_nome_profissao = {
    "Daniel": "Analista de qualidade",
    "Thai": "Analista de negocio",
    "Renato": "Desenvolvedor",
    "Maria": "Gerente",
    "Aline": "Marketing"
}
dicionario_nome_profissao.pop('Aline')
print("Remove o ultimo valor do dicionário: ", dicionario_nome_profissao)
print(150 * '-')

print("Atividade 32")
dicionario_nome_nota = {}

while True:
    menu = int(input("Digite: \n1) Criar aluno e Nota \n2) Atualizar nota \n3) Deleta Aluno \n4) calcula a média \n5) Sair \n"))
    if menu == 1:
        contador = 1
        while contador < 4:
            nome = input("Digite o nome do Aluno: ")
            nota = float(input("Digite a nota de {}: ".format(nome)))
            dicionario_nome_nota[nome] = nota

            print("Aluno e nota adicionado: ", dicionario_nome_nota)
            contador += 1

    elif menu == 2:
        nome_edicao = input("Digite o nome do aluno que deseja alterar: ")
        if nome_edicao in dicionario_nome_nota:
            nova_nota = float(input("Digite a nota autualizada: "))
            dicionario_nome_nota[nome_edicao] = nova_nota
            print("Aluno e nota atualizado: ", dicionario_nome_nota)
        else:
            print("Valor inválido")

    elif menu == 3:
        nome_deleta = input("Digite o nome do aluno que deseja alterar: ")
        if nome_deleta in dicionario_nome_nota:
            del dicionario_nome_nota[nome_deleta]
            print("Aluno e nota atualizado: ", dicionario_nome_nota)
        else:
            print("Valor inválido")
    elif menu == 4:
        nome_calcula = input("Digite o nome do aluno que deseja alterar: ")
        if nome_calcula in dicionario_nome_nota:
            media = sum(dicionario_nome_nota.get(nome_calcula)) / 3

    elif menu == 5:
        exit()
    else:
        print("Valor inválido")

