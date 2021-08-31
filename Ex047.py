#mostrar todos os números pares que existirem entre 1 e 50.
from time import sleep
for c in range (1, 51):
    if c % 2 == 0:
        print(c)
        sleep(0.3)
print('Acima foram mostrados todos os números pares existentes entre 1 e 50.')