#Perguntar comprimento de 3 retas e falar se é possível formar um triangulo a partir delas.
from time import sleep
print('Digite o comprimento das três retas, vamos checar se é possível formar um triângulo a partir delas')
sleep(1)
a = float(input('Digite o primeiro segmento: '))
b = float(input('Digite o segundo segmento: '))
c = float(input('Digite o terceiro segmento: '))
ab = a - b
ac = a - c
bc = b - c
if bc < a < (b + c) and ac < b < (a + c) and ab < c < (a + b):
    print(f'Com os segmentos {a}, {b} e {c} é possível de se formar um triângulo.')
else:
    print (f'Com os segmentos {a}, {b} e {c} não é possível de se formar um triângulo.')
#poderia ser usado if < b + c and b < c + a and c < a + b