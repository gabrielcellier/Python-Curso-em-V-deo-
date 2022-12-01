# pegar preço e dar valor com desconto de 5% da liquidação
from time import sleep
print('Digite o preço do produto em reais. Calcularemos seu valor com desconto de 5%.')
sleep(1)
v = float(input('Digite o valor do produto em reais. R$ '))
sleep(1)
print(f'O produto de valor R$ {v:.2f} sai por R$ {(v*0.95):.2f} com 5% de desconto aplicado.')
