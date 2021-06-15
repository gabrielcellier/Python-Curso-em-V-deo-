#pegar uma temperatura celsius e converter para F e K
c = float(input('Qual a temperatura em celsius:'))
f = c * 1.8 + 32
print('A temperatura {}°C equivale a {:.1f}°F e a {:.2f} Kelvin'.format(c, f, c + 273.15))
#O cálculo para F poderia ser feito no .format() ao invés da variável 'f' que foi criada
