print('-' * 18)
print('Sistema de Compras')
print('-' * 18)
k = c = t = vb = 0
b = r = ''
while True:
    i = str(input('Nome do produto:')).strip().capitalize()
    v = int(input('Valor: R$'))
    print('-' * 18)
    c += 1
    t += v
    if v > 1000:
        k += 1
    if c == 1 or v < vb:
        b = i
        vb = v
    while r != 'S' and r != 'N':
        r = str(input('Quer continuar? [S/N]')).strip().upper()
        print('-' * 18)
    if r == 'N':
        break
    r = ''
print(f"""Sua compra tem valor total de R${t:.2f};
Você comprou {k} produtos acima de R$1.000,00;
O item com valor mais baixo foi o {b}.
Obrigado pela preferência. Volte Sempre!""")
