#Função chamada voto() que recebe o ano de nascimento da pessoa. Retornar se ela tem que votar ou não
#ou se o voto é opcional (entre 16-18 anos e acima de 65 anos)
def voto(ano):
    from datetime import date
    idade = date.today().year - ano
    if idade >= 18:
        return f'O voto é obrigatório pois a pessoa tem {idade} anos.'
    elif 16 <= idade < 18 or idade >= 65:
        return f'O voto é opcional pois a pessoa tem {idade} anos.'
    else:
        return f'O voto é proibido pois a pessoa tem {idade} anos.'

ano = int(input('Digite o ano de nascimento para saber a situação da pessoa: '))
print(voto(ano))

#Não precisa escrever um voto(ano) se eu já jogar ele direto no print, que pegará o resultado com o return na função.

