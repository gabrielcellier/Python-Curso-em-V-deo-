#ler 6 números inteiros (com for) e mostrar soma apenas dos números pares digitados
soma = 0
cont = 0
for c in range (0, 6):
    n = int(input('Digite um número inteiro: '))
    if n % 2 == 0:
        soma = soma + n
        cont = cont +1
print('Você digitou {} números pares e a soma total deles foi {}.'.format(cont, soma))
