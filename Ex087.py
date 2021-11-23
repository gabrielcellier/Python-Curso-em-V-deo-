#Pegue a matriz do ex anterior. Mostrar: a) Soma dos n pares, B) Soma dos n da 3° coluna,
#C) Maior n da 2° linha
from time import sleep
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma = somac = 0
for l in range (0, 3):   #para fazer a matriz
    for c in range (0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
for l in range (0, 3):     #para calcular valores da terceira coluna
    somac += matriz[l][2]  #valores de 3 coluna são sempre c = 2 logo por isso o [2] no lugar de [c]
for l in range (0, 3):     #para mostrar a matriz
    for c in range (0, 3):
        print(f'[{matriz[l][c]:^6}]', end='')
        if matriz[l][c] % 2 == 0:    #para selecionar os valores pares da matriz
            soma += matriz[l][c]     #os valores pares são adicionados na variável soma
    print()
print('-*-' * 12)
sleep(0.5)
print(f'A soma de todos os números pares é {soma}.')
print(f'A soma dos números da terceira coluna é {somac}.')
print(f'O maior número da segunda linha é {max(matriz[1])}.')
print('-*-' * 12)

#para se achar o maior valor poderia ter sido feito algo semelhante ao usado para calcular valores da 3 coluna.