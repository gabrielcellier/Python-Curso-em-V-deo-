#ler duas notas, calcular a média e se for aciam de 7 tá aprovado, entre 5-6.9 recuperação e abaixo de 5 reprovado
n1 = float(input('Digite a primeira nota da matéria: '))
n2 = float(input('Digite a segunda nota da matéria: '))
media = (n1 + n2) / 2
if media >= 7:
    input ('O aluno obteve média {}, sendo \033[1maprovado\033[m na matéria.'.format(media))
elif media < 5:
    input ('O aluno obteve média {}, sendo \033[1mreprovado\033[m na matéria.'.format(media))
else:
    input ('O aluno obteve média {}, ficando em \033[mrecuperação\033[m na matéria.'.format(media))