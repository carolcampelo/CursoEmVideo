print('\033[92mCondições de pagamento\033[m')
v1 = float(input('Digite aqui o valor do produto: R$'))
print(f'O produto custa R${v1:.2f}. \nSeu preço à vista é R${v1 - (v1*10/100):.2f} e à prazo é R${v1 + (v1*8/100):.2f}')
