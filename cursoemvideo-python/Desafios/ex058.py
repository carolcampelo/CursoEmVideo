from random import randint
from time import sleep
print('\033[33m-=-\033[m' * 10)
print('~ Joguinho de Adivinhação ~')
print('\033[33m-=-\033[m' * 10)
print('\nSou seu computador e pensei em um número.'
      '\nSerá que você consegue acertar?')
n = randint(0, 10)
a = False
t = 0
sleep(1)
print('\033[31m\nPROCESSANDO...\n\033[m')
sleep(2)
while not a:
    p = int(input('Digite seu palpite de 0 a 10: '))
    t += 1
    if p == n:
        a = True
    else:
        if p > n:
            print('Menos.. Tente novamente.')
        elif p < n:
            print('Mais.. Tente novamente.')
if t == 1:
    print(f'\nParabéns! Você acertou na primeira tentativa! O número era {n}.')
else:
    print(f"""\nParabéns! Você acertou! 
    O número era {n} e foram {t} tentativas até o acerto.""")
