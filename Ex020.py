#Ler 4 nomes e sortear uma ordem entre os nomes dados
from random import shuffle
from time import sleep
print('Digite quatro nomes, sortearemos uma ordem entre os nomes.')
sleep(1)
a1 = str(input('Digite o primeiro nome: ')).strip().capitalize()
a2 = str(input('Digite o segundo nome: ')).strip().capitalize()
a3 = str(input('Digite o terceiro nome: ')).strip().capitalize()
a4 = str(input('Digite o quarto nome: ')).strip().capitalize()
lista = [a1, a2, a3, a4]
shuffle(lista)
sleep(1)
print(f'A ordem sorteada entre os nomes digitados é: {lista}')