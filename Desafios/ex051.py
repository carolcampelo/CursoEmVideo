print('\033[91m*\033[m Calculadora de Progressão Aritmética \033[91m*\033[m')
x = int(input('Digite o primeiro termo da Progressão Artimética: '))
r = int(input('Digite a razão da PA: '))
d = x + (10 - 1) * r
print('Os 10 primeiros termos desta progressão são:')
for c in range(x, d + r, r):
    print(c, end=' → ')
print('FIM')
