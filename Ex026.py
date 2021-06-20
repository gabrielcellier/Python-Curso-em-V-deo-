#Ler uma frase e contar quantas vezes aparece a letra A, qual a primeira posição e a última de ocorrência da letra.
frase = str(input('Digite uma frase a escolha: ')).strip().lower()
print ('A letra "a" ocorre {} vezes na frase digitada.'
       '\nPrimeira ocorrência da letra A na posiçao {} e a última na posição {}.'
       .format(frase.count('a'), frase.find('a') + 1, frase.rfind('a') + 1))
#+1 no .find é por conta que a contagem de caract. começa no 0 e não no 1.
#.rfind() serve para que a busca comece da direita, ou seja, final da frase.