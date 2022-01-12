#Fazer lista com números. 2 funçoes 'sorteio()' e 'somapar()' Sorteio fará um sorteio pegando 5 números
# e a segunda vai mostrar a soma entre todos os n PARES sorteados no sorteio()
from random import randint
from time import sleep

def sorteio(lista):
    for cont in range(0, 5):  #adicionarei 5 números na lista 'numeros'
        lista.append(randint(1, 100)) #cada número add será sorteado entre 1 a 100.
    print(f'Os cinco números sorteados foram: {lista}.')

def somapar(lista1):
    somatotal = 0
    todosnumeros = []
    for n in lista1:
        if n % 2 == 0:
            todosnumeros.append(n) #se o número for par ele entrará nessa lista
            somatotal += n #se o número for par ele será somado aqui
    print(f'Desse sorteios, os números pares são: {todosnumeros}, e a soma deles é {somatotal}.')

numeros = []
sorteio(numeros)
sleep(0.5)
somapar(numeros) #usando a lista número que já tem os números sorteados pela função sorteio() para fazer a soma
