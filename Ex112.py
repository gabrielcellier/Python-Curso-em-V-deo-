#Criar função leiadinheiro() no módulo dado (ex anterior) que funcione como um input(), validando dados
#p/ que seja aceitos apenas valores monetários.
from utilidadescev import dado
print('Digite os valores em FORMA NUMÉRICA. Não é possível deixar algum campo vazio, para isso digite 0.')
n = dado.leiadinheiro('Digite o valor (em reais) que será usado nos cálculos: R$ ')
ta = dado.leiadinheiro('Digite a taxa em % em quanto deseja aumentar o valor: ')
td = dado.leiadinheiro('Digite a taxa em % em quanto deseja diminuir o valor: ')
dado.resumo(n, ta, td)
print(n, ta, td)