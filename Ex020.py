#Ler 4 nomes e sortear uma ordem entre os nomes dados
from time import sleep
from random import shuffle
print('Digite quatro nomes. Iremos criar uma lista com eles em ordem aleatória.')
qtnomes = 0
lista = []
while qtnomes < 4:
    nomes = input(f'Digite o {qtnomes+1}° nome: ').strip().capitalize()
    if nomes.isalpha():
        nomes = str(nomes)
        lista.append(nomes)
        qtnomes += 1
    else:
        print('Erro. Tente novamente. Lembrando que só aceitamos letras.')
        sleep(0.5)
sleep(1)
shuffle(lista)
print(f'A lista com ordem aleatória dos nomes digitados é: {lista}.')
