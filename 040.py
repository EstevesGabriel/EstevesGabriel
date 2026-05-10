n1 = float(input('Primeira nota: ')) 
n2 = float(input('Segunda nota: '))
n3 = float(input('Terceira nota: '))

media = (n1 + n2 + n3) / 3

if media < 5.0:
    print(f'Nota final: {media:.2f}\nNota insuficiente para aprovação, o aluno será reprovado')
elif 6.9 > media >= 5.0:
    print(f'Nota final: {media:.2f}\nNota insuficiente para a aprovação, o aluno deverá fazer a recuperação')
else:
    print(f'Nota final: {media:.2f}\nNota suficiente para a aprovação, parabéns!')
