#Ler um nome completo e separar o nome e o último sobrenome.
from time import sleep
print('Digite um nome completo. Iremos separar o nome e o último sobrenome.')
sleep(1)
nome = str(input('Digite o nome completo: ')).strip().title()
separado = nome.split()
sleep(1)
print(f'O nome digitado foi {nome}.'
      f'\n O primeiro nome é {separado[0]} e o último sobrenome é {separado[-1]}.')
#[-1] foi usado pois sempre buscará o último item da lista criada pelo .split()

