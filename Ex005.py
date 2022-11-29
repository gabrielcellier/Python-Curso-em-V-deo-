#ler um número e mostrar o número que vem antes e o que vem depois
from time import sleep
print('Digite um número inteiro. Mostraremos o número que vem antes e o que vem depois do valor escrito.')
print('-------')
sleep(1)
num = ""
while type(num) != int: #se o valor não for um INT repetirá esse laço.
      num = input('Digite um número: ').strip()
      if num.isnumeric():
            num = int(num)
      else:
            print('Valor inválido. Por favor digite um número inteiro.')
print(f'O valor digitado foi {num}. O numero anterior é {num-1} e o seguinte é {num+1}.')


