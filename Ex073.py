#Tupla com 20 colocados do Brasileirao. Dai mostrar: 1) Os primeiros 5; 2) Os últimos 4;
#3)Listado em ordem alfabética e 4) Posição da Chapecoense
from time import sleep
tabela = ('Atletico MG', 'Palmeiras', 'Flamengo', 'Fortaleza', 'Bragantino', 'Corinthians',
          'Internacional', 'Fluminense', 'Atletico PR', 'Atletico GO', 'Cuiabá', 'Ceará',
          'São Paulo', 'América MG', 'Juventude', 'Santos', 'Bahia', 'Grêmio', 'Sport', 'Chapecoense')
print ('A seguir a tabela do Brasileirão 2021!')
sleep(0.3)
print (tabela)
sleep(0.5)
print (f'Os primeiros cinco colocados atualmente são {tabela[0:5]}')
sleep(0.5)
print (f'Os quatro últimos colocados atualmente são {tabela [-4:]}')
sleep(0.5)
print (f'A tabela dos times em ordem alfabética é: {sorted(tabela)}')
sleep(0.5)
print (f'O Chapecoense se encontra atualmente na {tabela.index("Chapecoense") + 1}° Posição na tabela.')
#como usamos '' no print(), no .index() usamos o " ".