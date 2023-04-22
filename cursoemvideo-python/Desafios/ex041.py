from datetime import date
from time import sleep
print('\033[94m~\033[m' * 44)
print('Sistema da Confederação Nacional de Natação')
print('\033[94m~\033[m' * 44)
n = str(input('Olá, qual o seu nome? ')).strip().capitalize()
print(f'Prazer, {n}. Vamos iniciar...')
sleep(1)
nasc = int(input('Qual seu ano de nascimento?'))
ano = date.today().year
idade = int(ano - nasc)
if idade == 1:
    print(f'Você tem {idade} ano. Você foi classificado na categoria \033[94mMIRIM\033[m.')
elif 1 < idade <= 9:
    print(f'Você tem {idade} anos. Sua classificação é \033[94mMIRIM\033[m.')
elif idade <= 14:
    print(f'Você tem {idade} anos. Sua classificação é \033[94mINFANTIL\033[m.')
elif idade <= 19:
    print(f'Você tem {idade} anos. Sua classificação é \033[94mJÚNIOR\033[m.')
elif idade <= 25:
    print(f'Você tem {idade} anos. Sua classificação é \033[94mSÊNIOR\033[m.')
elif idade <= 0:
    print('Desculpe, sua idade não é válida. Tente novamente.')
else:
    print(f'Você tem {idade} anos. Você foi classificado na categoria \033[94mMASTER\033[m.')
print('Obrigado pelo interesse.\n'
      'Esperamos te ver nas raias em breve!')
print('\033[94m~~\033[m' * 18)
