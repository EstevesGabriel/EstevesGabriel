produtos = (
    'USB quebrado', 25.30,
    'Maconha fumada', 99.88,
    'Losartana', 10.40,
    'Predinisolona', 987.00,
    'Controle de Ps4 One', 345.99,
    'Chapeu do Lula', 2.50,
    'Cocktell molotoff', 80.75
)

passador = 0

print('-'*55)
while passador != len(produtos):
    print(f'Produto: {produtos[passador]:.<30}', end='')
    passador += 1
    print(f'Preço: R${produtos[passador]:>7.2f}')
    passador += 1
print('-'*55)
