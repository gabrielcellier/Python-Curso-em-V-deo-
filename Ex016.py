#Crie um programa que lê um número real qualquer e mostre sua porção inteira ex: 6.7263 parte inteira: 6
import math
nq = float(input('Digite um número qualquer: '))
ni = math.trunc(nq)
ni2 = math.floor(nq)
print('O numero dado foi {} e sua porção inteira é {}.'.format(nq, ni2))
#pode ser usado as variáveis ni ou ni2, bem como já aplicar elas direto no .format()
#o ni2 pode ser usado pois arredonda o número para baixo

