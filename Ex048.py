#calcular a soma entre todos os números ímpares que são multiplos de 3 que ocorrem entre 1 a 500
soma = cont = 0
for c in range (1, 501):
    if c % 3 == 0:
        soma += c
        cont += 1
print(f'A soma de todos os números ímpares multiplos de 3 é {soma}. Ao todo foram {cont} números.')

