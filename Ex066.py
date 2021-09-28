#programa que leia vários números inteiros. Só para quando digitar '999'.
#Mostrar quantos números foram digitados a soma deles.
print ('Digite um número inteiro, mostraremos a soma total deles e quantos números foram digitados!')
print ('Digite 999 para que o programa seja encerrado')
qt = s = 0
while True:
    n = int(input('Digite um número inteiro (999 p/ parar): '))
    if n == 999: #colocar antes para que o 999 não conte no 'qt' e 's'
        break
    qt += 1
    s += n
print(f'Ao todo foram digitados {qt} números, no total somando {s}.')