#ler um numero 'n' inteiro e mostra na tela os 'n' primeiros elementos da sequencia de fibonacci.
print ('Aqui mostraremos a Sequência de Fibonacci até o número indicado pelo usuário')
n = int(input('Digite qual posição na sequência que você quer ver: '))
t1 = 0
t2 = 1
cont = 3
print ('{} -> {}'.format(t1, t2), end=' ') #isso é fixo pois t1 = 0 e t2 = 1 sempre.
while cont <= n:
    t3 = t1 + t2 #o T seguinte é sempre soma dos 2 T anteriores
    print ('-> {}'.format(t3), end=' ')
    t1 = t2 #pra continuar migrando a sequencia o t1 vira t2, t2 vira t3 e eles são somados de novo, como no começo
    t2 = t3
    cont += 1

