#ler duas notas, calcular a média e se for aciam de 7 tá aprovado,
# entre 5-6.9 recuperação e abaixo de 5 reprovado
from time import sleep
print('Escreva as duas notas (de 0 a 10), vamos calcular a situação do aluno.'
      '\nAcima de 7 está aprovado. 5 a 6.9 em recuperação e abaixo de 5 reprovado.')
sleep(1)
while True:
    n1 = float(input('Digite a primeira nota: '))
    if 0 <= n1 <= 10:
        print(f'Primeira nota digitada foi: {n1:.2f}.')
        break
    else:
        print(f'Nota digitada {n1:.2f} inválida. Digite uma nota entre 0 a 10.')
while True:
    n2 = float(input('Digite a segunda nota: '))
    if 0 <= n2 <= 10:
        print(f'Segunda nota digitada foi: {n2:.2f}.')
        break
    else:
        print(f'Nota digitada {n2:.2f} inválida. Digite uma nota entre 0 a 10.')
media = (n1+n2)/2
if media >= 7:
    print(f'A soma das notas {n1:.1f} + {n2:.1f} deu média {media:.1f}. O aluno foi aprovado.')
elif 5 <= media <= 6.99:
    print(f'A soma das notas {n1:.1f} + {n2:.1f} deu média {media:.1f}. O aluno está de recuperação.')
elif media < 5:
    print(f'A soma das notas {n1:.1f} + {n2:.1f} deu média {media:.1f}. O aluno está reprovado.')


