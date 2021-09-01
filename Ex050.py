#ler 6 números inteiros (com for) e mostrar soma apenas dos números pares digitados
soma = 0
cont = 0
for n in range (1, 7):
    num = int(input('Digite um número inteiro: '))
    if num % 2 == 0:
        soma += num
        cont += 1
print ('Dos 6 números digitados, {} eram pares e a soma total deles é de {}.'.format(cont, soma))
