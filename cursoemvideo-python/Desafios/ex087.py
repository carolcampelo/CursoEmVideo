matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
s = terc = max2 = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
        if matriz[l][c] % 2 == 0:
            s += matriz[l][c]
        if c == 2:
            terc += matriz[l][c]
        if l == 1:
            if c == 0:
                max2 = matriz[l][c]
            else:
                if max2 < matriz[l][c]:
                    max2 = matriz[l][c]
print('=-' * 20)
print('A matriz gerada foi: ')
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
print('=-' * 20)
print(f'\nA soma de todos os números pares é {s}.')
print(f'A terceira coluna soma {terc}.')
print(f'O maior número da segunda linha é {max2}.')
