#Ler nome do jogador e número de partidas. Perguntar qt de gols pra CADA partida.
#Guardar num dicionário o nome, qt de partidas e total de gols.
from time import sleep
jogador = {}
totalgol = 0
jogador['Nome'] = str(input('Qual o nome do jogador? ')).strip().capitalize()
jogador['Partidas'] = int(input('Quantas partidas ele participou? '))
for g in range (0, jogador['Partidas']):  #para perguntar conforme o tanto de partidas
    gols = int(input(f'Quantos gols o jogador fez na {g+1}° partida? '))
    totalgol += gols
jogador['Total de gols'] = totalgol
sleep(1)
print('-*-' * 12)
print('Dados do jogador:')
for k, i in jogador.items():
    print(f'{k}: {i}')
    sleep(0.5)
print('-*-' * 12)




