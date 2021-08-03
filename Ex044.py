#perguntar valor a ser pago e a condição: se for a vista no dinheiro 10% de desconto,
# a vista no cartão 5%, 2x preço normal, 3x ou mais 20% de juros
valor = float(input('Qual o valor do produto: R$ '))
parcela = int(input('Em quantas vezes será o pagamento: '))
print (''' O método de pagamento por ser por:
[ 1 ] Dinheiro.
[ 2 ] Cartão.''')
metodo = int(input('Digite o código do método de pagamento: '))
if metodo == 1 and parcela == 1:
    print ('O valor será de R$ {} pois aplicou-se 10% de desconto.'.format(valor * 0.90))
if metodo == 2 and parcela == 1:
    print ('O valor será de R$ {} pois aplicou-se 5% de desconto.'.format(valor * 0.95))
if parcela == 2:
    print ('O valor será de R$ {}, sem qualquer desconto.'.format(valor))
if parcela >= 3:
    print ('O valor será de R$ {}, acrescido de 20% de juros.'.format(valor * 1.2))