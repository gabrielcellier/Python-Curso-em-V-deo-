#Criar função fatorial() que recebe o número e o show, que se sim mostra como foi feita a conta.
#Além disso criar um docstring explicando como funciona a função fatorial.
def fatorial(num, show=False):
    """
    A função fatorial irá calcular o fatorial do número escolhido pelo usuário.
    :param num: Número escolhido pelo usuário.
    :param show: Se verdadeiro, mostrará como o cálculo do número foi efetuado.
    :return:
    """
    from math import factorial
    from time import sleep
    calculo = factorial(num)
    print(f'O cálculo do fatorial de {num} é {calculo}')
    sleep(1)
    if show:
        for c in range(num, 0, -1):
            print(f'{c}', end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')

num = int(input('Qual número você quer calcular o fatorial? '))
show = str(input(f'Você deseja ver o cálculo do fatorial de {num} (s = sim, n = não): ').lower().strip()[0]
if show in 's':
    show=True
if show in 'n':
    show=False
fatorial(num, show)
