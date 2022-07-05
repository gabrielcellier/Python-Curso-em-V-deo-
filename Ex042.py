#ver se pode fazer triangulo, se todos os lados forem iguais: equilatero, 2 lados iguais: isósceles
#escaleno se forem todos diferentes
from time import sleep
print('Digite os três lados do triângulo, vamos definir que tipo de triangulo que ele é.')
sleep(1)
while True:
    l1 = float(input('Digite o 1° segmento do triangulo: '))
    l2 = float(input('Digite o 2° segmento do triangulo: '))
    l3 = float(input('Digite o 2° segmento do triangulo: '))
    sleep(0.5)
    if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
        print(f'O triângulo pode ser formado com os segmentos {l1}, {l2} e {l3}.')
        break
    else:
        print('Os segmentos não apresentam condições de formar um triangulo.')
        print('Digite valores válidos.')
sleep(1)
if l1 == l2 == l3:
    print('O triângulo é equilátero pois todos os segmentos são iguais.')
elif l1 == l2 or l1 == l3 or l3 == l2:
    print('O triângulo é isósceles pois tem dois segmentos iguais.')
elif l1 != l2 != l3 != l1:
    print('O triangulo é escaleno pois conta com três segmentos diferentes.')