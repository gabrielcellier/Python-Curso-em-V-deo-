#ler o ano de nascimento de 7 pessoas e mostrar quantas são maiores e quantas são menores de idade
from datetime import date
maior = 0
menor = 0
hoje = date.today().year
for i in range (1, 8):
    ano = int(input('Digite o ano de nascimento da pessoa: '))
    idade = hoje - ano
    if idade >= 18:
        maior += 1
    else:
        menor += 1
print ('Das idades informadas {} são maiores de idade e {} são menores.'.format(maior, menor))