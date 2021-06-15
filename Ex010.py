#quanto de dinheiro a pessoa tem e quanto vale em dólar (R$3,27 o dólar)
n = float(input('Quantos reais você tem na carteira? R$'))
ud = n/3.27
print('O valor na carteira de {} reais equivale a {:.2f} dólares.'.format(n, n/3.27))
#posso fazer a conta direto no .format() ou pela variável 'ud' que criei