#ler 2 números inteiros e comparar eles, dando mensagem se primeiro for maior, se segundo for maior e
# se os 2 forem iguais.
n1 = int(input('Digite um número inteiro: '))
n2 = int(input('Digite outro número inteiro: '))

if n1 > n2:
    input ('O primeiro número digitado {} é maior que o segundo número {}.'.format(n1, n2))
elif n1 == n2:
    input ('O primeiro número {} e o segundo número {} digitado são iguais.'.format(n1, n2))
else:
    input ('O segundo número digitado {} é maior que o primeiro {}.'.format(n2, n1))
