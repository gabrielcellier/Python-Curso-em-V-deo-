#pegar salário e mostrar valor com 15% de aumento
from time import sleep
print('Digite o salário (em reais) e calcularemos o valor com reajuste de 15%.')
sleep(1)
s = float(input('Por favor digite o valor do salário em reais. R$ '))
sleep(1)
print(f'O salário atual é de R$ {s:.2f}. Com reajuste de 15% passará a ser R$ {(s * 1.15):.2f}.')