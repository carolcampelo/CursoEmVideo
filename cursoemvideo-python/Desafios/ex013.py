print('Calculadora de reajustes')
print()
v1 = float(input('Digite aqui o \033[;4mseu salário\033[m em R$: '))
a1 = int(input('Digite aqui o valor do aumento em %: '))
a2 = v1 * a1 / 100
v2 = v1 + a2
print()
print(f'O novo salário será de \033[92mR${v2:.2f}\033[m')
