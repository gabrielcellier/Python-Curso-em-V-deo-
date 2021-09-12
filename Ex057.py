#ler sexo da pessoa (m/f), se a pessoa digitar errado peça pra digitar novamente.
s = str(input('Por favor informe o seu sexo (m/f): ')).lower().strip()[0]
while s not in 'MFmf': #se resposta de s não for M, m, F ou f repetira a s abaixo
    s = str(input('Resposta inválida. Por favor informe o seu sexo (m/f): ')).lower().strip()[0]
print ('A resposta dada foi {} e foi registrada com sucesso.'.format(s))
