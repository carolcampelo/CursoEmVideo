from random import shuffle
print('\033[97m~\033[m' * 25)
print('Sorteador de apresentação!')
print('\033[97m~\033[m' * 25)
a = input('Digite o nome de um alune: ')
b = input('Escreva o nome de outre: ')
c = input('Mais um: ')
d = input('Só mais uma vez: ')
alunos = [a, b, c, d]
shuffle(alunos)
print()
print(f'A ordem escolhida foi: \n\033[97m{alunos}\033[m \nBoa sorte!')
