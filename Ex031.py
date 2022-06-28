#Perguntar distancia de uma viagem, até 200km cobrar 0,50 por km, acima de 200km cobrar 0,45
from time import sleep
print('Calcularemos o custo da viagem. Até 200 km de distância custa R$0,50 por km rodado.'
      '\nAcima de 200 km rodados o km custará R$0,45.')
dist = float(input('Qual a distância total da viagem? Digitar em km. '))
sleep(1)
if dist > 200:
    print(f'A viagem será de {dist:.1f} km, custará R$ {(dist * 0.45):.2f} (R$0,45 por km).')
else:
    print(f'A viagem será de {dist:.1f} km, custará ao todo R$ {(dist * 0.50):.2f} (R$0,50 por km).')
