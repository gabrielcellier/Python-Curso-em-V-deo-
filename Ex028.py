#Computador sorteia um numero de 0 a 5 e a pessoa tenta descobrir qual é. Avisar se acertou ou errou
import random
num = int(input('Tente adivinha o número de 0 a 5 que o computador irá sortear: '))
lista = [0, 1, 2, 3, 4, 5]
sorteio = random.choice(lista)
if sorteio == num:
    print ('Parabéns o número digitado foi {} e o sorteado foi {}.'.format(num, sorteio))
else:
    print ('Infelizmente você errou pois o número digitado foi {} e o sorteado foi {}'.format(num, sorteio))

