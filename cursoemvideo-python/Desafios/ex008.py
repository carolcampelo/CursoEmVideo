print('\033[31m+-\033[m' * 10)
print('Conversor de medidas')
print('\033[31m+-\033[m' * 10)
a = float(input('Escreva uma metragem: '))
dm = a * 10
cm = a * 100
mm = a * 1000
dam = a * 0.1
hm = a * 0.01
km = a * 0.001
print(f'{a:.2f}m equivale a {dm:.0f}dm, {cm:.0f}cm ou {mm:.0f}mm')
print(f'{a:.2f}m também é equivalente a {dam}dam, {hm}hm e {km}km')
