#Perguntar distancia de uma viagem, até 200km cobrar 0,50 por km, acima de 200km cobrar 0,45
km = int(input('Digite a distancia total da viagem (em km): ')).
print ('A viagem percorrerá {} km de distância, sendo assim:'.format(km))
if km <=200:
    print ('O preço da viagem será de R${:.2f}, cobrando R$0,50 por km, valor para viagens de até 200 km de distância'
           .format(km * 0.50))
else:
    print ('O preço da viagem será de R${:.2f}, cobrando R$0,45 por km, valor para viagens acima de 200 km de distância\n'
           .format(km * 0.45))
print ('obrigado.')
