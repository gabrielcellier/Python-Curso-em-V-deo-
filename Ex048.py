#calcular a soma entre todos os números ímpares que são multiplos de 3 que ocorrem entre 1 a 500
soma = 0
cont = 0
for c in range (1, 501, 2):
    if c % 3 == 0:
        soma += c #ou soma = soma + c
        cont += 1 #ou cont = cont + 1
print ('A soma entre todos os números ímpares multiplos de 3 entre 1 e 500 é: {}.'.format(soma))
print ('O total de números ímpares múltiplos de 3 é de {}.'.format(cont))
