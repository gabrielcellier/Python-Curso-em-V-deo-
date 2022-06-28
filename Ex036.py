#perguntar I) valor da casa, II) salário do comprador, III) quantos anos pra pagar
#Calcular o valor da prestação mensal, não pode exceder 30% do salário ou o empréstimo será negado
from time import sleep
print('Digite o valor da casa, o prazo de pagamento e o seu salário. Vamos calculas o valor das prestações.'
      '\nSe o valor mensal for maior que 30% do seu salário, o empréstimo será negado.')
sleep(1)
valor = float(input('Digite o valor da casa: R$ '))
salario = float(input('Digite o salário do comprador da casa: R$ '))
prazo = float(input('Prazo de pagamento da casa (em anos): '))
mensalidade = valor / (prazo * 12)
sleep(1)
if mensalidade > (salario * 0.30):
    print(f'Devido o valor mensal da casa (R$ {mensalidade:.2f}) ser maior que 30% do salário '
          f'(R$ {(salario * 0.30):.2f}'
          f'\no empréstimo será negado.')
else:
    print(f'Devido o valor mensal da casa (R$ {mensalidade:.2f}) ser menor que 30% do salário '
          f'(R$ {(salario * 0.30):.2f})'
          f'\no empréstimo será aceito.')
