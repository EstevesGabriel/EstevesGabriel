import random

cont = 0

while True:
    print('Vamos jogar um jogo de par ou impar!\nFaça sua jogada')
    jogada = int(input("Digite 0 para par ou 1 para impar: "))
    if jogada == 0:
        print("Você escolheu par!")
    elif jogada == 1:
        print("Você escolheu impar!")

    print('Computador está rolando os dados...')
    computador = random.choice(['Par', 'Impar'])
    print(f'Computador rodou {computador}')

    if jogada == 0 and computador == 'Par':
        cont += 1
        print('Você ganhou!')
        print('Rodando novamente...')
    elif jogada == 1 and computador == 'Impar':
        cont += 1
        print('Você ganhou!')
        print('Rodando novamente...')
    else:
        print('Você perdeu!')
        break

print(f'Você ganhou {cont} vezes!')
