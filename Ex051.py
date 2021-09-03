#ler o primeiro termo e a razão de uma PA e # mostrar os 10 primeiros termos
t = float(input('Digite o primeiro termo da PA: '))
r = float(input('Digite a razão da PA: '))
print ('Com o primeiro termo {:.0f} e a razão {} os 10 primeiros termos da PA são:'.format(t, r))
for c in range (1, 11, 1):
    t = t + r
    print ('{}, '.format(t), end=' ')
print ('Foram mostrados acima os 10 primeiros termos da PA')