#Sorteio entre 4 nomes de alunos dados, lendo o nome e sorteando um deles
from random import choice, shuffle
a1 = str(input('Digite o nome do primeiro aluno: '))
a2 = str(input('Digite o nome do segundo aluno: '))
a3 = str(input('Digite o nome do terceiro aluno: '))
a4 = str(input('Digite o nome do quarto aluno: '))
lista = [a1, a2, a3, a4]
print ('Os nomes dados foram {}, {}, {} e {}. O escolhido foi {}.'.format(a1, a2, a3, a4, choice(lista)))
#possivel criar também uma variável para o choice



