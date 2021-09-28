#mostrar a tabuada do número digitado. Programa será interrompido se valor digitado for negativo
from time import sleep
while True:
    n = int(input('Digite um número para que seja calculado sua tabuada: '))
    if n < 0:
        break
    print ('--' * 10)
    for c in range (1, 11):
        print (f'{n} x {c} = {n * c}')
    print ('--' * 10)
    sleep(1)
print (f'Devido o número negativo {n} digitado, o programa foi encerrado.')