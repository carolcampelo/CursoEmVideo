cidade = input('Digite aqui o nome de uma cidade: ').lower().strip().split()
perg = 'santo' in cidade[0]
print(f'O nome da cidade começa com "Santo"? {perg}')
