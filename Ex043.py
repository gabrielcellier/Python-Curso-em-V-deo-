#ler peso e altura, calcular IMC e classificar o status: <18.5 abaixo do peso, 18.5-25 peso ideal
#25-30 sobrepeso, 30-40 obesidade, 40 obesidade mórbida
altura = float(input('Digite sua altura (em metros): '))
peso = float(input('Digite o seu peso (em kg): '))
imc = peso / (altura ** 2)
if imc < 18.5:
    print ('Devido o IMC {:.2f} a pessoa está "abaixo do peso" (< 18.5).'.format(imc))
elif imc < 25:
    print ('Devido o IMC {:.2f} a pessoa está no "peso ideal" (18.5 a 25).'.format(imc))
elif imc < 30:
    print ('Devido o IMC {:.2f} a pessoa está no "sobrepeso" (25 a 30).'.format(imc))
elif imc < 40:
    print ('Devido o IMC {:.2f} a pessoa está na "obesidade" (30 a 40).'.format(imc))
else:
    print ('Devido o IMC {:.2f} a pessoa está na "obesidade mórbida" (acima de 40).'.format(imc))
#dá pra fazer o elif seguinte considerando só o limite superior do imc pois o inferior foi definido nos if/elifs anteriores.