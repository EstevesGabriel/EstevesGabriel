dados_pesos = []
for pessoas in range(1, 6):
    peso = float(input(f'Digite o pesso da {pessoas}° pessoa: '))
    dados_pesos.append(peso)

print(f'A {dados_pesos.index(max(dados_pesos)) + 1}° pessoa foi a com o maior peso, com {max(dados_pesos)}Kg')
print(f'A {dados_pesos.index(min(dados_pesos)) + 1}° pessoa foi a com o menor peso, com {min(dados_pesos)}Kg')
