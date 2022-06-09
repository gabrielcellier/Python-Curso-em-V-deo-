#analisar o que for digitado
print('Digite uma palavra, valor ou mistura dos dois e analisaremos.')
valor = input('Digite algo: ')

print(f'{valor} é uma letra? {valor.isalpha()}.')
print(f'{valor} é um número? {valor.isnumeric()}.')
print(f'{valor} é alfanumérico? {valor.isalnum()}')

