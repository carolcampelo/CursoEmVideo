numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze',
           'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
a = int(input('Digite um número entre 0 e 20: '))
while a not in range(0, 21):
    a = int(input('Número inválido. Digite um número de 0 a 20: '))
print(f'Você digitou o número {numeros[a]}.')
