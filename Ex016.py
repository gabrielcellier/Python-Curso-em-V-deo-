#criar um program aque ao ler um numero quebrado (ex: 6.13652) mostre sua porção inteira (ex: 6)
import math
num = float(input('Digite um numero: '))
a = math.trunc(num)
print('O numero arredondado de {} é {}.'.format(num, math.floor(num)))
# poderia ser usado a variável com o math.floor(num) ou math.trunc ao invés de tacar no format
# poderia só importar os métodos trunc ou floor
# poderia ser usado int(num) que int é inteiro e corta os valores após o ponto

