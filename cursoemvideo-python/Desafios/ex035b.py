print('Calculadora de triângulos')
a = float(input('Digite aqui o tamanho da primeira reta: '))
b = float(input('Digite aqui o tamanho da segunda reta: '))
c = float(input('Digite o tamanho da terceira reta: '))
if a < b + c and b < c + a and c < a + b:
    print('Suas retas \033[92mPODEM\033[m formar um triângulo!')
else:
    print('Suas retas \033[91mNÃO PODEM\033[m formar um triângulo.')