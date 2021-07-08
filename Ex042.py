#ver se pode fazer triangulo, se todos os lados forem iguais: equilatero, 2 lados iguais: isósceles
#escaleno se forem todos diferentes
l1 = float(input('Digite o primeiro segmento do triangulo: '))
l2 = float(input('Digite o segundo segmento do triangulo: '))
l3 = float(input('Digite o terceiro segmento do triangulo: '))
if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    print ('O triângulo tem condições de ser formado com os segmentos {}, {} e {} apresentados'.format(l1, l2, l3))
    if l1 == l2 == l3:
        print ('O triângulo é equilatero devido ter os 3 segmentos iguais.')
    elif (l1 == l2 or l1 == l3 or l2 == l3):
        print ('O triângulo é isósceles pois tem dois lados iguais.')
    elif l1 != l2 != l3 != l1:
        print ('O triângulo é escaleno pois os três segmentos são diferentes.')
else:
    print ('Os segmentos dados não se encaixam nas condições para formar um triângulo.')

