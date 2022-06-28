#Ler 3 números e mostrar qual o maior e o menor deles.
print('Digite três números. Ao fim mostraremos qual foi o maior e qual foi o menor')
maior = menor = 0
n1 = int(input('Digite um número: '))
maior = menor = n1
n2 = int(input('Digite um outro número: '))
if n2 > maior:
    maior = n2
if n2 < menor:
    menor = n2
n3 = int(input('Digite um terceiro número: '))
if n3 > maior:
    maior = n3
if n3 < menor:
    menor = n3
print(f'Os números digitados foram {n1}, {n2}, {n3}. O maior é o {maior} e o menor é o {menor}.')
#a cada pergunta se o valor fosse maior ou menor que o maior e o menor, substituiria o equivalente
