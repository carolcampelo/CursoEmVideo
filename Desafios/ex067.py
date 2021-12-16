print('~' * 25)
print('Tabuada Automatizada 3.0')
print('~' * 25)
while True:
    n = int(input('Diga um número: '))
    if n < 0:
        break
    for c in range(1, 11):
        print(f'{n} x {c:2} = {n * c}')
print('Programa encerrado. Obrigada pela preferência.')
