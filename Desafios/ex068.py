from random import randint
from time import sleep
print('=-' * 11)
print(' JOGO DE PAR OU ÍMPAR ')
print('=-' * 11)
sleep(0.5)
print(3)
sleep(0.5)
print(2)
sleep(0.5)
print(1)
print("""\nJá pensei no meu número.
Pense no seu e logo começamos (Somente 1 ou 2).""")
v = 0
p = 0
s = 0
o = ''
while True:
    o = str(input('\nPar ou Ímpar? [P/I] ')).strip().upper()[0]
    while o not in 'PI':
        print('Valor inválido. Tente de novo (não use acentos): ')
    cpu = randint(1, 2)
    p = int(input('\nVai: '))
    print(f'Eu escolhi {cpu} e você escolheu {p}.')
    s = cpu + p
    if o == 'P':
        if s % 2 == 0:
            print('Você ganhou!')
            v += 1
        else:
            break
    elif o == 'I':
        if s % 2 == 1:
            print('Você ganhou!')
            v += 1
        else:
            break
if v == 1:
    print(f'Você perdeu. Você venceu {v} vez.')
if v > 1:
    print(f'Você perdeu. Você venceu {v} vezes consecutivas.')
