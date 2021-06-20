#Ler um nome completo e escrever em minusculo, maiusculo
#Qt de letras e qt de letras do primeiro nome
nome = str(input('Digite o nome completo: ')).strip()
separado = nome.split()
print ('O nome dado foi {}'
       '\nO nome todo em minúsculo: {}'
       '\nO nome todo em maíusculo: {}'
       '\nO nome ao todo conta com {} letras'
       '\nO primeiro nome é {} e conta com {} letras ao todo.'
       .format(nome, nome.lower(), nome.upper(), len(nome) - nome.count(' '), separado[0], len(separado[0])))
#Para saber a qt de letra do primeiro nome poderia usar nome.find(' ') pois o primeiro espaço só ocorre
#depois do primeiro nome, como ele aponta qual o ponto que ocorre o espaço e a contagem começa no 0, logo ele apontaria
#a quantidade de espaços que tem letras.
