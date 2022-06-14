# pegar largura e altura de uma parede e calcular quanto de tinta gasta pra pintar,
# sendo que cada l pinta 2 m² de parede
a = float(input('Digite a altura da parede (em metros): '))
l = float(input('Digite a largura da parede (em metros): '))
area = a*l
tinta = area/2
print(f'A parede tem {a:.2f} de altura e {l:.2f} de largura. Isso equivale a uma área de {area:.2f} m², '
      f'assim necessitando {tinta:.2f} litros de tinta.')
