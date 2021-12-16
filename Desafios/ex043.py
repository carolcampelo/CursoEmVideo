print('= \033[;4mCalculadora de IMC\033[m =')
peso = float(input('Digite seu peso em kg: '))
altura = float(input('Digite sua altura em m: '))
imc = peso / altura ** 2
if 0 < imc < 18.5:
    print(f'Seu IMC é {imc:.1f}. Você está abaixo do peso.')
elif 18.5 <= imc < 25:
    print(f'Seu peso é ideal para sua altura. Seu IMC é {imc:.1f}')
elif 25 <= imc < 30:
    print(f'Seu IMC foi calculado em {imc:.1f}. Você tem sobrepeso.')
elif 30 <= imc < 40:
    print(f'Você está com obesidade. Seu IMC é de {imc:.1f}.')
elif imc >= 40:
    print(f'Seu IMC é de {imc:.1f}. Você tem obesidade mórbida.')
else:
    print('Não entendi. Tente novamente.')
