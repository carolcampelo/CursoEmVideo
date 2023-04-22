print('Bora brincar de conversão!')
n = int(input('Digite um número inteiro: '))
c = int(input('Selecione a opção desejada para conversão:\n'
              '[1] - Binário\n'
              '[2] - Octal\n'
              '[3] - Hexadecimal\n'))
if c == 1:
    print(f'O número {n} binário é {n:b}')
elif c == 2:
    print(f'O número {n} octal equivale a {n:o}')
elif c == 3:
    print(f'O número {n} hexadecimal é {n:x}')
else:
    print('Opção inválida. Tente novamente.')
