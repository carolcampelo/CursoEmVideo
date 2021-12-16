# Condições Aninhadas -> if, elif, else.
nome = str(input('Qual é seu nome? ')).title()
if nome == 'Carolina':
    print('Que nome lindo!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome é bem Popular no Brasil.')
elif nome in 'Ana Juliana Vanessa Jéssica':
    print('É um belo nome feminino.')
else:
    print('Que nome normal.')
print(f'Tenha um bom dia, {nome}!')