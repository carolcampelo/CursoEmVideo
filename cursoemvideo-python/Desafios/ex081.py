lista = []
r = 'S'
while r in 'S':
    lista.append(int(input('Digite um número: ')))
    r = str(input('Quer continuar? [S/N] ')).strip().upper()
    while r not in 'SN':
        r = str(input('Não entendi. Quer continuar? Digite apenas S ou N: ')).strip().upper()
lista.sort(reverse=True)
print('=-' * 15)
print(f'Você digitou {len(lista)} números.')
print(f'Os números em ordem decrescente são: {lista}')
if 5 in lista:
    print('O número 5 foi digitado na lista!')
else:
    print('O número 5 não foi listado.')
