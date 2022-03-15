#Criar módulo chamado 'moeda.py' que tenha funções aumentar(), diminuir(), dobro() e metade()
#Fazer programa importando esse módulo criado e usando as funções.
from modulos import moeda
print('Digite o valor que deseja que seja usado no cálculo e as taxas de acréscimo e decréscimo.')

n = float(input('Digite o valor (em reais) que será usado nos cálculos: R$'))
ta = float(input('Digite a taxa em % em quanto deseja aumentar o valor: '))
td = float(input('Digite a taxa em % em quanto deseja diminuir o valor: '))

print(f'O dobro de R${n} é R${moeda.dobro(n)}.')
print(f'Metade de R${n} é R${moeda.metade(n)}.')
print(f'O valor de R${n} com aumento de {ta}% é R${moeda.aumentar(n, ta)}.')
print(f'O valor de R${n} com decréscimo de {td}% é R${moeda.diminuir(n, td)}.')

#ta, td as taxas para o aumentar() e diminuir().
#No caso não trabalhei frases no print() porque as fiz nas funções