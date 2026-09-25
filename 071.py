print('=' * 25)
print(' ' * 5, 'Banco master', ' ' * 5)
print('=' * 25)


valor_sacado = int(input('Valor a ser sacado: '))
qnt_50 = valor_sacado // 50
qnt_20 = valor_sacado % 50 // 20
qnt_10 = valor_sacado % 50 % 20 // 10
qnt_1 =  valor_sacado % 50 % 20 % 10 // 1

print(f'Total de celulas de R$50.00: {qnt_50}')
print(f'Total de celulas de R$20.00: {qnt_20}')
print(f'Total de celulas de R$10.00: {qnt_10}')
print(f'Total de celulas de R$1.00: {qnt_1}')

print('Volte sempre ao banco master. Tenha um bom dia!')
