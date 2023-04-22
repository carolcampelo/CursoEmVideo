print('Calculadora de triângulos')
a = float(input('Digite aqui o tamanho da primeira reta: '))
b = float(input('Digite aqui o tamanho da segunda reta: '))
c = float(input('Digite o tamanho da terceira reta: '))
tri = [a, b, c]
tri.sort()
if tri[0] + tri[1] > tri[2]:
    print('Suas retas \033[92mpodem\033[m formar um triângulo.')
else:
    print('Suas retas \033[91mnão formam\033[m um triângulo.')
