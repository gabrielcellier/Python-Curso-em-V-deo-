#Ler nome e preço de vários produtos. Perguntar sempre se usuário quer continuar. No fim:
#a) Qual total gasto, b) Qt de produtos acima de 1000 reais, c)Nome do produto mais barato
from time import sleep
total = p1000 = 0
pbarato = 0
nbarato = ' '
while True:
    nome = str(input('Digite o nome do produto: ')).capitalize().strip()
    preco = float(input('Digite o preço do produto: R$ '))
    total += preco
    pbarato = preco
    if preco > 1000:
        p1000 += 1
    if preco < pbarato or pbarato == 0:
        nbarato = nome
    continuar = str(input('Você deseja continuar a lista (s/n)? ')).strip().lower()[0]
        if continuar == 'n':
            break
    sleep(1)
print (f'O valor total da lista é R${total}, com {p1000} produtos acima de R$1000.00'
       f' e com o produto {nbarato} sendo o mais barato')


