#perguntar ano de nascimento, calcular idade e falar se ta na hora de se alistar, se falta ou se já passou
#calcular quanto tempo falta ou que já passou de se alistar
from datetime import date
ano = int(input('Qual o ano de nascimento do indivíduo? '))
dt = date.today().year
idadedt = dt - ano #calculo de idade a partir do uso do date da lib datetime
idade = 2021 - ano
if idade < 18:
    input ('Devido completar a idade de {} este ano, o indivíduo não pode se alistar ainda, falta {} ano(s).'
           .format(idade, (18 - idade)))
elif idade > 18:
    input ('Devido completar a idade de {} este ano, o indivíduo deve se alistar imediamente, o indivíduo'
           ' está {} anos atrasado quanto ao seu alistamento.'.format(idade, (idade - 18)))
else:
    input ('Como o indivíduo nasceu em 2003 e completa 18 anos em 2021, este é o ano dele se alistar.')
#usando o date.today().year você garante estar pegando o ano atual,
#não precisando trocar o ano na variável 'idade' a cada troca de ano