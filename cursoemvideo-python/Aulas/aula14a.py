"""r = 'S'
n = 0
while r == 'S':
    n = int(input('Digite um valor: '))
    r = str(input('Quer continuar? [S/N]')).strip().upper()
print('Fim')"""
n = 1
par = impar = 0
while n != 0:
    n = int(input('Digite um valor (ou 0 para sair): '))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print(f'Você digitou {par} números pares e {impar} números ímpares.')
