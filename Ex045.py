#crie um programa pro computador jogar pedra, papel e tesoura com você.
import random
jogador = str(input('Escolha pedra, papel ou tesoura: ')).strip().lower()
computador = ['pedra', 'papel', 'tesoura']
escolha = random.choice(computador)
if jogador == escolha:
    input ('Deu empate! pois o jogador escolheu {} e o computador escolheu {}.'.format(jogador, escolha))
elif jogador == 'pedra' and escolha == 'tesoura':
     input ('O jogador ganhou do computador, pois escolheu pedra e o computador escolheu tesoura.')
elif jogador == 'tesoura' and escolha == 'papel':
    input ('O jogador ganhou do computador, pois escolheu tesoura e o computador escolheu papel.')
elif jogador == 'papel' and escolha == 'pedra':
    input ('O jogador ganhou do computador, pois escolheu papel e o computador escolheu pedra.')
else:
    input ('O computador ganhou, pois escolheu {} e o jogador escolheu {}.'.format(escolha, jogador ))