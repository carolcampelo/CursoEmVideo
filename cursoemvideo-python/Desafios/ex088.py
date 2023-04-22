from random import randint as r
from time import sleep as s
print('-' * 35)
print(f'{"JOGA NA MEGA!":^35}')
print('-' * 35)
num = 0
jogo = []
lista = []
n = int(input('Quantos jogos deseja fazer? '))
s(1)
print(f'\n{f" SORTEANDO {n} JOGOS ":-^35}\n')
for j in range(0, n):
    s(1)
    for c in range(0, 6):
        num = r(1, 60)
        while num in jogo:
            num = r(1, 60)
        jogo.append(num)
    jogo.sort()
    lista.append(jogo[:])
    jogo.clear()
    print(f'Jogo {j+1}: {lista[j]}')
s(1)
print(f'\n{f" BOA SORTE! ":-^35}')
