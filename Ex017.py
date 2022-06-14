#Dado o cateto oposto e o adjacente, calcule a hipotenusa
from math import hypot
from time import sleep
print('Digite o cateto oposto e o cateto adjacente que calcularemos a hipotenusa do triangulo.')
sleep(1)
co = float(input('Digite o cateto oposto: '))
ca = float(input('Digite o cateto adjacente: '))
sleep(1)
print('---------')
print(f'Com o cateto oposto {co}° e cateto adjacente {ca}° a hipotenusa é {hypot(co, ca):.1f}.')

