a = int(input('Digite um número (999 para encerrar): '))
c = 0
s = 0
while a != 999:
    s += a
    c += 1
    a = int(input('Digite um número (999 para encerrar): '))
print(f'\nA soma de todos os {c} números digitados foi {s}.')
