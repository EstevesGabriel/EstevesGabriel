#Desafio do código em 4 linhas usando for
numero = int(input('Digite o número fatorial: '))
for i in range(numero, 1, -1):
    numero = numero * (i - 1)
    print(f'{i}! =',)
'''incompleto, terminar outro dia'''