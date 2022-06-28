#Perguntar salário e calcular valor do aumento. aumento de 10% se salário for acima de 1250,00 e 15% se for abaixo.
from time import sleep
print('Calcularemos o aumento do salário. Reajuste de 10% se acima de R$1250 e 15% se for abaixo.')
sleep(1)
salario = float(input('Digite o salário (em reais): R$ '))
sleep(0.5)
if salario > 1250:
    print(f'Salário atual de R$ {salario:.2f}, logo com aumento de 10% ficará R$ {(salario * 1.10):.2f}.')
else:
    print(f'Salário atual de R$ {salario:.2f}, logo com aumento de 15% ficará R$ {(salario * 1.15):.2f}')