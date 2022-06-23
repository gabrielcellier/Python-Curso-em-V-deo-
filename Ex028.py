#Computador sorteia um numero de 0 a 5 e a pessoa tenta descobrir qual é. Avisar se acertou ou errou
from time import sleep
from random import randint, choice
print('O computador sorteará um número entre 0 a 5, tente descobrir qual é o número.')
sleep(0.5)
sorteio = randint(0, 5)
while True:
    num = int(input('Qual número entre 0 a 5 você escolhe? '))
    if num in range(0, 6):
        print('Boa escolha! Boa sorte!')
        break
    print('Número inválido. Por favor escolha um número entre 0 a 5.')
print('Sorteando um número....')
sleep(1)
if num == sorteio:
    print(f'Olha só! O número sorteado foi {sorteio}, o mesmo {num} que você escolheu!. Você acertou!')
else:
    print(f'Que azar! O número sorteado foi {sorteio} enquanto você escolheu {num}. Você errou!')


