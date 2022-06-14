#perguntas quantos dias ficou com o carro e a km. cobrar 60 por dia + 0,15 por km rodado.
from time import sleep
print('O valor do aluguel do carro é de R$60,00 reais por dia e R$0,15 por km rodado.')
sleep(0.5)
d = int(input('Quantos dias o carro foi/será alugado? '))
k = float(input('Quantos KM foram/serão rodados com o carro? '))
print(f'Alugando o carro por {d} dias (R${d*60}) e rodando ao todo {k:.2f} km (R${k*0.15}) '
      f'o valor do aluguel será de R${((d*60)+(k*0.15)):.2f}.')