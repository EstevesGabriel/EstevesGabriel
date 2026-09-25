valores = int(input('Digite um valor de 0 a 10: ')), int(input('Digite um valor de 0 a 10: ')), int(input('Digite um valor de 0 a 10: ')), int(input('Digite um valor de 0 a 10: '))

print(f'O valor 9 apareceu {valores.count(9)} vezes')

if 3 in valores:
    print(f'O número 3 foi encontrado na posição {valores.index(3) + 1}')
else:
    print('Valor 3 não encontrado')

print('Os valores pares foram ', end='')
for numeros in valores:
    if numeros % 2 == 0:
        print(numeros, end=' ')

