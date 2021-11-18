#Digitar 5 numeros e colocar na lista na posição correta crescente sem usar sort(). Ao fim mostrar a lista na ordem.
lista = []
pos = 0
for n in range (0, 5):
    num = int(input('Digite um número inteiro: '))
    if n == 0 or num > lista[-1]: #se for o primeiro valor ou maior que o último, o valor vai pra último
        lista.append(num)
    else:
        for pos, x in enumerate(lista):  #se o num for menor ou igual ao valor x da lista, ele entra no lugar desse valor.
            if num <= x:
                lista.insert(pos, num)
                break
print(f'Os valores digitados em ordem crescente foram: {lista}')


