#Ler numeros e colocar na lista. Mostrar a) qt de numeros digitados, b) Lista em ordem decrescente e c) Se valor '5' foi digitado
from time import sleep
lista = []
qtn = n5 = 0
while True:
    n = int(input('Digite um valor inteiro: '))  #posso colocar o lista.append() e fazer a pergunta direto nele
    lista.append(n)
    qtn += 1
    if n == 5:
        n5 += 1
    cont = str(input('Você deseja digitar mais um número (s/n): ')).strip().lower()[0]
    while cont not in 'sn':
        cont = str(input('Responda "s" ou "n". Você deseja digitar mais um número (s/n)? ')).strip().lower()[0]
    if cont in 'n':
        break
lista.sort(reverse=True)
sleep(0.5)
print('~*~' * 10)
print(f'Foram digitados ao todo {qtn} números.')
print(f'A lista em ordem decrescente é: {lista}')
print(f'O número 5 foi digitado ao todo {n5} vezes.')


