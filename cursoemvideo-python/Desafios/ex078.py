n = list()

for c in range(0, 5):
    n.append(int(input(f'Digite um valor para a Posição {c}: ')))

print(f'Os números digitados foram {n}')

a = (min(n))
print(f'O menor número foi {a} e sua posição é {n.index(a)}.')

b = (max(n))
print(f'O maior número foi {b} e sua posição é {n.index(b)}.')
