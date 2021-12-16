n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1+n2)/2
print(f'A sua média foi: {m}')
if m >= 7.0:
    print('Parabéns! Você foi aprovado!')
else:
    print('Você não foi aprovado. Tente novamente :/')
