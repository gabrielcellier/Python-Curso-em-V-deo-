# ler duas notas e mostrar a média delas.
from time import sleep
print('Digite duas notas. Mostraremos a média entre elas.')
sleep(1)
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
sleep(1)
print(f'A média das notas {n1:.2f} e {n2:.2f} é {((n1+n2)/2):.2f}.')


