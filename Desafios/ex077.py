palavras = ['carol', 'maravilhosa', 'psicóloga', 'programadora', 'consertadora de coisas', 'inteligente', 'linda',
            'criativa', 'ousadah', 'fit', 'saudável', 'vegana', 'porém', 'ultimamente', 'nem', 'tanto', 's2']
for palavra in palavras:
    print(f'\nNa palavra {palavra.upper()} temos as vogais: ', end='')
    for letra in palavra:
        if letra.lower() in 'aáãâeêéiíoôõóuú':
            print(letra, end=' ')
