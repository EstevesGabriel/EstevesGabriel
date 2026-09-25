times = ('Palmeiras', 'Flamengo', 'Athletico-PR', 'Fluminense','Bahia'
        'Cruzeiro', 'Atlético-MG', 'Coritiba', 'Bragantino', 'Santos'
        'São Paulo', 'Vitória', 'Corinthians', 'Botafogo', 'Mirassol', 'Grêmio',
        'Vasco', 'Internacional', 'Remo', 'Chapecoense')

print(f'Classificação do brasileirão: {times}')
print(f'-=' * 50)
print(f'5 primmeiros colocados: {times[0:5]}')
print(f'-=' * 50)
print(f'Últimos 4 colocados: {times[-4]}')
print(f'-=' * 50)
print(f'Classificação em ordem alfabética: {sorted(times)}')
print(f'-=' * 50)
print(f'O Chapecoense está na posição {times.index('Chapecoense')}')
print(f'-=' * 50)
