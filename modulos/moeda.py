from time import sleep

def dobro(n=0, formato=False):
    """
    Função que dobrará o valor dado pelo usuário.
    :param n: Valor dado pelo usuário.
    :param formato: Se verdadeiro, valor será formatado em R$.
    :return: O valor já calculado.
    """
    sleep(1)
    calculo = n * 2
    if formato is False:
        return calculo
    if formato is True:
        return moeda(calculo)

def metade(n=0, formato=False):
    """
    Função que calculará a metade do valor dado pelo usuário.
    :param n: Valor dado pelo usuário.
    :param formato: Se verdadeiro, valor será formatado em R$.
    :return: Metade do valor dado pelo usuário.
    """
    sleep(1)
    calculo = n / 2
    if formato is False:
        return calculo
    if formato is True:
        return moeda(calculo)

def aumentar(n=0, t=0, formato=False):
    """
    Função que aumentará o valor dado pelo usuário pela taxa também dada pelo usuário.
    :param n: Valor dado pelo usuário.
    :param t: Taxa de aumento dada pelo usuário (em %).
    :param formato: Se verdadeiro, formatará o valor em R$.
    :return: O valor acrescido da taxa em % dada pelo usuário.
    """
    sleep(1)
    calculo = (n + (n * t/100))
    if formato is False:
        return calculo
    if formato is True:
        return moeda(calculo)

def diminuir(n=0, t=0, formato=False):
    """
    Função que diminuirá o valor dado pelo usuário pela taxa também dada pelo usuário.
    :param n: Valor dado pelo usuário.
    :param t: Taxa de diminuição (em %).
    :param formato: Se verdadeiro, formatará o valor em R$.
    :return: O valor decrescido da taxa em % dada pelo usuário.
    """
    sleep(1)
    calculo = (n -(n * t/100))
    if formato is False:
        return calculo
    if formato is True:
        return moeda(calculo)

def moeda(n=0, moeda='R$'):
    return f'{moeda}{n}'.replace('.',',')