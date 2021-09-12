#o computador pensa num numero entre 0 a 10. O jogador tenta adivinhar o numero até acertar
#ao acertar mostrar o numero de tentativas
from random import randint
tentativa = 0
sorteio = randint(0, 10)
print ('Olá, jogaremos um jogo de adivinhação, onde você chutará o número que eu estou pensando!')
n = int(input('Qual número entre 0 a 10 que eu estou pensando? '))
while n != sorteio:
    n = int(input('Errou! Digite outro número de 0 a 10 que estou pensando: '))
    tentativa += 1
print ('Finalmente! O número que pensei foi o {}. Você tentou {} vezes até '
       'conseguir acertar.'.format(sorteio, tentativa))
