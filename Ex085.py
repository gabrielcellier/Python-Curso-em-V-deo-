#Escrever 7 números. Dentro da lista já separar os pares e ímpares.
#No fim mostrar esses valores em ordem crescente.
numeros = [[], []]
valor = 0
for n in range (0, 7):
    valor = int(input(f'Digite o {n+1}° valor: '))
    if valor % 2 == 0:
        numeros[0].append(valor)  #p/ add o valor par na primeira lista de números
    else:
        numeros[1].append(valor)   #p/ add o valor ímpar na segunda lista de números
numeros[0].sort()
numeros[1].sort()
print(f'Os números pares digitados foram: {numeros[0]}.')
print(f'Os números ímpares digitados foram: {numeros[1]}.')


