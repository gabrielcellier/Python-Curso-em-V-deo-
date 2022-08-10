#programa ler um número e mostrar o seu fatorial usando for
from time import sleep
print('Digite um número e calcularemos o seu fatorial.')
sleep(1)
f = c = 1
while True:
    n = int(input('Digite o número a ser calculado: '))
    if n.isnumeric():
        n = int(n)
        print('Valor válido. Obrigado')
        break
    else:
        print('Valor inválido. Tente novamente.')
sleep(0.5)
for c in range(n, 0, -1):
    f *= c
print ('O fatorial do número digitado {} é {}.'.format(n, f))
#1) o 'c' vai no N ao 0 diminuindo -1 por vez. o 'f *=c' significa c * (c - 1)
#essa conta será feita até que se chegue a 0, fazendo o calculo do fatorial

#2) nesse caso o uso de for foi possível pois sabiamos que era até de n até 0 (1, no caso)
