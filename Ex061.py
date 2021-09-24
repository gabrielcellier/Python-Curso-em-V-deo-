#ler o primeiro termo e razão do PA, mostrar os 10 primeiros termos usando while
print ('Gerador de PA, coloque o 1° termo e a razão que calcularemos os 10 primeiros termos.')
t = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão da PA: '))
termo = t
cont = 1
while cont <= 10: #limitando o processo acontecer 10x
    print ('{} ->'.format(termo), end=' ')
    cont += 1 #esse contador ganhará +1 a cada vez que o processo for feito
    termo += r #termo (seja lá qual for) será adicionado o valor 'r' indicado.
print ('\n' 'Acima os 10 primeiros termos da PA a partir de {} com razão {}.'.format(t, r))
