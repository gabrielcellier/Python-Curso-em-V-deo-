#criar tupla com contagem de 0 a 20 por extenso. Usuário deve escolher um número de 0 a 20 e ele aparecer escrito.
from time import sleep
num = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito',
       'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis',
       'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    n = int(input('Digite um número entre 0 e 20: '))
    if n < 0 or n > 20:
        print(f'Erro, o valor digitado {n} não está entre 0 e 20! Digite novamente.')
        n = int(input('Digite um número entre 0 e 20: '))
    print (f'O número digitado foi {n}, que escrito por extenso é {num[n]}.')
    sleep(0.3)
    cont = str(input('Deseja continuar? (s/n): ')).lower().strip()[0]
    if cont == 'n':
        break
    sleep(0.5)
print ('O programa foi encerrado!')
