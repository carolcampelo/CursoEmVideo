print('~ \033[;4mCalculadora de métodos de pagamento\033[m ~')
p1 = float(input('Digite o valor do produto: R$ '))
m = int(input('Selecione o método de pagamento: \n'
              '[1] - À vista em dinheiro ou cheque;\n'
              '[2] - À vista no cartão;\n'
              '[3] - Em até 2x no cartão;\n'
              '[4] - Em 3x ou mais.\n'))
if m == 1:
    p2 = p1 - (p1 * 10 / 100)
    print(f'O método selecionado foi: [1] - À vista em dinheiro ou cheque.\n\n'
          f'Você receberá 10% de desconto no produto de R${p1:.2f}\n'
          f'O novo valor será R${p2:.2f}.')
elif m == 2:
    p3 = p1 - (p1 * 5 / 100)
    print('O método selecionado foi: [2] - À vista no cartão.\n\n'
          f'Você receberá 5% de desconto no produto de R${p1:.2f}\n'
          f'O novo valor será R${p3:.2f}.')
elif m == 3:
    print('O método de pagamento selecionado foi: [3] - Em até 2x no cartão.\n\n'
          f'O valor do seu produto será de R${p1:.2f}.\n'
          f'Cada parcela custará R${p1 / 2 :.2f}.')
elif m == 4:
    p4 = p1 + (p1 * 20 / 100)
    v = int(input('Informe a quantidade de parcelas (máx 12): '))
    if 3 <= v <= 12:
        print('A forma de pagamento escolhida foi: [4] - Em 3x ou mais.\n\n'
              f'O valor do seu produto será de R${p4:.2f}.\n'
              f'Serão {v} parcelas de R${p4 / v:.2f}.')
    else:
        print('A quantidade de parcelas selecionadas não é compatível com o método de pagamento escolhido.')
        print('Tente novamente.')
else:
    print('Não entendi. Tente novamente.')
print()
print('Obrigada. Volte sempre!')
