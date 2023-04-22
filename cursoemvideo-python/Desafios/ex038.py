print('~ Analisando números ~')
print()
n1 = int(input('Digite aqui um número inteiro: '))
n2 = int(input('Digite aqui outro número inteiro: '))
if n1 > n2:
    print(f'O primeiro valor digitado é maior que o segundo. {n1} > {n2}')
elif n2 > n1:
    print(f'O segundo valor digitado é maior. {n2} > {n1}')
else:
    print('Não existem valores maiores. Os dois números digitados são iguais.')
