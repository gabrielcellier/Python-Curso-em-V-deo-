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
    calculo = (n + (n * t/100))
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
    calculo = (n - (n * t/100))
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

def resumo(n=0, ta=0, td=0):
    """
    Faz uma tabela com resumo de todos as funções e seus cálculos que esse módulo tem.
    :param n: Valor a ser usado nos cálculos
    :param ta: Taxa de aumento do valor
    :param td: Taxa de subtração do valor
    :return: Tabela com valor analisado, o dobro, metade, aumento e substração em % dado pelo usuário
    """
    sleep(1)
    print('-' * 30)
    print('Resumo do Valor'.center(30))
    print('-' * 30)
    print(f'Preço analisado: {moeda(n)}'.center(30))
    print('-' * 30)
    print(f'Dobro do valor: {dobro(n, True)}'.center(30))
    print(f'Metade do valor: {metade(n, True)}'.center(30))
    print(f'Aumento de {ta}%: {aumentar(n, ta, True)}'.center(30))
    print(f'Subtração de {td}%: {diminuir(n, td, True)}'.center(30))
    print('-' * 30)