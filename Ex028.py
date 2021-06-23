#Computador sorteia um numero de 0 a 5 e a pessoa tenta descobrir qual é. Avisar se acertou ou errou
import random
num = int(input('Tente adivinhar o número de 0 a 5 que o computador irá sortear: '))
lista = [0, 1, 2, 3, 4, 5]
sorteio = random.choice(lista)
#sorteio1 = random.randint(0, 5)
if sorteio == num:
    print ('Parabéns! O número digitado foi {} e o sorteado foi {}.'.format(num, sorteio))
else:
    print ('Infelizmente você errou pois o número digitado foi {} e o sorteado foi {}'.format(num, sorteio))
#o sorteio pode ser feito pelo .choice() a partir de uma lista ou .randint(x,y) nos intervalos x a y
