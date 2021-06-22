#Escreva a velocidade do carro, se for acima de 80km/h deverá tomar multa de valor R$7 pra cada km/h a mais
vel = int(input('Qual a velocidade do carro (em km/h): '))
multa = (vel - 80)
print ('Velocidade de carro acima de 80 km/h está sujeito a multa no valor de R$7,00 para cada 1 km/h excedente.')
if multa >=1:
    print ('A multa será de R${:.2f}, pois a velocidade registrada de {} km/h excedeu o limite de 80 km/h'
           .format(multa * 7, vel))
else:
    print ('O carro está dentro dos limites de velocidade')
#poderia fazer if vel >=81 também.