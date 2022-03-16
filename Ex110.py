#Add no módulo moeda.py a função resumo(), mostrando informações geradas pelas funções já criadas até aqui.
from modulos import moeda
print('A partir do valor dado (em R$) realizaremos diferentes cálculos.')

n = float(input('Digite o valor (em reais) que será usado nos cálculos: R$ '))
ta = float(input('Digite a taxa em % em quanto deseja aumentar o valor: '))
td = float(input('Digite a taxa em % em quanto deseja diminuir o valor: '))
moeda.resumo(n, ta, td)