#Computador sorteia um numero de 0 a 5 e a pessoa tenta descobrir qual é. Avisar se acertou ou errou
import random
num = int(input('Digite um número de 0 a 5: '))
sorteio = random.randint(0, 5)
lista = [0, 1, 2, 3, 4, 5]
sorteio2 = random.choice(lista)
if sorteio2 == num:
    print ('Parabéns! O numero digitado foi {} e o sorteado foi {}'.format(num, sorteio2))
else:
    print ('Você errou! O numero digitado foi {} e o sorteado foi {}'.format(num, sorteio2))
#pode ser feito pelo .randint (sorteio) ou criando lista e escolhendo dela .choice(lista)

