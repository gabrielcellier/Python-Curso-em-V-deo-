#Gerar 5 números aleatórios na tupla. Após isso mostrar a listagem dos números gerados e o maior e menor.
from random import randint
from time import sleep
n = (randint(1, 100), randint(1, 100),  randint(1, 100), randint(1, 100), randint(1, 100))
print(f'Os números sorteados foram: {n}')
print(f'O maior valor dentre os sorteados foi {max(n)} e o menor foi {min(n)}.')