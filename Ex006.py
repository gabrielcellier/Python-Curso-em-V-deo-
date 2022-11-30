# ler um número e mostrar seu dobro, triplo e raiz quadrada
from time import sleep
from math import log10
print('Digite um número, calcularemos seu dobro, triplo e sua raíz quadrada.')
sleep(1)
t = n = 0
while t == 0 or t > 2:
      t = int(input('Digite o código do tipo de número desejado. [1] Número inteiro, '
                    '[2] Número decimal: '))
      if int(log10(t))+1 == 1: #int(log10(x)) checa se tem apenas 1 número o int
            if t == 1:
                  print('O usuário escolheu calcular com número inteiro.')
            elif t == 2:
                  print('O usuário escolheu calcular com número decimal.')
            else:
                  print('Erro. Digite um valor de código válido.')
      else:
            print('Código inválido. Digite apenas UM número para indicar sua escolha.')
sleep(1)
if t == 1:
      while True:
            n = input('Digite um número inteiro: ')
            if n.isnumeric():
                  n = int(n)
                  print(f'O valor digitado foi {n}. Seu dobro é {n*2}, o triplo é {n*3}'
                        f' e sua raíz quadrada {n**2}.')
                  break
            else:
                  print('Erro. Digite um valor válido (número inteiro).')
if t == 2:
      n = float(input('Digite um número decimal: '))
      print(f'O valor digitado foi {n.2f}. Seu dobro é {(n*2).2f}, o triplo é {(n*3).2f}'
            f' e sua raíz quadrada {(n**2).2f}.')