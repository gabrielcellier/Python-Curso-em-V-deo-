#Função notas() recebendo vários números. No fim mostrar: qt de notas, maior nota, menor nota, média da turma
# e situaçao (opcional). Fazer docstring da função.
#obs: Situação é em relação a média da sala. Se for abaixo da média é ruim.
def notas(* num, sit=False):
    dic = {}
    dic['Total das notas'] = len(num)
    dic['Maior nota'] = max(num)
    dic['Menor nota'] = min(num)
    dic['Média'] = (sum(num)/len(num))
    if sit:
        if dic['Média'] > 7:
            print(f'A situação do aluno é boa, com média {dic["Média"]}.')
        elif dic['Média'] < 5:
            print(f'A situação do aluno é ruim, com média de {dic["Média"]}.')
        else:
            print(f'A situação do aluno é regular, com média de {dic["Média"]}.')
    return dic

print(notas(8, 9, 10, sit=True))
print('----------')
print(notas(3, 3, 8, 9, 7, 6, 8.5, sit=True))


