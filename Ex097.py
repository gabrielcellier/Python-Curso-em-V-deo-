# Ter função 'escreva()' pra texto. Mostrar ela com barras (~~~) adaptada pro tamanho pra frase digitada
def escreva(frase):
    a = len(frase) + 6
    print('~' * a)
    print(f'   {frase}')
    print('~' * a)

escreva('oioioioi')

