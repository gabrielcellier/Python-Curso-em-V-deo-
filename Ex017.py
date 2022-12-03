#Dado o cateto oposto e o adjacente, calcule a hipotenusa
from math import hypot
from time import sleep
print('Digite o cateto oposto e o cateto adjacente, calcularemos a hipotenusa.')
sleep(1)
co = float(input('Digite o cateto oposto: '))
ca = float(input('Digite o cateto adjacente: '))
print('------')
sleep(1)
print(f'O cateto oposto é {co}° e o cateto adjacente {ca}°. Sua hipotenusa é {hypot(co, ca):.2f}°.')
