#programa ler um número e mostrar o seu fatorial
from time import sleep
print('Digite um número e iremos calcular o seu fatorial.')
sleep(1)
while True:
    n = int(input('Digite um número: )
    if n.isnumeric():
        n = int(n)
        print('Obrigado. O valor que foi digitado é válido.')
        break
    else:
        print('Valor inválido. Tente Novamente.')
c = n
f = 1
while c > 0:
    f *= c
    c -= 1
print(f'O fatorial do valor "{n}" é {f}.')
#a) nesse modo enquanto C for maior que 0, ele será multiplicado por ele mesmo - 1
#isso irá ocorrer até que o próprio valor do c chegue a 0
#obs: fatorial pode ser resolvido usando 'factorial()' da biblioteca math.