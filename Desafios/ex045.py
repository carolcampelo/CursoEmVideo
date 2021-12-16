import random
from time import sleep
print('*~' * 8)
print('\033[93m J O K E N P Ô \033[m')
print('*~' * 8)
sleep(1)
print('Vamos jogar?!\n')
game = ['Pedra', 'Papel', 'Tesoura']
CPU = random.choice(game)
player = int(input('Escolha sua opção:\n'
                   '[1] - Pedra\n'
                   '[2] - Papel\n'
                   '[3] - Tesoura\n'))
sleep(0.5)
print('\033[93mJO\033[m')
sleep(0.5)
print('\033[93mKEN\033[m')
sleep(0.5)
print('\033[93mPO\033[m')
sleep(1)
if player == 1:
    print(f'O computador selecionou {CPU.lower()} e você escolheu pedra.')
    if CPU == 'Pedra':
        print('Houve um \033[;4mempate\033[m!\n Tente novamente.')
    elif CPU == 'Papel':
        print('\033[91mVocê perdeu!\033[m :(\n'
              'Tente novamente.')
    elif CPU == 'Tesoura':
        print('\033[92mVocê venceu!\033[m :)\n'
              'Vamos de novo?!')
elif player == 2:
    print(f'O computador selecionou {CPU.lower()} e você escolheu papel.')
    if CPU == 'Papel':
        print('Houve um \033[;4mempate\033[m!\n Tente novamente.')
    elif CPU == 'Tesoura':
        print('\033[91mVocê perdeu!\033[m :(\n'
              'Tente novamente.')
    elif CPU == 'Pedra':
        print('\033[92mVocê venceu!\033[m :)\n'
              'Vamos de novo?!')
elif player == 3:
    print(f'O computador selecionou {CPU.lower()} e você escolheu tesoura.')
    if CPU == 'Tesoura':
        print('Houve um \033[;4mempate\033[m!\n Tente novamente.')
    elif CPU == 'Pedra':
        print('\033[91mVocê perdeu!\033[m :(\n'
              'Tente novamente.')
    elif CPU == 'Papel':
        print('\033[92mVocê venceu!\033[m :)\n'
              'Vamos de novo?!')
else:
    print('Não entendi.\nTente novamente.')
