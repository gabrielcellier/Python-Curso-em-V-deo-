#ao ler um angulo dado calcule seno, cosseno e tangente dele
from math import sin, cos, tan, radians
from time import sleep
print('Digite um ângulo. Iremos calcular seus valores de seno, cosseno e tangente.')
sleep(1)
ang = float(input('Digite um ângulo: '))
sleep(1)
print(f'O ângulo digitado foi: {ang}°. Seu seno é {sin(radians(ang))}, seu cosseno {cos(radians(ang))}\n'
      f'e sua tangente {tan(radians(ang))}.')
