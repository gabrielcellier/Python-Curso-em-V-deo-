#ler um valor em metros e converter ele para cm e mm
num = float(input('Digite um valor metros, vamos converter para cm e mm: '))
print(f'O valor digitado foi de {(num):.2f} metros. '
      f'Esse valor equivale a {(num * 100):.2f} centimetros. '
      f'E equivale a {(num * 1000):.2f} milímetros.')
