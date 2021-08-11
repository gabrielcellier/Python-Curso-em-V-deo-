#ler peso de 5 pessoas e mostrar qual o maior e o menor
lista = []
for p in range (1, 6):
    peso = float(input('Digite o peso da {}ª pessoa (em kg): '.format(p)))
    lista = lista + [peso] #adicionaremos os 'peso' nessa lista 'lista'
print('O maior peso foi {:.2f} kg e o menor foi {:.2f} kg.'.format(max(lista), min(lista)))
#nesse modo criamos uma lista que será atualizada com todos os valores de 'peso' inseridos
#usando max() e min() selecionaremos os maiores e menores valores dessa lista