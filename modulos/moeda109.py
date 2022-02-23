from time import sleep
def aumentar(n=0, t=0, formato=False):
    """
    Funçao que aumentará o valor dado conforme a taxa indicada pelo usuário.
    :param n: Valor
    :param t: Taxa de aumento do valor
    :param formato: Para formatar valores em R$.
    :return: Retorna o valor com o acréscimo da taxa
    """
    sleep(1)
    calculo = (t + (n * t/100))
    if formato is False:
        return calculo
    if formato is True:
        return moeda(calculo)

def diminuir(n=0, t=0, formato=False):
    """
    Função que irá diminuir o valor dado conforme a taxa indicado pelo usuário.
    :param n: Valor
    :param t: Taxa de subtração do valor
    :param formato: Para formatar os valores em R$
    :return: Valor calculado conforme a taxa indicada
    """
    sleep(1)
    calculo = (t - (n * t/100))
    if formato is False:
        return calculo
    if formato is True:
        return moeda(calculo)

def dobro(n=0, formato=False):
    """
    Função que dobrará o valor indicado pelo usuário
    :param n: Valor
    :param formato: Para formatar o valor em R$
    :return: O dobro do valor indicado pelo usuário
    """
    sleep(1)
    calculo = n * 2
    if formato is False:
        return calculo
    if formato is True:
        return moeda(calculo)

def metade(n=0, formato=False):
    """
    Função calculará metade do valor indicado pelo usuário
    :param n: Valor
    :param formato: Para formatar o valor em R$
    :return: Metade do valor indicado pelo usuário
    """
    sleep(1)
    calculo = n / 2
    if formato is False:
        return calculo
    if formato is True:
        return moeda(calculo)

def moeda(n=0, moeda='R$'):
    """
    Função para formatar o valor e os resultados usando R$ e vírgula no lugar do ponto
    :param n: Valor
    :param moeda: Para colocar R$ antes do valor
    :return: Retorna o valor no formato R$XX,XX
    """
    return f'{moeda}{n}'.replace('.', ',')