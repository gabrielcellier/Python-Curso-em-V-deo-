#Ler 4 números digitados. Mostrar: 1) Qts vezes apareceu o '9'; 2) Posição do primeiro valor 3;
#c) Quais números pares.
from time import sleep
print (f'O usuário deverá digitar um número quatro vezes.')
sleep(0.5)
numeros = (int(input('Digite um número: ')), int(input('Digite mais um número: ')),
           int(input('Digite outro número: ')), int(input('Digite outro número: ')))
print(f'Os números digitados pelo usuário foram: {numeros}')
print('-*-' * 13)
print(f'O número "9" foi digitado {numeros.count(9)} vezes ao todo.')
print('-*-' * 13)
sleep(0.5)
if 3 in numeros:
    print(f'O primeiro valor "3" foi digitado pela primeira vez na posição {numeros.index(3) + 1}.')
else:
    print('O valor 3 não foi digitado nenhuma vez, logo não foi encontrado!')
print('-*-' * 13)
sleep(0.5)
print('A seguir os números pares que foram digitados pelo usuário:')
for n in numeros:
    if n % 2 == 0:
        print (f'O valor digitado {n} é par.')