# Ter função 'escreva()' pra texto. Mostrar ela com barras (~~~) adaptada pro tamanho pra frase digitada
def escreva(texto):
    a = len(texto)
    print('~' * a)
    print(f'{texto}')
    print('~' * a)


frase = str(input('Digite um texto aqui: ')).strip()
escreva(frase)

