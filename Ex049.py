#fazer tabuada do número que o usuário colocar usando for
n = float(input('Digite um número para que seja calculado a sua tabuada: '))
for c in range (1, 11):
    print ('A tabuada do {}: {} x {} = {} .'.format(n, n, c, n * c))
