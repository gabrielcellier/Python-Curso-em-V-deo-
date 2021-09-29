#Ler idade e sexo de várias pessoas e perguntar se usuário quer parar. Quando parar mostrar:
#a)Quantas pessoas com 18 ou mais anos, b) Quantos homens no total, c)Qt mulheres com menos de 20 anos.
maior = homem = mulher20 = 0
print ('Digite a idade e sexo das pessoas. Mostraremos algumas estatísticas quanto aos dados escritos')
while True:
    i = int(input('Digite a idade da pessoa: '))
    s = ' '
    while s not in 'MmFf':
        s = str(input('Digite o sexo da pessoa (m/f): ')).strip().lower()[0]
    if i >= 18:
        maior += 1
    if s in 'm':
        homem += 1
    if s in 'f':      #poderia fazer o if com as duas condições s in 'f' AND i < 20.
        if i < 20:
            mulher20 += 1
    p = str(input('Você deseja digitar mais dados (s/n)? ')).strip().lower() [0]
    if p not in 'sn':
        p = str(input('Resposta inválida! Você deseja digitar mais dados (s/n)? '))
    if p == 'n':
        break
print ('---' * 10)
print (f'''Conforme solicitado o programa foi encerrado!
Foram escritos {maior} pessoas acima de 18 anos, total de {homem} homens e {mulher20} mulheres abaixo dos 20 anos.''')

