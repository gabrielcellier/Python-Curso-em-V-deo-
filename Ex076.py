#Fazer tupla com produto e seus preços e depois listar todos eles como se fosse uma tabela.
lista = ('Cerveja', 20,
         'Refrigerante', 10,
         'Pao de alho', 23,
         'Farofa', 9.90,
         'Picanha', 50,
         'Linguiça', 28.80,
         'Água', 6.80,
         'Maionese', 18.90)
print ('----' * 9)
for pos in range (0, len(lista)):
    if pos % 2 == 0:   #como o primeiro, terceiro, quinto etc itens são os nomes, puxamos eles a esquerda
        print(f'{lista[pos]:.<30}', end='')
    if pos % 2 == 1:   #como o segundo, quarto etc items são os preços, eles vão a direita
        print(f'R${lista[pos]:>5.2f}')
('----' * 9)
#ver anotações no caderno.