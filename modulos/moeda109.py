from time import sleep
def aumentar(n=0, t=0, formato=False):
    sleep(1)
    calculo = (t + (n * t/100))
    if formato is False:
        return calculo
    if formato is True:
        return moeda(calculo)

def diminuir(n=0, t=0, formato=False):
    sleep(1)
    calculo = (t - (n * t/100))
    if formato is False:
        return calculo
    if formato is True:
        return moeda(calculo)

def dobro(n=0, formato=False):
    sleep(1)
    calculo = n * 2
    if formato is False:
        return calculo
    if formato is True:
        return moeda(calculo)

def metade(n=0, formato=False):
    sleep(1)
    calculo = n / 2
    if formato is False:
        return calculo
    if formato is True:
        return moeda(calculo)

def moeda(n=0, moeda='R$'):
    return f'{moeda}{n}'.replace('.', ',')