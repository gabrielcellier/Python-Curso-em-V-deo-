#analisar o que for digitado
a = input('Digite algo:')

print('O tipo primitivo do valor é:', type(a))
print('O valor é um número?', a.isnumeric())
print('O valor é uma letra?', a.isalpha())
print('O valor é alfanumérico?', a.isalnum())
print('A palavra está em maiúsculo?', a.isupper())
print('A palavra está em minúsculo?', a.islower())
print('A palavra está capitalizada?', a.istitle())
