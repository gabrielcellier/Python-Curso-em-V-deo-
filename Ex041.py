#ler o ano e classificar pela idade: até 9 anos: mirim, 9-14: infantil,
# 14-19: junior, 19-20: sênior, acima: master
from datetime import date
ano = int(input('Digite o ano de nascimento do inscrito: '))
dt = date.today().year
idade = dt - ano
if idade <= 9:
    print ('Devido a idade de {} o inscrito está na categoria mirim (abaixo de 9 anos).'.format(idade))
elif idade > 9 and idade < 14:
    print ('Devido a idade de {} o inscrito está na categoria infantil (9-14 anos).'.format(idade))
elif idade >= 14 and idade < 19:
    print ('Devido a idade de {} o inscrito está na categoria junior (14-19 anos).'.format(idade))
elif idade >= 19 and idade <= 20:
    print ('Devido a idade de {} o inscrito está na categoria sênior (19-20 anos).'.format(idade))
else:
    print ('Devido a idade de {} o inscrito está na categoria master (acima de 20 anos).'.format(idade))

