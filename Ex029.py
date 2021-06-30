#Escreva a velocidade do carro, se for acima de 80km/h deverá tomar multa de valor R$7 pra cada km/h a mais
vel = int(input('Qual a velocidade do carro: '))
multa = vel - 80
if multa >=1:
    print ('Devido a velocidade {} o motorista pagará multa de R${:.2f}'.format(vel, multa * 7))
else:
    print ('O motorista está dentro da velocidade permitida.')
#poderia fazer o cálculo direto no .format((vel - 80) * 7) com if vel > 80