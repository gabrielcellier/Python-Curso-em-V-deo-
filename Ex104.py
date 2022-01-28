#Função leiaint() para receber valor númerico. Enquanto não receber INT dará erro.
def leiaint(* num):
    """
    A função vai ler um número digitado pelo usuário. Só aceitará caso seja valor numérico.
    :param num: O valor numérco digitado pelo usuário.
    :return: Retornará frase validando o valor numérico digitado.
    """
    while True:
        n = str(input('Digite um valor númerico: '))
        if n.isnumeric():
            n = int(n)
            return f'O valor numérico digitado foi {n}.'
            break
        else:
            print('Erro! O valor digitado não é numérico.')


print(leiaint('num'))