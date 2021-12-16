frase = 'Curso em Vídeo Python'
frase2 = '   Aprenda Python  '
# fatiamento
print(frase[9::3])
print(frase[9:18])
print(frase[:9])
print(frase[9:])
print(frase[9:21:2])
# análise
print(len(frase))
print(frase.count('o'))
print(frase.count('o', 0, 13))
print(frase.find('deo'))
print(frase.find('Android'))
print('Curso' in frase)
# transformação
print(frase.replace('Python', 'Android'))
print(frase.upper())
print(frase.lower())
print(frase.capitalize())
print(frase.title())
print(frase2.strip())
print(frase2.rstrip())
print(frase2.lstrip())
# tb dá pra unir 2 funções, como frase.lower().find('o')
# divisão
print(frase.split())
dividido = frase.split()
print(dividido)
print(dividido[2][2])
print(len(dividido[0]))
# junção
print(' '.join(frase))
