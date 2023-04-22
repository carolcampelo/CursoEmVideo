cont = 0
soma = 0
for n in range(1, 7):
    c = int(input('Digite um número: '))
    if c % 2 == 0:
        soma += c
        cont += 1
if cont == 1:
    print(f'O único número par digitado foi {soma}.')
elif cont == 0:
    print(f'Você não digitou números pares. A soma é {soma}.')
else:
    print(f'A soma dos {cont} números pares digitados é {soma}.')
