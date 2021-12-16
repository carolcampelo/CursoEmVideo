lista = []
pares = []
impares = []
r = 'S'
n = 0
while r in 'S':
    lista.append(int(input('Digite um número: ')))
    r = str(input('Quer continuar? [S/N] ')).strip().upper()
    while r not in 'SN':
        r = str(input('Não entendi. Quer continuar? Digite apenas S ou N: ')).strip().upper()
for c in range(0, len(lista)):
    if lista[c] % 2 == 0:
        pares.append(lista[c])
    else:
        impares.append(lista[c])
print(f'A lista de números digitados foi: {lista}.')
print(f'Os números pares digitados foram: {pares}')
print(f'Já os números ímpares foram: {impares}')
