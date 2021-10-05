#Tupla com várias palavras (s/ acentos), mostrar todas as vogais de cada palavra.
lista = ('arroz', 'feijao', 'agua', 'cafe', 'canela', 'pao', 'queijo', 'manteiga',
       'presunto', 'biscoito', 'torrada', 'mortadela', 'leite', 'pao doce',
       'margarina', 'bolo', 'torta', 'suco', 'cha')
for comida in lista:   #cada item da lista se torna uma 'comida'
    print(f'\nNa palavra "{comida}" tem as vogais:', end=' ')
    for letra in comida:    #cada item de comida (letra) se torna um 'letra'
        if letra in 'aeiou':   #se a letrar for vogal printar a própria letra
            print (letra, end=' ')