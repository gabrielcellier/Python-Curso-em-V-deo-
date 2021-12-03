#Ler nome, ano de nasc, cart. de trabalho. cadastrar em um dicionário com a idade.
#Se carteira for diferente de 0, perguntar ano de contratação e salário.
#Calcular qts anos pessoa vai se aposentar. Assumindo 35 anos de contribuição.
from time import sleep
from time import sleep
from datetime import datetime
pessoa = {}  #é possível adicionar os dados direto no dict, tirando idade que temos que calcular a partir do ano dado
pessoa['Nome'] = str(input('Qual o nome da pessoa: ')).capitalize().strip()
idade = int(input('Ano de nascimento: '))  #só obtemos o ano como variável
pessoa['Idade'] = datetime.now().year - idade  #usamos essa variavel pra calcular a idade direto como value na key 'idade'
pessoa['CTPS'] = int(input('Número da Carteira de Trabalho: '))
if pessoa['CTPS'] != 0:   #se o número for 0 de carteira de trabalho não precisamos perguntar as coisas abaixo
    pessoa['Ano de contratação'] = int(input('Qual ano de contratação: '))
    pessoa['Salário'] = float(input('Qual seu atual salário: R$ '))
    pessoa['Aposentadoria'] = pessoa['Idade'] + \
                              ((pessoa['Ano de contratação'] + 35) - datetime.now().year)
sleep(0.5)
print('~*~' * 13)
for k, v in pessoa.items():
    sleep(0.5)
    if k == 'Salário':     #para diagramar uma resposta diferente pra key 'salário'
        print(f'{k}: R${v}')
    elif k == 'Aposentadoria':   #para diagramar uma resp diferente pra key 'aposentadoria'
        print(f'A {k} ocorrerá com {v} anos.')
    else:
        print(f'{k}: {v}')
print('~*~' * 13)



