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
    """
    Função que serve para colocar R$ e trocar ponto por vírgula na formatação dos valores.
    :param n: Valor a ser formatado, indicado pelo usuário.
    :param moeda: Campo usado para colocar o R$
    :return: Valor formatado usando R$ e vírgula no lugar do ponto.
    """
    return f'{moeda}{n}'.replace('.',',')

def resumo(n=0, ta=0, td=0):
    """
    Faz um resumo de todos os cálculos feitos com o valor dado pelo usuário.
    :param n: Valor dado pelo usuário.
    :param ta: Taxa de aumento dada pelo usuário.
    :param td: Taxa de subtração dada pelo usuário.
    :return: Resumo com os cálculos de dobro, metade, aumento e diminuição do valor dado pelo usuário.
    """
    sleep(1)
    print('-' * 30)
    print('Resumo do valor'.center(30))
    print('-' * 30)
    print(f'Preço analisado: {moeda(n)}'.center(30))
    print('-' * 30)
    print(f'Dobro do valor: {dobro(n, True)}'.center(30))
    print(f'Metade do valor: {metade(n, True)}'.center(30))
    print(f'Aumento de {ta}%: {aumentar(n, ta, True)}'.center(30))
    print(f'Subtraçao de {ta}%: {diminuir(n, td, True)}'.center(30))
    print('-' * 30)

def leiadinheiro(msg):
    valido = False
    while valido is False:
        numero = str(input(msg)).replace('.', ',').strip()
        if numero.isalpha():  #checando se resposta está escrita em extenso
            print('Erro! Digite o valor em forma numérica.')
        if numero.strip() == '': #checando se resposta foi vazia
            print('Erro! Preencha o campo com um valor numérico.')
        if numero.isalnum():
            print('Erro! Digite o valor somenta em forma numérica.')
        if numero.isnumeric(): #se valor for de fato número, transformar o str em float e retornar ele
            numero = float(numero)
            return numero
            valido = True

#.replace troca o ponto pela vírgula e .strip() tira espaços que tiverem sobrando antes e depois da resposta