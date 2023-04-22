print('Calculadora de aumentos')
s = float(input('Digite aqui o seu salário: R$'))
if s >= 1250.00:
    a1 = s * 10 / 100
    print(f'Você recebeu um aumento de 10%. Seu novo salário é R${(s + a1):.2f}')
else:
    a2 = s * 15 / 100
    print(f'O aumento que você recebeu foi de 15%. Seu novo salário é R${(s + a2):.2f}')
print('Aproveite!')
