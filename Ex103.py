#Função ficha() recebendo nome e gols de um jogador. Criar uma frase falando que jogador fez x gols.
#Se não receber nenhum parametro seja nome ou gols, ainda sim criar frase com 'desconhecido' p/ nome e 0 p/ gols.
def ficha(jogador='desconhecido', gols=0):
    if jogador == '':
        jogador = '<desconhecido>'
    if gols == '':
        gols = 0
    return f'O jogador {jogador} marcou {gols} gol(s) na competição.'

jogador = str(input('Digite o nome do jogador: ')).strip().capitalize()
gols = str(input('Digite a quantidade de gols que {jogador} marcou: '))
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0
print(ficha(jogador, gols))

