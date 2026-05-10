print('=' * 15)
print('Gerador de PA')
print('=' * 15)

primeiro = int(input('Valor do primeiro termo: '))
razao = int(input('Valor da razão aritimética: '))

for pa in range(1, 11):
    print(f'{primeiro}', end=' -> ')
    primeiro += razao
print('Fim da progressão')