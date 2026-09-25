continuar = 'S'
total_gasto = mais_1000 = menor_preco = 0 
produto_mais_barato = ''

while continuar in 'Ss':
    nome_produto = input('Nome do produto: ')
    preco_produto = float(input('Preço do produto: '))
    total_gasto += preco_produto

    if preco_produto > 1000:
        mais_1000 += 1

    if preco_produto < menor_preco or menor_preco == 0:
        menor_preco = preco_produto
        produto_mais_barato = nome_produto

    continuar = input('Deseja continuar? [S/N] ').strip().upper()

    if continuar in 'Nn':
        print(f'=' * 5,'Dados da compra', '=' * 5)
        print(f'Preço total: {total_gasto:.2f}')
        print(f'Produtos acima de mil reais: {mais_1000}')
        print(f'Produto mais barato: {produto_mais_barato}')
        break

