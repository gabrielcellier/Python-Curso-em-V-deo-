def fatorial(num, show=False):
    """
    Função fatorial() irá calcular o fatorial no número colocado pelo usuário.
    :param num: O número inteiro colocado pelo usuário.
    :param show: Se colocado True, será mostrado o cálculo fatorial feito no num.
    :return:
    """
    from time import sleep
    from math import factorial
    n = factorial(num)
    print(f'O fatorial de {num} é {n}.')
    sleep(1)
    if show:
        for c in range(num, 0, -1):
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            elif c == 1:
                print(' = ', end='')
                print(n)


num = int(input('Digite o número para cálculo de seu fatorial: '))
show = bool(input('Digite True se deseja ver o cálculo e False se não deseja: '))
fatorial(num, show)
