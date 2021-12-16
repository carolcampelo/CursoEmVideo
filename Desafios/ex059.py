a = 0
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
while a != 5:
    a = int(input("""\nDigite a operação que deseja realizar:
    [1] Somar
    [2] Multiplicar
    [3] Mostrar o maior número
    [4] Trocar números
    [5] Sair do programa
    """))
    if a == 1:
        print(f'\n{n1} + {n2} = {n1 + n2}')
    elif a == 2:
        print(f'\n{n1} x {n2} = {n1 * n2}')
    elif a == 3:
        if n1 > n2:
            print(f'\nO maior número é {n1}.')
        elif n1 == n2:
            print('\nOs dois números são iguais.')
        else:
            print(f'\nO maior número é {n2}.')
    elif a == 4:
        n1 = int(input('\nDigite um número: '))
        n2 = int(input('\nDigite outro número: '))
    elif a != 5:
        print('Código inválido. Tente novamente.')
print('Fim')
