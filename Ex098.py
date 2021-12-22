#Criar função 'contador()' que recebe inicio, fim e passo (intervalo de crescimento)
#Programa tem que criar 3 contagens: 1) 1 a 10 de 1 em 1. 2) 10 a 0, de 2 em 2. 3) a Personalizada
#pro 3) Fazer evolução positiva, negativa, com números negativos e se passo for 0, fazer de 1 em 1.
from time import sleep
def contador(x, y, z):



print('Contagem de 1 a 10, aumentando de 1 em 1.')
for c in range (1, 11):
    print(f'{c}', end=' ')
    sleep(0.3)
print()
print('-*-' * 9)
print('Contagem de 10 a 1, diminuindo de 2 em 2.')
for a in range (10, 0, -2):
    print(f'{a}', end=' ')
    sleep(0.3)
print()
print('-*-' * 9)
i = int(input('Digite o número inicial: '))
f = int(input('Digite o número final: '))
p = int(input('Digite o passo (intervalo): '))

#for b in range (10, 1, -1):
    #print(b, end=' ')

