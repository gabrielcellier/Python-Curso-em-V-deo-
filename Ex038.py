#ler 2 números inteiros e comparar eles, dando mensagem se primeiro for maior, se segundo for maior e
# se os 2 forem iguais.
n1 = int(input('Digite o primeiro número inteiro: '))
n2 = int(input('Digite o segundo número inteiro: '))
if n1 > n2:
    print ('O primeiro número digitado {} é maior que o segundo {}.'.format(n1, n2))
elif n2 > n1:
    print ('O segundo número digitado {} é maior que o primeiro {}.'.format(n2, n1))
else:
    print ('Os números digitados são iguais e foram ambos {}.'.format(n1))

