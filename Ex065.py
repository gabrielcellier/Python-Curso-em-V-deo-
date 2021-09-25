#Ler números inteiros, mostrar a média de todos eles, maior e menor valor digitado
#perguntar ao usuário se ele quer continuar digitando outros números
from time import sleep
print ('O usuário digitará quantos números quiser, no fim indicaremos o maior, o menor e a média.')
soma = numeros = 0
num = int(input('Digite um número: '))
maior = menor = num     #maior e menor definido como o primeiro valor 'num'
continuar = 0
while continuar != 'n':
   soma += num       #soma de todos os valores 'num' que forem escritos, p/ calcular média
   numeros += 1      #+1 pra cada 'num' digitado, p/ calcular média
   if num > maior:   #substitui o primeiro 'num' se algum 'num' dps for maior
      maior = num
   if num < menor:   #substitui o primeiro 'num' se algum 'num' dps for menor.
      menor = num
   sleep(0.5)
   continuar = str(input('Deseja continuar (s/n): ')).strip().lower()
   if continuar not in 'n':       #se for indicado 's' será perguntado novo 'num'
      num = int(input('Digite um novo número: '))
print ('O maior número digitado foi: {}, o menor: {}, a média dos valores: {:.2f}.'
       .format(maior, menor, (soma / numeros)))

#1) poderia fazer um valor de 's' e deixar o while continuar in 'Ss', isso tiraria necessidade do .lower()
