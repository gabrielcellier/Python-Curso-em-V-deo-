# ler duas notas e mostrar a média delas.
from time import sleep
print('Digite duas notas, iremos calcular a média delas.')
sleep(0.5)
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
sleep(0.5)
print('----------------------')
print(f'A 1° nota foi {n1}, a 2° nota foi {n2}. A média delas é {((n1+n2)/2):.1f}')

#colocar n1+n2 em () para que essa adição seja feita primeiro, antes da divisão pro 2.


