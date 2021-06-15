# pegar largura e altura de uma parede e calcular quanto de tinta gasta pra pintar,
# sendo que cada l pinta 2 m² de parede
h = float(input('Quanto de altura tem a parede? '))
l = float(input('Quanto de largura tem a parede? '))
a = h*l
t = a/2
print('A parede de {} de altura e {} de largura, uma area total de {}m²,\nsendo assim gasta {:.1f}l '
      'de tinta, considerando 1 litro para cada 2 m² de parede.'.format(h, l, a, t))
#cálculo poderia ser feito direto no format ao invés de criar variaveis

