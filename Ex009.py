#pegar um numero dado e mostrar sua tabuada
from time import sleep
x = 1
n = ""
print('Digite um número inteiro. Mostraremos sua tabuada.')
sleep(1)
while type(n) != int:
    n = input('Digite um número inteiro: ')
    if n.isnumeric():
        n = int(n)
        sleep(1)
    else:
        sleep(0.5)
        print('Valor inválido. Favor digitar um número inteiro.')
print(f'Tabuada do {n}.')
while x != 11:
    sleep(0.5)
    print(f'{n} x {x} = {n*x}.')
    x += 1