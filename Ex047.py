#mostrar todos os números pares que existirem entre 1 e 50.
from time import sleep
for c in range(1, 51):
    if c % 2 == 0:
        print(c)
        sleep(0.5)
print ('Todos os números pares entre 0 e 50 foram digitados acima.')

#poderia fazer range (2, 51, 2), assim só pulando de 2 em 2 (nos números pares)