#pegar um numero dado e mostrar sua tabuada
n = int(input('Digite um valor inteiro para ser feito sua tabuada: '))
print('A tabuada do valor {} é: 1: {}, 2: {}, 3: {}, 4: {}, 5: {},'
      ' 6: {}, 7: {}, 8: {}, 9: {} e 10: {}.'
      .format(n, n*1, n*2, n*3, n*4, n*5, n*6, n*7, n*8, n*9, n*10))
#poderia colocar cada conta dentro dos {}
#ou criar uma variável para cada um (mt + trabalho)
#ou ainda fazer {} x {} = {} .format(n, 2, n*2) ; (n, 3, n*3) e por ai vai