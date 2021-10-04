#Tupla com 20 colocados do Brasileirao. Dai mostrar: 1) Os primeiros 5; 2) Os últimos 4;
#3)Listado em ordem alfabética e 4) Posição da Chapecoense
from time import sleep
tabela = ('Atletico MG', 'Palmeiras', 'Flamengo', 'Fortaleza', 'Bragantino', 'Corinthians',
          'Internacional', 'Fluminense', 'Atletico PR', 'Atletico GO', 'Cuiabá', 'Ceará',
          'São Paulo', 'América MG', 'Juventude', 'Santos', 'Bahia', 'Grêmio', 'Sport', 'Chapecoense')

print ('A seguir a classificação atual do Brasileirão 2021.')
print (tabela)
sleep(0.3)
print (f'Os 5 primeiros colocados são: {tabela [0:6]}')
sleep(0.3)
print (f'Os 4 últimos colocados são: {tabela [-4:]}')
sleep(0.3)
print (f'Os times arrumados em ordem alfabética: {sorted(tabela)}')
sleep(0.3)
print (f'A Chapecoense esta atualmente na {tabela.index("Chapecoense") + 1}° posição..')
#no tabela.index("chapecoense") usar aspas diferentes do usado no print()
#no caso no print usamos (' ') então no .index() usamos ""