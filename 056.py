soma_idade = 0
mulheres_20 = 0
idade_homem = 0
homem_velho = ''

for pessoas in range(1, 5):
    print(f'===Dados da {pessoas}° pessoa===')

    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo[M/F]: ')).strip().upper()

    soma_idade += idade

    if sexo == 'F'  and idade < 20:
        mulheres_20 += 1
    
    if sexo == 'M':
        if idade > idade_homem:
            idade_homem = idade
            homem_velho = nome    

media = soma_idade / pessoas

print('===Análise de dados terminada===\n' \
    f'Média da idade do grupo: {media}\n' \
    f'Homem mais velho: {homem_velho} com {idade_homem} anos\n' \
    f'Mulheres abaixo de 20 anos: {mulheres_20}')

