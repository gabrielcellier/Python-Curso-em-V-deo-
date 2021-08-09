#ler uma frase e descobrir se ela é um palíndromo (igual se digitada de trás pra frente)
frase = str(input('Digite uma frase: ')).strip().lower().split()
junto = ''.join(frase)
inverso = ''
for letra in range (len(junto) - 1, -1, -1): #ver a nota no final
    inverso = inverso + junto[letra]
print (junto, inverso)
if junto == inverso:
    print ('A frase é palíndromo.')
else:
    print ('A frase não é um palíndromo, como observado.')
#poderia tirar o for e usar apenas inverso = junto[::-1] junto do if pra comparar.