lista = []
for p in range(1, 6):
    lista.append(float(input(f'Insira o peso da {p}ª pessoa (em kgs):')))
print(f'O menor peso listado foi {min(lista):}kg e o maior peso listado foi {max(lista):}kg.')
