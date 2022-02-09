#pegar o módulo do 107 e adaptar criando a função moeda() que mostre valores como valor monetário formatado.
from modulos import moeda108
n = float(input('Digite um valor em reais (R$): '))
ta = int(input('Digite o valor (em %) de aumento para o valor: '))
td = int(input('Digite o valor (em %) de diminuição para o valor: '))
print(f'{moeda108.moeda(moeda108.dobro(n))}.')
print(f'{moeda108.moeda(moeda108.metade(n))}.')
print(f'{moeda108.moeda(moeda108.aumentar(n, ta))}.')
print(f'{moeda108.moeda(moeda108.diminuir(n, td))}.')
print('---------')

#1) O uso do moeda108.moeda() antes das outras funções é para aplicar sua funcionalidade dentro das funções, ou seja,
#aplicar a formatação com R$ e , no lugar de .

#2) O prof usou um módulo chamado moeda.py para confundir, mas fiz usando moeda108.py mesmo.
