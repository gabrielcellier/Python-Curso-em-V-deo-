#quanto de dinheiro a pessoa tem e quanto vale em dólar (R$3,27 o dólar)
from time import sleep
print('**** CONVERSOR DE MOEDAS ****')
sleep(1)
print('Digite um valor de dinheiro (em reais) e iremos converter o valor para dólar americano (R$3,27 o dólar).')
print('---------')
sleep(1)
n = float(input('Digite o valor do dinheiro: R$ '))
print('---------')
sleep(1)
print(f'O valor digitado foi R${n:.2f}. Sua conversão em dólar é de R${(n/3.27):.2f}.')