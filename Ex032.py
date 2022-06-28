#Ler um ano e avisar se ele é bissexto
from time import sleep
print('Digite um ano, vamos dizer se ele é bissexto ou não.')
sleep(1)
ano = int(input('Digite o ano: '))
c1 = (((ano % 4) % 100) % 400) #poderia fazer os 3 cálculos em váriaveis diferentes
sleep(0.5)
if c1 == 0:
    print(f'O ano digitado foi {ano}, ele é um ano bissexto.')
else:
    print(f'O ano digitado foi {ano}, ele não é um ano bissexto.')


