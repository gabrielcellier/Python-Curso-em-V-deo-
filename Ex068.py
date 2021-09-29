#programa de jogar par ou ímpar. Ele é interrompido quando o usuário perder.
#Contar quantas vitórias o usuário teve. Perguntar número que o usuário vai dar e se ele quer par ou ímpar.
from time import sleep
from random import randint
vit = 0
while True:
    num = randint(0, 100)
    print ('---' * 10)
    n = int(input('Digite um número p/ jogar par ou ímpar: '))
    pi = str(input('Você quer par ou ímpar (P/I)? ')).strip().lower()[0]
    print ('---' * 10)
    if pi not in 'PpIi':
        print ('O valor indicado de par ou ímpar está errado, favor indicar P ou I')
        pi = str(input('Você quer par ou ímpar (P/I)? ')).strip().lower()[0]
        print ('---' * 10)
    print (f'Seu numero: {n} + o nº do computador: {num} - soma um total de: {n + num}')
    if (n + num) % 2 == 0:
        if pi in 'Pp':
            print ('Parabéns! o número acima é par e você escolheu par, você ganhou!')
            vit += 1
        if pi in 'Ii':
            print ('Você escolheu ímpar e o número é par! você perdeu.')
            break
    if (n + num) % 2 == 1:
        if pi in 'Ii':
            print ('Parabéns! o número acima é ímpar e você escolheu ímpar, você ganhou!')
            vit += 1
        if pi in 'Pp':
            print ('Você escolheu ímpar e o número é par! você perdeu.')
            break
print ('---' * 10)
print (f'O usuário ganhou o total de {vit} vezes seguidas.')


