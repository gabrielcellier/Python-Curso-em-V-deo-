#Perguntar salário e calcular valor do aumento. aumento de 10% se salário for acima de 1250,00 e 15% se for abaixo.
slr = float(input('Digite o seu salário atual R$ '))
if slr >=1250.00:
    print ('O salário passará de R${:.2f} para R${:.2f}, reajustado 10%, reajuste para salários acima de R$1250,00'
           .format(slr, slr * 1.10))
else:
    print ('O salário passará de R${:.2f} para R${:.2f}, reajustado 15%, reajuste para salários abaixo de R$1250,00'
           .format(slr, slr * 1.15))