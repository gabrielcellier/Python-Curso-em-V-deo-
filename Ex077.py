#Tupla com várias palavras (s/ acentos), mostrar todas as vogais de cada palavra.
lista = ('arroz', 'feijao', 'agua', 'cafe', 'canela', 'pao', 'queijo', 'manteiga',
       'presunto', 'biscoito', 'torrada', 'mortadela', 'leite', 'pao doce',
       'margarina', 'bolo', 'torta', 'suco', 'cha')
for comida in lista:
    print(f'\n A comida "{comida}" tem as vogais:', end=' ')
    for letra in comida:
        if letra in 'aeiou':
            print(f'{letra}', end=' ')