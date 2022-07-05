#ler peso e altura, calcular IMC e classificar o status: <18.5 abaixo do peso, 18.5-25 peso ideal
#25-30 sobrepeso, 30-40 obesidade, 40 obesidade mórbida
from time import sleep
print('Digite sua altura e seu peso (em kg), vamos calcular o seu IMC.')
sleep(1)
while True:
    altura = float(input('Digite sua altura em metros: '))
    peso = float(input('Digite seu peso (em kg): '))
    if 0.2 <= altura <= 2.30 and 10 <= peso <= 250:
        print(f'Usuário digitou valor de {altura:.2f} metros de altura e {peso:.2f} quilos.')
        break
    else:
        print('Valores digitados de altura e/ou peso inválidos. Digite novamente.')
        sleep(1)
imc = peso / (altura ** 2)
sleep(1)
print('Cálculo de IMC:')
sleep(0.5)
if imc < 18.5:
    print(f'Com IMC de {imc:.1f} a pessoa é considerada "abaixo do peso" (até IMC 18.5)')
elif 18.5 <= imc <= 24.9:
    print(f'Com IMC de {imc:.1f} a pessoa é considerada no "peso ideal" (até IMC 25).')
elif 25 <= imc <= 29.9:
    print(f'Com IMC de {imc:.1f} a pessoa é considerada "sobrepeso" (até IMC 30).')
elif 30 <= imc <= 39.9:
    print(f'Com IMC de {imc:.1f} a pessoa é considerada "obesa" (até IMC 40).')
elif imc >= 40:
    print(f'Com IMC de {imc:.1f} a pessoa é considerada em "obesidade mórbida" (IMC acima de 40).')