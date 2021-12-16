from random import randint
from time import sleep
print('\033[33m-=-\033[m' * 10)
print('~ Joguinho de Adivinhação ~')
print('\033[33m-=-\033[m' * 10)
n = randint(0, 5)
a = int(input('Digite aqui um número de 0 a 5: '))
sleep(1)
print('\033[31mPROCESSANDO...\033[m')
sleep(2)
if n == a:
    print(f'Parabéns, você acertou! O número era {n}!')
else:
    print(f'Que pena, você errou... O número era {n}. Tente outra vez!')
