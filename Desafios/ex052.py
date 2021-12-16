print('Calculadora de números primos')
n = int(input('Digite um número:'))
teste = 0
for c in range(1, n + 1):
    if n % c == 0:
        print('\033[33m', end='')
        teste += 1
    else:
        print('\033[31m', end='')
    print(c, end=' ')
print(f'\n\033[mO número {n} foi divisível {teste} vezes.')
if teste == 2:
    print('Desta forma, seu número é primo.')
elif teste > 2:
    print('Assim, seu número não é primo.')
