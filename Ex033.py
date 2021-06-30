#Ler 3 números e mostrar qual o maior e o menor deles.
n1 = int(input('Digite um valor: '))
n2 = int(input('Digite um segundo valor: '))
n3 = int(input('Digite um terceiro valor: '))

print ('Primeiramente analisando o maior número:')
if n1 > n2 >= n3 or n1 > n3 >= n2:
    print ('O valor {}, o primeiro, foi o maior dos três valores.'.format(n1))
if n2 > n1 >= n3 or n2 > n3 >= n1:
    print ('O valor {}, o segundo, foi o maior dos três valores.'.format(n2))
if n3 > n1 >= n2 or n3 > n2 >= n1:
    print ('O valor {}, o terceiro, foi o maior dos três valores.'.format(n3))

print ('\nAgora analisando o menor número: ')
if n1 < n2 <= n3 or n1 < n3 <= n2:
    print ('O valor {}, o primeiro, foi o menor dos três valores.'.format(n1))
if n2 < n1 <= n3 or n2 < n3 <= n1:
    print ('O valor {}, o segundo, foi o menor dos três valores.'.format(n2))
if n3 < n1 <= n2 or n3 < n2 <= n1:
    print ('O valor {}, o terceiro, foi o menor dos três valores.'.format(n3))
#poderia fazer usando if n1 > n2 and n1 > 2 etc para definir os maiores e menores.


