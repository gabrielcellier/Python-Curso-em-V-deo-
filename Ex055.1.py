#ler peso de 5 pessoas e mostrar qual o maior e o menor
lista = []
for p in range (1, 6):
    peso = float(input('Digite o peso em kg da {}ª pessoa: '.format(p)))
    lista += [peso]
print ('O maior peso escrito foi de {:.1f} kg e o menor de {:.1f} kg.'.format(max(lista), min(lista)))

#nesse modo criamos uma lista que será atualizada com todos os valores de 'peso' inseridos
#usando max() e min() selecionaremos os maiores e menores valores dessa lista