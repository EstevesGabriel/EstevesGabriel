from random import randint as aleatorio

print('Ha Ha Ha!\nSou seu computador! Você veio novamente para um jogo de advinhação? Vamos nesssa!\nEu pensei em um número de 0 a 10, tente advinhar!')
computador = aleatorio(0, 10)
jogador = int(input('Diga o seu palpite: '))
tentativas = 0

while jogador != computador:
    if jogador < computador:
        print('Eu pensei em um número maior, tente novamente')
        jogador = int(input('Diga o seu palpite: '))
    elif jogador > computador: 
        print('Eu pensei em um número menor, tente novamente')
        jogador = int(input('Diga o seu palpite: '))
    tentativas += 1
print(f'\nVocê acertou! Parabéns!\nVocê fez {tentativas} palpites')

