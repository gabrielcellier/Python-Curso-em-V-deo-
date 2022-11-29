#analisar o que for digitado
from time import sleep
print('Digite uma palavra, ou valor, um mistura de letras e números. Iremos avaliar o que foi digitado.')
sleep(1)
valor = input('Digite o que você quer que seja avaliado (ex letras, números etc): ')
sleep(1)
print(f'{valor} é um valor numérico? {valor.isnumeric()}.')
print(f'{valor} é composto apenas por letras? {valor.isalpha()}.')
print(f'{valor} é composto por números e letras? {valor.isalnum()}.')
print(f'{valor} é totalmente composto por letras minúsculas? {valor.islower()}.')
print(f'{valor} é totalmente composto por letras maísculas? {valor.isupper()}.')
print(f'{valor} é uma frase que se inicia com letra maíuscula? {valor.istitle()}.')
print(f'{valor} é composto apenas por dígitos? {valor.isdigit()}.')
