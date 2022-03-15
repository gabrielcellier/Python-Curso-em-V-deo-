#Criar módulo chamado 'moeda.py' que tenha funções aumentar(), diminuir(), dobro() e metade()
#Fazer programa importando esse módulo criado e usando as funções.
from modulos import moeda
print('Digite o valor que deseja que seja usado no cálculo e as taxas de acréscimo e decréscimo.')

n = float(input('Digite o valor que será usado nos cálculos: '))
ta = float(input('Digite a taxa em % em quanto deseja aumentar o valor: '))
td = float(input('Digite a taxa em % em quanto deseja diminuir o valor: '))

print(moeda.dobro(n))
print(moeda.metade(n))
print(moeda.aumentar(n, ta))
print(moeda.diminuir(n, td))

#ta, td as taxas para o aumentar() e diminuir().
#No caso não trabalhei frases no print() porque as fiz nas funções