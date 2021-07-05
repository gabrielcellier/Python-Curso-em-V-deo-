#perguntar I) valor da casa, II) salário do comprador, III) quantos anos pra pagar
#Calcular o valor da prestação mensal, não pode exceder 30% do salário ou o empréstimo será negado
casa = float(input('Qual o valor da casa? R$ '))
salario = float(input('Qual o seu salário atualmente? R$ '))
prazo = int(input('Quantos anos para pagar o imóvel? '))
prestacao = casa / (prazo * 12)

if prestacao >= (salario * 0.30):
    input ('Como a prestação no valor de R${:.2f} é maior que 30% do salário de R$ {} '
           'o empréstimo será \033[1mnegado\033[m'.format(prestacao, salario))
else:
    input ('Como a prestação no valor de R${:.2f} é menor que 30% do salário de R$ {} '
           'o empréstimo será \033[1maceito\033[m'.format(prestacao, salario))
