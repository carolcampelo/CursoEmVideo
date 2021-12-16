pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.')

print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())

pessoas['peso'] = 98

for k, v in pessoas.items():
    print(f'{k} = {v}')

brasil = []
estado1 = {'UF': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'UF': 'São Paulo', 'sigla': 'RJ'}
brasil.append(estado1)
brasil.append(estado2)
