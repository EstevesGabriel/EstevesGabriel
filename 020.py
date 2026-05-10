from random import shuffle
Aluno1 = str(input('Primeiro aluno: '))
Aluno2 = str(input('Segundo aluno: '))
Aluno3 = str(input('Terceiro aluno: '))
Aluno4 = str(input('Quarto aluno: '))
Aluno5 = str(input('Quinto aluno: '))
sala = [Aluno1, Aluno2, Aluno3, Aluno4, Aluno5]
shuffle(sala)

print('A ordem de apresentação será: ', sala)

