from math import sin, cos, tan, pi

angulo = float(input('Digite o valor do ângulo: ')) * (pi/180)


print(f'O valor do seno é: {round(sin((angulo)), 2)} \nO valor de cosseno é: {round(cos((angulo)), 2)} \nO valor da tangente é: {round(tan((angulo)), 2)}')
