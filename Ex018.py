#ao ler um angulo dado calcule seno, cosseno e tangente dele
from math import sin, cos, tan, radians
from time import sleep
print('Digite um ângulo, calcularemos seu seno, cosseno e tangente.')
sleep(1)
a = float(input('Digite um ângulo: '))
sleep(1)
print(f'O ângulo digitado foi {a}°. Seu seno é {sin(radians(a)):.2f}°, cos é {cos(radians(a)):.2f} '
      f'e tangente {tan(radians(a)):.2f}.')
