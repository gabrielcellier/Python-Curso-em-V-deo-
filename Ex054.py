#ler o ano de nascimento de 7 pessoas e mostrar quantas são maiores e quantas são menores de idade
from time import sleep
from datetime import date
print('Digite o ano de nascimento de 7 pessoas. Mostaremos quantas são maiores e menores de idade.')
sleep(1)
maior = menor = 0
hoje = date.today().year
for c in range (1, 8):
    while True:
        ano = input(f'Digite o ano de nascimento da {c}° pessoa: ')
        if len(ano) == 4 and ano.isnumeric():
            ano = int(ano)
            print(f'Valor válido.')
            idade = hoje - ano
            if idade >= 18:
                maior += 1
                print(f'Nascido em {ano}, a {c}° pessoa tem {idade} anos. Logo é maior de idade.')
            else:
                menor += 1
                print(f'Nascido em {ano}, a {c}° pessoa tem {idade} anos. logo é menor de idade.')
            sleep(1)
            break
        else:
            print(f'Valor inválido. Digite um ano de nascimento válido.')
            sleep(0.5)
print('Os sete anos de nascimento foram computados. Estamos calculando.')
sleep(2)
print(f'Ao todo {maior} pessoas são maiores de idade e {menor} pessoas são menores de idade.')