#Sortear dado (1 a 6) para quatro jogadores. Falar o valor dado e depois rankear os jogadores.
from time import sleep
from random import randint
from operator import itemgetter
jogos = {'Jogador 1':randint(1, 6),   #definindo dict já com cada jogador como uma chave e o sorteio do seu valor
         'Jogador 2':randint(1, 6),
         'Jogador 3':randint(1, 6),
         'Jogador 4':randint(1, 6)}
for k, v in jogos.items():
    print(f'O {k} sorteou dado no valor: {v}') #Mostrando o jogador (key) e o valor sorteado (v)
    sleep(0.5)
print('-*-' * 12)
sleep(0.5)
rank = sorted(jogos.items(), key=itemgetter(1), reverse=True) #lista ordenando a partir do item (1)(valor do dado) em ordem decrescente(reverse=True)
print('Ranking dos jogadores pelo valor dos dados: ')
for i, v in enumerate(rank):   #Como 'rank' é uma lista (sorted transforma em lista?), usar enumerate.
    print(f'{i+1}° lugar foi o {v[0]} com o dado {v[1]}')
    sleep(0.5)
#I = índice dos elementos (cada elemento é jogador + valor do dado), logo v[0] = jogador e v[1] = valor do dado


