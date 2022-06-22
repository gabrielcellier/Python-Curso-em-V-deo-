#Ler um n° de 0 a 9999 e mostrar cada digito separado, digito de milhar, centena, dezena e unidade
from time import sleep
print('Digite um número de 0 a 9999. Mostraremos os dígitos separados.')
sleep(0.5)
while True:
       numero = int(input('Digite um numero inteiro entre 0 e 9999: '))
       if numero >= 0 and numero <= 9999:
              break
print(f'O número digitado foi {numero}.'
      f'\nSua unidade é {numero//1%10}.'
      f'\nSua dezena é {numero//10%10}.'
      f'\nSua centena é {numero//100%10}.'
      f'\nSeu milhar é {numero//1000%10}.')


