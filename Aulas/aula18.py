teste = list()
teste.append('Gustavo')
teste.append(40)
galera = list()
galera.append(teste[:])
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])
print(teste)
print(galera)

glr = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
print(glr[-1][1])
for p in glr:
    print(f'{p[0]} tem {p[1]} anos de idade.')

povo = list()
dado = list()
for c in range(0, 5):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    povo.append(dado[:])
    dado.clear()
print(povo)

totmaior = 0
totmenor = 0
for p in povo:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade.')
        totmaior += 1
    else:
        print(f'{p[0]} é menor de idade.')
        totmenor += 1
print(f'Temos {totmaior} maiores de idade e {totmenor} menores.')
