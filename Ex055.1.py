#ler peso de 5 pessoas e mostrar qual o maior e o menor
from time import sleep
maior = menor = 0
print('Digite o peso de 5 pessoas, informaremos o menor e maior valor.')
sleep(1)
for c in range (1, 6):
    peso = float(input('Digite o peso (em kg): '))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
    sleep(1)
print(f'O menor valor de peso foi de {menor:.1f} kg e o maior de {maior:.1f} kgs.')

#nesse modo criamos uma lista que será atualizada com todos os valores de 'peso' inseridos
#usando max() e min() selecionaremos os maiores e menores valores dessa lista