#Add no módulo moeda.py a função resumo(), mostrando informações geradas pelas funções já criadas até aqui.
from modulos import moeda110
p = float(input('Digite um valor em reais: R$ '))
ta = float(input('Digite uma taxa (em %) para aumento do valor: '))
td = float(input('Digite uma taxa (em %) para subtração do valor: '))
moeda110.resumo(p, ta, td)