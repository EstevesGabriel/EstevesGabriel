num = int(input('Digite um número: '))
primo = 0

for p in range(1, num + 1):
    conferir = num % p
    if conferir == 0:
        print('\033[33m', end='')
        primo += 1
    else:
        print('\033[34m', end='')
    print(f'{p}', end=', ')
if primo == 2:
    print(f'\n Por ser divisível apenas por 1 e por ele mesmo, {num} é um número primo')
