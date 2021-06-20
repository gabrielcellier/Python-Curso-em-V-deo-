#Digite o nome da cidade e reconheça se ela começa com a palavra "santo"
cidade = str(input('Digite o nome da cidade que você nasceu: ')).strip().title()
separado = cidade.split()
print ('O nome da cidade que você nasceu é {}.'
       '\nEla tem "Santo" no primeiro nome? {}.'
       '\nO primeiro nome da cidade é "{}" justificando a resposta acima.'
       .format(cidade, 'Santo' in cidade, separado[0]))
#poderia fazer (cidade[:5] == 'Santo') no .format(), o :5 se justifica pois a palavra Santo tem 5 caracteres
#logo ele procuraria se os 5 primeiros caracteres são iguais a 'Santo', poderia usar cidade[0:5] também.