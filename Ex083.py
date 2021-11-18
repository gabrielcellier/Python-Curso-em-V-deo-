#Usuario digitar uma expressão qualquer com parênteses. Analisar se a expressão está com parenteses abertos e
#fechados na ordem correta
formula = str(input('Digite a expressão que será verificada: '))
lista = []
for simbolo in formula:
    if simbolo == '(':
        lista.append('(')  #a cada "(" ele adicionará um "(" na "lista"
    elif simbolo == ')':
        if len(lista) > 0:  #a cada ")", se tiver já um "(" na lista ele deletará esse (
            lista.pop()
        else:
            lista.append(')') #se não tiver nenhum item na lista, ou seja, algum "(" o ")" só será adicionado.
            break
if len(lista) == 0:
    print('Sua fórmula está correta, com mesma quantidade de "(" e ")".')
else:
    print('Sua fórmula está incorreta, conta com diferentes quantidades e "(" e ")".')

