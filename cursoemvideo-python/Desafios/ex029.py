print('\033[97m= Calculador de Multas =\033[m')
vel = float(input('Digite aqui a velocidade que você trafegava (em km/h): '))
if vel >= 80:
    print(f'Você estava {(vel - 80)}km/h acima do limite permitido.')
    print(f'\033[91mVocê será multado em R${(vel - 80) * 7:.2f}.\033[m')
else:
    print('\033[92mVocê estava dentro do limite permitido. Fique tranquilo e continue assim!\033[m')
