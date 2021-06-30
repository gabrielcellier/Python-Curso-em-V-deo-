#Perguntar comprimento de 3 retas e falar se é possível formar um triangulo a partir delas.
a = float(input('Digite o primeiro segmento: '))
b = float(input('Digite o segundo segmento: '))
c = float(input('Digite o terceiro segmento: '))
ab = a - b
ac = a - c
bc = b - c
if bc < a < (b + c) and ac < b < (a + c) and ab < c < (a + b):
    print ('O triangulo pode ser formado com os segmentos dados ({:.0f}, {:.0f}, {:.0f}).'.format(a, b, c))
else:
    print ('Os segmentos dados não podem formar um triangulo.')
#poderia ser usado if < b + c and b < c + a and c < a + b