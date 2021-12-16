numeros = (int(input('Digite um número: ')), int(input('Digite outro número: ')), int(input('Digite mais um número:')),
           int(input('Digite o último número: ')))

if 9 in numeros:
    e = numeros.count(9)
    print(f'O número 9 apareceu {e} vez(es).')
else:
    print('O número 9 apareceu 0 vezes.')

if 3 in numeros:
    f = numeros.index(3)
    print(f'O número 3 apareceu na {f+1}ª posição.')
else:
    print('O número 3 não apareceu.')

print('Os números pares que apareceram foram: ', end='')
for num in numeros:
    if num % 2 == 0:
        print(num, end=' ')
