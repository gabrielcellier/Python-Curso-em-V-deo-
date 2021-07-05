#ler peso e altura, calcular IMC e classificar o status: <18.5 abaixo do peso, 18.5-25 peso ideal
#25-30 sobrepeso, 30-40 obesidade, 40 obesidade mórbida
altura = float(input('Indique a altura do indivíduo (em metros): '))
peso = float(input('Indique o peso do indivíduo (em quilos): '))
imc = altura / (peso ** 2)
if imc < 18.5:
    input ('Com altura {} e peso {} kg o IMC do indivíduo é {:.2f}, considerado "magro".'.format(altura, peso, imc))
elif >= 18.5 and <= 24.9:
    input ('Com altura {} e peso {} kg o IMC do indivíduo é {:.2f}, considerado "normal".'.format(altura, peso, imc))
elif >= 25 and <= 29.9:
    input ('Com altura {} e peso {} kg o IMC do indivíduo é {:.2f}, considerado "sobrepeso".'.format(altura, peso, imc))
elif >= 30 and <= 39.9:
    input ('Com altura {} e peso {} kg o IMC do indivíduo é {:.2f}, considerado "obesidade".'.format(altura, peso, imc))
elif >= 40:
    input ('Com altura {} e peso {} kg o IMC do indivíduo é {:.2f}, considerado "obesidade grave".'.format(altura, peso, imc))