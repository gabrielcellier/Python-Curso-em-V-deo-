#pegar uma temperatura celsius e converter para F e K
t = float(input('Digite o valor de temperatura em celsius (°C): '))
f = t * 1.8 + 32
print(f'A temperatura {t}°C equivale a {f} F e {t+273.15} Kelvin.')
