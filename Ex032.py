#Ler um ano e avisar se ele é bissexto
ano = int(input('Digite um ano para saber se ele é bissexto: '))
c1 = ano % 4
c2 = c1 % 100
c3 = c2 % 400
if c3 == 0:
    print ('O ano de {} é um ano bissexto.'.format(ano))
else:
    print ('O ano de {} não é um ano bissexto.'.format(ano))

