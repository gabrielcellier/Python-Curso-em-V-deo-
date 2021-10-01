# Perguntar valor a sacar. Informar quantas cédulas serão entregues (valores de 50, 20, 10 e 1)
valor = int(input('Qual o valor que você deseja sacar? R$ '))
total = valor
ced = 50
totalced = 0
while True:
    if total >= ced:  # se valor total for MAIOR que valor de cédula (dá pra tirar cédula, logo)
        total -= ced  # tirar o máximo possível do valor com a cédula, no caso de 50, definido no começo
        totalced += 1
    else:
        if totalced > 0:
            print(f'Total de {totalced} cédulas de R${ced:.2f}')   #como tá escrito antes ele vai sempre escrever antes de fazer o if/elif seguinte
        if ced == 50:  # aqui estamos mudando o valor da nota, abaixando, pra continuar tentando tirar do total
            ced = 20  # se não dá pra tirar mais cédula de 50, mudar pra de 20
        elif ced == 20:
            ced = 10  # se não dá pra tirar mais cédula de 20 do valor, mudar pra de 10
        elif ced == 10:
            ced = 1  # se não dá pra tirar mais cédula de 10, mudar pra de 1
        totalced = 0
        if total == 0:
            break
