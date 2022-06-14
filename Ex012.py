# pegar preço e dar valor com desconto de 5% da liquidação
from time import sleep
print('Digite o valor do produto (em reais) que calcularemos 5% de desconto sobre o valor.')
sleep(0.5)
p = float(input('Digite o valor do produto: R$ '))
sleep(0.5)
print(f'O produto tem preço original de R$ {p:.2f}, com desconto de 5% o preço cai para R$ {(p * 0.95):.2f}.')
