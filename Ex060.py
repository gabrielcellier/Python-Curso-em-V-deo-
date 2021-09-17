#programa ler um número e mostrar o seu fatorial
n = int(input('Digite um número para calcularmos seu fatorial: '))
c = n
f = 1
while c > 0:
    f *= c
    c -= 1
print ('fatorial de {} é {}'.format(n, f))

#pode ser resolvido usando 'from math import factorial' e usar factorial(x) sendo x o número do fatorial
#from math import factorial
#n = int(input('Digite o número para calcularmos o seu fatorial: '))
#f = factorial(n)
#print ('Fatorial de {} é {}'.format(n, f)