#Criar módulo chamado 'moeda.py' que tenha funções aumentar(), diminuir(), dobro() e metade()
#Fazer programa importando esse módulo criado e usando as funções.
from modulos import moeda

n = float(input('Digite um valor em reais: R$ '))
ta = int(input('Digite uma taxa (em %) de aumento para valor: '))
td = int(input('Digite qual taxa (em %) de diminuição do valor: '))
print(moeda.dobro(n))
print(moeda.metade(n))
print(moeda.aumentar(n, ta))
print(moeda.diminuir(n, td))
print('------')

#ta, td as taxas para o aumentar() e diminuir(). No caso não trabalhei frases no print() porque as fiz nas funções