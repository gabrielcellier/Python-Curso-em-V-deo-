#Modificar as funções do 108, aceitando um parametro a mais, essa informado se os valores serão formatado
#ou não pela função moeda()
from modulos import moeda109
n = float(input('Digite o um valor em reais: '))
ta = float(input('Digite uma taxa (em %) para aumento do valor: '))
td = float(input('Digite uma taxa (em %) para subtração do valor: '))
formato = bool(input('Digite "True" ou "False" para))