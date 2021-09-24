#seguir a ideia do 61 porém perguntando se o usuario quer que mostre mais termos
#e responder até que ele digite que quer 0 termos.
print ('A seguir, digite o 1) termo inicial da PA, 2) razão e 3) número de termos desejados')
t1 = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão de progressão da PA: '))
td = int(input('Digite quantos termos você deseja na PA: '))
termo = t1
cont = 1
while cont <= td:
    print ('{} ->'.format(termo), end=' ')
    termo += r
    cont += 1
print ('fim!')
print ('Acima foram listados todos os {} termos da PA de razão {} e primeiro termo {}'
       .format(td, r, t1))