from time import sleep
def aumentar(n=0, t=0):
    sleep(1)
    print('------')
    return f'O valor R${n} aumentado em {t}% fica R${t + (n * t/100)}'

def diminuir(n=0, t=0):
    sleep(1)
    print('------')
    return f'O valor R${n} diminuido em {t}% fica R${t - (n * t/100)}'

def dobro(n=0):
    sleep(1)
    print('------')
    return f'O dobro de R${n} é R${n * 2}'

def metade(n=0):
    sleep(1)
    print('------')
    return f'Metade de R${n} é R${n / 2}'

def moeda(n=0, moeda='R$'):
    return f'{moeda}{n}'.replace('.', ',')


#1)elemento 'moeda=R$' criado apenas para jogar na função, sempre será R$ pois não perguntamos pro usuário sobre ele.
#2) .replace('.', ',') substituirá tudo nessa frase que tiver '.' por ','