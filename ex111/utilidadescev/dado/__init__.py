def leiadinheiro(msg):
    while True:
        entrada = str(input(msg)).strip().replace('.', ',')
        if entrada.isalpha() or entrada == '':
            print('Erro! Digite um valor válido (valor numérico).')

