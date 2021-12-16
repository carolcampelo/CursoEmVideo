times = ('Athletico-PR', 'Fortaleza', 'Bragantino', 'Palmeiras', 'Atlético-MG', 'Fluminense', 'Bahia', 'Atlético-GO',
         'Santos', 'Flamengo', 'Corinthians', 'Ceará SC', 'Internacional', 'Juventude', 'Sport Recife', 'Cuiabá',
         'Chapecoense', 'São Paulo', 'América-MG', 'Grêmio')
print('=-' * 15)
print(f'Lista de times do Brasileirão: \n{times}')
print('=-' * 15)
print(f'Os 5 primeiros colocados são: \n{times[:5]}')
print('=-' * 15)
print(f'Os 4 últimos são: \n{times[-4:]}')
print('=-' * 15)
print(f'A lista dos times em ordem alfabética fica: \n{sorted(times)}')
print('=-' * 15)
print(f'O Chapecoense está na {times.index("Chapecoense")+1}ª posição.')
