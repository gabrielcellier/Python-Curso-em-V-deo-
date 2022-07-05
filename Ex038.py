#ler 2 números inteiros e comparar eles, dando mensagem se primeiro for maior, se segundo for maior e
# se os 2 forem iguais.
from time import sleep
print('Digite dois números, vamos comparar eles e falar qual é o maior e o menor.')
n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))
sleep(0.5)
if n1 > n2:
    print(f'O primeiro número ({n1:.2f}) digitado é maior que o segundo ({n2:.2f}).')
elif n2 > n1:
    print(f'O segundo número ({n2:.2f}) digitado é maior que o primeiro ({n1:.2f}).')
else:
    print(f'Os dois números digitados ({n1:.2f}) são iguais.')


