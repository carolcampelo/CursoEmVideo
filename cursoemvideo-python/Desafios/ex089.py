ficha = []
resp = 'S'

while resp in 'Ss':
    nome = str(input('Nome: ')).strip().title()
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
    m = (n1 + n2) / 2
    ficha.append([nome, [n1, n2], m])
    resp = input('Deseja continuar? [S/N]')
    if resp not in 'SsNn':
        resp = input('Não entendi. Digite apenas S ou N.')

print('=-' * 15)
print('No. ' + f'{"NOME":<15}' + 'MÉDIA')
print('-' * 30)
for c in range(0, len(ficha)):
    print(c, f'  {ficha[c][0]:<15}', ficha[c][2])
print('-' * 30)

while True:
    n = int(input('Mostrar notas de qual aluno? (999 interrompe):'))
    if n == 999:
        break
    elif n <= len(ficha) - 1:
        print(f'\nAs notas de {ficha[n][0]} são: {ficha[n][1]}\n')
    elif n > len(ficha) - 1:
        n = int(input('Ops, número de aluno não encontrado. Tente novamente:'))

print('\nAplicativo encerrado. Volte sempre!')
