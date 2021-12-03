#Ler nome e média do aluno. Se média for maior que 7 ele tá aprovado, menor reprovado. Mostrar tudo na tela
from time import sleep
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
