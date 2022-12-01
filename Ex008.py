#ler um valor em metros e converter ele para cm e mm
from time import sleep
print('Digite um valor em metros. Converteremos ele para cm e mm.')
sleep(1)
v = float(input('Digite o valor em metros: '))
sleep(1)
print(f'O valor digitado foi {v:.2f} metros.\n'
      f'Sua conversão em cm é {(v * 100):.2f} centrimetros.\n'
      f'Sua conversão em mm é {(v * 1000):.2f} milimetros.')