tupla = ('Pindamanhangaba', 'Maconha', 'Liquido encefaloraquidiano', 'Diarreia proteolitica', 'Joqo gilberto')
vogais = 'aeiouAEIOU'

for palavra in tupla:
    print(f'\nNa palavra {palavra.upper()} temos as seguintes vogais: ', end='')
    for letras in palavra:
        if letras in vogais:
            print(f'{letras}', end=', ')