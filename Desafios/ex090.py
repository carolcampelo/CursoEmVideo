aluno = dict()

aluno['Nome'] = str(input('Nome: ')).title()
aluno['Média'] = float(input(f'Média de {aluno["Nome"]}: '))

if 7 <= aluno['Média'] <= 10:
    aluno['Situação'] = 'Aprovado'
elif 7 > aluno['Média'] >= 5:
    aluno['Situação'] = 'Reprovado'
elif 5 > aluno['Média'] >= 0:
    aluno['Situação'] = 'Reprovado'
else:
    while 10 < aluno['Média'] < 0:
        print('Algo errado aconteceu. Tente novamente.')
        aluno['Média'] = float(input(f'Média de {aluno["Nome"]}: '))

for k, v in aluno.items():
    print(f'{k} é igual a {v}.')
