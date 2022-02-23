#Modificar as funções do 108, aceitando um parametro a mais, essa informado se os valores serão formatado
#ou não pela função moeda()
from modulos import moeda109
n = float(input('Digite o um valor em reais: '))
ta = float(input('Digite uma taxa (em %) para aumento do valor: '))
td = float(input('Digite uma taxa (em %) para subtração do valor: '))
formato = ''
while True:
    pergunta = str(input('Deseja que o valor venha formado em R$ (s ou n): ')).strip().lower()[0]
    if pergunta in 'Ss':
        formato=True
        break
    if pergunta in 'Nn':
        formato=False
        break
    else:
        print('A resposta dada é inválida, favor responder "s" para sim e "n" para não.')
print(f'A metade de {moeda109.moeda(n)} é {moeda109.metade(n, formato)}.')
print(f'O dobro de {moeda109.moeda(n)} é {moeda109.dobro(n, formato)}.')
print(f'O valor {moeda109.moeda(n)} aumentado em {ta}% é {moeda109.aumentar(n, ta, formato)}.')
print(f'O valor de {moeda109.moeda(n)} subtraído em {td}% é {moeda109.diminuir(n, td, formato)}')
