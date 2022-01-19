#Função leiaint() para receber valor númerico. Enquanto não receber INT dará erro.
def leiaint(* num):
    while True:
        n = str(input('Digite um número: '))
        if n.isnumeric():
            n = int(n)
            break
        else:
            print('Erro! Não foi digitado um número.')
    print(f'O número digitado foi {n}.')

n = leiaint('Digite um número: ')

#Como no ex103, usamos str para pegar o valor e depois fazemos a validaçao de ser um número ou não usando o g.isnumeric()
