f1 = input('Digite aqui uma frase legal: ').strip().lower()
a = f1.count('a')
p = f1.find('a')+1
u = f1.rfind('a')+1
print(f'A letra "A" aparece {a} vezes.')
print(f'Aparece pela primeira vez na posição {p}.')
print(f'Aparece pela última vez na posição {u}.')
