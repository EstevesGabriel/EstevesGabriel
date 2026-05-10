import os

os.system('clear')
valor_casa = float(input('Valor do imóvel: '))
salario = float(input('Quanto você ganha:'))
financiamento = int(input('Em quantos anos será quitato: '))

if valor_casa / (financiamento * 12) > salario * 0.30:
    print(f'O imóvel dividido em {financiamento} tem {financiamento * 12} prestações de R${valor_casa / (financiamento * 12):.2f}\n Sua proposta não atingiu o necessário, emprestimo \033[31mNEGADO\033')
elif valor_casa / (financiamento * 12) < salario * 0.30:
    print(f'O imóvel dividido em {financiamento} tem {financiamento * 12} prestações de R${valor_casa / (financiamento * 12):.2f}\n Sua proposta atingiu o necessário, emprestimo \033[32mACEITO\033')