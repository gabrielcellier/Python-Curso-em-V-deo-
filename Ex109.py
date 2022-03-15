#Modificar as funções do 108, aceitando um parametro a mais, essa informado se os valores serão formatado
#ou não pela função moeda()
from modulos import moeda
print('A partir do valor dado (em R$) realizaremos diferentes cálculos.')

n = float(input('Digite o valor (em reais) que será usado nos cálculos: R$ '))
ta = float(input('Digite a taxa em % em quanto deseja aumentar o valor: '))
td = float(input('Digite a taxa em % em quanto deseja diminuir o valor: '))
formato = ''
while True:
    pergunta = str(input('Formatar valores em "R$x,xx"? Responda "s" ou "n": ')).strip().lower()[0]
    if pergunta in 'Ss':
        print('A resposta foi sim, os valores serão formatados usando R$ e vírgula.')
        formato=True
        break
    elif pergunta in 'Nn':
        print('A resposta foi não, os valores não serão formatados usando R$ e vírgula.')
        formato=False
        break
    else:
        print('A resposta dada é inválida. Responda com "s" para sim e "n" para não.')

print('---' * 10)
print(f'O dobro de {n} é {moeda.dobro(n)}.')
print(f'A metade de {n} é {moeda.metade(n)}.')
print(f'O valor {n} acrescido de {ta}% é {moeda.aumentar(n, ta)}.')
print(f'O valor {n} com decréscimo de {td}% é {moeda.diminuir(n, td)}.')

