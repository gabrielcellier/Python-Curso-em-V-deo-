#pegar uma temperatura celsius e converter para F e K
from time import sleep
print('Digite uma temperatura em celsius. Vamos calcular o seu valor em Fahrenheit e Kelvin.')
sleep(1)
t = float(input('Digite a temperatura em graus celsius: '))
sleep(1)
f = t * 1.8 + 32
print(f'A temperatura de {t:.2f}°c é igual a {t:.2f} F e {t+273.15} K.')