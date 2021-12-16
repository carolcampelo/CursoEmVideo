r = ''
c = 0
li = list()
while r != 'N':
    n = int(input('Digite um número: '))
    c += 1
    if c == 1:
        li.append(n)
    else:
        if n in li:
            print('Número já existente. Não irei adicionar.')
        else:
            li.append(n)
            print('Número adicionado com sucesso.')
    r = str(input('Deseja continuar? [S/N] ')).strip().upper()
    if r != 'N' and r != 'S':
        r = str(input('Não entendi. Deseja continuar? [S/N] ')).strip().upper()
print(f'Todos os valores únicos adicionados foram: {sorted(li)}')
