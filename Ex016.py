#Crie um programa que lê um número real qualquer e mostre sua porção inteira ex: 6.7263 parte inteira: 6
from math import trunc
from time import sleep
print('Digite um número decimal qualquer, nós mostraremos sua porção inteira.')
sleep(1)
n = float(input('Digite um número decimal qualquer: '))
sleep(1)
print(f'O número digitado foi {n}, sua porção inteira é {trunc(n)}.')

#poderia ser usado math.floor() também, que desce para o primeiro número inteiro
