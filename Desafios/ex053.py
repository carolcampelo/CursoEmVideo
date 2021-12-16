print('\033[31mD E T E C T O R  D E  P A L Í N D R O M O\033[m')
f = str(input('Digite uma frase:')).strip().lower().replace(' ', '')
n = len(f)
cont = 0
for c in range(0, n-1):
    if f[c] == f[(n-1) - c]:
        cont += 1
if cont == n-1:
    print('Sua frase é um palíndromo!')
else:
    print('Sua frase não é um palíndromo!')
