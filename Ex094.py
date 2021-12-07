#Ler nome, sexo e idade. No final juntar tudo em uma única lista. Mostrar: A) Total de pessoas
#B) Média de idade, C) Lista com todas as mulheres, D)Lista com todas as pessoas com idade acima da média.
from time import sleep
pessoas = {}
lista = []
somai = 0
while True:
    pessoas['Nome'] = str(input('Digite o nome da pessoa: ')).strip().capitalize()
    pessoas['Idade'] = int(input('Digite a idade da pessoa: '))
    somai += pessoas['Idade']
    pessoas['Sexo'] = str(input('Digite o sexo da pessoa (m/f): ')).upper().strip()[0]
    while pessoas['Sexo'] not in 'MmFf':
        print('Resposta inválida! Responda "F" ou "M".')
        pessoas['Sexo'] = str(input('Digite o sexo da pessoa (m/f): ')).upper().strip()[0]
    lista.append(pessoas.copy())
    pessoas.clear()
    cont = str(input('Deseja continuar (s/n)? ')).strip().lower()[0]
    while cont not in 'sn':
        cont = str(input('Resposta inválida. Deseja continuar (s/n)? ')).strip().lower()[0]
    if cont in 'Nn':
        break
sleep(0.5)
print(f'1) O total de pessoas cadastradas foi de {len(lista)}.')
print(f'2) A média de idade dos cadastrados foi de {(somai / len(lista)):.1f}.')
print(f'3) A lista com todas as mulheres a seguir: ')
for m in lista:
    if m['Sexo'] in 'Mm':
        print(f'{m["Nome"]}')
        sleep(0.5)
print(f'4) Lista de pessoas com idade acima da média ({(somai / len(lista)):.1f}):')
for p in lista:
    if p['Idade'] >= (somai/len(lista)):
        print(f'{p["Nome"]}')
        sleep(0.5)


