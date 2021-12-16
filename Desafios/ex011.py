cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[93m',
         'peb':'\033[;7m'}
a1 = float(input('{}Insira a altura da parede:{} '.format(cores['peb'], cores['limpa'])))
l1 = float(input('{}Insira a largura da parede:{} '.format(cores['peb'], cores['limpa'])))
a2 = a1 * l1
t = a2 / 2
print()
print('Para pintar uma parede de {}{}{}m² você precisará de {}{}{}l de tinta!'.format(cores['azul'], a2, cores['limpa'],
                                                                                      cores['amarelo'], t, cores['limpa']))
