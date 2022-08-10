#ler 2 valores e criar um menu na tela com [1] somar, [2] multiplicar, [3] qual o maior
#[4] novos números e [5] sair do programa e quando o usuario escolher realizar a operação escolhida
from time import sleep
print('Digite 2 valores inteiros. Depois escolha a opção do que você deseja fazer com esses valores.')
sleep(1)
while True:
    n1 = input('Digite o primeiro número: ').strip()
    if n1.isnumeric():
        print('Valor válido! Agora digite o segundo valor.')
        n1 = int(n1)
        break
    else:
        print('Valor inválido. Digite um número inteiro.')
        sleep(1)
sleep(1)
while True:
    n2 = input('Digite o segundo número: ').strip()
    if n2.isnumeric():
        print('Valor válido. Agora selecione a opção conforme a operação desejada.')
        n2 = int(n2)
        break
    else:
        print('Valor inválido. Digite um número inteiro.')
        sleep(1)
sleep(1)
print('''A seguir as operações possíveis e seus códigos:
[ 1 ] soma dos valores
[ 2 ] multiplicação dos valores
[ 3 ] Qual o maior valor
[ 4 ] Digitar novos valores
[ 5 ] Sair do programa''')
sleep(0.5)
opcao = 0
while opcao != 5:
    opcao = int(input('Digite o código da operação desejada: '))
    sleep(0.5)
    if opcao == 1:
        print(f'A soma de {n1} + {n2} = {n1+n2}.')
    if opcao == 2:
        print(f'A multiplicação de {n1} x {n2} = {n1*n2}.')
    if opcao == 3:
        if n1 > n2:
            print(f'O primeiro número digitado, "{n1}" é maior que o segundo "{n2}".')
        if n2 > n1:
            print(f'O segundo número digitado "{n2}" é maior que o primeiro "{n1}".')
        else:
            print(f'Os dois números digitados foram {n1} e são iguais.')
    if opcao == 4:
        print('Conforme solicitado digite novos números inteiros: ')
        sleep(0.5)
        while True:
            n1 = (input('Digite o primeiro número inteiro: '))
            n2 = (input('Digite o segundo número inteiro: '))
            if n1.isnumeric() and n2.isnumeric():
                n1 = int(n1)
                n2 = int(n2)
                break
            else:
                print('Um ou mais valores são inválidos. Digite apenas números inteiros.')
    if opcao == 5:
        print('Finalizando o programa.')
    else:
        print('Código inválido! Digite um código entre 1 e 5.')
sleep(1)
print('Programa encerrado!')