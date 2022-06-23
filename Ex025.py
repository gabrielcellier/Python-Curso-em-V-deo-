#Crie um programa que leia um nome completo e reconheça se tem "Silva" ou não no nome.
print('Digite um nome completo, vamos procurar se tem o sobrenome Silva nele.')
nome = str(input('Digite o nome completo: ')).strip().title()
print(f'O nome digitado foi {nome}.'
      f'\nEle tem Silva no nome? {"Silva" in nome}.')
