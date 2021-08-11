#ler o ano de nascimento de 7 pessoas e mostrar quantas são maiores e quantas são menores de idade
from datetime import date
maior = 0
menor = 0
atual = date.today().year
for idade in range (0,7):
    ano = int(input('Digite o ano de nascimento: '))
    if atual - ano >= 18:
        maior = maior + 1
    elif atual - ano < 18:
        menor = menor + 1
print ('Do total de anos lidos, {} são maiores de idade e {} menores.'.format(maior, menor))