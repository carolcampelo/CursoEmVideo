cores = {'limpa':'\033[m',
         'verde':'\033[92m',
         'vermelho':'\033[91m'}
print('Calculadora de descontos')
print()
p1 = float(input('Digite aqui o preço original: {}R${} '.format(cores['verde'], cores['limpa'])))
d = int(input('Digite aqui o {}desconto desejado em %{}: '.format(cores['vermelho'], cores['limpa'])))
p2 = float(p1 - (p1 * d / 100))
print()
print('O valor total com desconto é {}R${:.2f}{}'.format(cores['verde'], p2, cores['limpa']))
