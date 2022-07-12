#ler um número digitado e ver se ele é um número primo
from time import sleep
tot = 0
print('Digite um número inteiro, vamos checar se ele é um número primo.')
sleep(1)
while True:
    n = input('Digite um número inteiro: ')
    if n.isnumeric():
        n = int(n)
        print(f'O número digitado foi {n}.')
        break
    else:
        print('Número inválido. Digite um número inteiro.')
sleep(1)
for c in range (1, n+1): #n+1 faz com que se cheque até o número digitado.
    if n % c == 0
        tot += 1 #somará 1 a cada vez que o número foi divisivel. se for só 2x dai é numero primo.
if tot == 2:
    print(f'O número digitado {n} é divisível apenas duas vezes, logo é um número primo.')
else:
    print(f'Como o número digitado {n} é divisível mais de duas vezes, ele não é um número primo.')