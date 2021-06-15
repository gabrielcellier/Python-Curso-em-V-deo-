# pegar preço e dar valor com desconto de 5% da liquidação
p = float(input('Digite o valor original do produto: R$'))
d = p * 0.95
print('O produto de valor original R${} tem o valor de R${:.2f} com desconto de 5%.'.format(p, p * 0.95))
#poder fazer a conta direto no .format() ou com a variável 'd' que foi criada
