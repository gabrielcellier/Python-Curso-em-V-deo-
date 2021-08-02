#escrever um número inteiro e pedir pro usuário escolher sua base de conversão
#1 p/ binário, 2 p/ octal e 3 p/ hexadecimal
num = int(input('Digite um número inteiro: '))
print ('''Escolha uma das opções a seguir:
[ 1 ] transformar o número em binário
[ 2 ] transformar o número em octal
[ 3 ] transformar o número em hexadecimal''')
escolha = int(input('Digite uma opção das oferecidas anteriormente: '))
if escolha == 1:
    print ('O número digitado foi {} e sua versão binária é {}.'.format(num, bin(num)[2:]))
elif escolha == 2:
    print ('O número digitado foi {} e sua versão octal é {}'.format(num, oct(num)[2:]))
elif escolha == 3:
    print ('O número digitado foi {} e sua versão hexadecimal é {}'.format(num, hex(num)[2:]))
