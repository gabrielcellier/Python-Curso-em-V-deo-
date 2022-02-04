from time import sleep
def aumentar(n, t):
    sleep(1)
    print('------')
    return f'O valor R${n} aumentado em {t}% fica R${t + (n * t/100)}.'

def diminuir(n, t):
    sleep(1)
    print('------')
    return f'O valor R${n} diminuido em {t}% fica R${t - (n * t/100)}.'

def dobro(n):
    sleep(1)
    print('------')
    return f'O dobro de R${n} é R${n * 2}.'

def metade(n):
    sleep(1)
    print('------')
    return f'Metade de R${n} é R${n / 2}.'

#No caso fiz as contas necessárias já direto na resposta.