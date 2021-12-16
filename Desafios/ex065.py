a = ''
b = c = s = maior = menor = 0
while a != 'N':
    b = int(input('Digite um número: '))
    s += b
    c += 1
    if c == 1:
        menor = maior = b
    else:
        if b > maior:
            maior = b
        if b < menor:
            menor = b
    a = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if a not in 'SN':
        a = str(input('Não entendi. Digite apenas S ou N:'))
print(f"""\nA soma de todos os {c} números digitados foi {s}.
A média entre eles vale {s / c}.
O maior número é {maior} e o menor é {menor}.
Obrigada!""")
