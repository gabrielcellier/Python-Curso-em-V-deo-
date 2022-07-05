#perguntar ano de nascimento, calcular idade e falar se ta na hora de se alistar, se falta ou se já passou
#calcular quanto tempo falta ou que já passou de se alistar
from datetime import date
from time import sleep
print('Responda o ano de nascimento, informaremos se já está na hora de participar do alistamento.')
sleep(0.5)
ano = int(input('Digite o ano de nascimento: '))
sleep(1)
hoje = date.today().year
idade = hoje - ano
if idade == 18:
    print(f'Nascidos em {ano} completam 18 anos neste ano. Procure a junta militar próxima para se alistar.')
elif idade > 18:
    print(f'Nascidos em {ano} fizeram/farão {idade} este ano. Logo passaram {idade - 18} anos do prazo de alistamento.')
else:
    print(f'Nascidos em {ano} completam {idade} este ano. Logo faltam {18 - idade} anos do prazo de alistamento.')