#ler o primeiro termo e a razão de uma PA e # mostrar os 10 primeiros termos
from time import sleep
import numbers
print('Digite o primeiro termo e a razão da progressão aritmética. Calcularemos os 10 primeiro termos.')
sleep(1)
t = float(input('Digite o primeiro termo: '))
r = float(input('Digite a razão da progressão aritmética: '))
sleep(1)
print(f'A progressão aritmética com primeiro termo {t:.1f} e razão {r:.1f}, tem os 10 primeiros termos: ')
sleep(1)
for c in range (1, 11, 1):
    t += r
    print(f'{t},', end=' ')
    sleep(1)
print('fim!')

