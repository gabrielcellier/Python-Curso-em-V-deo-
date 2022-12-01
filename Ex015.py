#perguntas quantos dias ficou com o carro e a km. cobrar 60 por dia + 0,15 por km rodado.
from time import sleep
print('Coloque quantos dias o carro será alugado e a km total. Calcularemos o valor a ser pago.')
sleep(0.5)
print('A cobrança é de R$60 por dia de aluguel + R$0,15 por km rodado.')
print('------')
while True:
      d = input('Quantos dias o carro será/foi alugado? ')
      if d.isnumeric():
            d = int(d)
            break
      else:
            print('Erro. Coloque em valor inteiro o total de dias que o carro foi/será alugado.')
            sleep(0.5)
sleep(1)
k = float(input('Qual foi/será o total de km rodados? '))
print('-------')
sleep(1)
print(f'Ao todo serão {d} dias de aluguel, que custarão R$ {d * 60}, \n'
      f'{k} km rodados, que custarão R$ {(k * 0.15):.2f}.\n'
      f'Totalizando assim R$ {((d*60)+(k*0.15)):.2f} o valor a ser pago.')
