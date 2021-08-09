#calcular a soma entre todos os números ímpares que são multiplos de 3
# que ocorrem entre 1 a 500
soma = 0 #acumulador
cont = 0 #contador
for c in range (1, 501, 2):
    if c % 3 == 0:
        soma = soma + c
        cont = cont + 1
print('A soma de todos os múltiplos de 3 entre 1 e 500 é {}.'.format(soma))
print('No total {} números são ímpares e múltiplos de 3 entre 1 e 500.'.format(cont))
