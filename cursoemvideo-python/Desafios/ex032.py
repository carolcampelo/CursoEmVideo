from datetime import date
print('=-' * 11)
print('\033[;1;30;43mEste ano é bissexto?!\033[m')
print('=-' * 11)
ano = int(input('Que ano quer analisar? Digite 0 para usar o ano atual: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O ano de {ano} é bissexto.')
else:
    print(f'O ano de {ano} não é bissexto.')
