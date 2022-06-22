#Ler um nome completo e escrever em minusculo, maiusculo
#Qt de letras e qt de letras do primeiro nome
from time import sleep
print('Digite o nome completo, mostraremos variações na sua escrita.')
sleep(1)
nome = str(input('Digite o nome completo a seguir: ')).strip()
separado = nome.split() #separa cada palavra. Usaremos para selecionar só o 1o nome.
sleep(1)
print(f'O nome digitado foi: {nome}.'
      f'\no nome arrumado é: {nome.title()}'
      f'\no nome todo em maíusculo: {nome.upper()}.'
      f'\no nome todo em minúsculo: {nome.lower()}.'
      f'\no nome conta com {len(nome) - nome.count(" ")} letras.'
      f'\no primeiro nome tem {len(separado[0])}.')

#'- nome.count(" ")' foi usado para substrair os espaços vazios da contagem do len().