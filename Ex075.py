#Ler 4 números digitados. Mostrar: 1) Qts vezes apareceu o '9'; 2) Posição do primeiro valor 3;
#c) Quais números pares.
from time import sleep
print ('Digite 4 números: Mostraremos qt de 9; Onde está o primeiro 3 e quantos pares foram escritos.')
numeros = (int(input('Digite um número: ')), int(input('Digite outro número: ')),
           int(input('Digite outro número: ')), int(input('Digite outro número: ')))
print (f'O usuário digitou os números: {numeros}')
print ('---' * 10)
sleep(0.8)
print(f'O número 9 aparece {numeros.count(9)} vezes.')
if 3 in numeros:
    print(f'O número 3 aparece pela primeira vez na posição {numeros.index(3) + 1}.')
print('Os números pares digitados foram:')
for n in numeros:
    if n % 2 == 0:
        print (n, end=' ')