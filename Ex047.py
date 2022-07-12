#mostrar todos os números pares que existirem entre 1 e 50.
from time import sleep
print('Mostraremos todos os números pares existentes entre 1 e 50 em uma contagem.')
for c in range (1, 51):
    if c % 2 == 0:
        print(c)
        sleep(1)
print('Terminada a contagem. Acima, todos os números pares no intervalo entre 1 a 50.')