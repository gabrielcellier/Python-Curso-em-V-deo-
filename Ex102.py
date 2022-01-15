#Criar função fatorial() que recebe o número e o show, que se sim mostra como foi feita a conta.
#Além disso criar um docstring explicando como funciona a função fatorial.
def fatorial(a, show=False):
    """
    A função fatorial(a, show=False) serve para calcular o fatorial do número desejado.
    :param a: O número que o usuário escolhe para ser calculado o fatorial
    :param show: Por padrão não aparece, se desejado pode-se mostrar o cálculo do fatorial.
    """
    from math import factorial
    from time import sleep
    resultado = factorial(a)
    print('---' * 11)
    print(f'O fatorial do número {a} é {resultado}')
    sleep(1)
    if show == True:
        print(f'O cálculo do fatorial de {a}:')
        sleep(1)
        for c in range(a, 0, -1):   #fazer contador do número escolhido até 1 (calculo fatorial)
            print(f'{c}', end='')  #Para mostrar sempre o número entre cada x ou =
            if c > 1:
                print(' x ', end='') #se número for maior que 1, ou seja, não o último da multiplicação, botar x entre eles.
            else:
                print(' = ', end='') #se número for o 1, ele é o último da multipli. logo botar um = após ele.
        print(resultado) #finalmente o resultado após todos os n da multiplicação mostrados
        print('---' * 11)

num = int(input('Digite o número para calcular seu fatorial: '))
show = bool(input('Você deseja ver o calculo que foi feito (True ou False)? '))
fatorial(num, show)
