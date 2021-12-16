print('\033[91m*\033[m Calculadora de Progressão Aritmética 2.0 \033[91m*\033[m')
x = int(input('Digite o primeiro termo da Progressão Artimética: '))
r = int(input('Digite a razão da PA: '))
c = 1
print('Os 10 primeiros termos desta progressão são:')
while c != 11:
    print(f'{x}', end=' → ')
    x += r
    c += 1
print('FIM')
