print('\033[35m~ Tabuada Instantânea 2.0 ~\033[m\n')
n = int(input('\033[;1mDigite um número:\033[m '))
print(f'\nA tabuada de \033[35m{n}\033[m é:')
for c in range(0, 11):
    print(f'{n} * {c:2} = {n * c}')
print('Obrigade!')
