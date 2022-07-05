 #ler o ano e classificar pela idade: até 9 anos: mirim, 9-14: infantil,
# 14-19: junior, 19-20: sênior, acima: master
from datetime import date
from time import sleep
print('Digite o ano de nascimento do aluno. Vamos classificar sua categoria conforme sua idade.')
sleep(1)
while True:
    ano = int(input('Digite o ano de nascimento do aluno: '))
    if 1910 <= ano <= 2022:
        break
    else:
        print('Ano inválido. Digite um ano válido')
sleep(1)
hoje = date.today().year
idade = hoje - ano
if idade < 9:
    print(f'Devido a idade de {idade} anos, o aluno será inscrito na categoria mirim (até 9 anos).')
elif 9 <= idade <= 13:
    print(f'Devido a idade de {idade} anos, o aluno será inscrito na categoria infantil (9 aos 14 anos).')
elif 14 <= idade <= 18:
    print(f'Devido a idade de {idade} anos, o aluno será inscrito na categoria júnior (14 aos 19 anos).')
elif 19 <= idade <= 20:
    print(f'Devido a idade de {idade} anos, o aluno será inscrito na categoria sênior (19 e 20 anos).')
elif idade > 20:
    print(f'Devido a idade de {idade} anos, o alunos erá inscrito na categoria master (acima dos 20 anos).')