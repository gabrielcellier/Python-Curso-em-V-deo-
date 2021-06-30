#Ler um número dado e avisar se ele é par ou ímpar
num = int(input('Digite um número qualquer: '))
conta = num % 2
if conta == 0:
    print ('O número digitado {} é par'.format(num))
else:
    print ('O número digitado {} é ímpar.'.format(num))
