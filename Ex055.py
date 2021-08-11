#ler peso de 5 pessoas e mostrar qual o maior e o menor
maior = 0
menor = 0
for p in range (1, 6):
    peso = float(input('Digite o peso da {}ª pessoa (em kg): '.format(p)))
    if p == 1:   #aqui definimos o primeiro valor como maior e menor
        maior = p
        menor = p
    else:  #aqui definimos que os seguintes 'p' (2-6) substituirão o maior e menor
        if peso > maior:   #se o peso dos 'p' seguintes for maior substituirá o 'maior' atual
            maior = peso
        if peso < menor:    #se o peso dos 'p' seguintes for menor substituirá o 'menor' atual
            menor = peso
print ('O maior peso foi {:.2f} kg e o menor {:.2f} kg.'.format(maior, menor))
#nesse método o primeiro valor dado é definido tanto como maior e menor, e os outros serão testados e caso
#sejam maiores ou menores substituiram o valor do 'p' anterior definido como 'maior' ou 'menor', respectivamente.

