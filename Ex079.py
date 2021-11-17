#Usuário pode digitar vários números e eles entram numa lista. Caso já tenha sido digitado ignorar o numero.
#Perguntar se quer continuar. No final mostrar todos os valores únicos digitados em ordem crescente.
from time import sleep
lista = []
while True:
    n = int(input('Digite um número inteiro: '))
    if n not in lista:    #só adicionará o valor se ele não estiver já na lista
        lista.append(n)
    else:
        print('Valor já adicionado a lista anteriormente, será desconsiderado.')
    sleep(0.3)
    cont = str(input('Você deseja continuar (s/n)? ')).strip().lower()[0]
    if cont not in 'ns':
        cont = str(input('Responda s (sim) ou n (não). Você deseja continuar (s/n)? '))
    if cont in 'n':
        break
    sleep(0.3)
lista.sort()
print(f'A lista dos números digitados em ordem crescente foi: {lista}')