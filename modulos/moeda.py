from time import sleep

def dobro(n=0):
    sleep(1)
    print('---' * 10)
    return f'{(n * 2):.2f}'

def metade(n=0):
    sleep(1)
    print('---' * 10)
    return f'{(n / 2):.2f}'

def aumentar(n=0, t=0):
    sleep(1)
    print('---' * 10)
    return f'{(n + (n * t/100)):.2f}'

def diminuir(n=0, t=0):
    sleep(1)
    print('---' * 10)
    return f'{(n -(n * t/100)):.2f}'

def moeda(n=0, moeda='R$'):
    return f'{moeda}{n}'.replace('.',',')