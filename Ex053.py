#ler uma frase e descobrir se ela é um palíndromo (igual se digitada de trás pra frente)
from time import sleep
print('Digite uma frase, vamos descobrir se ela é um palíndromo.')
sleep(1)
while True:
    frase = input('Digite uma frase: ').strip().lower()
    if frase.islower():
        frase = str(frase).split()
        print('Frase válida. Aguarde.')
        break
    else:
        print('Frase inválida. Digite apenas letras, sem números.')
sleep(1)
junto = ''.join(frase) #coloca a string da 'frase' na variável junto sem espaços.
inverso = '' #variável vazia.
for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra] #adicionará uma letra por vez de tras pra frente.
print(junto, inverso)
sleep(1)
if junto == inverso:
    print ('A frase é palíndromo. Ou seja, igual se escrita dos dois lados.')
else:
    print ('A frase não é um palíndromo, como observado.')
#range(len(junto) -1*, -1**, -1***) (explicação abaixo)
#*: pega a última letra do 'junto' pois se a str tem 10 letras a última é no espaço 9 (pois a primeira é 0)
#**: -1 é pra ir pra primeira letra (a primeira letra é 0 mas tem que ir um a menos)
#***: ir diminuindo 1 por vez.