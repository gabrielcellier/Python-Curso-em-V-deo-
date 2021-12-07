#aprimorar ex 093, perguntando se quer continuar e fazendo um quadro com os dados. A partir disso
#perguntar qual jogador que você quer ver mais detalhes e depois mostrar esses detalhes
from time import sleep
jogador = {}
time = []
partidas = []
while True:
    jogador.clear()  #limpar os dados para entrar os dados do próximo jogador
    jogador['Nome'] = str(input('Nome do jogador: ')).capitalize().strip()
    tot = int(input(f'Quantas partidas {jogador["Nome"]} jogou? '))  #para saber o tanto de partidas
    partidas.clear()
    for c in range (0, tot):  #definimos a pergunta dos gols a partir da qt de partidas
        partidas.append(int(input(f'Quantos gols marcou na partida {c+1}? '))) #add os dados gol por gol na lista partida
    jogador['Gols'] = partidas[:] #copiar a quantidade de gols pra key 'gols' de forma separada por partida
    jogador['Total de gols'] = sum(partidas) #soma de todos os gols respondidos por partida
    time.append(jogador.copy())
    cont = str(input('Deseja continuar (s/n)? ')).strip().lower()[0]
    while cont not in 'sn':
        print('Resposta inválida! Responda S ou N.')
        cont = str(input('Deseja continuar (s/n)? ')).strip().lower()[0]
    if cont in 'n':
        break
sleep(1)
print('---' * 18)
print('Cod.', end='')  #primeiro item do índice da tabela
for i in jogador.keys():
    print(f'{i:<15}', end='') #colocar as keys do dict (nome, gols, total gols) com espaçamento de 15 cada.
print()
print('---' * 18)
for i, v in enumerate(time):
    print(f'{i:>3} ', end='')   #para colocar os números do 'cod.'
    for d in v.values():
        print(f'{str(d):<15}', end='')   #preenchendo os dados de gols e total de gols na tabela
    print()
print('---' * 18)
while True:  #aqui a busca onde usuário digitará o código do jogador que ele quer mais detalhes
    busca = int(input('Qual jogador você deseja ver mais informações? (digite 999 para encerrar): '))
    if busca == 999:
        break
    if busca >= len(time): #se digitar valor maior ou igual o número de jogadores da lista (lista começo do 0) da erro.
        print('Erro! O código de jogador digitado não existe. Digite novamente.')
    else:
        print(f'Você digitou o código {busca}, referente ao jogador {time[busca]["Nome"]}: ')
        for i, g in enumerate(time[busca]['Gols']):  #queremos o jogador do código 'busca' na lista time, no índice 'gols', por isso digitado assim
            print(f'Na partida {i} o jogador marcou {g} gols.')
    print('---' * 18)
print('Programa encerrado.')
