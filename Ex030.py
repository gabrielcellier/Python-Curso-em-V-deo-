#Ler um número dado e avisar se ele é par ou ímpar
num = int(input('Digite um número inteiro qualquer: '))
conta = num % 2
if conta == 0:
    print ('O número digitado {} é par'.format(num))
else:
    print ('O número digitado {} é ímpar'.format(num))
#o '% 2' poderia ser colocado na variável num mas como quis mostrar ele nos prints criei a variável conta