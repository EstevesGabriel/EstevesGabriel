from math import pow, sqrt

cateto_oposto = float(input('Digite o comprimento do cateto oposto: '))
cateto_adjacente = float(input('Digite o comprimento do cateto adjacente: '))

triangulo = sqrt(pow(cateto_adjacente, 2) + pow(cateto_oposto, 2))

print(f'O valor da hipotenusa é: {triangulo}')