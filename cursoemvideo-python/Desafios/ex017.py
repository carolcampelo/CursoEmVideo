import math
a = float(input('Insira o valor do cateto adjacente: '))
o = float(input('Insira o valor do cateto oposto: '))
h = math.hypot(a, o)
print(f'O valor da hipotenusa é \033[95m{h:.2f}\033[m.')
