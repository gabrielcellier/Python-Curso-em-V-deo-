#criar tupla com contagem de 0 a 20 por extenso. Usuário deve escolher um número de 0 a 20 e ele aparecer escrito.
from time import sleep
lista = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete',
         'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze',
         'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    n = int(input('Escolha um valor entre 0 e 20: '))
    if 0 <= n <= 20:      #ou if n < 0 or n > 20
        print (f'Erro! O valor digitado {n} não está entre 0 e 20.')
        n = int(input('Escolha um valor entre 0 e 20: '))
    print (f'O número digitado foi {n}, que por extenso é {lista [n]}.')
    cont = str(input('Você deseja continuar (s/n)? ')).strip().lower()[0]
    if cont not in 'sn':
        cont = str(input('Erro! Você deseja continuar (s/n)? ')).strip().lower()[0]
    if cont in 'n':
        break
print ('O programa foi encerrado!')