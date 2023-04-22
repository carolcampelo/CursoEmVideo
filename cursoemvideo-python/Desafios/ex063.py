print('-' * 23)
print('\033[91m~\033[m Sequência Fibonacci \033[91m~\033[m')
print('-' * 23)
n = int(input('Digite quantos termos deseja obter: '))
print(f'Os {n} primeiros termos da Sequência de Fibonacci são:')
t1 = 0
t2 = 1
print(f'{t1} → {t2}', end=' → ')
c = 3
while c <= n:
    t3 = t1 + t2
    print(f'{t3}', end=' → ')
    t1 = t2
    t2 = t3
    c += 1
print('FIM')
