#fazer tabuada do número que o usuário colocar usando for
num = float(input('Digite um número para ser calculado sua tabuada: '))
for c in range (1, 11):
    print('A tabuada do {}: {} x {} = {:.2f}.'.format(num, num, c, num * c))
