#perguntar valor a ser pago e a condição: se for a vista no dinheiro 10% de desconto, a vista no cartão 5%
#2x preço normal, 3x ou mais 20% de juros
valor = float(input('Qual o valor do produto a ser pago R$ '))
metodo = str(input('Qual o método de pagamento (dinheiro ou cartão?): ')).strip().lower()
parcela = int(input('O pagamento será feito em quantas vezes (digitar o número): '))
if parcela == 1 and metodo == 'dinheiro':
    print ('O valor a ser pago será de R$ {:.2f}, pois como o pagamento será a vista no dinheiro são aplicados '
           '10% de desconto sobre o valor original de R$ {:.2f}.'.format(valor * 0.90, valor))
elif parcela == 1 and metodo == 'cartão':
    print ('O valor a ser pago será de R$ {:.2f}, pois como o pagamento será a vista no cartão '
           'são aplicados 5% de desconto sobre o valor original de R$ {:.2f}.'.format(valor * 0.95, valor))
elif parcela == 2:
    print ('O valor a ser pago será de R$ {:.2f}, pois o pagamento será parcelado em 2 vezes '
           'assim sendo cobrado o valor sem qualquer alteração.'.format(valor))
elif parcela >= 3:
    print ('O valor a ser pago será de R$ {:.2f} pois a partir de 3 vezes são adicionados 20% de juros sobre '
           'o valor original de R$ {:.2f}.'.format(valor * 1.20, valor))
#poderia criar uma lista de opções no print(), criar um input() pro cliente digitar o código e usar esse código nas condicionais.