#ler um número digitado e ver se ele é um número primo
n = int(input('Digite um número para verificar se ele é um número primo: '))
tot = 0
for c in range (1, n+1):
    if n % c == 0:
        tot = tot + 1
if tot == 2:
    print ('O número {} é divisível apenas 2x, logo é um número primo.'.format(c))
else:
    print ('O número {} é divisível mais de 2x logo não é número primo.'.format(c))
#'range (1, n+1)' faz com que a condição 'n % c == 0' seja checada em todos os números de 1 até o número digitado
#tot soma o tanto de vezes que a condição 'n % c == 0' é verdadeira, se for só duas o N é primo