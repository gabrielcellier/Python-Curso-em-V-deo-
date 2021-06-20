#Ler um n° de 0 a 9999 e mostrar cada digito separado, digito de milhar, centena, dezena e unidade
numero = int(input('Digite um número entre 0 a 9999: '))
print ('O numero digitado foi {}'
       '\nSua unidade é {}.'
       '\nSua dezena é {}.'
       '\nSua centena é {}.'
       '\nSeu milhar é {}.'
       .format(numero, (numero//1%10), (numero//10%10), (numero//100%10), (numero//1000%10)))
#poderia também criar uma variável para cada conta e só jogar as variáveis no .format()
