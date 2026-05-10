salario = float(input('Qual o seu salário: '))

if salario > 1250:
    salario = salario + salario * 0.10
else:
    salario = salario + salario * 0.15
print(f'Seu salário passará a ser {salario}')
