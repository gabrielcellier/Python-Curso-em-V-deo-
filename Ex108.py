#pegar o módulo do 107 e adaptar criando a função moeda() que mostre valores como valor monetário formatado.
from modulos import moeda
print('A partir do valor dado (em R$) realizaremos diferentes cálculos.')

n = float(input('Digite o valor (em reais) que será usado nos cálculos: R$ '))
ta = float(input('Digite a taxa em % em quanto deseja aumentar o valor: '))
td = float(input('Digite a taxa em % em quanto deseja diminuir o valor: '))

print(f'O dobro de {moeda.moeda(n)} é {moeda.moeda(moeda.dobro(n))}.')
print(f'Metade de {moeda.moeda(n)} é {moeda.moeda(moeda.metade(n))}.')
print(f'O valor {moeda.moeda(n)} acrescido de {ta}% é {moeda.moeda(moeda.aumentar(n, ta))}.')
print(f'O valor {moeda.moeda(n)} com decréscimo de {td}% é {moeda.moeda(moeda.diminuir(n, td))}.')

#1) O uso do moeda108.moeda() antes das outras funções é para aplicar sua funcionalidade dentro das funções, ou seja,
#aplicar a formatação com R$ e ',' no lugar de '.'
#2) O prof usou um módulo chamado moeda.py para confundir, mas fiz usando moeda108.py mesmo.
