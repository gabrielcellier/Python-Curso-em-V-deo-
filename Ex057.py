#ler sexo da pessoa (m/f), se a pessoa digitar errado peça pra digitar novamente.
from time import sleep
print('Digite o sexo da pessoa por favor a seguir.')
sleep(0.5)
sexo = str(input('Digite o sexo da pessoa (digite "m" ou "f"): ')).strip().lower()[0]
while sexo not in 'mf':
    sexo = str(input('Resposta inválida. Digite o sexo ("m" ou "f"): ')).strip().lower()[0]
    sleep(0.5)
if sexo in 'm':
    print('A resposta dada foi "m" logo o sexo é masculino.')
elif sexo in 'f':
    print('A resposta dada foi "f" logo o sexo é feminino.')
