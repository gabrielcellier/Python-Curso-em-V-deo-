#Função notas() recebendo vários números. No fim mostrar: qt de notas, maior nota, menor nota, média da turma
# e situaçao (opcional). Fazer docstring da função.
#obs: Situação é em relação a média da sala. Se for abaixo da média é ruim.
def notas(*n, sit=False):
    """
    A função receberá as notas colocadas pelo usuário e fará uma análise delas, apontando quantidade,
    média e maior e menor nota.
    :param n: As notas, que serão colocadas pelo usuário na quantidade desejada.
    :param sit: Opcional, a situação será definida a partir da média das notas inseridas.
    :return: Retornaremos uma lista com as notas e as informações extraídas delas.
    """
    dici = {}
    dici['total das notas'] = len(n)
    dici['maior nota'] = max(n)
    dici['menor nota'] = min(n)
    dici['média das notas'] = sum(n)/len(n)
    if sit:
        if dici['média das notas'] >= 7:
            dici['situação'] = 'Boa (média acima de 7)'
        if dici['média das notas'] >= 5:
            dici['situação'] = 'Média (média entre 5 e 7)'
        if dici['média das notas'] < 5:
            dici['situação'] ='Ruim (média abaixo de 5)'
    print(dici)

resposta = notas(8, 10, 8, 3, sit=True)


