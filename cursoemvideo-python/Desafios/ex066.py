n = s = c = 0
while True:
    n = int(input('Digite um número (999 para encerrar): '))
    if n == 999:
        break
    s += n
    c += 1
if c == 1:
    print(f'O único número digitado foi {n}.')
else:
    print(f'A soma dos {c} números digitados foi {s}.')
