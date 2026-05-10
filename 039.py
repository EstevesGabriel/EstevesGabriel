from datetime import datetime

ano_atual = datetime.now().year
nascimento = int(input('Ano de nascimento: '))

if ano_atual- nascimento < 18:
    print(f'Quem nasceu em {nascimento} ainda não tem 18. Não precisa se alistar')
elif ano_atual - nascimento == 18:
    print(f'Quem nasceu em {nascimento} já tem 18 em {ano_atual}.\nJá deve realizar o alistamento obrigatório ')
else:
    print(f'Quem nasceu em {nascimento} já passou do prazo de alistamento\nAlistamento obrigatório urgente')