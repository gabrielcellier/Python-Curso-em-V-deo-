#Criar função 'contador()' que recebe inicio, fim e passo (intervalo de crescimento)
#Programa tem que criar 3 contagens: 1) 1 a 10 de 1 em 1. 2) 10 a 0, de 2 em 2. 3) a Personalizada
#pro 3) Fazer evolução positiva, negativa, com números negativos e se passo for 0, fazer de 1 em 1.
from time import sleep
def contador(x, y, z):
    if z == 0:
        z == 1
    if z < 0:
        z *= -1
    if x > y:
        z = -z
    if y > 0 and y > x: #garantindo que número final irá aparecer em progressão positiva
        for a in range(x, y + 1, z):
            print(a, end=' ')
            sleep(0.4)
        print()
    if y <= 0 or x > y:  #garantindo que o número final irá aparecer em progressão negativa
        for b in range(x, y - 1, z):
            print(b, end=' ')
            sleep(0.4)
        print()


print ('Contador de 1 a 10 (1 em 1):')
contador(1, 10, 1)
print('---' * 8)
print ('Contador de 10 a 0 (2 em 2):')
contador(10, 0, 2)
print('---' * 8)
print('Informe agora a sua sequência, informando o valor inicial, final e o intervalo de progressão')
contador(int(input('Digite o valor inicial: ')),
         int(input('Digite o valor final: ')),
         int(input('Digite o intervalo de progressão da sua sequência: ')))

