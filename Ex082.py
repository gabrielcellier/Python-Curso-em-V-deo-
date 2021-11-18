#Perguntar numeros. No fim criar 3 listas: com só n pares, ímpares e a lista toda
from time import sleep
lista = []
listap = []
listai = []
while True:
    n = int(input('Digite um número inteiro: '))
    lista.append(n)
    if n % 2 == 0:
        listap.append(n)
    if n % 2 == 1:
        listai.append(n)
    cont = str(input('Você deseja digitar outro número (s/n)? ')).lower().strip()[0]
    while cont not in 'sn':
        cont = str(input('Resposta inválida. Você deseja continuar (s/n)? ')).strip().lower()[0]
    if cont in 'n':
        break
print(f'1) A lista só com os números pares: {listap}')
print(f'2) A lista só com os números ímpares: {listai}')
print(f'3) A lista com todos os números: {lista}')
#poderia separar par ou ímpar por 'for i, v in enumerate(lista) e aplicar o '% 2 == 0' e '~== 1' direto no 'v'.
