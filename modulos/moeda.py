from time import sleep

def dobro(n):
    sleep(1)
    print('---' * 10)
    return f'O dobro de R${n} é R${(n * 2):.2f}.'

def metade(n):
    sleep(1)
    print('---' * 10)
    return f'A metade de R${n} é R${(n / 2):.2f}.'

def aumentar(n, t):
    sleep(1)
    print('---' * 10)
    return f'O valor R${n} aumentado em {t}% é R${(n + (n * t/100)):.2f}.'

def diminuir(n, t):
    sleep(1)
    print('---' * 10)
    return f'O valor R${n} diminuído em {t}% é R${(n -(n * t/100)):.2f}.'