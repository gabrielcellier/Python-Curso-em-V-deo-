#o computador pensa num numero entre 0 a 10. O jogador tenta adivinhar o numero até acertar
#ao acertar mostrar o numero de tentativas
from random import randint
from time import sleep
tent = 0
sorteio = randint(0, 10)
acerto = False
print('O computador sorteará um número entre 0 a 10. Tente adivinha qual número foi sorteado.')
sleep(1)
while not acerto:
    n = input('Digite um número de 0 a 10: ')
    tent += 1
    if n.isnumeric():
        n = int(n)
        if 0 <= n <= 10:
            if n == sorteio:
                acerto = True
            else:
                if n > sorteio:
                    print('O número sorteado é menor. Tente novamente.')
                elif n < sorteio:
                    print('O número sorteado é maior. Tente novamente.')
        else:
            print('Número fora do intervalo entre 0 a 10. Digite um número nesse intervalo.')
    else:
        print('Erro! Digite um número inteiro.')
    sleep(0.5)
print(f'Você acertou! Ao todo foram necessárias {tent} tentativas.')







