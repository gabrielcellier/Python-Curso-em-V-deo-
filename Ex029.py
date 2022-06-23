#Escreva a velocidade do carro, se for acima de 80km/h deverá tomar multa de valor R$7 pra cada km/h a mais
from time import sleep
print('Digite a velocidade do carro. '
      '\nSe for acima de 80km/h, uma multa no valor de R$7 para cada km/h excedente será cobrado')
sleep(0.5)
velocidade = float(input('Digite a velocidade do carro (em km/h): '))
multa = velocidade - 80
if multa > 0:
    print(f'A velocidade de {velocidade:.2f} km/h é ilegal, está {multa:.2f} km/h acima do permitido.'
          f'\nUma multa no valor de R$ {(7 * multa):.2f} será cobrada.')
else:
    print(f'A velocidade de {velocidade:.2f} km/h é legal, está abaixo dos 80 km/h.')
