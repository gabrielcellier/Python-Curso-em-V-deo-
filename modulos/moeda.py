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
    return f'O valor de R${n} aumentado em {t}% fica R${(t + (n * t/100)):.2f}.'

def diminuir(n, t):
    sleep(1)
    print('---' * 10)
    return f'O valor de R${n} diminuindo em {t}% fica R${(t - (n * t/100)):.2f}.'

#No caso fiz as contas necessárias já direto na resposta.