#ler um número e mostrar o número que vem antes e o que vem depois
while True:
      num = input('Digite um número inteiro: ').strip()
      if num.isnumeric():
            num = int(num)
            break
      else:
            print('Você não digitou um número inteiro. Por favor digite um número inteiro.')

print(f"O valor digitado foi {num}. Seu sucessor é {(num+1)}. Seu antecessor é {(num-1)}.")


