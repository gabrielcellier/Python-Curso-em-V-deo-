#Gerar 5 números aleatórios na tupla. Após isso mostrar a listagem dos números gerados e o maior e menor.
from random import randint
from time import sleep
n = (randint(0, 1000), randint(0, 1000), randint(0, 1000),
     randint(0, 1000), randint(0, 1000))
print ('Sortearemos cinco números entre 0 e 1000. Mostraremos os valores e qual o menor e o maior deles!')
sleep(1)
print (f'Os números sorteados foram {n}')
sleep(1)
print (f'Dentre os números sorteados o maior foi o {max(n)} e o menor {min(n)}.')