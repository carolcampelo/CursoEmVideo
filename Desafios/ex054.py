from datetime import date
print('Analisador de idades')
a = date.today().year
menor = 0
maior = 0
n = 0
for c in range(1, 8):
    n = int(input(f'Digite o ano de nascimento da {c}ª pessoa: '))
    if a - n >= 18:
        maior += 1
    else:
        menor += 1
print(f'Entre vocês existem {menor} pessoas menores de idade e {maior} maiores de idade.')
