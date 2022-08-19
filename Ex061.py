#ler o primeiro termo e razão do PA, mostrar os 10 primeiros termos usando while
from time import sleep
print('Digite o primeiro termo e a razão da PA, mostraremos os 10 primeiros termos.')
print('O programa só trabalha com números inteiros.')
sleep(1)
t = r = 0
while t != "" and r != "":
    t = input('Digite o primeiro termo: ').strip()
    r = input('Digite a razão da PA: ').strip()
    if t.isnumeric() and r.isnumeric():
        t = int(t)
        r = int(r)
        print('Valores válidos. Calcularemos a sua PA.')
    else:
        print('Valores inválidos. Digite números inteiros.')
        sleep(1)
sleep(1)
cont = 1
while cont <= 10: #contador até 10 pois PA de 10 termos.
    print(f'{t}', end=' ')
    cont += 1
    t += r #adicionando o valor 'r' no termo anterior.
print(f'\n Acima os 10 primeiros termos da PA, com primeiro termo {p} e razão {r}.')
#\n para quebrar a linha depois de usarmos o end=' ' no print()

