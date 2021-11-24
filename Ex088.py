#Perguntar qt de jogos. Fazer jogos de 6 números (não podem se repetir) na qt desejada.
#Mostrar tudo como lista composta em ordem crescente.
jogo = []
for n in range (0, 6):
    num = int(input(f'Digite o {n+1}º número: '))
    while num in jogo:
        num = int(input(f'Número já digitado! Digite um novo número: '))
    jogo.append(num)
    cont = str(input())

