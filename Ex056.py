#ler o nome, idade e sexo de 4 pessoas. mostrar a 1) média de idade do grupo,
# 2) nome do homem mais velho, #3) quantas mulheres tem menos de 20 anos.
from time import sleep
idadetotal = qtmulheres = idadehomem = 0
nomehomem = ''
print('Digite o nome, idade e sexto de 4 pessoas. Vamos comparar as informações.')
sleep(1)
for c in range (1, 5):
    while True:
        nome = input('Digite o nome: ').strip().capitalize()
        if nome.isalpha():
            nome = str(nome)
            sleep(0.5)
            break
        else:
            print('Resposta inválida. Digite um nome válido.')
    while True:
        idade = input('Digite a idade: ')
        if idade.isnumeric():
            idade = int(idade)
            idadetotal += idade
            sleep(0.5)
            break
        else:
            print('Valor inválido. Digite uma idade com número inteiro.')
            sleep(1)
    while True:
        sexo = input('Digite o sexo da pessoa (m/f): ').strip().lower()[0]
        if sexo in 'mf' and len(sexo) == 1:
            sexo = str(sexo)
            sleep(0.5)
            break
        else:
            print('Resposta inválida. Escreva apenas "m" ou "f" para apontar o sexo.')
    if c == 1 and sexo in 'm': #primeiro homem será o mais velho. mudaremos a partir dele
        nomehomem = nome
        idadehomem = idade
    if sexo in 'm' and idade > idadehomem: #se idade de outro homem for maior que do primeiro, substituirá ele.
        idadehomem = idade
        nomehomem = nome
    if sexo in 'f' and idade < 20: #anotar qt de mulheres menores que 20.
        qtmulheres += 1
sleep(1)
print(f'A média de idade do grupo é de {(idadetotal/4):.1f}.')
sleep(0.5)
if nomehomem == '':
    print(f'Nenhum homem foi inserido. Logo não tem um homem mais velho.')
else:
    print(f'O homem mais velho é o {nomehomem} que tem {idadehomem} anos.')
sleep(0.5)
if qtmulheres == 0:
    print(f'Nenhuma mulher foi inserida na lista.')
elif qtmulheres == 1:
    print(f'Ao todo, {qtmulheres} mulher tem menos de 20 anos.')
else:
    print(f'Ao todo, {qtmulheres} mulheres tem menos de 20 anos.')


