# Criar pacote 'utilidadesCEV' c/ módulos internos 'moeda' e 'dado'. Transferir as funções do 107, 108 e 109
# p/ o primeiro pacote e tudo funcionar.
from ex111.utilidadescev import moeda, dado

p = float(input('Digite um valor em reais: R$ '))
ta = float(input('Digite uma taxa (em %) para aumento do valor: '))
td = float(input('Digite uma taxa (em %) para subtração do valor: '))
moeda.resumo(p, ta, td)
