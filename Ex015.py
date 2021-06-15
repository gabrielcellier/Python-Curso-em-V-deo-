#perguntas quantos dias ficou com o carro e a km. cobrar 60 por dia + 0,15 por km rodado.
d = int(input('Quantos dias o carro ficou alugado?'))
km = int(input('Quantos km foram rodados com o carro?'))
print('Será cobrado o valor de R${:.2f} pelos dias alugados e R${:.2f} pela kilometragem rodada'
      '\ntotalizando o valor de {:.2f}'
      '\nlembrando que é cobrado o valor de R$60 por dia e R$0,15 por km rodado.'
      .format(d * 60, km * 0.15, (d*60)+(km*0.15)))
#poderia ser criado uma variável já com o cálculo (d*60)+(km*0.15)