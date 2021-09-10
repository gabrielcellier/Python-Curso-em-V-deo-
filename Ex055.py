#ler peso de 5 pessoas e mostrar qual o maior e o menor
maior = 0
menor = 0
for p in range(1, 6):
    peso = float(input('Digite o peso (em kg) da {}ª pessoa: '.format(p)))
    if peso > maior or maior == 0: #se o valor for maior que o maior atual ou que 0 (o maior inicial), substitui ele
        maior = peso
    if peso < menor or menor == 0: #se o valor for menor que o emnor atual ou que 0 (menor inicial), substitui ele.
        menor = peso
print ('O maior peso escrito foi de {:.1f} kg e o menor de {:.1f} kg.'.format(maior, menor))
