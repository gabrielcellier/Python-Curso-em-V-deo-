#Criar função 'area()' que recebe dimensões de um terreno (largura e comprimento) e mostra a área.
def area(a, b):
    print('~*~' * 10)
    print(f'O terreno tem {l:.2f} x {c:.2f}')
    a = l * c
    print(f'Á área total do terreno é de {a:.2f} metros.')
    print('~*~' * 10)

print('Calculadora de Terreno. Digite a seguir as dimensões do terreno.')
l = float(input('Digite a largura do terreno (em metros): '))
c = float(input('Digite o comprimento do terreno (em metros): '))

area(l, c)