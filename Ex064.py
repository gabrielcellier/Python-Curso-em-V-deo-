#pedir pro usuario escrever números, só parar quando ele escrever 999. ao final mostrar a soma de todos
#os numeros que foram digitados e quantos números que foram digitados (desconsiderando o 999)
from time import sleep
print ('Digite números quantas vezes você quiser, somaremos todos e e falaremos quantos foram digitados')
print ('O número tem que ser menor que 1000. Se for digitado 999 o programa irá encerrar')
n = int(input('Digite um número: '))
cont = 0
soma = 0
while n != 999:
    if n >= 1000:
        n = int(input('Erro, digite outro número que seja menor que 1000: '))
    cont += 1
    soma += n
    sleep(0.5)
    n = int(input('Ok! Agora digite um novo número: '))
print ('Foram digitados {} números diferentes e a soma total deles foi {}.'.format(cont, soma))