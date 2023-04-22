numeros = [[], []]

for c in range(1, 8):
    num = int(input(f'Digite o {c}º número: '))
    if num % 2 == 0:
        numeros[0].append(num)
    else:
        numeros[1].append(num)
numeros[0].sort()
numeros[1].sort()
print(f'Os números pares digitados foram {numeros[0]} e os ímpares foram {numeros[1]}')
