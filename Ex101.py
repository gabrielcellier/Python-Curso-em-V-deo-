#Função chamada voto() que recebe o ano de nascimento da pessoa. Retornar se ela tem que votar ou não
#ou se o voto é opcional (entre 16-18 anos e acima de 65 anos)
def voto(ano):
    from datetime import date   #válido colocar dentro se só for ser usado na função
    idade = date.today().year - ano
    if idade < 16:
        return f'Na idade de {idade} o voto é PROIBIDO.'
    elif 16 <= idade < 18 or idade >= 65:
        return f'Na idade de {idade} o voto é OPCIONAL.'
    elif idade >= 18:
        return f'Na idade de {idade} o voto é OBRIGATÓRIO.'

ano = int(input('Digite o ano de nascimento da pessoa: '))
print(voto(ano))

#Não precisa escrever um voto(ano) se eu já jogar ele direto no print, que pegará o resultado com o return na função.

