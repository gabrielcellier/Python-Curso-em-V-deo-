#Ler nome e média do aluno. Se média for maior que 7 ele tá aprovado, menor reprovado. Mostrar tudo na tela
from time import sleep
while True:
    aluno = {}
    aluno['Nome'] = str(input('Digite o nome do aluno: ')).strip().capitalize()
    aluno['Média'] = float(input('Digite a média do aluno: '))
    if aluno['Média'] >= 7:
        aluno['Aprovação'] = 'O aluno foi aprovado'
    else:
        aluno['Aprovação'] = 'O aluno foi reprovado'
    print('-*-' * 10)
    sleep(0.5)
    print('Situação do aluno: ')
    for k, v in aluno.items():
        print(f'{k}: {v}')
    sleep(0.5)
    print('-*-' * 10)
    cont = str(input('Deseja continuar (s/n)? ')).strip().lower()[0]
    while cont not in 'sn':
        cont = str(input('Resposta inválida. Deseja continuar (s/n)? ')).strip().lower()[0]
    if cont in 's':
        aluno.clear()
    if cont in 'n':
        break
print('Programa encerrado.')
