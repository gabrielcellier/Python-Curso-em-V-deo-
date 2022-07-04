#escrever um número inteiro e pedir pro usuário escolher sua base de conversão
#1 p/ binário, 2 p/ octal e 3 p/ hexadecimal
from time import sleep
print('Digite um número. Depois escolha o código correspondente a conversão desejada.')
sleep(0.8)
num = int(input('Digite um número inteiro: '))
sleep(0.5)
print('''Escolha o código da conversão desejada:
[1] Transformar o número em binário
[2] Transformar o número em octal
[3] Transformar o número em hexadecimal''')
while True:
    cod = int(input('Digite o código (de 1 a 3) da conversão desejada: '))
    sleep(0.5)
    if cod in range (1, 4):
        print(f'O código escolhido foi {cod}.')
        break
    else:
        print(f'O código {cod} é inválido. Digite um código entre 1 e 3.')
sleep(0.5)
if cod == 1:
    print(f'O número {num} transformado em binário fica {bin(num)[2:]}.')
if cod == 2:
    print(f'O número {num} transformado em octal fica {oct(num)[2:0]}.')
if cod == 3:
    print(f'O número {num} transformado em hexadecimal fica {hex(num)[2:0]}')


