#Crie um programa que leia um nome completo e reconheça se tem "Silva" ou não no nome.
nome = str(input('Digite o nome completo: ')).strip().title()
print ('O nome completo dado foi {}.'
       '\nO nome tem "Silva" nele? {}.'.format(nome, 'Silva' in nome))
#poderia colocar 'SILVA' in nome.upper() ou 'silva' in nome.lower() transformando tudo escrito em
#maiusculo ou minusculo e assim procurando do mesmo jeito no ''