"""Cores no terminal por \033
    Style       text        back
    0 none      30 white    40 white
    1 bold      31 red      41 red
    4 underline 32 green    42 green
    7 negative  33 yellow   43 yellow
                34 purple   44 purple
                35 pink     45 pink
                36 blue     46 blue
                37 grey     47 grey"""

vel_car = float(input('Digite a velocidade do carro: '))
if vel_car > 80:
    print(f'\033[32m Você foi multado, sua multa será de:\003 \033[31mR${(vel_car - 80) * 7:.2f}\033')
else:
    print('\033[34m A velocidade está dentro do limite, siga em frente')