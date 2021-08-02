#ler duas notas, calcular a média e se for aciam de 7 tá aprovado,
# entre 5-6.9 recuperação e abaixo de 5 reprovado
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2) / 2
if media > 7:
    print ('A média foi de {:.2f}, logo o aluno foi aprovado!'.format(media))
elif media < 5:
    print ('A média foi de {:.2f}, logo o aluno foi reprovado!'.format(media))
else:
    print ('A média foi de {:.2f}, logo o aluno está em recuperação!'.format(media))

