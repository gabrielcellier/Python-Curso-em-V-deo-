#Criar função 'area()' que recebe dimensões de um terreno (largura e comprimento) e mostra a área.
from time import sleep
def area(a, b):
    print('~*~' * 14)
    print(f'O terreno tem as dimensões de {a:.2f} m x {b:.2f} m.')
    area = a * b
    sleep(0.8)
    print(f'A área total do terreno é de {area:.2f} m².')
    print('~*~' * 14)

print('Vamos calcular a área total do terreno, digite os valores de comprimento e largura.')
c = float(input('Digite o comprimento total do terreno (em metros): '))
l = float(input('Digite a largura total do terreno (em metros): '))
area(l, c)

