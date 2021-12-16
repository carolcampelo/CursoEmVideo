n1 = int(input('\033[95mDigite um número:\033[m '))
d = n1*2
t = n1*3
r = n1**(1/2)
print(f'O número escolhido foi \033[93m{n1}\033[m.'
      f' Seu dobro é \033[93m{d}\033[m,'
      f' o triplo é \033[93m{t}\033[m'
      f' e a raiz quadrada tem resultado de \033[93m{r:.2f}\033[m')
