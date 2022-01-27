# Fazer mini-sistema do Interactive Help. O usuário digitará o comando e aparecerá o manual.
# Se digitar 'fim' se encerra.

# lista com índice de cores que serão associadas as funções do interactive help
c = ('\033[m',  # 0 - sem cor
     '\033[0;30;41m',  # 1 - vermelho
     '\033[0;30;42m',  # 2 - verde
     '\033[0;30;43m',  # 3 - amarelo
     '\033[0;30;44m',  # 4 - azul
     '\033[0;30;45m',  # 5 - roxo
     '\033[7;30m'      # 6 - branco
     );


def ajuda(com):  # função para pegar o valor colocado dentro do () do help()
    título(f'Acessando o manual da função \'{com}\'', 4)
    print(cor[6], end='')
    help(com)
    print(cor[0], end='')


def título(msg, cor=0):  #função para associar as cores a cada uma das funções.
    tamanho = len(msg)
    print(c[cor], end='')  # para adicionar a cor no texto abaixo
    print('~' * tamanho + 4)
    print(f'  {msg}')
    print('~' * tamanho + 4)
    print(c[0], end='')  # termina a adição de cor


comando = ''
while True:
    título('Sistema de ajuda PyHelp', 1)  # (msg, cor) conforme definido na função 'título()'
    comando = str(input('Função ou Biblioteca ("fim" p/ sair) >> '))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
