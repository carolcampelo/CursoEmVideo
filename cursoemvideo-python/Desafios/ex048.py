soma = 0
conta = 0
for n in range(1, 501, 2):
    if n % 3 == 0:
        conta += 1
        soma += n
print(f'A soma de todos os {conta} valores solicitados é {soma}.')
