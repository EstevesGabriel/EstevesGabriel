num1 = float(input('Digite o primeiro número: '))
num2 = float(input('Digite o segundo número: '))

if num1 > num2:
    print(f'O valor {num1} é maior que {num2}')
elif num2 > num1:
    print(f'O valor {num2} é maior que {num1}')
elif num1 == num2:
    print('Não há nada demais, os valores são iguais')
else:
    print('Pelo amor de Deus, isso é um número?')
