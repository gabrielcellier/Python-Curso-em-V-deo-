#pegar salário e mostrar valor com 15% de aumento
s = float(input('Digitar o salário: R$'))
a = s * 1.15
print('O salário original é R${:.2f}, com o aumento de 15% ficará R${:.2f}.'.format(s, s * 1.15))
#valor pode ser calculado direto no .format() ou pela variável criada 'a'.
