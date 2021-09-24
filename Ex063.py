#ler um numero 'n' inteiro e mostra na tela os 'n' primeiros elementos da sequencia de fibonacci.
print ('Calculadora para termos da Sequência de Fibonacci')
termos = int(input('Quantos termos você quer mostrar: '))
t1 = 0
t2 = 1
cont = 3
print ('{} -> {}'.format(t1, t2), end=' ')
while cont <= termos:
    t3 = t1 + t2
    print ('-> {}'.format(t3), end=' ')
    t1 = t2
    t2 = t3
    cont += 1
print('fim!')

