while True:
    sexo = str(input('Qual é o seu sexo? [M/F] ')).strip().upper()[0]
    idade = int(input('Qual é a sua idade? '))

    cadastro_18 = 0
    cadastro_masc = 0
    cadastro_fem20 = 0

    if idade >= 18:
        cadastro_18 += 1
    elif sexo in 'Mm':
        cadastro_masc += 1
    elif sexo in 'Ff' and idade < 20:
        cadastro_fem20 += 1

    continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if continuar in 'Ss':
        continue
    elif continuar in 'Nn':
        print(f'Certo, agora vamos fazer a análise dos dados:\nPessoas com mais de 18 anos: {cadastro_18}\nHomens cadastrados: {cadastro_masc}\nMulheres com menos de 20 anos: {cadastro_fem20}')
        break
    else:
        continue