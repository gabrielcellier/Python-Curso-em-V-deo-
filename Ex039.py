#perguntar ano de nascimento, calcular idade e falar se ta na hora de se alistar, se falta ou se já passou
#calcular quanto tempo falta ou que já passou de se alistar
from datetime import date
ano = int(input('Digite o ano de nascimento da pessoa: '))
dt = date.today().year
idade = dt - ano
if idade == 18:
    print ('A pessoa completa 18 anos em 2021 logo deve-se alistar.')
elif idade > 18:
    print ('A pessoa completa {} anos em 2021, logo já passou {} anos do ano de alistamento.'
           .format(idade, idade - 18))
else:
    print ('A pessoa completa {} anos em 2021, logo faltam {} anos para o seu alistamento.'
           .format(idade, 18 - idade))
