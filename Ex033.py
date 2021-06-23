#Ler 3 números e mostrar qual o maior e o menor deles.
n1 = int(input('Digite um valor: '))
n2 = int(input('Digite um segundo valor: '))
n3 = int(input('Digite um terceiro valor: '))
print ('Primeiramente analisando o maior número:')
if n1 > n2 >= n3 or n1 > n3 >= n2:
    print ('O valor {}, o primeiro a ser digitado, foi o maior dos três valores.'.format(n1))
if n2 > n1 >= n3 or n2 > n3 >= n1:
    print ('O valor {}, o segundo a ser digitado, foi o maior dos três valores.'.format(n2))
if n3 > n1 >= n2 or n3 > n2 >= n1:
    print ('O valor {}, o terceiro a ser digitado, foi o maior dos três valores.'.format(n3))

print ('\nAgora analisando o menor número: ')
if n1 < n2 <= n3 or n1 < n3 <= n2:
    print ('O valor {}, o primeiro a ser digitado, foi o menor dos três valores.'.format(n1))
if n2 < n1 <= n3 or n2 < n3 <= n1:
    print ('O valor {}, o segundo a ser digitado, foi o menor dos três valores.'.format(n2))
if n3 < n1 <= n2 or n3 < n2 <= n1:
    print ('O valor {}, o segundo a ser digitado, foi o menor dos três valores.'.format(n3))
#o uso do >= e <= foi para evitar erro em caso de valores menores e maiores iguais.
#poderia fazer usando if n1 > n2 and n1 > 2 para definir os maiores e menores (usando < p/ menor)
#poderia fazer uma variável como n1 como menor, e ai só 2 if pro n2 e n3. as variaveis com o mesmo nome
#pois só uma seria selecionada no fim.
#posso jogar o print no fim com essa variável no .format() (que vai ser escolhida conforme a condição verdadeira)
