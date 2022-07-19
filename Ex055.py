#ler peso de 5 pessoas e mostrar qual o maior e o menor
from time import sleep
#FEITO PELO MÉTODO DA LISTA. Criamos a lista e pegamos o menor e maior valor.
lista = []
print('Digite o peso de 5 pessoas, informaremos o menor e maior valor.')
sleep(1)
for c in range (1, 6):
    peso = float(input('Digite o peso (em kg): '))
    lista += [peso]
    sleep(1)
print('O peso das 5 pessoas foram computados.')
sleep(1)
print(f'O menor peso foi de {min(lista):.1f} kg, o maior de {max(lista):.1f} kg.')
