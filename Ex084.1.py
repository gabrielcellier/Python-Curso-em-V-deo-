#Ler nome e peso de pessoas. Mostrar: a) Total de pessoas, b) Pessoa(s) mais pesadas e o peso,
# c) Pessoa(s) mais leves e seu peso.
pessoas = []
dados = []
peso = []
while True:
    dados.append(str(input('Digite o nome da pessoa: ')))
    dados.append(float(input('Digite o peso da pessoa: ')))
    pessoas.append(dados[:])
    peso.append(dados[1])
    dados.clear()
    cont = str(input('Deseja continuar (s/n)? ')).lower().strip()[0]
    while cont not in 'sn':
        cont = str(input('Inválido. Deseja continuar (s/n)? ')).lower().strip()[0]
    if cont in 'Nn':
        break
print('-*-' * 10)
print(f'Ao todo foram listadas {len(pessoas)} pessoas.')
print(f'O menor peso registrado foi de {min(peso)} kg.')
for p in pessoas:
    if p[1] == min(peso):
        print(f'Associado a pessoa: {p[0]}')
print(f'O maior peso registrado foi de {max(peso)} kg.')
for p in pessoas:
    if p[1] == max(peso):
        print(f'Associado a pessoa: {p[0]}')

#nessa resolução foi criado uma lista com nome e peso e outra só com peso, a só com peso p/ definir min e max peso.
#a com os 2 dados (pessoas) foi utilizado como referencia para achar o p[0] (nome) associado aos valores p[1] max e min
