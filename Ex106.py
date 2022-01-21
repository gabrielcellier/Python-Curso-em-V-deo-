#Fazer mini-sistema do Interactive Help. O usuário digitará o comando e aparecerá o manual.
#Se digitar 'fim' se encerra.
def ajuda(com):
    help(com)

def titulo(msg, cor=0):
    tam = len(msg)
    print('~' * tam + 4)
    print(f'  {msg}')
    print('~' * tam + 4)

comando = ''
while True:
    comando = str(input('Função ou Biblioteca > '))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)