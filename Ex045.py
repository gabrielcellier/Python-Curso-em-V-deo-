#crie um programa pro computador jogar pedra, papel e tesoura com você.
from time import sleep
from random import choice
user = 0
print('Jogo de pedra, papel e tesoura. Escolha o código referente a sua escolha e você jogará contra o computador.')
sleep(1)
print('''Faça sua escolha:
[ 1 ] Pedra
[ 2 ] Papel
[ 3 ] Tesoura''')
while True:
    esc = int(input('Digite o código da sua escolha: '))
    sleep(1)
    if esc == 1:
        print('Você escolheu PEDRA. Boa sorte.')
        user = 'pedra'
        break
    if esc == 2:
        print('Você escolheu PAPEL. Boa sorte.')
        user = 'papel'
        break
    if esc == 3:
        print('Você escolheu TESOURA. Boa sorte.')
        user = 'tesoura'
        break
    else:
        print(f'Código digitado foi {esc}. Esse código é inválido. Digite um código válido.')
computador = ['pedra', 'papel', 'tesoura']
escolha = choice(computador)
sleep(1)
if esc == 1 and escolha == 'pedra' or esc == 2 and escolha == 'papel' or esc == 3 and escolha == 'tesoura':
    print(f'TEMOS UM EMPATE! Ambos escolheram {escolha}.')
if esc == 1 and escolha == 'tesoura' or esc == 2 and escolha == 'pedra' or esc == 3 and escolha == 'papel':
    print(f'VOCÊ VENCEU! Pois o computador escolheu {escolha} e você escolheu {user}.')
else:
    print(f'VOCÊ PERDEU! Pois o computador escolheu {escolha} e você escolheu {user}')
