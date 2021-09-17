#programa ler um número e mostrar o seu fatorial usando for
n = int(input('Digite um número para ser calculado o seu fatorial: '))
f = 1
c = 1
for c in range (n,0,-1):
    f *= c
print ('O fatorial do número digitado {} é {}.'.format(n, f))