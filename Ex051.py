#ler o primeiro termo e a razão de uma PA e mostrar os 10 primeiros termos dessa PA
t = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão da PA: '))
for c in range (0, 10):
    t = t + r #sempre somará t + r (a razão) e o fará 10x (range (0, 10)), acumulando o total
    print (t, end=' ')
