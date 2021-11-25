#Perguntas quantos jogos deseja fazer. Cada jogo serão sorteados 6 números diferentes.
#Listar eles no fim em ordem crescente.
from random import randint
from time import sleep
sorteio = []
jogos = []
tot = 1
print('Por favor responda a quantidade de jogos de 6 números que deseja calcular.')
print('-*-' * 12)
njogos = int(input('Quantos jogos você deseja fazer? '))
while tot <= njogos:
    while True:
        num = randint(1, 60)     #sortear número entre 1 e 60
        if num not in sorteio:   #se número sorteado não tiver na lista ele entrará
            sorteio.append(num)
        if len(sorteio) == 6:    #quando lista tiver 6 números o sorteio de números irá parar
            break
    sorteio.sort()
    jogos.append(sorteio[:])
    sorteio.clear()
    tot += 1      #cada ciclo é uma jogada desejada pelo usuário, ao chegar no valor de 'njogos' a repetição irá parar
sleep(0.2)
print('-*-' * 12)
print(f'Ao todo você decidiu fazer {njogos}, seguem eles:')
for i, l in enumerate(jogos):
    print(f'Jogo número {i+1}: {l}')
    sleep(0.7)
print('-*-' * 12)





