print('=' * 5, 'Detector de palíndromo', '=' * 5)
frase = str(input('Digite uma frase: '))

palindromo = []

for retorno in range(1, len(frase) + 1):
    palindromo.append(frase[-retorno])

palindromo = ''.join(palindromo)
if palindromo == frase:
    print(f'A frase "{frase}" ao contrário é "{palindromo}".\nPortanto, é um palindromo')
else:
    print(f'A frase "{frase}" ao contrário é "{palindromo}".\nPortanto, não é um palindromo')

