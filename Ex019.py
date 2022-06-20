#Sorteio entre 4 nomes de alunos dados, lendo o nome e sorteando um deles
from random import choice
from time import sleep
print('Escreva nome de quatro alunos, vamos sortear um deles.')
sleep(1)
a1 = str(input('Digite o primeiro nome: ')).strip().capitalize()
a2 = str(input('Digite o segundo nome: ')).strip().capitalize()
a3 = str(input('Digite o terceiro nome: ')).strip().capitalize()
a4 = str(input('Digite o quarto nome: ')).strip().capitalize()
lista = [a1, a2, a3, a4]
sleep(1)
print(f'O nome sorteado foi {choice(lista)}.')
#.choice() é usado para selecionar randomicamente um item de uma lista



