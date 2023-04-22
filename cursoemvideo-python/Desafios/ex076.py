itens = ['Adaptador Bluetooth 4.0', 40.30, 'Fonte', 200, 'Notebook', 2500, 'Celular', 1300, 'Capa para Notebook 15"',
         50, 'JBL Go 2', 149, 'Controle Dualshock 4', 250, 'Smartwatch Amazfit GTS2 Mini', 500, 'Mousepad', 20,
         'Headset', 199]
print('-' * 57)
print(f'{"LISTAGEM DE PREÇOS":^57}')
print('-' * 57)

for num, item in enumerate(itens):
    if num % 2 == 0:
        print(f'{item:.<45} R$', end='')
    else:
        print(f'{item:>9.2f}')

print('-' * 57)
