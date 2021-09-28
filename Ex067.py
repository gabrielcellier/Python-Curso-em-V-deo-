#mostrar a tabuada do número digitado. Programa será interrompido se valor digitado for negativo
from time import sleep
while True:
    n = int(input('Digite um número inteiro para que seja calculado sua tabuada: '))
    if n < 0:
        break
    print ('--' * 10)
    print (f'''    {n} x 1 = {n * 1}
    {n} x 2 = {n * 2}
    {n} x 3 = {n * 3}
    {n} x 4 = {n * 4}
    {n} x 5 = {n * 5}
    {n} x 6 = {n * 6}
    {n} x 7 = {n * 7}
    {n} x 8 = {n * 8}
    {n} x 9 = {n * 9}
    {n} x 10 = {n * 10}''')
    print ('--' * 10)
    sleep(1)
print (f'Devido o número negativo {n} digitado, o programa foi encerrado.')
