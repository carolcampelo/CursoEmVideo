pessoas = list()
dados = list()
r = 's'

while r in 'Ss':
    dados.append(str(input('Nome: ').strip().title()))
    dados.append(float(input('Peso em kg: ').strip()))
    pessoas.append(dados[:])
    dados.clear()
    r = str(input('Deseja cadastrar mais pessoas? [S/N]')).strip()
    if r in 'Nn':
        break
    elif r not in 'SsNn':
        r = str(input('Não entendi. Digite apenas S ou N: ')).strip()

somatotal = 0
for m in pessoas:
    somatotal += m[1]
mediapeso = somatotal / len(pessoas)

print(f'\nForam cadastradas {len(pessoas)} pessoas e o peso médio foi {mediapeso:.1f}kg.')
print(f'\nAs pessoas mais pesadas foram: ')
for p in pessoas:
    if p[1] > mediapeso:
        print(p[0])

print(f'\nAs pessoas mais leves são: ')
for p in pessoas:
    if p[1] <= mediapeso:
        print(p[0])
