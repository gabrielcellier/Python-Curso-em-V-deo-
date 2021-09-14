#ler 2 valores e criar um menu na tela com [1] somar, [2] multiplicar, [3] qual o maior
#[4] novos números e [5] sair do programa e quando o usuario escolher realizar a operação escolhida
from time import sleep
print ('Este programa irá fazer cálculos com os 2 números que você colocar a seguir')
n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))
opcao = 0
while opcao != 5:
    print('''
    [1] somar
    [2] multiplicar
    [3] qual o maior número
    [4] trocar os números
    [5] sair do programa''')
    opcao = int(input('>>>>Digite qual a opção desejada: '))
    if opcao == 1:
        print ('A soma entre {} e {} é {}.'.format(n1, n2, n1 + n2))
    if opcao == 2:
        print ('A multiplicação entre {} e {} resulta em {:.1f}.'.format(n1, n2, n1 * n2))
    if opcao == 3:
        if n1 > n2:
            print ('O primeiro número, {}, é maior que o segundo, {}.'.format(n1, n2))
        elif n2 > n1:
            print ('O segundo número, {}, é maior que o primeiro, {}.'.format(n1, n2))
        else:
            print ('Os números digitados são iguais')
    if opcao == 4:
        print ('Como solicitado você poderá escrever novos números.')
        n1 = float(input('Digite o primeiro número: '))
        n2 = float(input('Digite o segundo número: '))
    if opcao == 5:
        print ('Finalizando o programa...')
    else:
        print ('Erro! o código digitado não corresponde a nenhuma opção!')
    print ('----------')
    sleep(1.5)
print ('O programa foi finalizado')