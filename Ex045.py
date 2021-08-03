#crie um programa pro computador jogar pedra, papel e tesoura com você.
from random import choice
print ('''Escolha uma das opções a seguir: [1]: pedra, [2]: papel ou [3]: tesoura''')
escolha = int(input('Digite o código da sua escolha: '))
computador = ['pedra', 'papel', 'tesoura']
sorteio = choice(computador)
if escolha == 1 and sorteio == 'tesoura':
    print ('O jogador venceu pois escolheu pedra o computador escolheu papel')
elif escolha == 2 and sorteio == 'pedra':
    print ('O jogador venceu pois escolheu papel e o computador escolheu pedra')
elif escolha == 3 and sorteio == 'papel':
    print ('O jogador venceu pois escolheu tesoura e o computador escolheu papel')
elif escolha == 1 and sorteio == 'pedra' or escolha == 2 and sorteio 'papel' or escolha == 3 and sorteio 'tesoura':
    print ('Deu empate pois jogador e computador fizeram a mesma escolha.')
else:
    print ('O computador venceu pois escolheu {}, batendo a escolha do jogador')
