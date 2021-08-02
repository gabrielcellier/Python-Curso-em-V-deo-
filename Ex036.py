#perguntar I) valor da casa, II) salário do comprador, III) quantos anos pra pagar
#Calcular o valor da prestação mensal, não pode exceder 30% do salário ou o empréstimo será negado
casa = float(input('Qual o valor da casa? R$ '))
salario = float(input('Qual o salário do comprador? R$ '))
tempo = int(input('Quantos anos para pagar a casa? '))
prestacao = casa // (tempo * 12)
if (salario * 0.30) > prestacao:
    print ('Como o valor da prestação (R${:.2f}) não ultrapassa 30% do salário o empréstimo foi aceito.'.format(prestacao))
else:
    print ('Como o valor da prestação (R${:.2f}) ultrapassa 30% do salário o empréstimo foi negado.'.format(prestacao))
