# montar uma programa que leia o numero inteiro e mostre o antecessor e sucessor
num = int(input('Digite um número inteiro:'))
print('O número digitado foi {}, seu antecessor é {} e seu sucessor {}.'
      .format(num, num -1, num + 1))

#poderia usar parenteses entre as contas no format, ou fazer também
# criando outras variáveis com as contas (n-1 e +1)
