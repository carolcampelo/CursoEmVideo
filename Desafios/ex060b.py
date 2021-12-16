print('\033[91m*\033[m Calculadora de Fatorial \033[91m*\033[m')
x = int(input('\nDigite um número: '))
print(f'Calculando {x}! =', end=' ')
f = 1
for c in range(x, 0, -1):
    print(f'{c}', end=' ')
    print(' x ' if c > 1 else ' = ', end=' ')
    f *= c
    c -= 1
print(f'{f}')
