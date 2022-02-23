from time import sleep
def aumentar(n=0, t=0):
    sleep(1)
    return (n + (n * t/100))

def diminuir(n=0, t=0):
    sleep(1)
    return (n - (n * t/100))

def dobro(n=0):
    sleep(1)
    return n * 2

def metade(n=0):
    sleep(1)
    return n / 2

def moeda(n=0, moeda='R$'):
    return f'{moeda}{n}'.replace('.', ',')