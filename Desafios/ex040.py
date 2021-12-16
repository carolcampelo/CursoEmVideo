print('\033[95m*~\033[m' * 12)
print(' Calculadora de Médias ')
print('\033[95m*~\033[m' * 12)
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2)/2
print(f'Sua média foi {m}.')
if m < 5:
    print('Você foi \033[91mreprovado\033[m. Tente novamente no próximo semestre :(')
elif 5 <= m < 7:
    print('Você está de \033[93mrecuperação\033[m. Estude para a próxima prova, ainda é possível ser aprovado!')
elif m >= 7:
    print('Você foi \033[92maprovado\033[m. Parabéns!')
