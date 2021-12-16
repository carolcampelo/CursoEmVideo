nome = input('Digite aqui seu nome completo: ').title().strip().split()
silva = 'Silva' in nome
print(f'Detector de sobrenome. Seu nome contém "Silva"? {silva}')
