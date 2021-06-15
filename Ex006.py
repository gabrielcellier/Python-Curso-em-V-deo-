# ler um número e mostrar seu dobro, triplo e raiz quadrada
n = int(input('Por favor digite um valor:'))
print('O valor digitado foi {},\no seu dobro é {},\nseu triplo {}'
      '\ne sua raiz quadrada {:.3f}'.format(n, n*2, n*3, n**0.5))
#poderia colocar as contas direto dentro do {} ex: {n*2}
