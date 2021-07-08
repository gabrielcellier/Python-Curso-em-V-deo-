#escrever um número inteiro e pedir pro usuário escolher sua base de conversão
#1 p/ binário, 2 p/ octal e 3 p/ hexadecimal
num = int(input('Digite um número inteiro: '))
print ('''escolha uma das bases para conversão:
[ 1 ] para binário
[ 2 ] para octal
[ 3 ] para hexadecimal''')
opcao = int(input('Digite a sua opção: '))
if opcao == 1:
    print ('O número digitado {} quando convertido para binário se torna {}.'.format(num, bin(num)[2:]))
elif opcao == 2:
    print ('O número digitado {} quando convertido para octal se torna {}.'.format(num, oct(num)[2:]))
elif opcao == 3:
    print ('O número digitado {} quando convertido para hexadecimal se torna {}.'.format(num, hex(num)[2:]))
else:
    print ('Opção inválida. Tente novamente')
