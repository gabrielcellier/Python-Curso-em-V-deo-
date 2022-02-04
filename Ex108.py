#pegar o módulo do 107 e adaptar criando a função moeda() que mostre valores como valor monetário formatado.
from modulos import moeda108
n = float(input('Digite um valor em reais (R$): '))
ta = int(input('Digite o valor (em %) de aumento para o valor: '))
td = int(input('Digite o valor (em %) de diminuição para o valor: '))
print(moeda108.dobro(n))
print(moeda108.metade(n))
print(moeda108.aumentar(n, ta))
print(moeda108.diminuir(n, td))
print('---------')
