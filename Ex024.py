#Digite o nome da cidade e reconheça se ela começa com a palavra "santo"
cidade = str(input('Digite o nome completo da cidade: ')).strip().title()
separado = cidade.split()
print(f'O nome da cidade é {cidade}.'
      f'\nO primeiro nome contém a palavra "Santo"? {"Santo" in separado[0]}.'
      f'\nA resposta acima se justifica pois a primeira palavra do nome é "{separado[0]}".')

#possível usar cidade[:5] == 'Santo' na segunda frase.