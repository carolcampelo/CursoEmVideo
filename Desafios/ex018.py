import math
print('\033[95m~ Facilitador de trigonometria ~\033[m')
a = float(input('Digite aqui o ângulo em graus: '))
b = math.radians(a)
s = math.sin(b)
c = math.cos(b)
t = math.tan(b)
print(f'O ângulo escolhido foi {a}, que equivale a {b:.2f}rad.')
print(f'Então o seno equivale a {s:.2f}, o cosseno é {c:.2f} e a tangente é {t:.2f}')
