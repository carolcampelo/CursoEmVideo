num = [2, 5, 9, 1]
num[2] = 3
num.append(7)
num.sort()
num.sort(reverse=True)
num.insert(2, 2)

if 4 in num:
    num.remove(4)
else:
    print('Não achei o número 4.')

#  num.pop(2) - se sem índice numérico elimina o 1 no final

print(num)
print(f'Esta lista tem {len(num)} elementos.')

valores = list()
for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))

for valor in valores:
    print(f'{valor}', end=' ')
    print('\n')

for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')
print('\nCheguei ao final da lista!\n')

a = [2, 3, 4, 7]
#  b = a - LIGAÇÃO
b = a[:]  # não existe ligação e o número de uma pode ser trocado sem afetar a outra
b[2] = 8
print(f'A lista A: {a}')
print(f'A lista B: {b}')
