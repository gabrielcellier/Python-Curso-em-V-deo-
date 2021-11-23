#Perguntar os valores e criar uma matriz (3x3) com os valores dados. Mostrar a matriz ao usuário.
from time import sleep
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range (0, 3):      #for para as linhas
    for c in range (0, 3):   #for para as colunas. A cada linha percorrerá o c 3x (range(0, 3))
        matriz[l][c] = int(input(f'Digite o valor de [{l}, {c}]: '))
sleep(0.5)
for l in range (0, 3):
    for c in range (0, 3):
        print(f'[{matriz[l][c]:^6}]', end='')
    print()  #para no final de cada linha ele desça 1 linha
#nesse método ele cria as listas com valores 0 e substitui eles. poderia criar zerada e ir por append.