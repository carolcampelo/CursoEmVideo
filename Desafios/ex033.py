a = int(input('Digite um número inteiro: '))
b = int(input('Digite mais um: '))
c = int(input('Escreva o último número aqui: '))
nums = [a, b, c]
nums.sort()
print(f'O menor número é \033[33m{nums[0]}\033[m e o maior é \033[33m{nums[2]}\033[m')
