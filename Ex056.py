#ler o nome, idade e sexo de 4 pessoas. mostrar a 1) média de idade do grupo,
# 2) nome do homem mais velho, #3) quantas mulheres tem menos de 20 anos.
from time import sleep
idadetotal = qtmulheres = idadehomem = 0
nomehomem = ''
print('Digite o nome, idade e sexto de 4 pessoas. Vamos comparar as informações.')
sleep(1)
for c in range (1, 5):
    while True:
        nome = input('Digite o nome: ').strip().capitalize()
        if nome.isalpha():
            nome = str(nome)
            print('Resposta válida!')
            sleep(1)
