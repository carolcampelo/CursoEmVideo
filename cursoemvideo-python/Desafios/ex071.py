print('=' * 20)
print('{:^20}'.format('Banco da Carol'))
print('=' * 20)
c = d = v = u = 0
while True:
    n = int(input('Qual o valor a ser sacado? R$'))
    if n < 0:
        n = int(input('O valor é inválido. Digite um valor inteiro para continuar ou 0 para sair:'))
    if n == 0:
        break
    if n > 0:
        c = n // 50
        r = n % 50
        v = r // 20
        r = r % 20
        d = r // 10
        r = r % 10
        u = r
    break
if n == 0:
    print('Obrigado. Volte sempre!')
if n > 0:
    print(f'\nO valor solicitado foi R${n:.2f}.\n')
    if c == 1:
        print(f'Total de {c} nota de R$50,00.')
    elif c > 1:
        print(f'Total de {c} notas de R$50,00.')
    if v == 1:
        print(f'Total de {v} nota de R$20,00.')
    elif v > 1:
        print(f'Total de {v} notas de R$20,00.')
    if d == 1:
        print(f'Total de {d} nota de R$10,00.')
    elif d > 1:
        print(f'Total de {d} notas de R$20,00.')
    if u == 1:
        print(f'Total de {u} nota de R$1,00.')
    elif u > 1:
        print(f'Total de {u} notas de R$1,00.')
    print('\nObrigado. Volte sempre!')
