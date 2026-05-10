from datetime import date
ano_atual = date.today().year
print('Escolha uma das opções abaixo:\n0: Verificar se o ano atual é bissexto\n1: Escolher um ano para verificar se ele é bissexto\n2: Entre dois anos, quantos foram bissextos')
ano = int(input('-> '))


if ano == 0:
    if ano_atual % 4 == 0 and ano_atual % 100 != 0 or ano_atual % 400 == 0:
        print(f'O ano {ano_atual} é um ano bissexto')
    else:
        print(f'O ano {ano_atual} não é bissexto')
elif ano == 1:
    ano = int(input('\nEscolha qual ano você deseja: '))
    if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
        print(f'O ano {ano} é um ano bissexto')
    else:
        print(f'O ano {ano} não é bissexto')
"""elif ano == 2:
    ano = int(input('Digite o primeiro ano\n-> '))
    ano2 = int(input('Digite o segundo ano\n-> '))
    
Vou voltar a este código para transformá-lo em algo melhor"""