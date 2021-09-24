#seguir a ideia do 61 porém perguntando se o usuario quer que mostre mais termos
#e responder até que ele digite que quer 0 termos.
print ('A seguir, digite o 1) termo inicial da PA, 2) razão e 3) número de termos desejados')
t1 = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão de progressão da PA: '))
termo = t1
cont = 1
total = 0
mais = 10 #o programa começa mostrando 10 termos
while mais != 0: #quando 'mais' = 0 quer dizer que o usuário não quer mais nenhum termo sendo calculado
    total = total + mais
    while cont <= total:
        print ('{} ->'.format(termo), end=' ')
        termo += r
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos a mais você deseja calcular na PA: '))
print ('O usuário indicou não querer mais calculos dessa PA.')

#1) como por padrão calculamos os 10 primeiros termos, o valor mais tá em 10.
#2) ele só para de calcular quando 'cont' atinge valor do total
#3) no entanto 'total' sempre pode aumentar enquanto receber valor (!= 0) de 'mais', perguntado no fim



