#ao ler um angulo dado calcule seno, cosseno e tangente dele
import math
x = float(input('Digite um ângulo: '))
print('O ângulo de {}° tem: \nseno de {:.2f}° \ncosseno {:.2f}° \ntangente {:.2f}°'
      .format(x, math.sin(math.radians(x)), math.cos(math.radians(x)), math.tan(math.radians(x))))