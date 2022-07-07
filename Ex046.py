# contagem regressiva de 10 até 0 com 1 segundo entre cada número
from time import sleep
print('Vamos fazer contagem regressiva de 10 a 0, diminuindo 1 número a cada segundo.')
for c in range(10, -1, -1):
    print(c)
    sleep(1)
