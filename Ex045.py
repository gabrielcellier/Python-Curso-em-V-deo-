#crie um programa pro computador jogar pedra, papel e tesoura com você.
from random import choice
jogador = str(input('Escolha pedra, papel ou tesoura: ')).strip().lower()
computador = ['pedra', 'papel', 'tesoura']
escolha = choice(computador)
if jogador == escolha:
    print ('Deu empate! pois ambos escolheram {}.'.format(jogador, escolha))
elif jogador == 'pedra' and escolha == 'tesoura':
     print ('O jogador ganhou, pois escolheu pedra e o computador escolheu tesoura.')
elif jogador == 'tesoura' and escolha == 'papel':
    print ('O jogador ganhou pois escolheu tesoura e o computador escolheu papel.')
elif jogador == 'papel' and escolha == 'pedra':
    print ('O jogador ganhou, pois escolheu papel e o computador escolheu pedra.')
else:
    print ('O computador ganhou, pois escolheu {} e o jogador escolheu {}.'.format(escolha, jogador ))
