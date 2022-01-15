#Função chamada voto() que recebe o ano de nascimento da pessoa. Retornar se ela tem que votar ou não
#ou se o voto é opcional (entre 16-18 anos e acima de 65 anos)
from datetime import date
def voto(ano):
    idade = date.today().year - ano
    if idade < 16:
        return print(f'Devido a idade de {idade} o voto é PROIBIDO.')
    if idade >=16 and idade < 18 or idade >= 65:
        return print(f'Devido a idade de {idade} o voto é OPCIONAL.')
    if idade >= 18:
        return print(f'Devido a idade de {idade} o voto é OBRIGATÓRIO.')

ano = int(input('Digite o ano de nascimento da pessoa: '))
voto(ano)
