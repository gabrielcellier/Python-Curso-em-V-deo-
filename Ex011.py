# pegar largura e altura de uma parede e calcular quanto de tinta gasta pra pintar,
# sendo que cada l pinta 2 m² de parede
from time import sleep
print('Digite a altura e a largura da parede.\n'
      'Iremos calcular a quantidade de tinta necessária para pintar toda a parede.\n'
      'ps: cada litro de tinta pinta em média 2 m² de parede.')
sleep(1)
a = float(input('Digite a altura da parede (em metros): '))
l = float(input('Digite a largura da parede (em metros): '))
sleep(1)
print(f'A parede conta com dimensões de {a:.2f} x {l:.2f}.')
sleep(1)
area = a*l
tinta = area/2
print(f'Com {a:.2f} x {l:.2f} a parede tem área total de {area:.2f} metros. \n'
      f'Necessitando assim de {tinta:.2f} litros de tinta para ser totalmente pintada.')
