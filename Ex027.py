#Ler um nome completo e separar o nome e o último sobrenome.
n = str(input('Digite um nome completo: ')).strip().title()
nome = n.split()
print ('O primeiro nome digitado foi {} e o último foi {}.'.format(nome[0], nome[-1]))
#no split nome[0] é o primeiro conjunto e o [-1] sempre será o último
#Como o nome nao é utilizado, o .split() poderia ser colocado junto a variavel n após o .title()

