#Ler uma frase e contar quantas vezes aparece a letra A, qual a primeira posição e a última de ocorrência da letra.
from time import sleep
print('Digite um frase. Contaremos quantas vezes ocorre a letra "A" na frase.')
sleep(1)
frase = str(input('Digite a frase: ')).strip().lower()
sleep(1)
print(f'A frase digitada foi: "{frase}".'
      f'\nNela, a letra "A" ocorre {frase.count("a")} vezes.'
      f'\nPrimeira ocorrência na {frase.find("a") + 1}° posição.'
      f'\nÚltima ocorrência na {frase.rfind("a")+ 1}° posição.')
#'+ 1' foi usado pois a contagem de caracteres começa do 0 e não do 1.