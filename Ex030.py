#Ler um número dado e avisar se ele é par ou ímpar
from time import sleep
print('Digite um número, vamos descobrir se ele é par ou ímpar.')
sleep(0.5)
numero = float(input('Digite um número: '))
if numero % 2 == 0:
    print(f'O número digitado foi {numero} e ele é par.')
else:
    print(f'O número digitado foi {numero} e ele é ímpar.')
