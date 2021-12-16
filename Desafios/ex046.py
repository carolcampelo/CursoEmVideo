from time import sleep
print('Faltam \033[;4m10 segundos\033[m para o novo ano:')
for c in range(10, -1, -1):
    print(c)
    sleep(1)
print('* - ' * 7)
print('\033[93mF E L I Z  A N O  N O V O  !\033[m')
print('* - ' * 7)
