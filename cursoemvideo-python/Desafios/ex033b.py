a = int(input('Digite um número inteiro: '))
b = int(input('Digite mais um: '))
c = int(input('Escreva o último número aqui: '))
menor = a
if b < c and b < a:
    menor = b
if c < a and c < b:
    menor = c
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print(f'O menor número é \033[34m{menor}\033[m e o maior é \033[34m{maior}\033[m')
