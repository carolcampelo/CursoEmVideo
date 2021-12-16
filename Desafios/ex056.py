print('\033[;4;94mAnalisador Completo\033[m')
media = 0
homens = 0
nomehomens = ''
mulheres = 0
for c in range(1, 5):
    print(f'\033[94m---- {c}ª PESSOA ----\033[m')
    nome = str(input(f'Nome:')).title().strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ').strip().upper())
    if sexo == 'F' and idade < 20:
        mulheres += 1
    if c == 1 and sexo == 'M':
        homens = idade
        nomehomens = nome
    if sexo == 'M' and idade > homens:
        homens = idade
        nomehomens = nome
    media += idade
print(f'\nA média de idade deste grupo é de {media / 4:.1f} anos.')
print(f'O homem mais velho tem {homens} anos e se chama {nomehomens}.')
if mulheres == 1:
    print(f'Existe apenas {mulheres} mulher menor de idade no grupo.')
elif mulheres == 0:
    print(f'Não existem mulheres no grupo.')
else:
    print(f'Existem {mulheres} mulheres menor de idade no grupo.')
