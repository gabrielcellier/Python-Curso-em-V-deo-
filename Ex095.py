#aprimorar ex 093.
from time import sleep
jogador = {}
lista = []
gol = []
totalgol = 0
while True:
    jogador['Nome'] = str(input('Digite o nome do jogador: ')).strip().capitalize()
    jogador['Partidas'] = int(input(f'Quantas partidas o {jogador["Nome"]} jogou? '))
    for g in range (0, jogador['Partidas']):
        gols = int(input(f'Quantos gols o jogador fez na partida {g+1}? '))
        totalgol += gols
        gol.append(gols)
    jogador['Total de gols'] = totalgol
    lista.append(jogador.copy())
    jogador.clear()
    cont = str(input('Deseja continuar (s/n)? ')).strip().lower()[0]
    while cont not in 'sn':
        cont = str(input('Deseja continuar (s/n)? ')).strip().lower()[0]
    if cont in 'Nn':
        break
sleep(1)
print('~*~' * 13)
print(f'{"No.":<5}{"Nome":<15}{"Gols":<6}{"Total":>12}')
print('---' * 12)
for i, v in enumerate(lista):
    print(f'{i:<5}{v["Nome"]:<15}{(gol):<6}{v["Total de gols"]}')