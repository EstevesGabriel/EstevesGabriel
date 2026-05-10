from datetime import date
ano_nascimento = int(input('Ano de nascimento: '))
idade = date.today().year - ano_nascimento

print(f'O atleta tem {idade} anos')

if idade <= 9:
    print('Atleta mirim')
elif idade <= 14:
    print('Atleta infantil')
elif idade <= 19:
    print('Atleta Junior')
elif idade <= 25:
    print('Atleta Sênior')
else:
    print('Atleta Master')


