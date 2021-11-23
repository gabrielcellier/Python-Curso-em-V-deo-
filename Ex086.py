#Perguntar os valores e criar uma matriz (3x3) com os valores dados. Mostrar a matriz ao usuário.
from time import sleep
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range (0, 3):
    for c in range (0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
sleep(0.6)
for l in range (0, 3):
    for c in range (0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()

#nesse método ele cria as listas com valores 0 e substitui eles. poderia criar zerada e ir por append.