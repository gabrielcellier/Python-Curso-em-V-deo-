#perguntar valor a ser pago e a condição: se for a vista no dinheiro 10% de desconto,
# a vista no cartão 5%, 2x preço normal, 3x ou mais 20% de juros
from time import sleep
print('Digite o valor a ser pago, o método e o parcelamento, calcularemos o valor final.')
sleep(1)
valor = float(input('Digite o valor a ser pago (em reais): R$ '))
print('''Digite o método de pagamento:
[ 1 ] Dinheiro
[ 2 ] Cartão''')
while True:
    met = int(input('Digite o código do método escolhido: '))
    if met != 1 and met != 2:
        print('Código inválido. Digite novamente o método escolhido.')
        sleep(1)
    if met == 1:
        print(f'O método de pagamento escolhido foi DINHEIRO.')
        break
    if met == 2:
        print(f'O método de pagamento escolhido foi CARTÃO.')
        break
sleep(0.5)
while True:
    vezes = int(input('Digite o parcelamento da compra (até 3x): '))
    if vezes in range (1, 4):
        print(f'A compra será parcelada em {vezes}x.')
        break
    else:
        print('Parcelamento inválido. Pode-se parcelar em até 3x. Escolha novamente.')
        sleep(0.5)
sleep(1)
if vezes == 1:
    if met == 1:
        print(f'O produto de valor R$ {valor:.2f} sairá por R$ {(valor * 0.90):.2f}, aplicado 10% de desconto.')
    if met == 2:
        print(f'O produto de valor R$ {valor:.2f} sairá por R$ {(valor * 0.95):.2f}, aplicado 5% de desconto.')
if vezes == 2:
    print(f'O produto de valor R$ {valor:.2f} sairá por R$ {valor}, sem nenhum desconto.')
if vezes == 3:
    print(f'O produto de valor R$ {valor:.2f} sairá por R$ {(valor * 1.2):.2f}, com juros de 20%.')