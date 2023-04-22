h = m20 = t18 = idade = 0
p = r = ''
while True:
    print('-' * 20)
    print('CADASTRE UMA PESSOA')
    print('-' * 20)
    idade = int(input('Idade:'))
    p = str(input('Sexo: [M/F] ')).strip().upper()
    while p != 'M' and p != 'F':
        p = str(input('Sexo: [M/F] ')).strip().upper()
    if idade >= 18:
        t18 += 1
    if p == 'F' and idade < 20:
        m20 += 1
    if p == 'M':
        h += 1
    r = str(input('Deseja continuar? [S/N]')).strip().upper()
    while r != 'S' and r != 'N':
        r = str(input('Deseja continuar? [S/N]')).strip().upper()
    if r == 'N':
        break
print(f"""\nForam cadastradas {t18} pessoas maiores de 18 anos.
Ao todo, {h} homens foram cadastrados.
Houveram {m20} cadastros de mulheres com menos de 20 anos.""")
