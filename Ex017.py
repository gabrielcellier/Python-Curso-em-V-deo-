#Dado o cateto oposto e o adjacente, calcule a hipotenusa
from math import hypot
co = float(input('Digite o comprimento do cateto oposto: '))
ca = float(input('Digite o comprimento do cateto adjacente: '))
hip = hypot(co, ca)
print('Com o cateto oposto {} e cateto adjacente {}, a hipotenusa do triangulo é {:.2f}.'.format(co, ca, hip))

