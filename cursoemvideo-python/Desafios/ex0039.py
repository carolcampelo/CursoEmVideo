from datetime import date
from time import sleep

print('\033[32m=-\033[m' * 15)
print('\033[32mSistema do Alistamento Militar\033[m')
print('\033[32m=-\033[m' * 15)
nome = str(input('Digite aqui o seu nome: ')).strip().title()
sexo = int(input(f'Olá, {nome}. Primeiro selecione seu sexo biológico abaixo:\n'
                 '[1] - Masculino\n'
                 '[2] - Feminino\n'))
if sexo == 1:
    print('Ok, vamos iniciar o processo...')
    sleep(1)
    atual = date.today().year
    ano = int(input('Em que ano você nasceu? '))
    idade = int(atual - ano)
    if idade == 18:
        print('Você tem de se alistar este ano. Procure o exército para maiores informações.')
    elif idade > 18:
        print(f'{nome}, você tinha de se alistar há {idade - 18} ano(s). Procure o exército para informações.')
    else:
        print(f'Fique tranquilo. Você terá de se alistar somente em {18 - idade} ano(s).')
elif sexo == 2:
    print('Mulheres não precisam passar pelo alistamento obrigatório.')
else:
    print('Digite apenas 1 ou 2.')
print('Tenha um bom dia.')
