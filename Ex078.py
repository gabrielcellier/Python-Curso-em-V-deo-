#ler 5 valores númericos e guardar numa lista. Mostrar maior e menor valor e suas posicoes na lista
min = max = posmin = posmax = 0
lista = []
for n in range(0, 5):     #para se adicionar os 5 valores
    lista.append(int(input('Digite um valor númerico inteiro: ')))
    if lista[n] > max or max == 0:   #se o valor for maior que o max definido ou se o max for 0, vai substituir o 'max'
        max = lista[n]
    if lista[n] < min or min == 0:   #se o valor for menor que o min definido ou o min for 0, vai substituir o 'min'
        min = lista[n]
for i, v in enumerate(lista): #verificando a posição. se o v (valor) for igual o max ou min, logo seu i (índice) é a posição do max ou min
    if v == max:
        posmax = i
    if v == min:
        posmin = i
print(f'O maior valor digitado foi {max} na posição {posmax + 1}, o menor foi {min} na posição {posmin + 1}.')




