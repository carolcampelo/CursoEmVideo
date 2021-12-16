print('- Calculadora de Passagens -')
d = float(input('Digite a distância da viagem (em km): '))
if d <= 200:
    print(f'Sua passagem custará R${(d * 0.5):.2f}')
else:
    print(f'Sua passagem custará R${(d * 0.45):.2f}')
print('Boa Viagem!')