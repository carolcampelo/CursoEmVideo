#n = input('Digite um número de 0 a 9999: ')
#print()
#print(f"""Ok, {n}
#Unidade: {n[3]}
#Dezena: {n[2]}
#Centena: {n[1]}
#Milhar: {n[0]}
#""")
n1 = int(input('Digite um número de 0 a 9999: '))
u = n1//1 % 10
d = n1//10 % 10
c = n1//100 % 10
m = n1//1000 % 10
print()
print(f"""Ok, {n1}
Unidade: {u}
Dezena: {d}
Centena: {c}
Milhar: {m}""")
