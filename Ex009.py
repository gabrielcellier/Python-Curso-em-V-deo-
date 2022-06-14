#pegar um numero dado e mostrar sua tabuada
from time import sleep
print('Digite um número, mostraremos sua tabuada.')
x = 1 #contador
n = int(input('Digite um número inteiro: '))
sleep(1)
print('-------------')
print(f'Tabuada do {n}:')
while x != 11:  #contador aumenta 1 a cada cálculo, ao chegar a 11 ele para.
    sleep(0.5)
    print(f'{n} x {x} = {n*x}') #o próprio contador é utilizado no cálculo.
    x+=1

#outro método mais simples:
#print(f'O valor digitado foi {n}. Sua tabuada é 1: {n*1}, 2: {n*2}, 3: {n*3}, 4: {n*4}, 5: {n*5}'
     #f', 6: {n*6}, 7: {n*7}, 8: {n*8}, 9: {n*9} e 10: {n*10}.')
