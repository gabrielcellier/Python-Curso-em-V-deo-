#ler 5 valores númericos e guardar numa lista. Mostrar maior e menor valor e suas posicoes na lista
lista = []
for numeros in range(0, 5):
    lista.append(int(input('Digite um valor númerico inteiro: ')))
for c, v in enumerate(lista):
print(f'A lista foi {lista}')



