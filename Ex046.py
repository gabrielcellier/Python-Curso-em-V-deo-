#contagem regressiva de 10 até 0 com 1 segundo entre cada número
from time import sleep
for c in range (10, 0, -1):
    print(c)
    sleep(1)
print('Foi feito contagem regressiva de 10 a 0 com intervalo de 1 segundo acima.')