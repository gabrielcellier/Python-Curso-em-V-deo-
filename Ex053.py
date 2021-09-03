#ler uma frase e descobrir se ela é um palíndromo (igual se digitada de trás pra frente)
frase = str(input('Digite uma frase: ')).strip().lower().split()
junto = ''.join(frase) #tirar espaços da frase
inverso = '' #criou a variavel inverso que tem nada.
for letra in range (len(junto) - 1, -1, -1): #ver a nota no final
    inverso = inverso + junto[letra] #adicionou a frase
print (junto, inverso)
if junto == inverso:
    print ('A frase é palíndromo.')
else:
    print ('A frase não é um palíndromo, como observado.')
# range(len(junto) -1*, -1**, -1***) (explicação abaixo)
#*: pega a última letra do 'junto' pois se a str tem 10 letras a última é no espaço 9 (pois a primeira é 0)
#**: -1 é pra ir pra primeira letra (a primeira letra é 0 mas tem que ir um a menos)
#***: ir diminuindo 1 por vez.