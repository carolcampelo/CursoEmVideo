print('\033[92m*~\033[m' * 20)
print('Calculadora de Financiamento Habitacional')
print('\033[92m*~\033[m' * 20)
n = str(input('Como posso lhe chamar? '))
v = float(input(f'Olá, {n.capitalize()}. Qual o valor da casa que você quer comprar? R$'))
s = float(input('Certo. Entendi. E qual é o seu salário? R$'))
s1 = s * 30 / 100
t = int(input('Ok! E em quantos anos deseja pagar a casa? ')) * 12
p = v / t
if p <= s1:
    print('Parabéns. Seu financiamento foi \033[92maprovado\033[m e em breve você terá uma casa para chamar de sua!\n'
          f'Serão {t} parcelas de R${p:.2f} para comprar a casa de R${v:.2f}')
else:
    print('Sinto muito. O financiamento foi \033[91mreprovado\033[m. Tente novamente com outras condições.')
