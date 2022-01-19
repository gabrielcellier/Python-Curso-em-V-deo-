#Função ficha() recebendo nome e gols de um jogador. Criar uma frase falando que jogador fez x gols.
#Se não receber nenhum parametro seja nome ou gols, ainda sim criar frase com 'desconhecido' p/ nome e 0 p/ gols.
def ficha(jogador='desconhecido', gols=0):
    if jogador == '':
        jogador == '<desconhecido>'
    if gols == '':
        gols == '0'
    return f'O jogador {jogador} fez {gols} gol(s) na competição.'

j = str(input('Nome do jogador: ')).capitalize().strip()
g = str(input(f'Gols que {j} marcou (apenas números): ')).strip()   #usamos str para poder aceitar valor caso usuário escreva por extenso
if g.isnumeric():    #caso o valor escrito seja númerico mesmo em str, transformaremos em número (int)
    g = int(g)     #transformando o g numérico de str para int
else:
    g = 0  #se tiver escrito por extenso o valor, transformaremos em 0.
print(ficha(j, g))
