print('\033[31mD E T E C T O R  D E  P A L Í N D R O M O  2.0\033[m')
f = str(input('Digite uma frase:')).strip().upper()
palavras = f.split()
junto = ''.join(palavras)
# inverso = ''
inverso = junto[::-1]
# for letra in range(len(junto) -1, -1, -1):
#   inverso += junto[letra]
print(f'O inverso de {junto} é {inverso}.')
if junto == inverso:
    print('Sua frase é um palíndromo!')
else:
    print('Sua frase não é um palíndromo!')
