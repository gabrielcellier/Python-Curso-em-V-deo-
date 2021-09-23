#programa ler um número e mostrar o seu fatorial
n = int(input('Digite um número para calcularmos seu fatorial: '))
c = n
f = 1
while c > 0:
    f *= c
    c -= 1
print ('fatorial de {} é {}'.format(n, f))

#a) nesse modo enquanto C for maior que 0, ele será multiplicado por ele mesmo - 1
#isso irá ocorrer até que o próprio valor do c chegue a 0
#obs: fatorial pode ser resolvido usando 'factorial()' da biblioteca math.