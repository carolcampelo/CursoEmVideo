print('\033[91m*\033[m Calculadora de Progressão Aritmética 2.0 \033[91m*\033[m')
x = int(input('Digite o primeiro termo da Progressão Artimética: '))
r = int(input('Digite a razão da PA: '))
c = 1
t = 0
d = 10
print('Os 10 primeiros termos desta progressão são:')
while d != 0:
    t = t + d
    while c <= t:
        print(f'{x}', end=' → ')
        x += r
        c += 1
    d = int(input('PAUSA\nDeseja mostrar mais quantos termos? Digite 0 para sair: '))
print(f'FIM. Progressão finalizada com {t} termos mostrados.')
