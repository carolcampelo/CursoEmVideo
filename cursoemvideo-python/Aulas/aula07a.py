n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
r = n1 % n2
e = n1 ** n2
print(f'A soma é {s}, o produto é {m} e a divisão é {d:.2f}', end='. ')
print(f'Divisão inteira é {di}, com resto {r} e a potência resulta em {e}')
