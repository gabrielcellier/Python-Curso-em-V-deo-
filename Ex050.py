#ler 6 números inteiros (com for) e mostrar soma apenas dos números pares digitados
from time import sleep
soma = cont = 0
print('O usuário digitará 6 números. Contaremos os números pares e somaremos eles.')
sleep(1)
for c in range (1, 7):
    while True:
        n = input(f'{c}° Número: Digite um número INTEIRO: ')
        if n.isnumeric(): #checa se valor é INT e transforma ele em INT
            n = int(n)
            if n % 2 == 0: #se esse número for par add 1 no contador e ele próprio na soma.
                cont += 1
                soma += n
            break
        else:
            print('Erro. Digite um número inteiro.')
sleep(1)
print(f'Ao todo foram digitados {cont} números pares. A soma deles é {soma}.')
