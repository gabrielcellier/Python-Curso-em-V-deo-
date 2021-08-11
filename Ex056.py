#ler o nome, idade e sexo de 4 pessoas. mostrar a 1) média de idade do grupo,
# 2) nome do homem mais velho, #3) quantas mulheres tem menos de 20 anos.
idadetotal = 0
mmenos20 = 0
idadedehomem = 0
nomehomem = ""
for p in range (1, 5):
    print ('-------[{}ª Pessoa]-------'.format(p))
    nome = str(input('Digite o nome da pessoa: ')).capitalize().strip()
    idade = int(input('Digite a idade da pessoa: '))
    sexo = str(input('Digite o sexo da pessoa (m/f): ')).strip().lower()
    idadetotal += idade
    if sexo == 'f' and idade < 20:
        mmenos20 += 1
    if sexo == 'm':
        if p == 1:
            idadedehomem = idade
        else:
            if idade > idadedehomem:
                idadedehomem = idade
                nomehomem = nome
print('A média de idade colocada é de {:.0f} anos.'.format(idadetotal / 4))
print('O homem mais velho se chama {} e tem idade de {} anos.'.format(nomehomem, idadedehomem))
print('Na lista ao total tem {} mulheres com menos de 20 anos.'.format(mmenos20))

