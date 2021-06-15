#ler cateto oposto e adjacente e calcule a hipotenusa
import math
cato = float(input('Digite o cateto oposto do triangulo: '))
cata = float(input('Digite o cateto adjacente do triangulo: '))
hip = pow(cato, 2) + pow(cata, 2)
rep = math.sqrt(hip)
hyp = math.hypot(cato, cata)
print('A hipotenusa de um triangulo com cat oposto {} e cat adj {} é {:.4f}.'.format(cato, cata, hyp))
#poderia elevar o hip a meio (** (1/2)), fazer por meio das contas 'hip e depois 'rep' ou pelo math.hypot


