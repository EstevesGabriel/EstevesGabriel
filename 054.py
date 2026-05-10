from datetime import datetime as dt

ano_atual = dt.now().year
maioridade = 0
nao_maioridade = 0
for num in range(1, 8):
    ano_nascimento = int(input(f'Ano de nascimento da {num}° pessoa: '))
    if ano_atual - ano_nascimento >= 18:
        maioridade += 1
    else:
        nao_maioridade += 1
print(f'{maioridade} pessoas já atingiram a maioridade')
print(f'{nao_maioridade} pessoas aindasão menores de idade')