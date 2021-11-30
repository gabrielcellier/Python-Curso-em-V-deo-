#Cadastrar 1 nome e 2 notas em cada lista. No fim mostrar o nome e média das notas.
#Perguntar se usuário quer ver a nota de algum aluno em específico e mostrar as notas.
lista = []
while True:
    nome = str(input('Digite o nome do aluno: ')).capitalize().strip()
    nota1 = float(input('Digite a 1a nota: '))
    nota2 = float(input('Digite a 2a nota: '))
    media = (nota1 + nota2) / 2
    lista.append([nome, [nota1, nota2], media])  #possível organizar como cada variavel vai entrar na lista
    cont = str(input('Deseja continuar (s/n)? ')).strip().lower()[0]
    while cont not in 'sn':
        cont = str(input('Resposta inválida. Deseja continuar (s/n)? ')).strip().lower()[0]
    if cont in 'n':
        break
print('---' * 12)
print(f'{"No.":<5}{"Nome":<15}{"Média":>8}')
print('---' * 12)
for i, n in enumerate(lista):
    print(f'{i:<5}{n[0]:<15}{n[2]:>7}')  #usado enumerate() para fazer em forma de lista vertical a lista de alunos
print('---' * 12)
while True:  #escolher número do aluno que quer ver info. Baseado em suas posições na lista
    valor = int(input('Escolha o No do aluno que deseja ver as notas. (0 interrompe): '))
    while valor > len(lista):  #não pode ser escolhido um número (índice) maior que o numero de alunos.
        valor = int(input('Escolha o No do aluno que deseja ver as notas. (0 interrompe): '))
    if valor == 0:
        break
    if valor <= len(lista) - 1 and valor != 0:     #se valor for menor que total de alunos e não for 0 (cancela ação) ele irá digitar as notas do aluno ecolhido
        print(f'As notas do aluno "{lista[valor][0]}" foram: {lista[valor][1]}'