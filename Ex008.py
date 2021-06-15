#ler um valor em metros e converter ele para cm e mm
n = float(input('Digite um valor em metros: '))
cm = n * 100
mm = n * 1000
print('O valor em metros é {}, em centrimetros {:.0f} cm e milimetros {:.0f} mm.'.format(n, cm, mm))
#como escrito abaixo a conta pode ser feita direto dentro do .format()
#print('O valor em metros é {}, em centímetros {:.0f}cm e milímetros {:.0f}mm.'.format(n, n*100, n*1000))
