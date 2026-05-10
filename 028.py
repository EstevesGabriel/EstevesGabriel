from random import randint

print('Vamos jogar um jogo, eu quero adivinhar qual número você está pensando ')

user_num = int(input('Digite um número de 0 a 5: '))
AI_num = randint(0, 5)

print(f'Você não é páreo para mim! Ha Ha Ha! ' if AI_num == user_num else f'Parabens, você me venceu! Eu pensei que fosse {AI_num}')
