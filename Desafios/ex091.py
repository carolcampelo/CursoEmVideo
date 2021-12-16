from random import randint as ri
from time import sleep as s
from operator import itemgetter as ig

jogo = {'jogador1': ri(1, 6),
        'jogador2': ri(1, 6),
        'jogador3': ri(1, 6),
        'jogador4': ri(1, 6)}

print('== JOGO DE DADOS ==')
print('Valores sorteados:')
for k, v in jogo.items():
    print(f'{k} jogou {v}.')
    s(1)

ranking = sorted(jogo.items(), key=ig(1), reverse=True)

print('=-' * 13)
print('== RANKING DOS JOGADORES ==')
for i, v in enumerate(ranking):
    print(f'{i+1}º lugar: {v[0]} com {v[1]}.')
    s(1)

print('\nObrigada por jogar! Até a próxima.')
