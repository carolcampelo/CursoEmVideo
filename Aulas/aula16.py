# Tuplas são imutáveis
lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')

print(sorted(lanche))

for comida in lanche:
    print(f'Eu vou comer {comida}')

for c in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[c]}, na posição {c}.')

for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida}, na posição {pos}.')

print('Comi pra caramba!')

print('=' * 50)

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = b + a
print(c)
print(len(c))
print(c.count(5))
print(c.index(8))

print('=' * 50)
pessoa = ('Gustavo', 39, 'M', 99.88)
del pessoa
