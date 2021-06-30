#Perguntar salário e calcular valor do aumento. aumento de 10% se salário for acima de 1250,00 e 15% se for abaixo.
salario = float(input('Digite o seu salário para calcular o aumento: '))
if salario <=1250:
    print ('O aumento foi de 15%, de R${:.2f} para R${:.2f}'.format(salario, salario * 1.15))
else:
    print ('O aumento foi de 10%, de R${:.2f} para R${:.2f}'.format(salario, salario * 1.10))
