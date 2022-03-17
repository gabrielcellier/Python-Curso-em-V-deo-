# Criar pacote 'utilidadesCEV' c/ módulos internos 'moeda' e 'dado'.
# Transferir as funções do 107, 108 e 109 p/ o primeiro pacote e tudo funcionar.
from utilidadescev import moeda

print('A partir do valor dado (em R$) realizaremos diferentes cálculos.')

n = float(input('Digite o valor (em reais) que será usado nos cálculos: R$ '))
ta = float(input('Digite a taxa em % em quanto deseja aumentar o valor: '))
td = float(input('Digite a taxa em % em quanto deseja diminuir o valor: '))
utilidadescev.moeda(n, ta, td)



