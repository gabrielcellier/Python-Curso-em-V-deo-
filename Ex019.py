#Sorteio entre 4 nomes de alunos dados, lendo o nome e sorteando um deles
from time import sleep
from random import choice
qtalunos = 0
lista = []
print('Escreva nome de quatro alunos. Iremos sortear um dos nomes escritos.')
sleep(1)
while qtalunos < 4:
    nome = input(f'Digite o nome do {qtalunos + 1}° aluno: ').strip().capitalize()
    if nome.isalpha():
        nome = str(nome)
        lista.append(nome)
        qtalunos += 1
    else:
        print('Nome inválido. Digite um nome apenas usando letras.')
sleep(1)
print('Sorteando um dos nomes escritos....')
sleep(2)
print(f'O nome sorteado da lista foi {choice(lista)}.')






