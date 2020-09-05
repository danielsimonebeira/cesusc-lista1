# 10 - receba três notas de um aluno e informe se ele passou ou reprovou.

class Avaliacao:
    def nota_final(self, nota):
        media = sum(nota) / 3
        if media >= 7:
            resultado = "APROVADO"
        else:
            resultado = "REPROVADO"
        return resultado


notas = []
contador = 0

while contador < 3:
    nota = float(input("Digite a {}ª nota: ".format(contador + 1)))
    notas.append(nota)
    contador += 1


avaliacao = Avaliacao()
resultado_final = avaliacao.nota_final(notas)
print("Resultado Final: ", resultado_final)