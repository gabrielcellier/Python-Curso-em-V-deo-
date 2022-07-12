#fazer tabuada do número que o usuário colocar usando for
from time import sleep
print('Digite um número inteiro. Vamos calcular a sua tabuada.')
while True:
    n = input('Digite o número inteiro: ')
    if n.isnumeric():
        n = int(n)
        print(f'O número digitado foi {n}.')
        break
    else:
        print('Valor inválido. Digite de novo.')
sleep(1)
for c in range(1, 10, 1):
    print(f'Tabuada do {n}: {n} x {c} = {n * c}.')
    sleep(1)
print(f'Fim! Acima a tabuada do {n}.')


