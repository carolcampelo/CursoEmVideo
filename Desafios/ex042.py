print('\033[93mΔ Calculadora de triângulos Δ\033[m')
a = float(input('Digite aqui o tamanho da primeira reta: '))
b = float(input('Digite aqui o tamanho da segunda reta: '))
c = float(input('Digite o tamanho da terceira reta: '))
if a < b + c and b < c + a and c < a + b:
    print('Suas retas \033[92mPODEM\033[m formar um triângulo!')
    if a == b == c:
        print('Seu triângulo será \033[93mequilátero\033[m.')
    elif a != b != c != a:
        print('Seu triângulo será \033[93mescaleno\033[m.')
    else:
        print('Seu triângulo será \033[93misóceles\033[m.')
else:
    print('Suas retas \033[91mNÃO PODEM\033[m formar um triângulo.')
