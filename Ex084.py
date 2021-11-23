#Ler nome e peso de pessoas. Mostrar: a) Total de pessoas, b) Pessoa(s) mais pesadas e o peso,
# c) Pessoa(s) mais leves e seu peso.
from time import sleep
pessoas = []
dados = []
maior = menos = 0
while True:
    dados.append(str(input('Digite o nome da pessoa: ')))
    dados.append(int(input('Digite o pessoa (em kg) da pessoa: ')))
    if len(dados) == 0:   #primeiro valor definirá o peso max e min
        maior = dados[1]
        menos = dados[1]
    else:                    #se valor for maior ou menor o maior ou menor peso ele substituirá o valor
        if dados[1] > maior:
            maior = dados[1]
        if dados[1] < menos:
            menos = dados[1]
    pessoas.append(dados[:])
    dados.clear()
    cont = str(input('Deseja continuar (s/n)? ')).strip().lower()[0]
    while cont not in 'sn':
        cont = str(input('Resposta inválida. Deseja continuar (s/n)?  ')).strip().lower()[0]
    if cont in 'n':
        break
sleep(0.5)
print('-*-' * 10)
print(f'Ao todo foram inseridas {len(pessoas)} pessoas na lista.')
for p in pessoas:
    if p[1] == menos:     #se o p[1] tiver valor igual o menor, pegaremos o p[0] nome associado
        print(f'A pessoa de menor peso é a {p[0]} pesando {p[1]:.2f} kg.')
for p in pessoas:
    if p[1] == maior:     #se o p[1] tiver o valor igual do maior, pegamos o p[0] nome associado
        print(f'A pessoa de maior peso é a {p[0]} pesando {p[1]:.2f} kg.')
