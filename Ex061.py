#ler o primeiro termo e razão do PA, mostrar os 10 primeiros termos usando while
from time import sleep
print('Gerador de Progressão Aritmética. Coloque o 1° termo e razão e calcularemos os 10 próximos termos.')
sleep(1)
t = r = 0
while t != "" and r != "":
    t = input('Digite o primeiro termo da PA: ').strip()
    r = input('Digite a razão da PA: ').strip()
    if t.isnumeric() and r.isnumeric():
        print('Valores válidos! Agora calcularemos a PA.')
        t = int(t)
        r = int(r)
    else:
        print('Valores inválidos. Digite um número inteiro como primeiro termo e razão da PA.')
        sleep(1)
sleep(1)
termo = t
cont = 1
while cont <= 10:
    print(f'{termo}', end=" ")
    cont += 1
    termo += r #adicionado o valor 'r' no termo anterior.
print(f'\n Acima os 10 primeiros termos da PA com primeiro termo {t} e razão {r}.')

