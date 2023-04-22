sexo = str(input('Digite seu sexo [M/F]: ')).strip().upper()[0]
while sexo not in 'MF':
    sexo = str(input('Dados inválidos. Digite somente M ou F: ')).strip().upper()[0]
if sexo == 'M':
    print('O sexo digitado foi masculino. Obrigado pela informação!')
else:
    print('O sexo digitado foi feminino. Obrigada pela informação!')
