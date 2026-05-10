peso = float(input('Seu peso em Kg: '))
altura = float(input('Sua altura em metros: '))
imc = peso / (altura ** 2)

print('-=' * 20)

print(f'Valor de IMC: {imc:.2f}')

if imc <= 18.5:
    print('Peso abaixo do normal')
elif 18.5 <= imc < 25:
    print('Peso dentro da normalidade')
elif 25 <= imc < 30:
    print('Peso acima do normal')
elif 30 <= imc <= 40:
    print('Peso em quadro de obesidade')
else:
    print('Peso em quadro de obesidade mórbida')

print('-=' * 20)