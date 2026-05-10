from os import system
system('clear')

number = int(input('Digite o número que será convertido: '))
base_conversão = int(input('Para qual base numérica será convertido?\n[ 1 ] - Binário\n[ 2 ] - Octal\n[ 3 ] - Hexadecimal\n-> '))

if base_conversão == 1:
    print(f'{number} convertido em binário é igual a {bin(number)[2:]}')

elif base_conversão == 2:
    print(f'{number} convertido em octal é igual a {oct(number)[2:]}')


elif base_conversão == 3:
    print(f'{number} convertido em hexadecimal é igual a {hex(number)[2:]}')

else:
    print('Opção inválida')

