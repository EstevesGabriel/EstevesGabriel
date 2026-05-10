#importação dos módulos necessários
from random import randint
from time import sleep as sp

#lista para fazer a seleção das jogadas
game = ('Pedra', 'Papel', 'Tesoura')

#repetição para manter o jogo funcionando até a pesso não querer jogar mais
while True:
    #jogada do jogador
    jogador = int(input('Faça sua jogada\n' \
    '[0] PEDRA\n' \
    '[1] PAPEL\n' \
    '[2] TESOURA\n' \
    '-> '))

    #momento de espera com sleep (sleep importado como sp)
    print('Vamos jogar!')
    sp(1.5)
    print('JO!')
    sp(1)
    print('KEN!!')
    sp(1)
    print('PO!!!')
    
    #jogada do computador
    cpu = randint(0, 2)

    print(f'O computador escolheu {game[cpu]}!\nO jogador escolheu {game[jogador]}')

    #condições separadas em cenários
    #término em empate
    if jogador == cpu:
        print('O resultado foi...')
        sp(1.5)
        print('EMPATE!!!')
    #término em vitória do computador
    elif jogador == 0 and cpu == 1 or jogador == 1 and cpu == 2 or jogador == 2 and cpu == 0:
        print('O resultado foi...')
        sp(1.5)
        print('VITÓRIA DO COMPUTADOR!!!')
    #término em vitória do jogador
    elif jogador == 1 and cpu == 0 or jogador == 2 and cpu == 1 or jogador == 0 and cpu == 2:
        print('O resultado foi...')
        sp(1.5)
        print('VITÓRIA DO JOGADOR!!!\n')
    print('-=' * 15)

    sp(2)

    #jogar novamente ou sair do jogo (parte do while True)
    jogar_novamente = int(input('Jogar novamente?\n' \
    '[1] Sim ' \
    '[2] Não\n'
    '-> '))

    if jogar_novamente == 1:
        continue
    else:
        print('Obrigado por jogar')
        break