num1 = int(input('Primeiro valor: '))
num2 = int(input('Segundo valor: '))
pare = False
opera = 0

while pare != True:
    print('[1] - Somar\n[2] - Multiplicar\n[3] - Maior\n[4] - Novos números\n[5] - Sair do programa')
    opera = int(input('Qual operação você deseja? '))
    print('=' * 25)
    if opera == 1:
        print(f'A soma entre {num1} e {num2} é {num1 + num2}')
    elif opera == 2:
        print(f'A multiplicação entre {num1} e {num2} é {num1 * num2}')
    elif opera == 3:
        print(f'O maior número entre {num1} e {num2} é {max(num1, num2)}')
    elif opera == 4:
        print('Novos valores serão adicionados')
        num1 = int(input('Primeiro valor: '))
        num2 = int(input('Segundo valor: '))
    elif opera == 5:
        print('Programa será encerrado...')
        pare = True
    else:
        print('Número incorreto\nDigite novamente')
    print('=' * 25)

