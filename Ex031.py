#Perguntar distancia de uma viagem, até 200km cobrar 0,50 por km, acima de 200km cobrar 0,45
km = int(input('Digite a distância total da viagem (em km): '))
print ('A viagem custa R$0,50/km até 200 km, a partir disso custa R$0,45/km')
if km > 200:
    print ('A viagem custará R${:.2f} pois sua km total é de {}km.'.format(km * 0.45, km))
else:
    print ('A viagem custará R${:.2f} pois sua km total é de {}km.'.format(km * 0.50, km))
#é possível fazer só a conta dentro do if..else e deixar o print no fim com a variável usada no if else